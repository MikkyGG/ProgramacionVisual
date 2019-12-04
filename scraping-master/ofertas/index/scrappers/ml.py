import requests
from bs4 import BeautifulSoup
from csv import writer


def getitemsml():
    response = requests.get('https://www.mercadolibre.com.mx/ofertas')

    soup = BeautifulSoup(response.content,'html.parser')

    posts = soup.find(class_='items_container')

    offers = posts.find_all(class_='promotion-item-b')

    itemsML = []

    for post in offers:
        today_offer = post.find(class_='promotion-item-b__today-offer-text')
        if today_offer:
            title = post.find(class_='promotion-item-b__title').get_text().replace('\n','')
            url = post.find('a')
            print(url['href'])
            new_price = post.select('.promotion-item-b__price')[0].get_text()
            old_price = post.find(class_='promotion-item-b__oldprice').get_text()
            img = post.find('img')

            data = {
                'item': {
                    'url': url['href'],
                    'img': img['data-src'],
                    'title': title,
                    'old_price': old_price,
                    'new_price_span': new_price
                }
                }
            itemsML.append(data)
    return itemsML


getitemsml()