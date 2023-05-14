import requests
import urllib3
import json

def get_news_data():
    lang = 'us'
    api_key = '283533136981441da324ba7c1b5d0cc5'
    url = f'https://newsapi.org/v2/top-headlines?country={lang}&apikey='+api_key
    try:
        news = requests.get(url).json()
    except:
        proxy = urllib3.ProxyManager('http://10.11.4.1:3128/')
        r1 = proxy.request('GET', url)
        news = json.loads(r1.data.decode('utf-8'))
    return news

news_data = get_news_data()
#print(news_data)

image_links = []
for article in news_data['articles']:
    image_links.append(article['urlToImage'])

print(image_links)
