import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('film_products.csv', 'w', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['Price', 'Description', 'Photo'])

# for items in stock

for ind in range(1, 5):
    url = f'https://filmcamerastore.co.uk/collections/latest-arrivals?filter.v.availability={ind}&grid_list=grid-view'
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        film_products = soup.find_all('div', class_='productitem')

        for product in film_products:
            product_img = product.img.attrs.get('src')
            product_img = 'https:' + product_img
            price = product.find('div', class_='price__current price__current--emphasize').span.span.text
            desc = product.h2.a.text
            desc = desc.replace('\n', '')
            desc = desc[10:-8]

            file_obj.writerow([price, desc, product_img])

    sleep(randint(12, 15))

# for items out of stock

for ind in range(1, 5):
    url2 = f'https://filmcamerastore.co.uk/collections/latest-arrivals?filter.v.availability=0&' \
          f'page={ind}&grid_list=grid-view'
    r2 = requests.get(url2)
    if r2.status_code == 200:
        soup = BeautifulSoup(r2.text, 'html.parser')
        film_products = soup.find_all('div', class_='productitem')

        for product in film_products:
            product_img = product.img.attrs.get('src')
            product_img = 'https:' + product_img
            price = 'Sold out'
            desc = product.h2.a.text
            desc = desc.replace('\n', '')
            desc = desc[10:-8]

            file_obj.writerow([price, desc, product_img])

    sleep(randint(12, 15))

file.close()


