javascript는 프로그래밍 언어로서 주로 명령을 내리기 위한 목적으로 사용된다.
자바스크립트에서의 객체는 이미 정의되어있다.
사용법
- 객체.data :일반적으로 속성이라고 함
- 객체.기능() : 일반적으로 메소드라고 함

window - 웹브라우저 객체
    console - 브라우저 내장객체 
명령 시 window 생략 가능 
        console.log()- 콘솔에 출력 ( 자바스크립트로 표현 가능한 데이터만 출력)

자료형 
숫자 
- int 
- float
- double

문자열
-

불리언
-

object
변수 선언 
let
- 변수명은 문자와 숫자, $,_만 포함 가능
- 변수명의 첫 번재 글자로 숫자는 올 수 없음
- 예약어 사용 안됨
상수 변수
const
placeholder ``
백틱 
${} 사용

confirm()   
document 쿼리 셀렉터 메소드는 선택자를 인자로 전달받아 전달받은 선택자와 일치하는 문서내 첫번째 요소를 반환

textContent :해당 객체(요소)가 포함하고 있는 텍스트 콘텐츠를 표현하는 속성 읽기, 쓰기가 가능, 코드 사이 공백도 포함시킴
p.textContent = asd; 쓰기
innerText = 위와 기능이 같다 코드 공백은 포함 안시킴

getElementBy 
- id 아이디 한개의 값만
- className 여러 클래스 전부

비교 연산자 
== 같다 - 추상적 비교 자료형 판단 X
=== 완전히 같다 - 자료형 까지 판단

write 메소드 
화면에 출력

createElement('해당태그')
프로그램 단계에서 만들어지기만 함 화면에 표시되진 않음 

target.appenChild(추가할 요소)
const p = document.createElement('p')
document.body.appendChild(p)

append와 appendChild 차이점
- append : 노드객체와 문자열 같이 추가 가능 반환 데이터 없음
- child : 노드 객체만 추가 가능 추가한 자식 노드 반환