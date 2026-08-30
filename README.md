# 가나 7일 · 로마자 언어 학습

원고용지(원고지) 모양의 한 페이지짜리 외국어 학습 자료. 빌드도 프레임워크도 없이
HTML 파일 하나가 그대로 학습 페이지가 된다.

배포: **https://seongilp.github.io/hira/**

## 담고 있는 것

| 파일 | 내용 |
|---|---|
| `index.html` | 히라가나·가타카나 7일 커리큘럼 (직접 편집) |
| `italian.html` · `french.html` · `spanish.html` | 이탈리아어 · 프랑스어 · 스페인어 (생성물) |

일본어 페이지는 가나 학습이라 구조가 달라서 손으로 관리하고,
로마자 세 언어는 **공통 템플릿 하나 + 언어별 데이터 파일**로 생성한다.
CSS·탭 구조·퀴즈 엔진이 세 페이지에서 완전히 같아서, 손으로 세 벌을 고치면 반드시 어긋나기 때문이다.

## 실행

빌드 도구도 의존성도 없다. 파일을 그대로 열면 된다.

```bash
python3 -m http.server 8000   # http://localhost:8000
```

로마자 언어 페이지를 다시 만들려면:

```bash
python3 build/build.py
```

`build/langs/*.py` 를 전부 읽어 저장소 루트에 HTML 을 쓰고, `index.html` 의 언어 전환 바도 같이 맞춘다.
표준 라이브러리만 쓴다. 생성 규칙과 언어 추가 방법은 [`build/README.md`](build/README.md) 에 있다.

## 구조

```
index.html            가나 7일 (직접 편집)
italian.html          ┐
french.html           ├ build/build.py 가 생성 — 직접 고치면 다음 실행 때 덮어쓴다
spanish.html          ┘
build/
  build.py            CSS · HTML 뼈대 · JS 엔진 · 섹션 정의
  langs/*.py          언어별 데이터 (LANG 딕셔너리 하나)
```

## 기술 스택

바닐라 HTML/CSS/JS · Google Fonts (Shippori Mincho, IBM Plex Sans KR) ·
페이지 생성기는 파이썬 표준 라이브러리만 사용

## 주의

- `build/build.py` 를 고치면 **로마자 세 페이지가 전부 바뀐다.**
- 생성된 HTML 을 직접 손보면 다음 실행 때 사라진다. 고칠 곳은 `build/langs/` 다.
- 재생성은 결정적이다 — 데이터를 안 건드리고 실행하면 파일이 바이트 단위로 그대로여야 한다.
