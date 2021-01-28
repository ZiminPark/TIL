#### 1. [str, \_\_str\_\_](https://shoark7.github.io/programming/python/difference-between-__repr__-vs-__str__)

> str, repr 함수가 인스턴스의 \_\_str\_\_,  \_\_repr\_\_ 메소드를 각각 호출한다고 이해할 수 있다. 


#### 2. [@dataclass](https://sjquant.tistory.com/30)
- \_\_init\_\_, \_\_repr\_\_ 을 자동으로 정의해 준다.

#### 3. [enum](https://stackoverflow.com/questions/22586895/python-enum-when-and-where-to-use)
- They give a name to a constant. 정확히 이해 못했다. 변수처럼 바뀌는 걸 방지하기 위해 사용하는 듯?

#### 4. [under score convention](https://dbader.org/blog/meaning-of-underscores-in-python)
- private 으로 보호하고 싶을 때 쓴다.

#### 5. [Program, Process, Thread](https://www.youtube.com/watch?v=iks_Xb9DtTM&feature=youtu.be)
- 자세한 [설명+실습 and GIL](https://www.youtube.com/watch?v=RrfASw-jfZ4)
> - Program : 실행 가능한 파일
> - Process : 실행 중인 파일, 다른 프로세스와 자원 공유 X
> - Thread  : Process 안에서 스레드로 나누어서 작업

#### 6. itertools.chain
```import itertools
list2d = [[1,2,3], [4,5,6], [7], [8,9]]
merged = list(itertools.chain(*list2d))
```

#### 7. [python -m](http://pythonwise.blogspot.com/2015/01/python-m.html)
- script에서 module을 실행한다.
- 모듈이 directory로 구성된 경우 \_\_main\_\_.py를 실행한다.

#### 8. [logging](https://hamait.tistory.com/880)
- 다른 모듈에서 로깅을 하려면 루트 파일에서 로거를 설정해둬야 한다.

#### 9. [Overriding Parent's Parent's method](https://stackoverflow.com/questions/18117974/calling-a-parents-parents-method-which-has-been-overridden-by-the-parent)
- super(Father, self).__init__() : Father가 상속받는 메소드를 상속
- Gradfather.__init__(): Grandfather를 직접 상속

#### 10. [@classmethod와 @staticmethod](https://wikidocs.net/16074)
- 클래스에서 직접 접근이 가능.
- 다른 언어와 다르게 인스턴스에서도 접근 가능.
- @classmethod 와 @staticmethod의 차이는 상속할 때 차이

#### 11. [argparse 디테일들](https://donghwa-kim.github.io/argparser.html)
- action='store_true'를 사용하여 해당하는 인자(argument)가 입력되면 True, 입력되지 않으면 False로 인식하게 됩니다.
- argument로 list나 dictionary를 넘겨주고 싶을 때 어떻게 하는지.

#### 12. [UTC(Coordinated Universal Time)](http://blog.naver.com/PostView.nhn?blogId=rydnz&logNo=130031720733)
- 세계 기준인 UTC+00 이 있고 지역에 맞게 +- 한다. 
- 한국은 UTC+09이다.

#### 13. [\[\], subscription, \_\_getitem\_\_, \_\_setitem\_\_](https://stackoverflow.com/questions/43627405/understanding-getitem-method)
- \[\] 로 값을 가져오는 것은 class에 구현된 \_\_getitem\_\_을 실행한다는 의미


#### 14. [@property](https://www.programiz.com/python-programming/property)
- 변수를 보호하고 싶다.
- get\_\*,  set\_\* 으로 방어한다?
- refactoring에 어려움이 있다.
- `@property`를 사용하면 깔끔.

#### 15. [numba]
- 속도 빨라짐 : jit (just in time) 기능을 사용하여 프로그램 실행 시점에 기계어로 컴파일하여 인터프리터 속도를 향상한다. (c처럼) 특히 numpy 벡터 연산, loop를 다룰 때 빠르다.
- 사용법 : 함수에 @jit 데코레이터만 붙여주면 끝.
- 파라미터 : @njit 은 @jit 파라미터에 noptyon=True 를 준 상태 / Fastmath : 수치제약을 해제하여 부가적인 성능 향상/ Parallel  GIL 무시하고 병렬로 실행
- 자세한 내용은 [정리글](https://gurujung.github.io/dev/numba_user_performance-tips/),  [docs](https://numba.pydata.org/numba-doc/latest/user/5minguide.html#). 


#### 16. [Ellipsis](https://stackoverflow.com/questions/772124/what-does-the-ellipsis-object-do)
- ... 로 쓰이는 것의 명칭
- slicing할 때 쓰이는 경우도 있고 (e.g. a[..., :3])
- Type Hinting 할 때 쓰이는 경우도 있다. (Callable[..., int] <- int를 return하고 signature는 아무거나 가능)

#### 17. 다이아몬드 상속시 super.__init__()을 어떻게 처리할까 [링크](https://stackoverflow.com/questions/34884567/python-multiple-inheritance-passing-arguments-to-constructors-using-super)
- \*\*kwargs를 활용한다.
- Diamond inheritance patterns 은 오류가 나기 쉽다. 피할 수 있게 구조를 설계하자.
