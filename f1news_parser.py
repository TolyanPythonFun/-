import requests
from bs4 import BeautifulSoup
import json
import datetime

url_site = "https://www.f1news.ru/"
headers = {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}


def get_data(url, headers):
    req = requests.get(url=url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    News = soup.find('div', class_="widget_body b-news-list__body").find_all("li", class_="b-news-list__item")
    data = []
    for item in News:
        try:
            link_new = "https://www.f1news.ru" + item.find('a', class_='b-news-list__title').get('href')
        except Exception as ex:
            link_new = 'Ссылка нестандартная'
        response = requests.get(url=link_new)
        source = response.text
        bs = BeautifulSoup(source, 'lxml')
        try:
            title_content = bs.find('h1', class_='post_title').text
        except Exception:
            title_content = 'Заголовок отсутсвует'
        try:
            content_in_site = bs.find('div', class_='post_content').text.strip()
        except Exception:
            content_in_site = 'Контент отсутствует'
        try:
            date_content = bs.find('div', class_='post_date').text
        except Exception:
            date_content = 'Дата отсутсвует'
        data.append(
            {
                'title': title_content,
                'content': content_in_site,
                'date': date_content,
                'link': link_new
            }
        )


    now = datetime.datetime.now()
    with open(('C:/Программирование/Скрипты/Парсинг/f1_news_' + now.strftime('%Y_%m_%d_%H_%M_%S') + '.json'), 'a',
              encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    get_data(url_site, headers)

if __name__ == '__main__':
    main()
