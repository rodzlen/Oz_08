### Day1
Git 셋팅 순서
1. git init 
2. git config 설정
    - git config user.name "설정할 이름"
    - git config user.email "설정할 이메일"
    위 코드는 로컬로 설정한 것임 전역보다 우선순위로 적용된다.    
    전역으로 설정할 때는 ''' git config --global ''' 을 사용한다. 
3. git add 
    - '''git add .'''는 모든 변경된 사항을 스테이징 한다. 
    - ''' git add 파일명 ''' 특정 파일만 스테이징
4. git commit -m "커밋 메세지"

5. git remote add origin "레포지토리 주소"
    - origin은 주소라고 생각하면 됨 
6. git branch -M main 
    기본 브랜치가 master로 설정되어 있는 경우가 있기에 main으로 바꿔주어야 한다.
7. git push -u origin main
    - ''' -u'''를 사용하였기 때문에 앞으로는 git push만 해주면 된다
    
mkdir로 폴더 생성 
touch Readme.md로 파일 생성     
