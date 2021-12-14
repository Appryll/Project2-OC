import requests
from bs4 import BeautifulSoup
import csv

# lien de la page à scrapper
url = "http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
url_cat_histoy = "http://books.toscrape.com/catalogue/category/books/history_32/index.html"
url_home = "http://books.toscrape.com/catalogue/category/books_1/index.html"

# recuperate le content de la page
reponse = requests.get(url)
reponse_cat_history = requests.get(url_cat_histoy)
reponse_home = requests.get(url_home)

# accede au content de la page
page = reponse.content
page_cat_history = reponse_cat_history.content
page_home = reponse_home.content

# affiche la page HTML
# print(page)

# transforme (parse) le HTML en objet BeautifulSoup (fail a lire)
soup = BeautifulSoup(page, "html.parser")
soup_cat_history = BeautifulSoup(page_cat_history, "html.parser")
soup_home = BeautifulSoup(page_home, "html.parser")

# recuperation du product page URL
tout_url_prod = 'http://books.toscrape.com/catalogue' + soup_cat_history.find("a", {"title": "Sapiens: A Brief History"
                                                                                             " of Humankind"}
                                                                              )['href'][8:]
# print(tout_url_prod)

# recuperation UPC
tout_td = soup.find_all("td")
universal_product_code = []
for code_product in tout_td:
    universal_product_code.append(code_product.string)
upc = universal_product_code[0]
# print(upc)

# recuperation du titres
titre = soup.find("h1")
titre_book = titre.string
# print(titre_book)

# récupération du price including tax
price_tax = universal_product_code[2]
# print(price_tax)

# récupération du price excluding tax
price_s_tax = universal_product_code[3]
# print(price_s_tax)

# récupération du number available
number_available = universal_product_code[5]
# print(number_available)

# récupération de la description
descriptions = soup.find_all("p")
description_textes = []
for description in descriptions:
    description_textes.append(description.string)
description_text = description_textes[3]
# print(description_text)

# récupération du category
categories = soup.find_all("a")
category_list_book = []
for category in categories:
    category_list_book.append(category.string)
# print(category_list_book[3])
category_book = category_list_book[3]
# print(category_book)

# récupération du review rating
review_rating = universal_product_code[6]
# print(review_rating)

# récupération de l'image URL
images = soup.findAll('img')[1]['src']
url_img = 'http://books.toscrape.com/' + images[6:]
# print(url_img)

"""
douxieme partie las url de cada libro en lista y despues for paracada una y la respuesta pasa por cada una
"""
# URL de la categorie choisie
url_mystery = 'http://books.toscrape.com/catalogue/category' + soup_home.findAll('a')[4]['href'][2:]
# print(url_mystery)

# URL de chaque livre de la categorie choisie
urls_mystery = []

""" var de la premiere maniere de le faire
titres_cat_mystery = []
urls_img_cat_mystery = []
price_cat_mystery = []
status_cat_mystery = []
img_cat_mystery = []
"""
# pagination
for i in range(3):
    url_cat_mystery = "http://books.toscrape.com/catalogue/category/books/mystery_3/page-" + str(i) + ".html"
    # recuperate le content de la page
    reponse_cat_mystery = requests.get(url_cat_mystery)
    if reponse_cat_mystery.ok:
        # accede au content de la page
        page_cat_mystery = reponse_cat_mystery.content
        # transform (parse) le HTML en objet BeautifulSoup (fail a lire)
        soup_cat_mystery = BeautifulSoup(page_cat_mystery, "html.parser")

        # URL toutes les livres de la categorie choisie
        div_container = soup_cat_mystery.findAll(class_='image_container')
        for a in div_container:
            urls_a_mystery = a.find('a')
            urls_href_mystery = urls_a_mystery['href']
            urls_mystery.append('http://books.toscrape.com/catalogue' + urls_href_mystery[8:])
# print(urls_mystery)

# deuxième maniere: utilisant les URL de toutes les livres=> boucle for + code de la premier partie

