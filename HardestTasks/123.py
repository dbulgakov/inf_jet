from bs4 import BeautifulSoup
import os

with open(os.getcwd() + '/1.xml', encoding="utf-8") as __json_data_file:
    __app_config = BeautifulSoup(__json_data_file, "lxml")
for tag in __app_config.find_all('domain'):
    domain_splited = tag.string.split('.')[-2:]
    print("{0}.{1}".format(domain_splited[0].strip(), domain_splited[1]))

