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