for ch_book in urls_mystery:
    # recuperate le content de la page
    reponse_ch_page_mystery = requests.get(ch_book)
    if reponse_ch_page_mystery.ok:
        # accede au content de la page
        page_ch_page_mystery = reponse_ch_page_mystery.content
        # transform (parse) le HTML en objet BeautifulSoup (fail a lire)
        soup_ch_page_mystery = BeautifulSoup(page_ch_page_mystery, "html.parser")

        # recuperation UPC
        tout_td_ch_page_mystery = soup_ch_page_mystery.find_all("td")
        td_ch_page_mystery = []
        for cod_prod_ch_page_mystery in tout_td_ch_page_mystery:
            td_ch_page_mystery.append(cod_prod_ch_page_mystery.string)
        upc_ch_book_mystery = td_ch_page_mystery[0]
        # print(upc_ch_book_mystery)

        # recuperation du titres
        h1_ch_page_mystery = soup_ch_page_mystery.find("h1")
        titre_ch_book_mystery = h1_ch_page_mystery.string
        # print(titre_ch_book_mystery)

        # récupération du price including tax
        price_tax_ch_book_mystery = td_ch_page_mystery[2]
        # print(price_tax_ch_book_mystery)

        # récupération du price excluding tax
        price_s_tax_ch_book_mystery = td_ch_page_mystery[3]
        # print(price_s_tax_ch_book_mystery)

        # récupération du number available
        number_available_ch_book_mystery = td_ch_page_mystery[5]
        # print(number_available_ch_book_mystery)

        # récupération du review rating
        review_rating_ch_book_mystery = td_ch_page_mystery[6]
        # print(review_rating_ch_book_mystery)

        # récupération de la description
        descriptions_p = soup_ch_page_mystery.find_all("p")
        description_ch_book_mystery = []
        for description in descriptions_p:
            description_ch_book_mystery.append(description.string)
        description_ch_book_mystery = description_ch_book_mystery[3]
        # print(description_ch_book_mystery)

        # récupération du category
        categories_a = soup_ch_page_mystery.find_all("a")
        category_ch_book_mystery = []
        for category in categories_a:
            category_ch_book_mystery.append(category.string)
        category_ch_book_mystery = category_ch_book_mystery[3]
        # print(category_ch_book_mystery)

        # récupération de l'image URL
        img_ch_book_mystery = soup_ch_page_mystery.findAll('img')[1]['src']
        url_img_ch_book_mystery = 'http://books.toscrape.com/' + img_ch_book_mystery[6:]
        # print(url_img_ch_book_mystery)

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
            # écrire la premiere line
            writer.writerow(en_tete)
            writer.writerow([tout_url_prod, upc, titre_book, price_tax, price_s_tax, number_available, description_text,
                             category_book, review_rating, url_img])
            for url, upc, titre, prix_tax, prix_s_tax, number_av, description, category, rating, url_img in zip(
                    urls_mystery, upc_ch_book_mystery, titre_ch_book_mystery, price_tax_ch_book_mystery,
                    price_s_tax_ch_book_mystery, number_available_ch_book_mystery, description_ch_book_mystery,
                    category_ch_book_mystery, review_rating_ch_book_mystery, url_img_ch_book_mystery):
                # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
                writer.writerow([url, upc, titre, prix_tax, prix_s_tax, number_av, description, category, rating,
                                 url_img])
"""
        # création du fichier data.csv
        file = open('data.csv', 'w', newline='')
        with file:
            header = ['product_page_url', 'universal_product_code(upc)', 'title', 'price_including_tax',
                      'price_excluding_tax', 'number_available', 'product_description',  'category',  'review_rating',
                      'image_url']
            writer = csv.DictWriter(file, fieldnames=header)

            writer.writeheader()
            writer.writerow({'product_page_url': tout_url_prod,
                             'universal_product_code(upc)': upc,
                             'title': titre_book,
                             'price_including_tax': price_tax,
                             'price_excluding_tax': price_s_tax,
                             'number_available': number_available,
                             'product_description': description_text,
                             'category': category_book,
                             'review_rating': review_rating,
                            'image_url': url_img})
            for url, upc, titre, prix_tax, prix_s_tax, number_av, description, category, rating, url_img in zip(
                    urls_mystery, upc_ch_book_mystery, titre_ch_book_mystery, price_tax_ch_book_mystery,
                    price_s_tax_ch_book_mystery, number_available_ch_book_mystery, description_ch_book_mystery,
                    category_ch_book_mystery, review_rating_ch_book_mystery, url_img_ch_book_mystery):
                # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
                writer.writerow({'product_page_url': {url},
                                 'universal_product_code(upc)': {upc},
                                 'title': {titre},
                                 'price_including_tax': {price_tax},
                                 'price_excluding_tax': {price_s_tax},
                                 'number_available': {number_av},
                                 'product_description': {description},
                                 'category': {category},
                                 'review_rating': {rating},
                                 'image_url': {url_img}})

                data1 = list(zip(urls_mystery, upc_ch_book_mystery, titre_ch_book_mystery, price_tax_ch_book_mystery,
                                 price_s_tax_ch_book_mystery, number_available_ch_book_mystery,
                                 description_ch_book_mystery, category_ch_book_mystery, review_rating_ch_book_mystery,
                                 url_img_ch_book_mystery))
                print(data1)
"""

"""
mystery = [urls_mystery,
           titres_cat_mystery,
           price_cat_mystery,
           status_cat_mystery,
           img_cat_mystery,
           ]
with open('data.csv', 'w') as fichier_csv:
    # permet d'ecrire dans csv
    writer = csv.writer(fichier_csv, delimiter=',')
    # écrire la premiere line
    writer.writerow(en_tete)
    writer.writerow([tout_url_prod, upc, titre_book, price_tax, price_s_tax, number_available, description_text,
                     category_book, review_rating, url_img])
    # writer.writerow(['URL categorie', 'Titre livre', 'Prix', 'Status', 'URL image'])
"""

