import requests
import bs4

res = requests.get('https://www.cineplex.com/#cineplex-movies-grid')

soup =  bs4.BeautifulSoup(res.text, 'lxml') 

results = soup.find_all('a', href = True)

for topRatedMovies in results:
    if '/Movie/' in topRatedMovies['href']:
        print(topRatedMovies.getText() + '\n')
        
    else: 
        pass
