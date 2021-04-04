import csv
from bs4 import BeautifulSoup

with open('movie.html','r') as html_file:
    content = html_file.read()
    print(content)

    soup = BeautifulSoup(content,'lxml')
    movie_details= soup.find_all('div',class_='lister-item mode-advanced')

    file = open('imdb.csv', 'w+',encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['movie_name', 'movie_genre', 'movie_rating,Run_Time'])
    for movie in movie_details:
        movie_name= movie.find('h3', class_='lister-item-header').text.replace("\n","")
        movie_genre= movie.find('span',class_='genre').text.replace("\n","")
        movie_rating= movie.find('div',class_='inline-block ratings-imdb-rating').text.strip()
        RUN_TIME = movie.find('span', class_='runtime').text.replace("\n", "")
        # certificate= movie.find('span',class_='certificate').text
        print(f'movie_NMAE: {movie_name}\nmovie_GENRE: {movie_genre}\nRATING:{movie_rating}\nRUN_TIME:{RUN_TIME}')


        writer.writerow([movie_name,movie_genre,movie_rating,RUN_TIME])

    file.close()
