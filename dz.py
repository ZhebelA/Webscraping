import requests
import bs4
from fake_http_header import FakeHttpHeader

keys = ['IT', 'проект', 'Android', '2022']

fake_headers = FakeHttpHeader(domain_name = 'ru').as_header_dict()

base_url = 'https://habr.com'
url = base_url + '/ru/all/'

response = requests.get(url, headers= fake_headers)
text = response.text
soup = bs4.BeautifulSoup(text, features = 'html.parser')

articles = soup.find_all("article")

for article in articles:
    href = article.find("h2").find("a").attrs["href"]
    description = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    description = [script.text.strip() for script in description]
    for word in keys:
        for item in description:
            if word in item:
                date = article.find("time").attrs['datetime'].split('T')[0]
                title = article.find('h2').find('span').text
                link = base_url + article.find('h2').find('a').attrs['href']
                print(f'{word}: {date}/ {title} / {link}')
