# TODO
### 딕셔너리 형태의 bool이 의미하는 것
```
bool([1,2,3] or [])
>>> True
```
- 함수형태에서 or이 의미하는 것과 딕셔너리 or 의 차이
```
## 함수형태 or 연산 : update와 동시에 결과 값을 반환하고 싶을 때
dic.update({'four': 4}) or dic
>>> {'four': 4, 'one': 1, 'three': 3, 'two': 2}
## 딕셔너리 or 연산
[1,2,3] or []
>>> [1,2,3]
```
### 실습 테이블 안에 있는 $표시되어있는 텍스트들 정규식으로 찾기.
- http://www.pythonscraping.com/pages/page3.html
### 실습 <span class="red">를 람다로 찾기.
- http://www.pythonscraping.com/pages/warandpeace.html

# 이해 안됐던 내용 공유
- p41. 모든 자식은 자손이지만, 모든 자손이 자식인게 아님.
- p51 람다표현식에서 이 태그를 찾는 이유. 
```
 soup.findall(lamda tag: len(tag,attrs) == 2)
  ## attrs가 key,value형태 찾는 것으로 key,value형태 2개인 것 찾기.
 <div class="body" id="content"></div>
```  

# 실습하면서 알게된 지식
> Calling a tag is like calling find_all()  
Because find_all() is the most popular method in the Beautiful Soup search API, you can use a shortcut for it. If you treat the BeautifulSoup object or a Tag object as though it were a function, then it’s the same as calling find_all() on that object. These two lines of code are equivalent:  
```
soup.find_all("a")
soup("a")
```
These two lines are also equivalent:
```
soup.title.find_all(string=True)
soup.title(string=True)
```
### 자손의 태그가 많을 경우, 첫 번째 태그가 출력됨.
```
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.parent.td);
```
### print(children) 은 출력되지 않음
- 원했던 것 : children의 tag정보를 출력하고 싶었음
- 실제 출력
```
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.parent.children);
>>> <list_iterator object at 0x000001EC48050550>
```
- 이유: children은 object이므로 객체 주소를 print하게됨
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#contents-and-children

### 여러 parser 사용
- lxml(beautiful soup) 또는 html parser(내장)
```
# bsObj = BeautifulSoup(html, "html.parser")
bsObj = BeautifulSoup(html, "lxml")

```

# 처음부터 끝까지 정리
- p33.2 원하지 않는 콘텐츠를 깍아내서 필요한 정보 얻기.
- p34 먼저 코드 생각하고 짜기.
- p35 네이밍 중요성

# Reference
### lambda in Java
- [Java 8 람다 표현식 자세히 살펴보기](https://skyoo2003.github.io/post/2016/11/09/java8-lambda-expression)
- [람다가 이끌어 갈 모던 Java](http://d2.naver.com/helloworld/4911107)
### lambda in python
- 'lambda는 왜 쓰는가?' - [초보몽키의 개발공부로그 - 강의노트 03. 파이썬 lambda, map, filter, reduce, dic](https://wayhome25.github.io/cs/2017/04/03/cs-03/)
- [점프투파이썬- lambda](https://wikidocs.net/32#lambda)
- 'Examples of reduce() / Exercises'-[Python3 Tutorial - Lambda, filter, reduce and map](https://www.python-course.eu/python3_lambda.php)
### find(), findAll() 공식문서
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all
###  정규표현식에 도움되는 사이트
- https://programmers.co.kr/learn/courses/11
- https://www.hackerrank.com/domains/regex

