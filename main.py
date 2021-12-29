import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os

# lien de las pages à scrapper
url = "http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
url_cat_histoy = "http://books.toscrape.com/catalogue/category/books/history_32/index.html"
url_home = "http://books.toscrape.com/catalogue/category/books_1/index.html"

# recuperate le content de las pages
reponse = requests.get(url)
reponse_cat_history = requests.get(url_cat_histoy)
reponse_home = requests.get(url_home)

# accede au content de las pages
page = reponse.content
page_cat_history = reponse_cat_history.content
page_home = reponse_home.content

# transforme (parse) le HTML en objet BeautifulSoup (fail a lire)
soup = BeautifulSoup(page, "html.parser")
soup_cat_history = BeautifulSoup(page_cat_history, "html.parser")
soup_home = BeautifulSoup(page_home, "html.parser")

"""
Extraire des informations d'un livre
"""
# recuperation du product page URL
tout_url_prod = 'http://books.toscrape.com/catalogue' + soup_cat_history.find("a", {"title": "Sapiens: A Brief History"
                                                                                             " of Humankind"}
                                                                              )['href'][8:]
# recuperation UPC
tout_td = soup.find_all("td")
universal_product_code = []
for code_product in tout_td:
    universal_product_code.append(code_product.string)
upc = universal_product_code[0]
# print(upc)

# recuperation de titre
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
category_book = category_list_book[3]
# print(category_book)

# récupération du review rating
review_rating = universal_product_code[6]
# print(review_rating)

# récupération de l'image URL
images = soup.findAll('img')[1]['src']
url_img = 'http://books.toscrape.com/' + images[6:]
# print(url_img)

# création du fichier Books to Scrape(1livre+1catégorie).csv
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

# création du dossier Téléchargements
dir_tel = 'Téléchargements'
if not os.path.exists(dir_tel):
    os.mkdir(dir_tel)

# écrire fichier
with open(dir_tel + '/Books to Scrape(1livre+1catégorie).csv', 'w', newline='', encoding='utf-8') as fichier_csv:
    print('Téléchargement en cours des informations du livre choisie...')
    # permet d'ecrire dans csv
    writer = csv.writer(fichier_csv, delimiter=',')
    # écrire la premiere line
    writer.writerow(en_tete)
    writer.writerow([tout_url_prod, upc, titre_book, price_tax, price_s_tax, number_available, description_text,
                     category_book, review_rating, url_img])
    print('Téléchargement terminé')
    print('Téléchargement en cours des informations des livres de la catégorie choisie...')

"""
Extraire les informations de tous les livres de la catégorie choisie : Mystery
"""
# URL de la catégorie choisie
url_mystery = 'http://books.toscrape.com/catalogue/category' + soup_home.findAll('a')[4]['href'][2:]
# print(url_mystery)

# pagination
for i in range(3):
    url_cat_mystery = "http://books.toscrape.com/catalogue/category/books/mystery_3/page-" + str(i) + ".html"
    # recuperate le content de la page
    reponse_cat_mystery = requests.get(url_cat_mystery)
    # accede au content de la page
    page_cat_mystery = reponse_cat_mystery.content
    # transform (parse) le HTML en objet BeautifulSoup (fail a lire)
    soup_cat_mystery = BeautifulSoup(page_cat_mystery, "html.parser")

    # URL de chaque livre de la catégorie choisie
    urls_mystery = []
    div_container = soup_cat_mystery.find_all(class_='image_container')
    for a in div_container:
        urls_a_mystery = a.find('a')
        # print(urls_a_mystery)
        urls_href_mystery = urls_a_mystery['href']
        # print(urls_href_mystery)
        urls_mystery.append('http://books.toscrape.com/catalogue' + urls_href_mystery[8:])
    # print(urls_mystery)

    # utilisant les URL de tous les livres=> boucle for + code de la première partie
    for ch_book in urls_mystery:
        # recuperate le content de la page
        reponse_ch_page_mystery = requests.get(ch_book)
        # accede au content de la page
        page_ch_page_mystery = reponse_ch_page_mystery.content
        # transform (parse) le HTML en objet BeautifulSoup (fail a lire)
        soup_ch_page_mystery = BeautifulSoup(page_ch_page_mystery, "html.parser")

        # recuperation UPC
        tout_td_ch_page_mystery = soup_ch_page_mystery.find_all("td")
        # print(tout_td_ch_page_mystery)
        upc_ch_book_mystery = []
        for upc in tout_td_ch_page_mystery[0]:
            upc_ch_book_mystery.append(upc.string)
        # print(upc_ch_book_mystery)

        # recuperation du titres
        h1_ch_page_mystery = soup_ch_page_mystery.find("h1")
        # print(h1_ch_page_mystery.text)
        titre_ch_book_mystery = []
        for titre in h1_ch_page_mystery:
            titre_ch_book_mystery.append(titre)
        # print(titre_ch_book_mystery)

        # récupération du price including tax
        price_tax_ch_book_mystery = tout_td_ch_page_mystery[2].text
        # print(price_tax_ch_book_mystery)

        # récupération du price excluding tax
        price_s_tax_ch_book_mystery = tout_td_ch_page_mystery[3].text
        # print(price_s_tax_ch_book_mystery)

        # récupération du number available
        number_available_ch_book_mystery = tout_td_ch_page_mystery[5].text
        # print(number_available_ch_book_mystery)

        # récupération du review rating
        review_rating_ch_book_mystery = tout_td_ch_page_mystery[6].text
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

        # création du fichier Books to Scrape(1livre+1catégorie).csv
        with open(dir_tel + '/Books to Scrape(1livre+1catégorie).csv', 'a', newline='', encoding='utf-8') as \
                fichier_csv:
            # permet d'ecrire dans csv
            writer = csv.writer(fichier_csv, delimiter=',')
            writer.writerow([ch_book, upc, titre, price_tax_ch_book_mystery, price_s_tax_ch_book_mystery,
                             number_available_ch_book_mystery, review_rating_ch_book_mystery,
                             description_ch_book_mystery, category_ch_book_mystery, url_img_ch_book_mystery])
