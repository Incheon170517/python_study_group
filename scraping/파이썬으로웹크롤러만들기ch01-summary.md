- 예외처리가 중요
  - 웹 크롤링 특성상, 웹의 구조 바뀌면 답이 없음. 예외처리 중요
  - 발생할 수 있는 에러 ([Beautiful Soup 4.4.0 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#))
    - part 'Errors when parsing a document' , 'Version mismatch problems', 'Miscellaneous' , 'Other parser problems'
- 범용 함수로 만들기
- virtualEnv 가상환경 만들어 프로젝트 관리
  - 라이브러리 설치시, 참조해서 쓰는 건지, 새로 설치해서 쓰는 건지?
  - [궁금] 가상환경 A 에서 '가'라이브러리 사용, 가상환경 B 에서 '가'라이브러리 사용한다고 하면, 중복으로 '가'라이브러리가 설치되는지, 중앙에서 한번 설치하고 참조해서 쓰는 개념인지? 컴퓨터 하드웨어 자원관리 차원에서 중복설치는 좀...
- Beautiful Soup는 html을 xml python 객체로 변환
  - 잘못된 html을 xml(well-formed) 로 바꿈
  - python '객체' 가 됨
