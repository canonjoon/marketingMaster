import requests
from bs4 import BeautifulSoup

NAVER_100 = "https://search.shopping.naver.com/best100v2/main.nhn"
popular10lists =[]
categories =['인기검색', '패션의류', '패션잡화', '화장품/미용', '디지털/가젼', '가구/인테리어', '식품', '스포츠/레져', '출산/육아', '생활/건강']
source = requests.get(NAVER_100).text
soup = BeautifulSoup(source,"html.parser")

ymd = soup.select("p.ymd") #날짜
print(ymd[0].text.replace('.',""))

popular10 = soup.find(id="popular_srch_lst")
popular10names = popular10.select(".txt")

for name in popular10names :
    print(name.text)
    popular10lists.append(name.text)

categorylists = soup.select("ul.type_normal")
for idx, category in enumerate(categorylists):
   
    for i, item in enumerate(category.find_all('img')):
        name = item.get('alt')
        href = item.get('data-original')
        print(categories[idx],i,name,href)
    print( "--------------------------" + "\n")
    


    
    
   

