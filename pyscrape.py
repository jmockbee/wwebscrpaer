import requests 
# changing name to bs
from bs4 import BeautifulSoup as bs

gecko  = input ('input gecko:')
url = 'https://www.coingecko.com/en' + gecko
r = requests.get(url)
soup = bs (r.content, 'html.parser')
picture = soup.find ('img',{'alt' :'CoinGecko Logo'}) ['src']
print (picture)
