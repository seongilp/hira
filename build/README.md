# build — 로마자 언어 페이지 생성기

이탈리아어 · 프랑스어 · 스페인어 페이지는 **공통 템플릿 하나 + 언어별 데이터 파일**로 만든다.
세 페이지의 CSS · 탭 구조 · 퀴즈 엔진이 완전히 같아서, 손으로 세 벌을 고치면 반드시 어긋난다.

일본어 `index.html` 은 **가나 학습이라 구조가 다르므로 생성 대상이 아니다.**
직접 편집하고, 언어 전환 바만 이 스크립트가 맞춰 준다.

## 실행

```bash
python3 build/build.py
```

`build/langs/*.py` 를 전부 읽어 저장소 루트에 HTML 을 쓰고, `index.html` 의 언어 전환 바를 갱신한다.
의존성 없음(표준 라이브러리만). 실행 후 배포:

```bash
npx vercel deploy --prod --scope seongilp
```

## 구성

```
build/
  build.py          CSS · HTML 뼈대 · JS 엔진 · 섹션 정의
  langs/
    italian.py      LANG = { ... }
    french.py
    spanish.py
```

## 언어 추가하기

`build/langs/` 에 파일 하나를 더 놓고 `python3 build/build.py` 를 실행하면 끝이다.
기존 파일을 복사해 값만 갈아 끼우는 쪽이 빠르다.

```python
LANG = {
 'order': 4,                       # 언어 전환 바에서의 순서
 'nav': ('PORTUGUES', '포르투갈어'), # 전환 바 라벨 (영문, 한글)
 'file': 'portuguese.html',        # 저장소 루트에 쓸 파일 이름
 'serif': 'Lora',                  # Google Fonts 이름 (공백은 그대로)
 'grid': '#7B4B2A',                # 강조색. gl/glh 는 같은 색의 30% / 55% 투명도
 'gl':   'rgba(123,75,42,.30)',
 'glh':  'rgba(123,75,42,.55)',
 'title': '...', 'eyebrow': '...', 'h1': '...', 'h1sub': '...', 'lede': '...',
 's1': '01 섹션 제목', 's1sub': '01 섹션 설명',
 's8': '동사 섹션 제목', 's8sub': '동사 섹션 설명',
 'foot': '...',
 'data': { ... },   # 아래 참고
}
```

### data 안의 항목

| 키 | 쓰이는 곳 | 형태 |
|---|---|---|
| `p1` `p2` | 동사 카드의 두 활용 칸 라벨 | `'YO · 나'` |
| `soundRules` `numRules` `timeRules` `placeRules` `verbRules` `talkRules` `conjRules` | 각 섹션 위의 요령 카드 | `[태그, 제목, 본문HTML]` |
| `soundGroups` `numGroups` `timeGroups` `placeGroups` | 단어 표 | `{label, items:[[표기, 원어읽기, 한글발음, 뜻, 주의]], ex:[[문장, 한글발음, 뜻]]}` |
| `pairs` | 헷갈리는 짝 | `[글자HTML, 설명HTML]` |
| `notes` | 소리 노트 | `[표제, 설명HTML]` |
| `quiz` | 발음 퀴즈 | `{label, items:[[단어, 한글발음, 뜻]]}` — label 이 칩 하나 |
| `verbSets` | 동사 | `{n, tip, items:[[원형, 발음, 뜻, 유형, 1인칭, 정중형, 예문, 예문발음, 예문뜻, 불규칙]]}` |
| `talkGroups` | 회화 | `{label, items:[[문장, 발음, 뜻, 설명, 강조]]}` |
| `conjGroups` | 접속사 | `{label, items:[[단어, 발음, 뜻, 설명, 예문, 예문발음, 예문뜻, 강조]]}` |

### 표기 규칙

- 마지막 `주의` / `불규칙` / `강조` 가 `True` 면 **붉게** 칠해진다. 읽는 법이 불규칙하거나 소리가 변하는 것에만 쓴다.
- 설명 본문에는 HTML 을 쓸 수 있다. `<b>` 강조, `<em>` 붉은 강조, `<span class="fr">` 원어(세리프체).
- 단어 표의 `원어읽기` 칸이 빈 문자열이면 그 줄은 렌더링되지 않는다. 로마자 언어는 대개 비워 둔다.
- 섹션 번호(01~10)와 탭 배치는 `build.py` 의 `SECTIONS` 가 정한다. 언어별로 바꿀 수 없다.

## 주의

- `build.py` 를 고치면 **세 페이지가 전부 바뀐다.** 생성된 HTML 을 직접 손보면 다음 실행 때 덮어쓴다.
- 재생성 결과는 결정적이다. 데이터를 안 건드리고 실행하면 파일이 바이트 단위로 그대로여야 한다.
