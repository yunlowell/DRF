## Sparta Market Using DRF

**Project Overview**
---
Sparta Market is a second-hand trading platform built using Django's extended package, DRF (Django REST Framework). Users can register, log in, and post items for sale.

**Development Period**
---
Start Date: 2024.09.06
End Date: 2024.09.10

**Full Technology Stack Overview**
---
Programming Language: Python 3.10
Web Framework: Django 4.2
Database: SQLite
IDE: Visual Studio Code
Version Control: Git, GitHub

**Main Features**
---
- User
  Sign-up and login functionality
  Profile viewing feature displaying username, email, name, nickname, birthday, gender, and bio
- Article
  CRUD functionality for posts (Create, Read, Update, Delete)
  Anyone can view posts, but only registered users can create, edit, or delete them.
  Users can only edit and delete their own posts.
  Posts can include an attached image, along with a title and description.

**Main Directories**
---
- spartamarket_DRF: Main project folder containing essential settings (e.g., settings.py).
- products: Handles CRUD operations for product posts.
- accounts: Manages user authentication, sign-up, and permissions.

**ERD Diagram**
---
![aPwEys5cRtBMSkcrr (1)](https://github.com/user-attachments/assets/b0ff010d-dc26-4d8f-86b2-9e0ee5c10cef)

**POSTMAN Test Results**
---
- Create Article
<img width="983" alt="KakaoTalk_20240910_111813745_11" src="https://github.com/user-attachments/assets/47ac1f3e-718f-4491-890a-ddf59add971d">

- View Article List
<img width="1010" alt="KakaoTalk_20240910_111813745_02" src="https://github.com/user-attachments/assets/0a957864-c2c7-4ac8-87a7-26bd28a1e498">

- View Article Detail
<img width="1001" alt="KakaoTalk_20240910_111813745" src="https://github.com/user-attachments/assets/24de8ef3-5979-43c7-abc6-e8f2f11c5d1f">

- Update Article

  When the user is the owner:
<img width="1023" alt="KakaoTalk_20240910_111813745_08" src="https://github.com/user-attachments/assets/2622926b-70b7-4168-b198-6df5869b113f">
  When the user is not the owner:
<img width="999" alt="KakaoTalk_20240910_111813745_06" src="https://github.com/user-attachments/assets/54925fb9-7efc-4d8f-b452-e834ce0241c0">

- Delete Article
<img width="1004" alt="KakaoTalk_20240910_111813745_09" src="https://github.com/user-attachments/assets/674164c7-eb64-4be2-88af-d8d84f80ca0a">

- Login
<img width="999" alt="KakaoTalk_20240910_111813745_07" src="https://github.com/user-attachments/assets/fede2457-dbd0-498c-8447-6e2eb153b6bc">

- Sign-up
<img width="991" alt="KakaoTalk_20240910_111813745_03" src="https://github.com/user-attachments/assets/1415b47f-ec48-4295-9073-d00ba73a9374">

- View Profile
<img width="1015" alt="KakaoTalk_20240910_111813745_10" src="https://github.com/user-attachments/assets/ffb12780-a780-443c-b318-e43648ad2398">

- Token
<img width="1009" alt="KakaoTalk_20240910_111813745_05" src="https://github.com/user-attachments/assets/f396b418-b360-4c10-9ef2-75fb4f931972">

**Project Structure**
---
```
Spartamarket_DRF/
│
├── accounts/          # App for user authentication and authorization
├── media/             # Folder for storing uploaded files
├── products/          # App managing product-related functionality
├── spartamarket_DRF/  # Project configuration files
├── .gitignore         # Files and directories to ignore in Git
├── manage.py          # Django management script
└── requirements.txt   # List of project dependencies
```



## DRF를 이용한 Sparta market
---
**프로젝트 소개**
---
Django의 확장 패키지인 DRF를 사용하여 구현한 Sparta market은 중고 거래 사이트입니다.
팔고 싶은 물건을 올릴 수 있고 회원가입 및 로그인이 가능합니다.

**개발기간**
---
- 시작일: 2024.09.06
- 종료일: 2024.09.10

**사용기술**
---
- Programming Language: Python 3.10
- Web Framework: Django 4.2
- Database: SQLite
- IDE: Vs code
- Version Control: Git, Github

**주요기능**
---
- 사용자
  회원가입, 로그인 기능, 프로필 조회 기능
  프로필에 usernme, email, name, nickname, birthday, gender, bio 표시  

- 게시물
  게시물 CRUD(생성, 읽기, 수정, 삭제) 기능
  목록조회는 모두가 가능하지만 그 외의 기능은 모두 회원만 사용 가능.
  자신이 작성한 글만 수정 및 삭제가 가능
  사진 첨부가 가능하며 제목과 내용을 적을 수 있음.

  **주요 폴더**
  ---
  - spartamarket_DRF
    프로젝트 폴더로 주요 설정 파일(예: `settings.py`)이 위치한 폴더입니다.
  - products
    제품과 관련된 CRUD(생성, 읽기, 수정, 삭제) 기능을 담담하는 앱입니다.
  - accounts
    사용자 로그인, 회원가입, 권한 관리 등의 기능을 처리하는 앱입니다.

  **ERD**
  ---
  ![aPwEys5cRtBMSkcrr (1)](https://github.com/user-attachments/assets/b0ff010d-dc26-4d8f-86b2-9e0ee5c10cef)


  **POSTMAN 실행 결과**
  ---
  - Article 생성
  <img width="983" alt="KakaoTalk_20240910_111813745_11" src="https://github.com/user-attachments/assets/47ac1f3e-718f-4491-890a-ddf59add971d">

  - Article 목록조회
  <img width="1010" alt="KakaoTalk_20240910_111813745_02" src="https://github.com/user-attachments/assets/0a957864-c2c7-4ac8-87a7-26bd28a1e498">

  - Article 상세 조회
  <img width="1001" alt="KakaoTalk_20240910_111813745" src="https://github.com/user-attachments/assets/24de8ef3-5979-43c7-abc6-e8f2f11c5d1f">

  - Article 수정
  
  본인 글일 때
  <img width="1023" alt="KakaoTalk_20240910_111813745_08" src="https://github.com/user-attachments/assets/2622926b-70b7-4168-b198-6df5869b113f">
  다른 사람의 글일 때
  <img width="999" alt="KakaoTalk_20240910_111813745_06" src="https://github.com/user-attachments/assets/54925fb9-7efc-4d8f-b452-e834ce0241c0">

  - Article 삭제
  <img width="1004" alt="KakaoTalk_20240910_111813745_09" src="https://github.com/user-attachments/assets/674164c7-eb64-4be2-88af-d8d84f80ca0a">

  - Login
  <img width="999" alt="KakaoTalk_20240910_111813745_07" src="https://github.com/user-attachments/assets/fede2457-dbd0-498c-8447-6e2eb153b6bc">
  - 회원가입
  <img width="991" alt="KakaoTalk_20240910_111813745_03" src="https://github.com/user-attachments/assets/1415b47f-ec48-4295-9073-d00ba73a9374">

  - Profile 조회
  <img width="1015" alt="KakaoTalk_20240910_111813745_10" src="https://github.com/user-attachments/assets/ffb12780-a780-443c-b318-e43648ad2398">

  - Token
  <img width="1009" alt="KakaoTalk_20240910_111813745_05" src="https://github.com/user-attachments/assets/f396b418-b360-4c10-9ef2-75fb4f931972">

  **폴더 구조**
  ---
  ```
  Spartamarket_DRF
  |
  |--accounts/    # 사용자 인증 권한을 처리하는 앱
  |--media/       # 사용자가 업로드한 파일을 저장하는 폴더
  |--products/    # 제품 관련 기능을 관리하는 앱
  |--spartamarket_DRF/    # 프로젝트 구성 파일
  |--.gitignore   # git에서 무시할 파일 및 디렉터리
  |--manage.py    # Django 관리 명령 파일
  |--reqirements.txt      # 프로젝트의 속성 목록
  ```
