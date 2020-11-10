# Hince

> 화장품 쇼핑몰 사이트 [ Hince ] clone project

## Table of contents

- [General info](#general-info)
- [Modeling](#modeling)
- [Technologies](#technologies)
- [Features](#features)

## General info

- 개발기간 : 2020. 08. 18 - 2020. 08. 28
- 팀원 : Front-end(김영지, 이상훈, 이조은, 조은별) Back-end(김태하, 이태현)

## Modeling

- 사이트 : https://aquerytool.com/aquerymain/index/?rurl=e77a7f0c-b543-43cd-9805-19d8ff1db45e&
- 비밀번호 : 8l376t
₩
## Technologies

### Tools

- Git(Control Commit history by Squash and Rebase)
- [Agile](https://www.notion.so/0417taehyun/Portfolio-3368151da4144e178d48c652a13e5b2b#f9eef248bf3b451c805f44dacd277387)
- AWS

### Back-End

- Python
- Django Web Framework
- CORS headers
- Beautiful Soup
- Selenium
- MySQL
- Bcrypt, JWT
- RESTful API
- AWS (EC2, RDS)

## Features

### 담당 역할

#### 이태현

- **Beautiful Soup**과 **Selenium**을 활용한 동적 페이지 크롤링
- Python 스크립트를 통한 **MySQL 데이터 베이스** 구축
- **`request`** 와 **`Q`** 를 통한 여러 필터가 적용 되는 **하나의 RESTful API** 구현
- **`POST`** , **`GET`** , **`PETCH`** , **`DELETE`** 메서드를 사용하여 장바구니 **CRUD API** 구현
- **`prefetch related`** , **`annotate`** 와 **`F`** , **`aggregate`** 와 **`Sum`**  등의 **ORM 문법** 사용으로 코드 가독성, 효율성 증대
- **AWS RDS**와 **EC2**를 활용한 서버 배포