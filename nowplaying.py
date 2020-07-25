import requests
import bs4

res = requests.get('https://www.cineplex.com/#cineplex-movies-grid')

soup =  bs4.BeautifulSoup(res.text, 'lxml') 

results = soup.find_all('a', href = True)

for moviesPlayingNow in results:
    if '/Movie/' in moviesPlayingNow['href']:
        print(moviesPlayingNow.getText() + '\n')
        
    else: 
        pass
