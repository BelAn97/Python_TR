import json
import unittest
from unittest.mock import patch
from os.path import exists

from homeworks.TR_02.setup_tags_counter.src.tags_counter.main import Tags_Counter


class TagsCounterTestCase(unittest.TestCase):
    def setUp(self):
        self.tc = Tags_Counter()

    def test_get(self):
        url = 'google.com'
        self.tc.delete_db(url)
        res = self.tc.fetch_db(url)
        self.assertEqual(res, None, 'Site not deleted')
        self.tc.get(url)
        res = self.tc.fetch_db(url)
        tags = json.loads(res[3])
        self.assertEqual(res[1], url, 'Wrong url')
        self.assertEqual(tags['body'], 1, 'Wrong body count')

    def test_get_log(self):
        self.assertTrue(exists('requests.log'))
        with open('requests.log', 'r') as f:
            self.assertRegexpMatches(f.readlines()[-1],
                                     r"\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}:\d{2} [A|P]M: Get google.com\n",
                                     'Wrong log line')

    @patch('builtins.print')
    def test_view(self, mock_print):
        url = 'google.com'
        self.tc.view(url)
        mock_print.assert_called_with('Tags:')

    def test_get_as_synonym(self):
        syn = 'ggl'
        url = self.tc.get_syn(syn)
        self.tc.delete_db(url)
        res = self.tc.fetch_db(url)
        self.assertEqual(res, None, 'Site not deleted')
        self.tc.get(syn)
        res = self.tc.fetch_db(url)
        tags = json.loads(res[3])
        self.assertEqual(res[1], url, 'Wrong url')
        self.assertEqual(tags['body'], 1, 'Wrong body count')

    @patch('builtins.print')
    def test_view_as_synonym(self, mock_print):
        syn = 'ggl'
        self.tc.view(syn)
        mock_print.assert_called_with('Tags:')

    def test_view_log(self):
        self.assertTrue(exists('requests.log'))
        with open('requests.log', 'r') as f:
            self.assertRegexpMatches(f.readlines()[-1],
                                     r"\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}:\d{2} [A|P]M: View google.com\n",
                                     'Wrong log line')


if __name__ == '__main__':
    unittest.main()
