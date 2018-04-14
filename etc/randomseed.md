## Random_seed
- random.seed() 왜 할까?
```python
random.seed(datetime.datetime.now())
random.seed(3):  
```
- [python random.seed() 예제](https://www.tutorialspoint.com/python/number_seed.htm) : 같은 seed값을 넣으면 같은 난수를 생성함.
- [Random 함수 난수 발생 - C언어](http://simplesolace.tistory.com/entry/Random-함수-난수-발생)
같은 seed 값을 입력하면 같은 값이 생성되므로, 언제나 다른 seed 값을 넣어줘야함. 현실적으로 매번 다른 값 입력하는 것이 불가능하므로 날짜시간같은 항상 변하는 값을 넣어주도록 함.
- [python API](https://docs.python.org/3/library/random.html#random.seed) : default로 언제나 변하는 값을 seed값으로 함.
> random.seed(a=None, version=2). Initialize the random number generator.
If a is omitted or None, the current system time is used. If randomness sources are provided by the operating system, they are used instead of the system time (see the os.urandom() function for details on availability).
