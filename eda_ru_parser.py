import requests
import os
import time

from bs4 import BeautifulSoup


def get_count_items():
    '''Функция для получения количества страниц'''
    titles = []
    for i in range(1, 750):
        url = f'https://eda.ru/recepty?page={i}' # url для каждой страницы
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        recepty = soup.find_all('div', class_='emotion-m0u77r')
        # print(f'Страница {i}')
        for item in recepty:
            if recepty:
                item_title = item.find('div', class_='emotion-1eugp2w').find('a').text
                titles.append(item_title)
    print(len(titles)) # количество страниц


def create_folders():
    '''Функция для создания папок по всем категориям'''
    for i in range(1, 715):
        url = f'https://eda.ru/recepty?page={i}'
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        recepty = soup.find_all('div', class_='emotion-m0u77r')
        # print(f'Страница №{i}')
        for item in recepty:
            if recepty:
                item_title = item.find('div', class_='emotion-1eugp2w').find('a').text
                item_link = 'https://eda.ru' + item.find('div', class_='emotion-1eugp2w').find('a').get('href')
                # print(f'{item_title} ---> {item_link}')
                response = requests.get(url=item_link)
                soup = BeautifulSoup(response.text, 'lxml')
                count = 1
                try:
                    categories = soup.find('div', class_='emotion-a90bfp').find_all('span', itemprop='itemListElement')
                except:
                    categories = f'Категория {count}'
                try:
                    folder_1 = categories[1].text
                except:
                    folder_1 = f'{count}'
                try:
                    folder_2 = categories[2].text
                except:
                    folder_2 = f'{count}'
                if not os.path.exists(f'{folder_1}\{folder_2}'):
                    os.makedirs(f'{folder_1}\{folder_2}')
                    count += 1
        # time.sleep(1)


def get_recepty():
    '''Функция для сбора рецептов с сайта'''
    for i in range(1, 715):
        url = f'https://eda.ru/recepty?page={i}'
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        recepty = soup.find_all('div', class_='emotion-m0u77r')
        print(f'Страница №{i}')
        for item in recepty:
            if recepty:
                try:
                    item_title = item.find('div', class_='emotion-1eugp2w').find('a').text
                except:
                    item_title = ''
                try:
                    item_link = 'https://eda.ru' + item.find('div', class_='emotion-1eugp2w').find('a').get('href')
                except:
                    item_link = ''
                response = requests.get(url=item_link)
                soup = BeautifulSoup(response.text, 'lxml')
                count = 1
                try:
                    categories = soup.find('div', class_='emotion-a90bfp').find_all('span', itemprop='itemListElement')
                except:
                    categories = f'Категория {count}'
                try:
                    folder_1 = categories[1].text
                except:
                    folder_1 = f'{count}'
                try:
                    folder_2 = categories[2].text
                except:
                    folder_2 = f'{count}'
                try:
                    with open(f'Еда/{folder_1}/{folder_2}/{item_title}.txt', 'w', encoding='utf-8') as file:
                        ingridients = soup.find_all('div', class_='emotion-7yevpr')
                        file.write(f'{item_title}\n')
                        bzu = soup.find('div', class_='emotion-1bpeio7')
                        try:
                            file.write(f'Каллорийность - {bzu.find("span", itemprop="calories").text} ккал\n'
                                       f'Белки - {bzu.find("span", itemprop="proteinContent").text} гр.\n'
                                       f'Жиры - {bzu.find("span", itemprop="fatContent").text} гр.\n'
                                       f'Углеводы - {bzu.find("span", itemprop="carbohydrateContent").text} гр.\n')
                        except:
                            file.write('БЖУ не найдено')
                        file.write('\n')
                        for i in ingridients:
                            file.write(
                                f'{i.find("span", class_="emotion-1g8buaa").text} --> {i.find("span", class_="emotion-15im4d2").text}\n')
                        file.write('\n')
                        try:
                            recept = soup.find('div', class_='emotion-1ywwzp6').find_all('span', itemprop='text')
                            for step in recept:
                                file.write(f'{step.text}')
                        except:
                            recept = 'Нет рецепта'

                        file.write('\n')
                        file.write('\n')
                        try:
                            file.write(f'Время приготовления --> {soup.find("span", itemprop="cookTime").text}\n')
                        except:
                            file.write('Неизвестно время приготовления')
                except:
                    if not os.path.exists(f'Еда/{folder_1}/{folder_2}'):
                        os.mkdir(f'Еда/{folder_1}/{folder_2}')
                    with open(f'Еда/{folder_1}/{folder_2}/{item_title}.txt', 'w', encoding='utf-8') as file:
                        ingridients = soup.find_all('div', class_='emotion-7yevpr')
                        file.write(f'{item_title}\n')
                        bzu = soup.find('div', class_='emotion-1bpeio7')
                        try:
                            file.write(f'Каллорийность - {bzu.find("span", itemprop="calories").text} ккал\n'
                                       f'Белки - {bzu.find("span", itemprop="proteinContent").text} гр.\n'
                                       f'Жиры - {bzu.find("span", itemprop="fatContent").text} гр.\n'
                                       f'Углеводы - {bzu.find("span", itemprop="carbohydrateContent").text} гр.\n')
                        except:
                            file.write('БЖУ не найдено')
                        file.write('\n')
                        for i in ingridients:
                            file.write(
                                f'{i.find("span", class_="emotion-1g8buaa").text} --> {i.find("span", class_="emotion-15im4d2").text}\n')
                        file.write('\n')
                        try:
                            recept = soup.find('div', class_='emotion-1ywwzp6').find_all('span', itemprop='text')
                            for step in recept:
                                file.write(f'{step.text}')
                        except:
                            recept = 'Нет рецепта'
                        file.write('\n')
                        file.write('\n')
                        try:
                            file.write(f'Время приготовления --> {soup.find("span", itemprop="cookTime").text}\n')
                        except:
                            file.write('Неизвестно время приготовления')
        time.sleep(1)


def main():
    get_count_items()
    create_folders()
    get_recepty()


if __name__ == '__main__':
    main()