""" premier maniere de faire l'exercice : utilisant la page de la categorie Mystery
        # title toutes les livres de la categorie choisie
        titres_h3 = soup_cat_mystery.findAll('h3')
        for h3 in titres_h3:
            titres_h3_mystery = h3.find('a')['title']
            titres_cat_mystery.append(titres_h3_mystery)

        # price toutes les livres de la categorie choisie
        price_mystery = soup_cat_mystery.find_all('p', class_='price_color')
        for prices in price_mystery:
            price_cat_mystery.append(prices.string)

        # status toutes les livres de la categorie choisie
        status = soup_cat_mystery.find_all('p', class_='instock availability')
        for stat in status:
            status_cat_mystery.append(stat.text[15:23])

        # img toutes les livres de la categorie choisie
        images = soup_cat_mystery.find_all('img')
        for img in images:
            img_cat_mystery.append('http://books.toscrape.com/' + img['src'][10:])

print(img_cat_mystery)
print(urls_mystery)
print(status_cat_mystery)
print(img_cat_mystery)
print(status_cat_mystery)
print(price_cat_mystery)
print(titres_cat_mystery)

"""
"""
troisieme partie
"""
# pagination
urls_tous_books = []
for i in range(51):
    url_tous_books = "http://books.toscrape.com/catalogue/category/books_1/page-" + str(i) + ".html"
    # recuperate le content de la page
    reponse_tous_books = requests.get(url_tous_books)
    if reponse_tous_books.ok:
        # accede au content de la page
        page_tous_books = reponse_tous_books.content
        # transform (parse) le HTML en objet BeautifulSoup (fail a lire)
        soup_tous_books = BeautifulSoup(page_tous_books, "html.parser")

        # URL tous books
        div_cont_tous_books = soup_tous_books.findAll(class_='image_container')
        for a in div_cont_tous_books:
            urls_a_tous_books = a.find('a')
            urls_href_tous_books = urls_a_tous_books['href']
            urls_tous_books.append('http://books.toscrape.com/catalogue/' + urls_href_tous_books[6:])
print(len(urls_tous_books))
print(urls_tous_books)

for chs_books in urls_tous_books:
    # recuperate le content de la page
    reponse_chs_books = requests.get(chs_books)
    if reponse_chs_books.ok:
        # accede au content de la page
        page_chs_books = reponse_chs_books.content
        # transform (parse) le HTML en objet BeautifulSoup (fail a lire)
        # print(reponse_chs_books)
        soup_chs_books = BeautifulSoup(page_chs_books, "html.parser")

        # recuperation UPC
        tout_td_chs_books = soup_chs_books.find_all("td")
        td_chs_books = []
        for cod_prod_chs_books in tout_td_chs_books:
            td_chs_books.append(cod_prod_chs_books.string)
        upc_chs_books = td_chs_books[0]
        # print(upc_chs_books)

        # recuperation du titres
        h1_ch_page_mystery = soup_chs_books.find("h1")
        titre_ch_book_mystery = h1_ch_page_mystery.string
        # print(titre_ch_book_mystery)

        # récupération du price including tax
        price_tax_chs_books = td_chs_books[2]
        # print(price_tax_chs_books)

        # récupération du price excluding tax
        price_s_tax_chs_books = td_chs_books[3]
        # print(price_s_tax_chs_books)

        # récupération du number available
        number_available_chs_books = td_chs_books[5]
        # print(number_available_chs_books)

        # récupération du review rating
        review_rating_chs_books = td_chs_books[6]
        # print(review_rating_chs_books)

        # récupération de la description
        descr_p = soup_chs_books.find_all("p")
        description_chs_books = []
        for description in descr_p:
            description_chs_books.append(description.string)
        description_chs_books = description_chs_books[3]
        # print(description_chs_books)

        # récupération du category
        cat_a = soup_chs_books.find_all("a")
        category_chs_books = []
        for category in cat_a:
            category_chs_books.append(category.string)
        category_chs_books = category_chs_books[3]
        # print(category_chs_books)

        # récupération de l'image URL
        # img_chs_books = soup_chs_books.findAll('img')[1]['src']
        # url_img_chs_books = 'http://books.toscrape.com/' + img_chs_books[6:]
        # print(url_img_chs_books)

"""
# URL toutes les categories
div = soup_home.find_all(class_='side_categories')
# print(div)

links_categories = []
for a in div:
    as_books = a.find_all('a')[1:]
    links_categories.append(as_books)
    print(links_categories)
as_books = []
uls = soup_home.find_all('ul', class_='nav-list')
for ul in uls:
    uls_books = ul.find('ul')
    # print(uls_books)
    for a in uls_books:
        a_books = a.find('a')['href']
        as_books.append(a_books)
        print(as_books)



télécharger et enregistrer le fichier image de chaque page Produit que vous consultez

from urllib import request
# Define the remote file to retrieve
remote_url = ‘'
# Define the local filename to save data
local_file = ‘ ’
# Download remote and save locally
request.urlretrieve(remote_url, local_file)


import urllib
resource = urllib.urlopen("http://www.digimouth.com/news/media/2011/09/google-logo.jpg")
output = open("file01.jpg","wb")
output.write(resource.read())
output.close()
"""