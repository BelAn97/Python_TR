# Взять файл country_data.xml и распечатать атрибут name для всех тегов country. Для парсинга xml
# можно использовать любую библиотеку.


from bs4 import BeautifulSoup

with open("country_data.xml", "r") as data:
    contents = data.read()
    xml_data = BeautifulSoup(contents, 'lxml')
    print([e['name'] for e in xml_data.findAll('country')])


import xml.etree.ElementTree as ElTree

with open("country_data.xml", "r") as data:
    root = ElTree.fromstring(data.read())
    countries = root.findall('.country')
    for country in countries:
        print(country.attrib['name'])
