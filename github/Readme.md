### Day 01
1. git init 
2. git config 설정
    - git config user.name "설정할 이름"
    - git config user.email "설정할 이메일"
    위 코드는 로컬로 설정한 것임 전역보다 우선순위로 적용된다.    
    전역으로 설정할 때는  git config --global  을 사용한다. 
3. git add 
    - git add . 는 모든 변경된 사항을 스테이징 한다. 
    - git add 파일명 특정 파일만 스테이징
    - git rm --cached 스테이징 취소를 원하는 파일명 (해당 코드는 스테이징 취소)
    - 모든 스테이징을 취소할 땐 git reset을 이용
4. git commit
    - git commit -m "커밋 메세지"

    - git commit -am "커밋 메시지" (변경된 사항을 바로 add 하고 커밋)

5. git remote add origin "레포지토리 주소"
    - origin은 주소라고 생각하면 됨 
6. git branch -M main 
    기본 브랜치가 master로 설정되어 있는 경우가 있기에 main으로 바꿔주어야 한다.
7. git push -u origin main
    -  -u 를 사용하였기 때문에 앞으로는 git push만 해주면 된다

### Day 02
8. git log 
    - git log -p 각 커밋들의 변경사항 함께 보기

    - git log -(숫자) 최근 n개의 커밋 보기
    
    - git log --oneline 한 줄로 보기 

    - git log -S (검색어) 변경사항 내 단어 검색 

    - git log --grep (검색어) commit 메세지로 검색

    - git log --all --decorate --oneline --graph    자주 사용되는 그래프로 로그 보기

9. git reset 
    - git reset --hard [커밋 해시]
    - git reset --soft [커밋 해시]
    - git reset --hard [커밋 해시]

10. git reflog
    - reset으로 사라진 커밋을 복구할 수있음
    - git reset --hard 해당 해시를 입력하면 다시 돌아갈 수 있다. (헷갈림 주의)

11. git revert *현업에서 주로 사용*
    - 원하는 시점의 커밋된 내용만 되돌림 (이전의 다른 이력을 바꾸지 않음)
    - 되돌린 내용에 대해 새로운 커밋을 생성함 (해시값도 달라짐)

    * 오류 시 해당 문제를 해결하고 아래 명령어로 다시 진행
    - git revert --countinue
    * 자동 커밋되지 않고 변경 이력만 되돌릴 때 아래명령어 진행
    - git revert --no-commit (되돌릴 커밋 해시)

12. git branch
    - branch는 하나의 작업 단위, 각각의 기능
    - Main코드는 건들지 않는다. Merge를 사용해 병합시킴

    - git branch (브랜치 이름) -- 브랜치를 생성한다
    - git switch 브랜치명 -- 브랜치 이동
    - git switch -c 브랜치 이름 -- 브랜치 만들고 바로 이동
    - git branch -d 브랜치명 -- 해당 브랜치를 삭제
    - git branch -m 기존브랜치명 새 브랜치명 -- 해당 브랜치 이름을 바꿈

13. HEAD 
    - 해당 branch의 마지막 commit을 뜻함
        즉, HEAD가 특정 commit에 위치하고 있다면 그 branch의 가장 마지막 commit이라고 해석할 수 있음

