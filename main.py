import requests
from bs4 import BeautifulSoup
import csv

# lien de la page à scrapper
url = "http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
url_ppal_prod = "http://books.toscrape.com/catalogue/category/books/history_32/index.html"

# recuperate le content de la page
reponse = requests.get(url)
reponse_ppal_prod = requests.get(url_ppal_prod)

# accede au content de la page
page = reponse.content
page_ppal_prod = reponse_ppal_prod.content

# affiche la page HTML
# print(page)

# transforme (parse) le HTML en objet BeautifulSoup (fail a lire)
soup = BeautifulSoup(page, "html.parser")
soup_ppal_prod = BeautifulSoup(page_ppal_prod, "html.parser")

# recuperation du product page URL
tout_url_prod = soup_ppal_prod.find_all("a")
url_prod_dic = []
for ch_url_prod in tout_url_prod:
    url_prod_dic.append(ch_url_prod.string)
    # print(ch_url_prod.get('href'))
# print(url_prod_dic)
url_prod = url_prod_dic[54]


# recuperation UPC
tout_td = soup.find_all("td")
universal_product_code = []
for code_product in tout_td:
    universal_product_code.append(code_product.string)
upc = universal_product_code[0]
print(upc)

# recuperation du titres
titre = soup.find("h1")
titre_book = titre.string

print(titre_book)

# récupération du price including tax
price_tax = universal_product_code[2]
print(price_tax)

# récupération du price excluding tax
price_s_tax = universal_product_code[3]
print(price_s_tax)

# récupération du number available
number_available = universal_product_code[5]
print(number_available)

# récupération de la descriptions
descriptions = soup.find_all("p")
description_textes = []
for description in descriptions:
    description_textes.append(description.string)

description_text = description_textes[3]
print(description_text)

# récupération du category
categories = soup.find_all("a")
category_book = []
for category in categories:
    category_book.append(category.string)
print(category_book[3])

# récupération du review rating
review_rating = universal_product_code[6]
print(review_rating)

# récupération de l'image URL
images = soup.findAll('img')[1]
url_img = images['src']
print(url_img)

# création du fichier data.csv
en_tete = [
    'product_page_url',
    'universal_product_code(upc)',
    'title',
    'price_including_tax',
    'price_excluding_tax',
    'number_available',
    'product_description',
    'category',
    'review_rating',
    'image_url']

with open('data.csv', 'w') as fichier_csv:
    # permet d'ecrire dans csv
    writer = csv.writer(fichier_csv, delimiter=',')
    # écrir la premiere line
    writer.writerow(en_tete)

    # zip permet d'itérer sur deux listes à la fois

    for product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, \
        product_description, category, review_rating, image_url in zip(url_prod, upc, titre_book, price_tax,
                                                                       price_s_tax, number_available, description_text,
                                                                       review_rating, url_img):
        writer.writerows([product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                         number_available, product_description, category, review_rating, image_url])
