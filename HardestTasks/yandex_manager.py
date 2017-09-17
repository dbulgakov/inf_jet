import asyncio
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import ssl
from urllib.parse import quote
import os

ssl._create_default_https_context = ssl._create_unverified_context


class YandexManager():
    def __init__(self, url, thread_number):
        self.thread_number = thread_number
        self.domains = {}
        self.url = url
        self.executor = ThreadPoolExecutor(thread_number)

    @asyncio.coroutine
    def get_search_results(self, search_query):
        search_url = self.url + quote(search_query)
        response = yield from self.loop.run_in_executor(self.executor, urllib.request.urlopen, search_url)

        # with open(os.getcwd() + '/1.xml', encoding="utf-8") as __json_data_file:
        #     response_xml = self.parse_xml(__json_data_file)

        response_xml = self.parse_xml(response.read())

        print(response_xml)
        self.count_domains(response_xml)

    def perform_search(self, queries_list):
        self.domains.clear()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        tasks = [asyncio.async(self.get_search_results(z)) for i, z in enumerate(queries_list)]
        self.loop.run_until_complete(asyncio.wait(tasks))
        self.loop.close()
        return self.domains

    def add_domain_to_dict(self, domain):
        if domain in self.domains:
            self.domains[domain] += 1
        else:
            self.domains[domain] = 1

    def count_domains(self, response_xml):
        for domain in self.extract_domains(response_xml):
            self.add_domain_to_dict(domain)

    def get_domain(self, url):
        domain_spited = url.string.split('.')[-2:]
        return "{0}.{1}".format(domain_spited[0].strip(), domain_spited[1])

    def extract_domains(self, response_xml):
        extracted_domains = []
        for tag in response_xml.find_all('domain'):
            extracted_domains.append(self.get_domain(tag))
        return extracted_domains

    def parse_xml(self, response_data):
        return BeautifulSoup(response_data.decode('utf-8'), "lxml")
