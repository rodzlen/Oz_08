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