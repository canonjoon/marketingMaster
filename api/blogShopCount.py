import urllib.request
import json


client_id = "2vI32KETz905YKR54cnv";
client_secret = "YpzyZUhkom";

NAVER_BLOG_API_URL = "https://openapi.naver.com/v1/search/blog?query="
NAVER_SHOP_API_URL = "https://openapi.naver.com/v1/search/shop?query="

keyword = "마스크";

def getSearchCount(keyword,URL):
    encText = urllib.parse.quote(keyword); # 키워드 문자를 utf-8fh 인코딩.
   # searchcount =10; # 검색 결과 수, 없을 땐 10개 기본.
    url = URL + encText   #  + "&display=" + str(searchcount); # 검색 + 검색수 10개, display 는 선택사항.
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    response_body = response.read();
    jsonString = response_body.decode('utf-8');
    jsonDict = json.loads(jsonString);
    items = jsonDict['items'];

    for item in items:
        title = item['title']
        link = item['link']
        print('Title : ',title,'Link : ',link)

    if(rescode==200): #json을 정상적으로 수신했을 때,
        totalCount = jsonDict['total']
        
    else:
        totalCount = 0;
    
   # searchTime = jsonDict['lastBuildDate'];   #검색 시간.
   # print(searchTime)
    return totalCount;

blogTotal = getSearchCount(keyword,NAVER_BLOG_API_URL);
# print("------------------------------------------------------------------------------------")
shopTotal = getSearchCount(keyword,NAVER_SHOP_API_URL);
print('Blog Total : ', blogTotal);
print('Shop Total : ',shopTotal);



