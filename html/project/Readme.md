# Admin 페이지 프론트단 제작 프로젝트 24.12.27
## 개요
- Kream 페이지중 일부를 크롤링 하여 Bootstrap(V.5.3)을 활용하여 재구성
--------

## 사용된 스택
<img width="316" alt="스크린샷 2024-12-27 오후 4 47 51" src="https://github.com/user-attachments/assets/bdbe45a4-3959-40b1-97df-14706e6438ec" />
<br>
- HTML5 & Javascript
- Bootstrap v5.3


-----
## 메인 페이지
<img width="1511" alt="스크린샷 2024-12-27 오후 4 33 47" src="https://github.com/user-attachments/assets/c5c55571-9bfe-4215-90a3-576069406f72" />

------
## 요구사항 

- 카테고리를 클릭하면 상의, 하의, 신발, 패션잡화 메뉴가 나오게 코드 작성
- 입력 버튼 안에 “제품명을 입력해주세요”가 나오게 코드 작성
- 조회 버튼이 입력창 옆에 붙어 있도록 코드 작성
- 테이블을 이용해 최 상단에는 속성 값을 넣고 하단에는 데이터가 입력되도록 코드 작성
- 최 하단에는 페이지 네이션 기능이 나타나도록 코드 작성
- 오늘 날짜와 현재 시간을 볼 수 있도록 기능을 구현해주세요
- 다크모드 기능을 만들어주세요
- 성별을 선택할 수 있는 셀렉터를 추가해주세요
- 회원 가입 버튼을 만들고 회원가입 버튼을 누르면 회원 가입 폼이 나오도록 기능을 만들어주세요
-------
### 기능 구성 
- 페이지 상단에 현재 시간을 표시하였음
- Light 모드와 Dark 모드 버튼을 만들어 이벤트 발생 시 `localStroage`에 해당 테마가 저장되어 새로고침이나 다른 페이지로 넘어가도 선택한 테마를 유지할 수 있음
- 회원가입 버튼을 만들어 이벤트 발생 시 joinForm.html로 좌표를 설정하여 해당 페이지로 넘어감
- `<select>` 태그를 사용하여 카테고리 및 성별을 설정할 수 있음.
 <img width="1512" alt="스크린샷 2024-12-27 오후 4 56 54" src="https://github.com/user-attachments/assets/79a4d8c2-00f4-4d8a-a5c4-55b73b4b52e1" />
<img width="1512" alt="스크린샷 2024-12-27 오후 4 56 07" src="https://github.com/user-attachments/assets/ba92a754-88f4-49c4-82fc-74eb87c8b2e6" />

- 페이지 네이션을 활용하여 해당 페이지를 조회할 수 있음(버튼만 구현)
------

## 회원가입 페이지
<img width="1512" alt="스크린샷 2024-12-27 오후 5 01 49" src="https://github.com/user-attachments/assets/cb1be2ac-8830-48c4-b315-d0b709be091c" />

-----

## 요구사항 

- 원하는 직무 선택란, 자기소개 작성란, 리셋 버튼 제거
- 부트스트랩을 활용하여 자신만의 회원가입 폼 제작
- 회원가입 완료 시 회원가입 내용을 볼 수 있는 알림창이 나오도록 코드 작성
- 아이디, 비밀번호 등 유효성검사를 할 수 있는 코드를 추가해주세요 (구글 등의 웹사이트의 내용 참고)
- 다크모드 기능을 만들어주세요
- 간단한 html 파일을 만들고 회원가입 완료 시 페이지 전환이 될 수 있게 설정 해주세요
-------
### 기능 구성 
- 기본적인 유효성 검사는 태그마다 `required`사용하여 구현하였음
<img width="1497" alt="스크린샷 2024-12-27 오후 5 11 37" src="https://github.com/user-attachments/assets/9b892d1c-e633-41ff-9b17-b0936c8baffb" />
-------
- 비밀번호가 요구조건을 만족하지 못하거나 비밀번호 확인의 입력 값이 다를 시 빨간 글씨로 입력란 아래에 설정한 문구가 나타남
<img width="619" alt="스크린샷 2024-12-27 오후 5 13 58" src="https://github.com/user-attachments/assets/b237e907-c75d-43c3-8336-1584d9561a75" />
<img width="633" alt="스크린샷 2024-12-27 오후 5 13 47" src="https://github.com/user-attachments/assets/8a89c74a-1fe2-4f33-9cef-679885efabf4" />
<img width="672" alt="스크린샷 2024-12-27 오후 5 13 33" src="https://github.com/user-attachments/assets/df568e39-36b7-4d51-939d-8f941ffc7d2e" />
--------
- 요구 조건을 만족하여 가입 버튼을 누르면 회원의 이름과 안내창이 뜨고 후에 정보 페이지로 전환된다

<img width="511" alt="스크린샷 2024-12-27 오후 5 15 03" src="https://github.com/user-attachments/assets/dc957ea9-0da4-4cce-b3da-48fcceb9fe73" />
<img width="1522" alt="스크린샷 2024-12-27 오후 5 15 13" src="https://github.com/user-attachments/assets/9b9cb368-f8b0-4ceb-864b-0ff5cb6959b3" />

--------



