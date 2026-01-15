import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")
# print(response.text)
soup = BeautifulSoup(response.text,"html.parser")
result = soup.find('span', class_='text')
print(result.text)

with open('D:\pythone\Pythone(12-1-25)\output3.txt','w') as f:
        f.writelines(result.text)