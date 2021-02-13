#### 1. [컴파일, 빌드, 배포](https://itholic.github.io/qa-compile-build-deploy/#:~:text=%EC%A6%89%2C%20%EC%88%9C%EC%84%9C%EB%8C%80%EB%A1%9C%20%EB%B3%B4%EC%9E%90%EB%A9%B4%20%EC%BB%B4%ED%8C%8C%EC%9D%BC,%ED%95%9C%EB%8B%A4'%20%EB%9D%BC%EA%B3%A0%20%ED%91%9C%ED%98%84%ED%95%98%EA%B8%B0%EB%8F%84%20%ED%95%9C%EB%8B%A4.)
- {컴파일 : 번역, 빌드 : 출간, 배포 : 진열대 전시}

#### 2. [Generic 하다](https://soooprmx.com/archives/5852)
- 함수가 인자의 Type을 다양하게 받고 그에 맞게 처리하는 방식을 말한다.
- 파이썬은 동적언어이기 때문에 사실상 필요하지는 않다. 정적언어에서 필요한 성질.

#### 3. [Side Effects](https://runestone.academy/runestone/books/published/fopp/Functions/SideEffects.html)
- 함수나 expression이 외부 상태에 영향을 줄 때 side effect가 있다고 한다.
- [참고자료](https://dojang.io/mod/page/view.php?id=2358)

#### 4. [Tail Recursion](https://medium.com/@soyoung823/tail-recursion-%EA%BC%AC%EB%A6%AC-%EC%9E%AC%EA%B7%80-a84c2cd9a7e8)
- Recursion에서 return 시에 함수의 결과가 연산에 사용되지 않고 바로 반환되어 call stack에 안 쌓임. -> stackoverflow 문제 회피
- 이렇게 하려면 return 할 때 연산이 들어가면 안 된다. ex) return n * f(n-1) 안 됨.

#### 5. [Serialization](https://medium.com/@lunay0ung/basics-%EC%A7%81%EB%A0%AC%ED%99%94-serialization-%EB%9E%80-feat-java-2f3eb11e9a8#:~:text=%EC%A7%81%EB%A0%AC%ED%99%94%EB%9E%80%20%EA%B0%9D%EC%B2%B4%EB%A5%BC%20%EB%B0%94%EC%9D%B4%ED%8A%B8,%EC%83%9D%EC%84%B1%ED%95%98%EC%97%AC%20%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94%20%EA%B2%83%EC%9D%B4%EB%8B%A4.)
- 객체를 플랫폼(언어, 메모리/파일/DB)에 의존하지 않는 ByteStream으로 변환하는 일

#### 6. [datetime format]
- %Y-%m-%d %H:%M:%S %Z

#### 7. Syntactic Sugar
- 없어도 작동하지만 있으면 편한 기능을 말하는듯...?
- python에서는 list comprehension이나 decorator 같은 애들

#### 8. 디버깅 [익히기](https://www.inflearn.com/course/pycharm-guide#)
- 디버그 마킹하고 실행하기
- Step in, out, into 개념 알기
- 식조사, Watchs, 디버그 마킹에 조건문 걸기

#### 9. 프로세서, 스레드 [얄코](https://www.youtube.com/watch?v=iks_Xb9DtTM)
- 현대의 컴퓨터는 여러개의 프로세스를 동시에 돌릴 수 있다. (멀티태스킹)
- 동시성(Concurrency)와 병렬성(Pararllelism)의 혼합으로 구성된다.
- 동시성 : 하나의 프로세서가 여러개의 프로세스를 Context Switching해가면서 일한다.
- 병렬성 : 프로세서 하나에 코어가 여러개 달려서 각각 동시에 진행한다.
- 스레드는 프로세스에 할당된 자원을 공유해서 사용한다. 반면 프로세스 끼리는 분할해서 사용한다.
- 멀티스레딩에는 단점도 있다. 공유 변수를 동시에 접근하면 에러가 난다. +1을 두 개가 동시에 하면 한 번 밖에 안 올라갈 수도 있다.
