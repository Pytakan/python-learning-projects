from bs4 import BeautifulSoup
import requests
import csv

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'# URL of the page to scrape
response = requests.get(url)# Get the HTML content of the page
html = response.text# Parse the HTML content before using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')# Create a BeautifulSoup object
#print(soup.prettify())# Print the prettified HTML
# Find all product titles and prices on the page
def extract_product_info(soup):
    products = soup.find_all('div', class_='thumbnail')
    product_info = []
    for product in products:
        title = product.find('a', class_='title')['title'].strip()
        price = product.find('span', itemprop='price').get_text(strip=True)
        rating = product.find('p', attrs={'data-rating': True})
        if rating:
            rating_count = int(rating['data-rating'])
        else:
            rating_count = 0
        product_info.append({
            'title': title,
            'price': price,
            'rating': rating_count
        })
    return product_info
product_info = extract_product_info(soup)
for info in product_info:
    print(f"Title: {info['title']}, Price: {info['price']}, Rating: {info['rating']}")\
# Короткая анотация по BeautifulSoup и методам для поиска
# find() - находит первый элемент, соответствующий критериям поиска.
# find_all() - находит все элементы, соответствующие критериям поиска.\
# find_parent() - находит родительский элемент.
# get() - позволяет получить значение атрибута элемента.
# select() - находит элементы с использованием CSS-селекторов.
# get_text() - извлекает текстовое содержимое элемента.
# attrs - позволяет искать элементы по любым атрибутам, например, {'data-rating': True}.
# prettify() - форматирует HTML для лучшей читаемости.
# strip() - удаляет лишние пробелы и символы новой строки из текста.
# requests - библиотека для выполнения HTTP-запросов и получения HTML-контента страницы.
# requests.get(url) - выполняет GET-запрос к указанному URL и возвращает объект ответа.
# response.text - содержит HTML-контент страницы в виде строки.

with open('products.csv', 'w', encoding='utf-8') as file:
   writer = csv.DictWriter(file, fieldnames=['title', 'price', 'rating'])
   writer.writeheader()
   writer.writerows(product_info)

print(f"{len(product_info)} products saved to products.csv")