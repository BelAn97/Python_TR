import argparse
import logging
import pathlib
import requests
import tldextract
import yaml
import sqlite3
import json
from os.path import join
from pprint import pprint
from html.parser import HTMLParser
from collections import defaultdict
from datetime import datetime


def get_html(url):
    source = requests.get(f"https://{url}")
    return source.text


class TagsParser(HTMLParser):
    def __init__(self):
        self.count = defaultdict(int)
        super().__init__()

    def handle_starttag(self, tag, attrs):
        self.count[tag] += 1

    def handle_startendtag(self, tag, attrs):
        self.count[tag] += 1


class Tags_Counter:
    def __init__(self, logfile='requests.log', synonym_file='synonyms.yaml', db='tags.db'):
        logging.basicConfig(filename=logfile, filemode='a', level=logging.INFO,
                            format='%(asctime)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        self.synonym = join(pathlib.Path(__file__).parent, 'dict', synonym_file)
        with open(self.synonym, 'r') as stream:
            dictionary = yaml.load(stream, Loader=yaml.Loader)
        self.dict = dictionary
        self.parser = TagsParser()
        self.conn = sqlite3.connect(join(pathlib.Path(__file__).parent, 'db', db))
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS site_tags (
            site_domain TEXT,
            site_url TEXT PRIMARY KEY,
            check_date TIMESTAMP,
            tags JSON)""")
        self.conn.commit()

    def update_db(self, url, tags):
        domain = tldextract.extract(url).domain
        self.cursor.execute("INSERT OR REPLACE INTO site_tags VALUES (?,?,?,?)",
                            (domain, url, datetime.now(), json.dumps(tags)))
        self.conn.commit()

    def fetch_db(self, url):
        self.cursor.execute("SELECT * FROM site_tags WHERE site_url=?", (url,))
        return self.cursor.fetchone()

    def delete_db(self, url):
        self.cursor.execute("Delete FROM site_tags WHERE site_url=?", (url,))
        self.conn.commit()

    def view(self, url):
        url = self.get_syn(url)
        logging.info(f"View {url}")
        tags = self.fetch_db(url)
        print("")
        print(f"Site: {tags[0]}")
        print(f"Synonym: {tags[1]}")
        print(f"Check date: {tags[2]}")
        print("Tags:")
        pprint(json.loads(tags[3]))

    def get(self, url):
        url = self.get_syn(url)
        logging.info(f"Get {url}")
        content = get_html(url)
        self.parser.feed(content)
        self.update_db(url, self.parser.count)
        print(f"Get tags from {url} done")

    def get_syn(self, text):
        return self.dict[text] if text in self.dict.keys() else text

    def add_syn(self, args):
        key, val = args
        self.del_syn(key)
        self.dict[key] = val
        self.save_dict()
        print(f"Synonym {key} added")

    def del_syn(self, key):
        if key in self.dict.keys():
            del self.dict[key]
            self.save_dict()
            print(f"Synonym {key} deleted")

    def save_dict(self):
        with open(self.synonym, 'w') as stream:
            yaml.dump(self.dict, stream)


def run():
    parser = argparse.ArgumentParser(description='Process site url.')
    parser.add_argument("-v", "--view", help="View Site URL or synonym", type=str)
    parser.add_argument("-g", "--get", help="Get Site URL or synonym", type=str)
    parser.add_argument("-a", "--add_syn", nargs='+', help='Add new synonym: -a "ya" "ya.ru"', type=str)
    parser.add_argument("-d", "--del_syn", help="Delete synonym", type=str)
    ...
    args = parser.parse_args()
    tc = Tags_Counter()
    if args.view:
        tc.view(args.view)
    if args.get:
        tc.get(args.get)
    if args.add_syn:
        tc.add_syn(args.add_syn)
    if args.del_syn:
        tc.del_syn(args.del_syn)


if __name__ == '__main__':
    run()

# import pytest as pytest
#
#
# def test_get():
#     tc = Tags_Counter()
#     # tc.get('google.ru')
#     tc.view('google.ru')
