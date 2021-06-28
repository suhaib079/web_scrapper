import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count(url):
    page = requests.get(url)
    soup =BeautifulSoup(page.content,'html.parser')
    results = soup.find_all('a',href='/wiki/Wikipedia:Citation_needed')
    return len(results)


def get_citations_needed_report(url):
    page = requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    results = soup.find_all('a',href='/wiki/Wikipedia:Citation_needed')
    content = []
    for i in range(len(results)):
            try:
                citation_number = 1+i
                paragraph = results[i].parent.parent.parent.getText().strip()


                content.append({'Citation number':citation_number, 'Paragraph':paragraph})

            except AttributeError as e:
                continue
    return content
print(get_citations_needed_count(url))
print(get_citations_needed_report(url))