#nowPlaying.py
#Cineplex Web Scraper
#Created by Dhruv Sharma on 2020-07-25
#Copyright © 2020 Dhruv Sharma. All rights reserved. 

import requests
import bs4

res = requests.get('https://www.cineplex.com/#cineplex-movies-grid')

soup =  bs4.BeautifulSoup(res.text, 'lxml') 
#res.text returns the whole html of the page. 

results = soup.find_all('a', href = True)
#finds an anchor tag within the whole html page and see's if the anchor has a href attribute within it 

print('Top Rated Movies at Cineplex Right Now: \n')

for topRatedMovies in results:
    if '/Movie/' in topRatedMovies['href']: 
        #the top rated movies gets just the href link from each for loop. This means that basically it will get /Movies/(The movie Name), but it looks for the /Movie/ in the actual href tag.  

        print(topRatedMovies.getText() + '\n')

        url = 'https://www.cineplex.com' + topRatedMovies['href']
        newRequest = requests.get(url)
        soups = bs4.BeautifulSoup(newRequest.text, 'lxml')
        moreResults = soups.find_all('strong', class_ = 'pad-right-sm margin-right-xs text-uppercase')
        lengthOfMovie = soups.find_all('span', class_ = 'md-movie-length') #looks for the specific class 

        for releaseDate in moreResults:
            print('Release Date: ' + releaseDate.getText() + '\n')
        
        for movieLength in lengthOfMovie: 
            print('Length of Movie: ' + movieLength.getText() + '\n' + '\n')
            
    else: 
        pass
