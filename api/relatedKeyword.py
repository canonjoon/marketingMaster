import time
from random import uniform
import urllib.request
import json
from powernad.API import RelKwdStat

#클라이언트 아이디,시크릿, 광고 아이디,라이센스.키



#여기까지


LIMIT = 30;
keywords =[];

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
    
    if(rescode==200): #json을 정상적으로 수신했을 때,
        totalCount = jsonDict['total']
        
    else:
        totalCount = 0;
    
   # searchTime = jsonDict['lastBuildDate'];   #검색 시간.
   # print(searchTime)
    return totalCount;


 
def naverRelKwdStat(keyword):
    relKwdStat = RelKwdStat.RelKwdStat(NAVER_AD_API_URL, NAVER_AD_ACCESS_LICENSE, NAVER_AD_SECRET_KEY, NAVER_AD_CUSTOMER_ID)
    kwDataList = relKwdStat.get_rel_kwd_stat_list(None, hintKeywords=keyword, showDetail='1')
    for idx, outdata in enumerate(kwDataList):
        time.sleep(uniform(0.3, 0.5)) # Naver search API limit - Daily 2500 Max 10/sec  
        relKeyword = outdata.relKeyword # A related keyword
        monthlyPcQcCnt = outdata.monthlyPcQcCnt # Sum of PC query counts in recent 30 days.
        monthlyMobileQcCnt = outdata.monthlyMobileQcCnt # Sum of Mobile query counts in recent 30 days. 
        # monthlyAvePcClkCnt = outdata.monthlyAvePcClkCnt # Average PC click counts per keyword's ad in recent 4 weeks
        # monthlyAveMobileClkCnt = outdata.monthlyAveMobileClkCnt # Average Mobile click counts per keyword's ad in recent 4 weeks. 
        monthlyAvePcCtr = outdata.monthlyAvePcCtr   # Click-through rate of PC in recent 4 weeks.
        monthlyAveMobileCtr = outdata.monthlyAveMobileCtr # Click-through rate of Mobile in recent 4 weeks.
        # plAvgDepth = outdata.plAvgDepth # Average depth of PC ad in recent 4 weeks. 
        compIdx = outdata.compIdx   # A competitiveness index based on PC ad. 

        blogsTotal = getSearchCount(relKeyword, NAVER_BLOG_API_URL)
        shopsTotal = getSearchCount(relKeyword, NAVER_SHOP_API_URL)                 

        if(str(monthlyPcQcCnt).isnumeric() or str(monthlyMobileQcCnt).isnumeric() or compIdx == "높음"):
            totalCnt = monthlyPcQcCnt + monthlyMobileQcCnt
            clickCnt = round(monthlyAvePcCtr + monthlyAveMobileCtr, 1)
            print(idx, relKeyword, totalCnt, clickCnt, blogsTotal, shopsTotal)
            keywords.append({ 'word': relKeyword, 'totalCnt': totalCnt, 'clickCnt': clickCnt, 'blogsTotal': blogsTotal, 'shopsTotal': shopsTotal })
            if(idx >= LIMIT):
                break

relKeyword = '마스크'
naverRelKwdStat(relKeyword)
