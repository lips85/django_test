# Django 정리

## 1. 가상환경 확인

>### 1. [poetry 다운](https://python-poetry.org/docs/>#installing-with-the-official-installer)
>
>### 2. 만들기
>
>```zsh
>poetry init
>이후
>License []:  MIT
>
>poetry add django
>```
>
>### 3. 가상환경에 접속방법
>
>```zsh
>poetry shell
>```
>
>### 4. 나가고 싶을 때
>
>```zsh
>exit
>```
>
>### 5. gitignore
>
>```내부
>ctrl +shift + p => gitignore
>```

## 2. oop 개념정리 필요 (나중에 다시 작성)

>
>### 1. Encapsulation
>
> 캡슐에 넣는다...
>
>### 2. Inhere
>

## 3. django 실행

>
> ## 1. 명령어 순서
>
>```powershell
>path 추가 - 시스템 환경변수
>poetry shell                        #가상환경 진입
>python .\manage.py runserver        #서버 실행
>
>python manage.py migrate            # migration 오류시
>
>python .\manage.py createsuperuser  # 유저 만들기
>python .\manage.py startapp houses  # house app 만들기
>python .\manage.py makemigrations   # house migration
>python .\manage.py migrate          # migration 적용
>```
>
>
