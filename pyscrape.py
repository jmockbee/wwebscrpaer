import requests 
# changing name to bs
from bs4 import BeautifulSoup as bs

awscert  = input ('input aws:')
url = 'https://www.aws.training/certification' + awscert
r = requests.get(url)
soup = bs (r.content, 'html.parser')
account = soup.find ('div',{'class' : 'CertificationFeatureList'})
print (account)
