import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

f = open('cars.csv', 'w', newline='\n', encoding="utf-8")
file = csv.writer(f)
file.writerow(['მარკა-მოდელი', 'გამოშვების წელი', 'განბაჟება', 'ფასი', 'სურათი'])
page = 1
page_count = 0
while page < 6:
    url ='https://ap.ge/ge/search?page='+str(page)
    r = requests.get(url)
    # print(r.status_code)
    # print(r.headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    car_list = soup.find('div', class_='boxCatalog')
    all_cars = car_list.find_all('div', class_='boxCatalog2')
    for car in all_cars:
        img_src = 'https://ap.ge/'+car.img.attrs.get('src')
        make_model = car.find('a', class_='with_hash2').text
        manu_year = car.find('div', class_='paramCatalog').text[4:12].strip()
        register_status = car.find('nobr').text
        price = car.find('div', class_='priceCatalog').text.strip()[:-1]
        file.writerow([make_model, manu_year, register_status, price, img_src])
    page_count += 1
    page += 1
    sleep(randint(2, 5))
    print("page parsed :", page_count)
f.close()


