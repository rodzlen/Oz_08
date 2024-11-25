# Day 06
## 함수
### 함수란 ?

    목적이 있는 코드 집합
```python
# 함수 선언
def oz():
    for i in range(6):ß
        print("oz")
# 함수 실행부 (호출)
oz()
```
#### print()
출력을 할 떄 사용하는 함수 

## 매개변수
### 가변 매개변수
 *values : object

**주의점**
* 가변 매개변수 뒤에는 일반 매개변수가 들어올 수 없다.
* 가변 매개변수는 호출당 한번만 사용 가능 

 
가변 매개변수 : 해당 뒤의 값들이 모두 파라미터로 들어감



### 기본 매개변수
sep :str | None = " ", end = ""

```python
def oz(value, n=2):
    for n in range(n):
        print("ㅂㅅ")


oz("인간",n= 30) # 기본 매개변수는 변형이 가능
```

### 재귀함수
스스로를 참조한다. ex)팩토리얼 함수

#### 팩토리얼 구하기
```python
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n)

fac(6)

```
#### 재귀함수 주의점
- stack overflow 가 발생할 수 있음
- 함수가 실행되면서 계속 생성하고 할당하기 때문에
메모리가 부족해 질 수 있다 : **메모리제이션** 필요

#### 피보나치 수열 
n +=  (n-1) + (n-2)

## tuple
튜플은 한번 값을 할당하면 바꿀 수 없다.

하지만 교환은 가능하다 
```
def tuple():
    return(1, 2)
x, y = tuple()
```
#### enumerate()
괄호를 제거한 값을 튜플로 반환
---


## 람다(Lamda)
함수 자체를 매개변수로 사용하기 쉽도록 하는 기능

### 콜백함수
함수의 매겨변수로 사용되는 함수

```python
def call(function) # 보통 콜백 파라미터로 받을 때 function 씀
    for i in range(5):
        function()

def talk():
    print("파이썬 이건 또 무슨개념?")

call(talk)
```

**map()** : 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성

```python
# 자기 자신을 ㄱ곱한 결과를 새로운 list로 만들어 주는 코드
def square(i):
    return i*i
numbers_list=[1,2,3,4,5,6,7,8,9,10]

result = map(square, numbers_list)
```
----
**filter()** : 리스트의 요소에 조건을 가진 함수를 넣고 True가 반환되는 요소를 반환
```python
def under(i):
    return i<5
result =filter(under, numbers_list)
```
해당 정보는 오브젝트로 반환된다. list()를 사용해서 형변환 해줘야 한다.

**lamda 사용**

map() 사용에 적용한 예
```python
square = lambda i : i * i
numbers_list=[1,2,3,4,5,6,7,8,9,10]

result = map(square, numbers_list)
```

filter()사용에 적용한 예

```python
under = lambda i : i < 5
numbers_list=[1,2,3,4,5,6,7,8,9,10]

result = filter(under, numbers_list)
```
## 제너레이터 
iterator를 생성하는 객체
iterator : next메소드를 갖고있고 순차적으로 다음 값을 리턴하는 객체

제너레이터는 함수안에 yield 키워드를 사용하여 만든다.
함수 안에 yield 키워드가 존재하기만 해도 제너레이터로 인식된다

제너레이터함수로 인식하면 호출해도 함수 내부 코드가 작동하지 않는다.

```python
def test():
    print("ㅈㅔ너레이터 함수")
    yield "test"
```
- 출력 실행 안됨

## 파이썬 타입 힌트
동적 프로그래밍 언어

인터프리터 언어인 파이썬은 코드 실행시 데이터 타입을 추론한다. 파이썬은 데이터 타입이 정해져 있지 않기에 개발자가 원하면 언제든 바꿀 수 있다. 

때문에 소규모 프로젝트나 일회성 스크립트에서는 유연하기 때문에 빠르게 진행할 수 있다. 

하지만 프로젝트의 규모가 커지면 안정성이 약하여 치명적인 버그로 이어질 확률이 높다.

타입 힌팅 이라는 개발 프로세스를 도입해 사용할 수 있다.

### 변수 타입 어노테이션
3.x 버전에서 사용됨 

### 함수 타입 어노테이션
인자 타입과 반환 타입 두 곳에 추가 가능 
인자에 타입 어노테이션을 추가할 때는 변수와 동일한 문법을 사용

반환값에 대한 타입을 추가할 떄는 -> 사용
