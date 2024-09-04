# 영화 추천 프로젝트 CINEMA - SCOPE

## CINEMA - SCOPE 프로젝트 정보

| 개발 기간 : 2023.05.17 ~ 2023.05.26

## 👩🏻‍💻 팀원
<table align="center">
  <tr width="300px">
    <td height="140px" align="center"> <a href="https://github.com/AndreaStudy">
      <img src="/image/hs.png" width="140px" /> <br><br> 정훈석 <br>(팀장) <br>(풀스택)</a> <br></td>
      <td height="140px" align="center"> <a href="https://github.com/SWan9710">
      <img src="image/sw.png" width="140px" /> <br><br> 정수완 <br>(팀원) <br>(프론트)</a> <br></td>
  </tr>
  <tr width="300px">
    <td align="center" width="250px">
      영화 데이터 수집 및 정제<br>
      db 구축<br>
      컴포넌트 세부 구조 정리<br>
      오류 수정 및 디버깅<br>
      vue-tinder, vue-anime 활용<br>
    </td>
    <td align="center" width="250px">
      컴포넌트 CRUD<br>
      세부 디테일 정의 <br>
      추가 기능 일부 구현 <br>
      CSS <br>
    </td>
  </tr>
</table>

## 🔧 기술 스택

### Front-End
<div>
  <img src="https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white">
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> 
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> 
</div>

### Back-End
<div>
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> 
</div>

## 🎯 구현 목표

- 사용자에게  인기순, 신작순, 장르별 인기순 원하는 영화를 추천.

- Tinder를 활용하여 랜덤으로 원하는 영화를 swipe를 통해 선택 할 수 있게 함.

- 검색을 통해 원하는 영화에 대한 정보를 제공

## ✏ 추가 기능

- vue-tinder 기능활용

- vue-anime 활용하여 넷플릭스처럼 처음 들어갈때 시선잡기용 로딩화면

- 슬라이싱을 활용한 내용 정리

- 모달창을 이용한 추가 내용 

## 📃 ERD

![system](/image/erd.png)

## 🎞 추가 구현 화면

### ⭐ Tinder

![system](/image/tinder.png)

- vue-tinder의 스와이핑을 통해 해당 영화의 좋아요의 싫어요 기능 구현

- api 통신을 스와이핑 마다 받아와 게임처럼 좋아하는 영화를 wish 리스트에 저장 가능

![system](/image/wish.png)

- vue-tinder 를 통해 위시리스트에 저장된 영화들

---

### ⭐ Slicing

![system](/image/slice.png)

- 슬라이싱 기능을 이용하여 화면에 나타나는 글자 수 동일하게 조절

- ... 버튼을 클릭하는 것으로 전체 내용이 나타남

---

### ⭐ Modal

![system](/image/modal.png)

- 모달창 기능을 구현하여 추가 내용 및 사진을 화면에 띄우게 함

- 사용자의 요구에 맞춰 동작 가능하도록 구현