print('Téléchargement terminé : Téléchargements/Books to Scrape(1livre+1catégorie).csv')
print('Téléchargement en cours de toutes les images des livres')

# création du dossier Images
dir_images = 'Images'
if not os.path.exists(dir_images):
    os.mkdir(dir_tel + '/' + dir_images)

# Pagination
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
        for urls in div_cont_tous_books:
            urls_a_tous_books = urls.find('a')
            urls_href_tous_books = urls_a_tous_books['href']
            urls_tous_books.append('http://books.toscrape.com/catalogue/' + urls_href_tous_books[6:])
        # print(urls_tous_books)

        """
        Télécharger et enregistrer le fichier image de chaque page Produit
        """
        # URL toutes images
        links_images = soup_tous_books.find_all("img")
        # print(links_images)
        for link in links_images:
            links_img = 'http://books.toscrape.com/' + link['src'][9:]
            name_img = link['src'][-36:]
            print(name_img)
            with open(dir_tel + '/' + dir_images + '/' + name_img, 'wb') as fichier:
                im = requests.get(links_img)
                fichier.write(im.content)
print('Téléchargement des images terminé: Téléchargements/Images/...')
print('Téléchargement en cours des informations des livres des différents catégories')

"""
Extraire les informations produit de tous les livres appartenant aux différentes catégories
"""
# Text catégories
ul_categories = soup_home.find('ul', class_='nav nav-list')
# print(ul_categories)
categorie_text = []
for a_categories in ul_categories:
    categorie_text = a_categories.text.split()
    # print(categorie_text)

# utilisant les URL de tous les livres=> boucle for + code de la première partie
for chs_books in urls_tous_books:
    # recuperate le content de la page
    reponse_chs_books = requests.get(chs_books)
    if reponse_chs_books.ok:
        # accede au content de la page
        page_chs_books = reponse_chs_books.content
        # transform (parse) le HTML en objet BeautifulSoup (fail a lire)
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
        price_tax_chs_books = td_chs_books[2].text
        # print(price_tax_chs_books)

        # récupération du price excluding tax
        price_s_tax_chs_books = td_chs_books[3].text
        # print(price_s_tax_chs_books)

        # récupération du number available
        number_available_chs_books = td_chs_books[5].text
        # print(number_available_chs_books)

        # récupération du review rating
        review_rating_chs_books = td_chs_books[6].text
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
        img_chs_book = soup_chs_books.find('img')
        name_img_chs_book = img_chs_book['alt']
        # print(name_img_chs_book)
        url_img_chs_book = 'http://books.toscrape.com/' + img_chs_book['src'][6:]
        # print(url_img_chs_book)

        # création du fichier Books to Scrape.csv
        with open("Books to Scrape.csv", "a", encoding='utf-8', newline="") as f:
            k = csv.writer(f, delimiter=',')
            with open("Books to Scrape.csv", "r", encoding='utf-8', newline="") as fs:
                reader = csv.reader(fs)
                if not [row for row in reader]:
                    k.writerow(en_tete)
                    k.writerow([chs_books, upc_chs_books, titre_ch_book_mystery, price_tax_chs_books,
                                price_s_tax_chs_books, number_available_chs_books, description_chs_books,
                                category_chs_books, review_rating_chs_books, url_img_chs_book])
                else:
                    k.writerow([chs_books, upc_chs_books, titre_ch_book_mystery, price_tax_chs_books,
                                price_s_tax_chs_books, number_available_chs_books, description_chs_books,
                                category_chs_books, review_rating_chs_books, url_img_chs_book])

# écriture des données dans un fichier CSV distinct pour chaque catégorie de livres
# Pandas select category
# read csv
data = pd.read_csv('Books to Scrape.csv')

cat_text = ['Travel', 'Mystery', 'Historical Fiction', 'Sequential Art', 'Classics', 'Philosophy', 'Romance',
            'Womens Fiction', 'Fiction', 'Childrens', 'Religion', 'Nonfiction', 'Music', 'Default', 'Science Fiction',
            'Sports and Games', 'Add a comment', 'Fantasy', 'New Adult', 'Young Adult', 'Science', 'Poetry',
            'Paranormal', 'Art', 'Psychology', 'Autobiography', 'Parenting', 'Adult Fiction', 'Humor', 'Horror',
            'History', 'Food and Drink', 'Christian Fiction', 'Business', 'Biography', 'Thriller', 'Contemporary',
            'Spirituality', 'Academic', 'Self Help', 'Historical', 'Christian', 'Suspense', 'Short Stories', 'Novels',
            'Health', 'Politics', 'Cultural', 'Erotica', 'Crime']

# création du dossier Info livres par catégorie
dir_info = 'Info livres par catégorie'
if not os.path.exists(dir_info):
    os.mkdir(dir_tel + '/' + dir_info)

for c in cat_text:
    print('...' + c)
    is_cat_boolean = data["category"] == c
    is_cat = data[is_cat_boolean]
    # print(is_cat)
    mystery_csv = is_cat.to_csv(dir_tel + '/' + dir_info + '/' + c + '.csv', index=False)
    print('Téléchargement terminé: Téléchargements/Info livres par catégorie/', c, '.csv')
