## ch.03.1,2
- 핵심키워드 : 재귀
- '웹스크래핑'과 '웹크롤링' 용어를 구분해서 작성하자
  - 웹스크래핑 : 
  - 웹크롤링: 
  
> 웹 크롤러를 사용할 때는 반드시 대역폭에 세심한 주의를 기울여야 하며, 타깃 서버의 부하를 줄일 방법을 강구해야합니다. (p.53)

> 위키백과의 서버 부하에 대한 대책은? (...)기부 하십시오. (p.54)
- python 1000번만 재귀호출됨
- 예외처리 중요하다! (책 샘플코드에는 예외처리가 없음)

> 웹사이트 전체 크롤링은 언제 유용하고, 언제 손해일까요? 
  - 사이트맵 생성 / 데이터 수집
> 같은 페이지를 두 번 크롤링하지 않으려면 발견되는 내부 링크가 모두 일정한 형식을 취하고,프로그램이 동작하는 동안 계속 유지되는 리스트에 보관하는 게 대단히 중요합니다. 새로운 링크만 탐색하고 거기서 다른 링크를 검색해야 합니다.

> 파이썬은 기본적으로 재귀 호출을 1,000회로 제한합니다.(...) 멈추는 일을 막으려면 재귀 카운터를 삽입하거나 다른 방법을 강구해야 합니다.

> 결국 필자는 URL이 너무 우스꽝스러워 보이지는 않는지, 무한 루프로 보이는 반복된 조각이 들어 있지는 않는지 체크하는 코드를 삽입해야 했습니다. 이렇게 하지 않고 밤새 돌아가도록 내버려뒀더라면 금새 정지했을 겁니다.

> 이런 일을 가장 잘하기 위해 첫 번째 할 일은 사이트의 페이지 몇 개를 살펴보며 패턴을 찾는 일입니다.

## ch.03.3 인터넷 크롤링
- 어떤 경우에 웹사이트 전체 크롤링이 유용할까?
- 크롤링을 하기 전에 물을 질문들
  > 내가 수집하려 하는 데이터는 어떤 것이지?

  > 크롤러가 특정 웹사이트에 도달하면, 즉시 새 웹사이트를 가리키는 링크를 따라가야 할까? 아니면 한동안 현재 웹사이트에 머물면서 파고들어야 할까?  

  > 특정 사이트를 스크랩에서 제외할 필요는 없나. 
  > 만약 크롤러가 방문한 사이트의 웹마스터가 크롤러의 방문을 알아차렸다면 나 자신을 법적으로 보호할 수 있을까?  
- 프로그램 설계하기 전에, 순서도 작성해 로직 확인해보기 - p.82 그림 3-2 순서도
  > 실제 코드를 작성하기 전에 그 코드가 무슨 일을 하는지 다이어그램을 그려보거나 메모해보는 습관을 들이는 게 좋습니다. 크롤러가 복잡해지면 이런 습관이 시간을 매우 많이 절약해주고,좌절하는 일도 훨씬 줄어들 겁니다.
- 크롤러에서의 재귀처리
  > 이 크롤러가 방문한 사이트에 외부 링크가 하나도 없다면(흔치 않지만, 크롤러를 오래 실행한다면 언젠가 반드시 일어납니다), 이 프로그램은 파이썬의 재귀 제한에 걸릴 때까지 계속 실행됩니다.

- 크롤러에서의 페이지 리다이렉트 처리
  > 파이썬 3.x에서 제공하는 urllib 라이브러리가 리다이렉트를 자동으로 처리해주니까요

- scrapy : python3 에서도 사용가능 / [공식 문서](http://doc.scrapy.org/)
  > 스크래파이Scrapy는 웹사이트의 링크를 찾아서 분석하고, 도메인이나 도메인 목록 크롤링작업을 쉽게 해주는 파이썬 라이브러리입니다.
  - scrapy 로그수준 조절

- 오늘의 코드 : 페이지 링크 스크래핑 + 예외처리
  - 위키피디아 페이지 내에 있는 모든 링크 출력 (잘못된 url 입력시, 에러메시지 출력)
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# [궁금] random.seed() 왜 하죠? 
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    try: 
        html = urlopen("https://en.wikipedia.org"+articleUrl)
    except Exception as e:
        print(e)
    else:
        bsObj = BeautifulSoup(html, "html.parser")
        articleUrl = bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
        return articleUrl
    return list()
links = getLinks("/wiki/Jessica_Chastain")
# links = getLinks("/wiki/Main_page/wiki/Jessica_Chastain") # wrong input url - error

while len(links) > 0:
    #link 범위 내에서,무작위로 목록을 뿌려줌 / [궁금] 왜 random을 하는데 중복된 링크를 출력하지 않는지?
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"] 
    
    print(newArticle)
    links = getLinks(newArticle)
```


