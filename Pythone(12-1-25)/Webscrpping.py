import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")
# print(response.text)
soup = BeautifulSoup(response.text,"html.parser")
result = soup.find_all('span', class_='text')
heading = soup.find('a')

with open('D:\pythone\Pythone(12-1-25)\output3.txt','w',encoding='utf-8') as f:
       f.write(heading.text + "\n")
       for x in result:
       
        f.writelines(x.text + "\n")
        f.writelines("...................\n")