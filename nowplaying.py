import requests
import bs4

res = requests.get('https://www.cineplex.com/#cineplex-movies-grid')

soup =  bs4.BeautifulSoup(res.text, 'lxml') 

results = soup.find_all('a', href = True)

print('Top Rated Movies at Cineplex Right Now: \n')

for topRatedMovies in results:
    if '/Movie/' in topRatedMovies['href']:

        print(topRatedMovies.getText() + '\n')

        url = 'https://www.cineplex.com' + topRatedMovies['href']
        newRequest = requests.get(url)
        soups = bs4.BeautifulSoup(newRequest.text, 'lxml')
        moreResults = soups.find_all('strong', class_ = 'pad-right-sm margin-right-xs text-uppercase')
        lengthOfMovie = soups.find_all('span', class_ = 'md-movie-length')

        for releaseDate in moreResults:
            print('Release Date: ' + releaseDate.getText() + '\n')
        
        for movieLength in lengthOfMovie: 
            print('Length of Movie: ' + movieLength.getText() + '\n' + '\n')
            
    else: 
        pass
