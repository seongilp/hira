# -*- coding: utf-8 -*-
LANG = {
 'order':3, 'nav':('ESPANOL','스페인어'),
 'file':'spanish.html', 'serif':'Lora',
 'grid':'#7B4B2A', 'gl':'rgba(123,75,42,.30)', 'glh':'rgba(123,75,42,.55)',
 'title':'스페인어 첫 일주일',
 'eyebrow':'ESPANOL · FIRST WEEK',
 'h1':'스페인어 일주일', 'h1sub':'español en una semana',
 'lede':'스페인어는 <b>쓰인 대로 읽습니다.</b> 모음 다섯 개가 한국어와 거의 같고, 묵음은 h 하나뿐입니다. 게다가 <b>강세 규칙이 세 줄로 끝나서</b>, 처음 보는 단어도 어디에 힘을 줄지 알 수 있습니다.',
 's1':'읽는 법 — 규칙 몇 개가 전부', 's1sub':'스페인어에 묵음은 <b>h 하나뿐</b>입니다. 아래 규칙만 알면 메뉴판이든 표지판이든 소리 내어 읽을 수 있습니다.',
 's8':'꼭 외워야 할 동사 29', 's8sub':'스페인어는 <b>주어를 생략합니다.</b> 동사 어미가 누구인지 말해주기 때문입니다. 동사 하나를 두 가지 꼴(나 / 정중한 상대)로 외우면 바로 문장이 됩니다.',
 'foot':'8일째부터는 새 규칙 없이, 바르 메뉴판과 거리 간판을 <b>소리 내어</b> 읽으세요. 스페인어는 쓰기보다 <b>읽는 속도</b>가 실력입니다. 그리고 무슨 말을 하든 <b>Vale</b> 하나면 절반은 통합니다.',
 'data':{
  'p1':'YO · 나', 'p2':'USTED · 정중',

  'soundRules':[
   ['RULE 1','쓰인 대로 읽습니다','스페인어에 묵음은 <b>h 하나뿐</b>입니다. <span class="fr">hola</span> 올라, <span class="fr">hotel</span> 오텔. 모음 다섯 개(<span class="fr">a e i o u</span>)는 위치가 어디든 <b>항상 같은 소리</b>라 한국인에게 아주 유리합니다.'],
   ['RULE 2','c와 g는 뒤 모음이 정합니다','<span class="fr">c·g + a·o·u</span> = 카·가. <span class="fr">ce·ci</span> = <em>세·시</em>, <span class="fr">ge·gi</span> = <em>헤·히</em>. 딱딱한 소리로 되돌리려면 <b>u를 끼웁니다</b> — <span class="fr">queso</span> <em>케소</em>, <span class="fr">guitarra</span> <em>기타라</em>.'],
   ['RULE 3','강세 규칙은 세 줄','① <b>모음·n·s로 끝나면</b> 뒤에서 두 번째 — <span class="fr">CA-sa · JO-ven</span>. ② <b>그 외 자음으로 끝나면</b> 마지막 — <span class="fr">ciu-DAD · es-pa-ÑOL</span>. ③ <b>악센트(´)가 있으면</b> 무조건 그 자리 — <span class="fr">ca-FÉ · es-ta-CIÓN</span>. <em>예외가 없습니다.</em>'],
   ['RULE 4','스페인 본토의 th 소리','스페인에서는 <span class="fr">ce·ci</span>와 <span class="fr">z</span>를 <b>영어 think의 th</b>처럼 냅니다 — <span class="fr">gracias</span> 그라<em>th</em>아스. 중남미와 안달루시아는 그냥 <b>ㅅ</b>. <em>둘 다 맞고 둘 다 통합니다</em> — 편한 쪽으로.'],
   ['RULE 5','b와 v는 같은 소리','스페인어 화자는 이 둘을 <b>구별하지 않습니다</b>. <span class="fr">vino</span>도 <span class="fr">bino</span>도 똑같이 「비노」. 그래서 스페인 사람도 받아쓰기에서 자주 틀립니다. <b>둘 다 ㅂ</b>으로 내면 됩니다.'],
   ['TIP','¿ 와 ¡ 는 시작 표시','문장 <b>맨 앞에 뒤집힌 부호</b>가 붙습니다 — <span class="fr">¿Cuánto cuesta?</span> 읽기 전에 <b>이게 질문인지 감탄인지</b> 미리 알려주는 장치입니다. 스페인어에만 있습니다.'],
  ],
  'soundGroups':[
   {'label':'모음 다섯 — 끝까지 이 소리 그대로','items':[
    ['a','아','casa','집',False],['e','에','mesa','테이블',False],['i','이','vino','와인',False],
    ['o','오','sol','해',False],['u','우','luna','달',False]],
    'ex':[['Una cerveza, por favor.','우나 세르베사, 포르 파보르','맥주 한 잔 주세요.'],
          ['¡Qué bonito!','케 보니토','정말 예쁘네요!']]},
   {'label':'c · g · qu — 뒤 모음이 소리를 정합니다','items':[
    ['ca / co / cu','카 · 코 · 쿠','casa · cosa','집 · 것',False],
    ['ce / ci','세 · 시 (스페인은 th)','cena · cinco','저녁 · 5',True],
    ['que / qui','케 · 키','queso · quién','치즈 · 누구',True],
    ['ga / go / gu','가 · 고 · 구','gato','고양이',False],
    ['ge / gi','헤 · 히','gente · girar','사람들 · 돌다',True],
    ['gue / gui','게 · 기','guerra · guitarra','전쟁 · 기타',True]],
    'ex':[['¿Cuánto cuesta el queso?','쿠안토 쿠에스타 엘 케소','치즈 얼마예요?'],
          ['La cena es a las nueve.','라 세나 에스 아 라스 누에베','저녁은 9시입니다.']]},
   {'label':'스페인어만의 글자','items':[
    ['ñ','니 (ㄴ+ㅣ)','año · señor','해 · 선생님',True],
    ['ll','이 (야 · 예)','llave · calle','열쇠 · 거리',True],
    ['j','흐 (목 안쪽)','jamón · ojo','하몬 · 눈',True],
    ['z','스 · th','zapato · plaza','신발 · 광장',True],
    ['rr','굴리는 ㄹ','perro · arroz','개 · 쌀',True],
    ['h','묵음','hola · hotel','안녕 · 호텔',True]],
    'ex':[['¿Dónde está la llave?','돈데 에스타 라 야베','열쇠가 어디 있어요?'],
          ['Jamón y queso, por favor.','하몬 이 케소, 포르 파보르','하몬이랑 치즈 주세요.']]},
   {'label':'악센트 표시 — 그 자리에 힘을 줍니다','items':[
    ['café','카페','café','커피',False],['adiós','아디오스','adiós','안녕히',False],
    ['estación','에스타시온','estación','역',False],['más','마스','más','더',False],
    ['aquí','아키','aquí','여기',False],['¿qué?','케','¿qué?','무엇',True],
    ['¿dónde?','돈데','¿dónde?','어디',True],['¿cuánto?','쿠안토','¿cuánto?','얼마',True]],
    'ex':[['¿Dónde está la estación?','돈데 에스타 라 에스타시온','역이 어디예요?'],
          ['Un café, por favor.','운 카페, 포르 파보르','커피 한 잔 주세요.']]},
  ],
  'pairs':[
   ['pero <em>/</em> perro','<b>r 하나면 「하지만」, rr이면 「개」</b>입니다. 스페인어에서 <em>가장 자주 웃음을 사는 실수</em>. rr은 혀끝을 여러 번 떨어야 하니 짧게라도 굴려주세요.'],
   ['año <em>/</em> ano','<span class="fr">ñ</span> 위의 물결 하나가 빠지면 <b>「해(年)」가 신체 부위</b>가 됩니다. <em>ñ는 절대 n으로 쓰지 마세요.</em> 스페인어 최대의 오타 사고입니다.'],
   ['cena <em>/</em> queso','같은 「ㅋ/ㅅ」 계열인데 <span class="fr">ce</span>는 <em>세</em>, <span class="fr">que</span>는 <em>케</em>. 딱딱한 소리로 되돌리려면 <b>u를 끼운다</b>고 기억하세요.'],
   ['gente <em>/</em> guerra','g도 똑같습니다. <span class="fr">ge</span>는 <em>헤</em>, <span class="fr">gue</span>는 <em>게</em>. c와 <b>완전히 같은 규칙</b>이라 하나로 묶어 외웁니다.'],
   ['llave <em>/</em> yo','<span class="fr">ll</span>과 <span class="fr">y</span>는 오늘날 <b>거의 같은 소리</b>입니다(야·예). 지역에 따라 「자」에 가깝게도 냅니다 — 아르헨티나에서는 <span class="fr">calle</span>가 「카셰」.'],
   ['vino <em>/</em> bino','<b>b와 v는 소리가 같습니다.</b> 스페인 사람도 헷갈려서 「b de burro, v de vaca」(당나귀 b, 소 v)라고 되물을 정도입니다.'],
   ['jefe <em>/</em> gente','<span class="fr">j</span>와 <span class="fr">g(e·i)</span>는 <b>같은 소리</b>(목 안쪽 ㅎ)입니다. 철자만 다릅니다 — 헤페 · 헨테.'],
   ['casa <em>/</em> caza','스페인 본토에서는 <span class="fr">s</span>(ㅅ)와 <span class="fr">z</span>(th)가 <b>다른 소리</b>라 집과 사냥이 갈립니다. 중남미에서는 <em>완전히 같습니다</em>.'],
  ],
  'notes':[
   ['h','스페인어의 <b>유일한 묵음</b>입니다. 절대 소리 내지 않습니다. <span class="fr">hola</span>는 <b>올라</b>, <span class="fr">hay</span>는 <b>아이</b>. 대신 <span class="fr">ch</span>에서는 <b>「치」</b> 소리를 냅니다 — <span class="fr">chico</span> 치코.'],
   ['j · g','목 안쪽에서 <b>긁듯이 내는 ㅎ</b>입니다. 한국어 「ㅎ」보다 훨씬 거칠게 — <span class="fr">jamón</span> 하몬, <span class="fr">Jorge</span> 호르헤. <em>약하게 내도 다 알아듣습니다.</em>'],
   ['r · rr','단어 <b>맨 앞의 r</b>과 <span class="fr">rr</span>은 여러 번 떱니다 — <span class="fr">Roma · perro</span>. 중간의 r 하나는 혀끝을 한 번만 튕깁니다. <b>pero(하지만)와 perro(개)</b>가 여기서 갈립니다.'],
   ['ñ','<b>ㄴ + ㅣ</b>를 한 번에 냅니다. 일본어 「にゃ」, 이탈리아어 <span class="fr">gn</span>과 같은 소리입니다. <span class="fr">España</span> 에스파냐, <span class="fr">mañana</span> 마냐나.'],
   ['b · v','<b>완전히 같은 소리</b>입니다. 모음 사이에서는 입술을 완전히 붙이지 않고 살짝 스치듯 — <span class="fr">Cuba</span>는 「쿠바」보다 「쿠βa」에 가깝습니다. <em>그냥 ㅂ으로 내도 됩니다.</em>'],
   ['강세','규칙이 <b>세 줄로 끝나고 예외가 없습니다</b>. 모음·n·s로 끝나면 뒤에서 두 번째, 그 외 자음이면 마지막, 악센트가 있으면 그 자리. <b>이것만 지켜도 억양이 확 자연스러워집니다.</b>'],
   ['끝의 d','거의 들리지 않습니다. <span class="fr">Madrid</span>는 <b>마드리</b>, <span class="fr">usted</span>은 <b>우스테</b>에 가깝습니다. 스페인 중부에서는 <em>th</em>처럼 내기도 합니다.'],
   ['스페인 · 중남미','<b>c(e·i)와 z</b>를 스페인은 th로, 중남미는 ㅅ으로 냅니다. 또 스페인은 「너희들」에 <span class="fr">vosotros</span>를 쓰지만 중남미는 안 씁니다. <em>여행자에게는 어느 쪽이든 문제없습니다.</em>'],
  ],
  'quiz':[
   {'label':'c · g · qu','items':[
    ['casa','카사','집'],['cena','세나','저녁'],['cinco','싱코','5'],['queso','케소','치즈'],
    ['quién','키엔','누구'],['gato','가토','고양이'],['gente','헨테','사람들'],['girar','히라르','돌다'],
    ['guitarra','기타라','기타'],['cuenta','쿠엔타','계산서']]},
   {'label':'스페인어만의 글자','items':[
    ['año','아뇨','해 · 년'],['mañana','마냐나','내일 · 아침'],['llave','야베','열쇠'],['calle','카예','거리'],
    ['jamón','하몬','하몬'],['ojo','오호','눈'],['zapato','사파토','신발'],
    ['perro','페로','개'],['hola','올라','안녕'],['chico','치코','소년']]},
   {'label':'자주 보는 단어','items':[
    ['gracias','그라시아스','고맙습니다'],['por favor','포르 파보르','부탁합니다'],['perdón','페르돈','실례합니다'],
    ['agua','아구아','물'],['vino','비노','와인'],['cuenta','쿠엔타','계산서'],
    ['estación','에스타시온','역'],['billete','비예테','표'],['salida','살리다','출구'],['abierto','아비에르토','영업 중']]},
   {'label':'악센트 · 강세','items':[
    ['café','카페','커피'],['adiós','아디오스','안녕히'],['aquí','아키','여기'],['más','마스','더'],
    ['ciudad','시우다드','도시'],['español','에스파뇰','스페인어'],['joven','호벤','젊은'],
    ['plaza','플라사','광장'],['tortilla','토르티야','토르티야'],['paella','파에야','파에야']]},
  ],

  'numRules':[
   ['RULE 1','16부터 붙여 씁니다','<span class="fr">dieciséis</span> = diez + y + seis. 16~19와 21~29는 <b>한 단어로 붙여 쓰고</b>, 31부터는 다시 <span class="fr">treinta <em>y</em> uno</span>처럼 <b>y로 띄웁니다</b>.'],
   ['RULE 2','1은 앞말에 따라 변합니다','<span class="fr">uno</span>는 혼자 쓸 때, 명사 앞에서는 <span class="fr">un</span>(남성) / <span class="fr">una</span>(여성) — <span class="fr">un café · una cerveza</span>. <b>2부터는 구별이 없습니다.</b>'],
   ['RULE 3','값은 「¿Cuánto cuesta?」','쿠안토 쿠에스타 = 얼마예요? 전부 합쳐서는 <span class="fr">¿Cuánto es?</span> 쿠안토 에스. <b>둘 다 통합니다.</b> 못 알아들으면 <span class="fr">¿Me lo escribe?</span>(써 주실래요?).'],
   ['TIP','바르에서는 서서 마십니다','바 카운터(<span class="fr">en la barra</span>)에 서서 마시면 싸고, 테라스(<span class="fr">en la terraza</span>)에 앉으면 비쌉니다. <b>같은 음료인데 자릿값이 붙습니다.</b> 그리고 스페인에서 <em>팁은 의무가 아닙니다</em> — 잔돈 정도면 충분합니다.'],
  ],
  'numGroups':[
   {'label':'0 ~ 10','items':[
    ['cero','','세로','0',False],['uno / un / una','','우노 · 운 · 우나','1',True],['dos','','도스','2',False],
    ['tres','','트레스','3',False],['cuatro','','쿠아트로','4',False],['cinco','','싱코','5',False],
    ['seis','','세이스','6',False],['siete','','시에테','7',False],['ocho','','오초','8',False],
    ['nueve','','누에베','9',False],['diez','','디에스','10',False]],
    'ex':[['Somos dos.','소모스 도스','두 명이에요.'],
          ['Un café y dos churros.','운 카페 이 도스 추로스','커피 하나랑 추로스 둘이요.']]},
   {'label':'11 ~ 20 — 16부터 붙여 씁니다','items':[
    ['once','','온세','11',False],['doce','','도세','12',False],['trece','','트레세','13',False],
    ['catorce','','카토르세','14',False],['quince','','킨세','15',False],
    ['dieciséis','','디에시세이스','16',True],['diecisiete','','디에시시에테','17',True],
    ['dieciocho','','디에시오초','18',True],['diecinueve','','디에시누에베','19',True],
    ['veinte','','베인테','20',False]],
    'ex':[['Son las quince horas.','손 라스 킨세 오라스','15시(오후 3시)입니다.'],
          ['La habitación dieciocho.','라 아비타시온 디에시오초','18호실이요.']]},
   {'label':'수십 · 백 · 천','items':[
    ['treinta','','트레인타','30',False],['cuarenta','','쿠아렌타','40',False],
    ['cincuenta','','싱쿠엔타','50',False],['sesenta','','세센타','60',False],
    ['setenta','','세텐타','70',False],['ochenta','','오첸타','80',False],
    ['noventa','','노벤타','90',False],['cien','','시엔','100',True],
    ['ciento uno','','시엔토 우노','101',True],['mil','','밀','1,000',False]],
    'ex':[['¿Cuánto cuesta?','쿠안토 쿠에스타','얼마예요?'],
          ['Son veinticinco euros.','손 베인티싱코 에우로스','25유로입니다.']]},
   {'label':'계산에 쓰는 말','items':[
    ['cuánto','','쿠안토','얼마 · 몇',False],['euro','','에우로','유로',False],
    ['precio','','프레시오','가격',False],['caro','','카로','비싼',False],
    ['barato','','바라토','싼',False],['la cuenta','','라 쿠엔타','계산서',False],
    ['recibo','','레시보','영수증',False],['efectivo','','에펙티보','현금',False],
    ['tarjeta','','타르헤타','카드',False],['cambio','','캄비오','거스름돈',False],
    ['propina','','프로피나','팁 (의무 아님)',True],['IVA incluido','','이바 인클루이도','부가세 포함',True]],
    'ex':[['La cuenta, por favor.','라 쿠엔타, 포르 파보르','계산서 주세요.'],
          ['¿Puedo pagar con tarjeta?','푸에도 파가르 콘 타르헤타','카드로 낼 수 있나요?'],
          ['¿Está el IVA incluido?','에스타 엘 이바 인클루이도','부가세 포함인가요?']]},
  ],

  'timeRules':[
   ['RULE 1','시간은 「Son las + 숫자」','<span class="fr">Son las tres</span> = 3시입니다. <b>1시만</b> <span class="fr">Es la una</span>. 「몇 시예요?」는 <span class="fr"><em>¿Qué hora es?</em></span> 케 오라 에스.'],
   ['RULE 2','mañana는 두 가지 뜻','<span class="fr"><em>mañana</em></span>는 <b>「내일」</b>이면서 <b>「아침」</b>입니다. <span class="fr">por la mañana</span>는 아침에, <span class="fr">mañana</span> 혼자면 내일. <span class="fr">mañana por la mañana</span> = <b>내일 아침</b>.'],
   ['RULE 3','식사 시간이 늦습니다','점심은 <b>오후 2~3시</b>, 저녁은 <b>밤 9~10시</b>. 그 사이에 문을 여는 식당이 거의 없습니다. 배가 고프면 <span class="fr">tapas</span>로 버티세요. <em>7시에 저녁 먹으러 가면 가게가 닫혀 있습니다.</em>'],
   ['TIP','요일과 달은 소문자','영어와 달리 <span class="fr">lunes · enero</span>처럼 <b>소문자</b>입니다. 요일 앞에 <span class="fr">el</span>을 붙이면 「~요일에」 — <span class="fr">el lunes</span> 월요일에.'],
  ],
  'timeGroups':[
   {'label':'몇 시 — hora','items':[
    ['¿Qué hora es?','','케 오라 에스','몇 시예요?',False],['Es la una','','에스 라 우나','1시입니다',True],
    ['Son las dos','','손 라스 도스','2시입니다',False],['y media','','이 메디아','30분',False],
    ['y cuarto','','이 쿠아르토','15분',False],['mediodía','','메디오디아','정오',False],
    ['medianoche','','메디아노체','자정',False],['minuto','','미누토','분',False],['hora','','오라','시간',False]],
    'ex':[['¿Qué hora es?','케 오라 에스','몇 시예요?'],
          ['Son las siete y media.','손 라스 시에테 이 메디아','7시 반이에요.'],
          ['¿A qué hora abren?','아 케 오라 아브렌','몇 시에 열어요?']]},
   {'label':'오늘 · 내일 · 하루의 때','items':[
    ['hoy','','오이','오늘',False],['mañana','','마냐나','내일 · 아침',True],
    ['ayer','','아예르','어제',False],['ahora','','아오라','지금',False],
    ['luego','','루에고','나중에',False],['temprano','','템프라노','일찍',False],
    ['tarde','','타르데','늦게 · 오후',True],['la mañana','','라 마냐나','아침',False],
    ['la tarde','','라 타르데','오후',False],['la noche','','라 노체','밤',False],
    ['esta noche','','에스타 노체','오늘 밤',False],['siesta','','시에스타','낮잠 · 휴식 시간',True]],
    'ex':[['Salimos mañana por la mañana.','살리모스 마냐나 포르 라 마냐나','내일 아침에 떠나요.'],
          ['¡Hasta esta noche!','아스타 에스타 노체','오늘 밤에 봐요!']]},
   {'label':'요일 — 소문자로 씁니다','items':[
    ['lunes','','루네스','월요일',False],['martes','','마르테스','화요일',False],
    ['miércoles','','미에르콜레스','수요일',False],['jueves','','후에베스','목요일',False],
    ['viernes','','비에르네스','금요일',False],['sábado','','사바도','토요일',False],
    ['domingo','','도밍고','일요일',False],['fin de semana','','핀 데 세마나','주말',False],
    ['abierto','','아비에르토','영업 중',False],['cerrado','','세라도','휴무 · 닫힘',True]],
    'ex':[['¿Abren el domingo?','아브렌 엘 도밍고','일요일에 여나요?'],
          ['Cerrado los lunes.','세라도 로스 루네스','매주 월요일 휴무.']]},
   {'label':'계절과 그때의 말','items':[
    ['primavera','','프리마베라','봄',False],['verano','','베라노','여름',False],
    ['otoño','','오토뇨','가을',False],['invierno','','인비에르노','겨울',False],
    ['calor','','칼로르','더위',False],['frío','','프리오','추위',False],
    ['sol','','솔','해',False],['lluvia','','유비아','비',False],
    ['fiesta','','피에스타','축제 · 파티',False],['feria','','페리아','장터 · 축제',True]],
    'ex':[['Hace calor hoy.','아세 칼로르 오이','오늘 덥네요.'],
          ['En verano hay mucha gente.','엔 베라노 아이 무차 헨테','여름엔 사람이 많아요.']]},
  ],

  'placeRules':[
   ['RULE 1','1층은 「planta baja」','스페인의 <span class="fr"><em>primera planta</em></span>는 <b>한국식 2층</b>입니다. 지상층은 <span class="fr">planta baja</span>(플란타 바하), 엘리베이터 버튼의 <b>B 또는 0</b>. 무심코 1을 누르면 한 층 위로 갑니다.'],
   ['RULE 2','길 안내는 네 단어면 됩니다','<span class="fr">a la derecha</span>(오른쪽) · <span class="fr">a la izquierda</span>(왼쪽) · <span class="fr">todo recto</span>(직진) · <span class="fr">aquí cerca</span>(이 근처). 앞에 <span class="fr">¿Dónde está...?</span>(돈데 에스타 = 어디예요?)만 붙이면 됩니다.'],
   ['RULE 3','화장실은 부르는 말이 여럿','<span class="fr">el baño · el aseo · los servicios</span> 셋 다 화장실입니다. 스페인에서는 <span class="fr"><em>los servicios</em></span>가 가장 흔합니다. <b>주문한 손님만</b> 쓸 수 있는 곳이 많습니다.'],
   ['TIP','표지판 단어만 알아도','<span class="fr">salida</span>(출구) · <span class="fr">entrada</span>(입구) · <span class="fr">empujar</span>(미시오) · <span class="fr">tirar</span>(당기시오) · <span class="fr">prohibido</span>(금지). <b>읽기만 하면</b> 헤맬 일이 없습니다.'],
  ],
  'placeGroups':[
   {'label':'층 — planta','items':[
    ['planta baja','','플란타 바하','지상층 (한국 1층)',True],
    ['primera planta','','프리메라 플란타','2층',True],
    ['segunda planta','','세군다 플란타','3층',False],
    ['última planta','','울티마 플란타','꼭대기 층',False],
    ['sótano','','소타노','지하',False],['escalera','','에스칼레라','계단',False],
    ['ascensor','','아센소르','엘리베이터',False]],
    'ex':[['¿Dónde están los servicios?','돈데 에스탄 로스 세르비시오스','화장실이 어디예요?'],
          ['Está en la primera planta.','에스타 엔 라 프리메라 플란타','2층에 있어요.']]},
   {'label':'방향과 위치','items':[
    ['dónde','','돈데','어디',False],['aquí','','아키','여기',False],['allí','','아이','저기',False],
    ['a la derecha','','아 라 데레차','오른쪽으로',False],['a la izquierda','','아 라 이스키에르다','왼쪽으로',False],
    ['todo recto','','토도 렉토','계속 직진',False],['cerca','','세르카','가까이',False],
    ['lejos','','레호스','멀리',False],['delante','','델란테','앞',False],
    ['detrás','','데트라스','뒤',False],['al lado','','알 라도','옆',False],['esquina','','에스키나','모퉁이',False]],
    'ex':[['¿Dónde está la estación?','돈데 에스타 라 에스타시온','역이 어디예요?'],
          ['Todo recto y luego a la derecha.','토도 렉토 이 루에고 아 라 데레차','계속 직진하다가 오른쪽이요.'],
          ['¿Está cerca de aquí?','에스타 세르카 데 아키','여기서 가까워요?']]},
   {'label':'시설 · 표지판','items':[
    ['estación','','에스타시온','역',False],['aeropuerto','','아에로푸에르토','공항',False],
    ['parada','','파라다','정류장',False],['billete','','비예테','표',False],
    ['andén','','안덴','승강장',False],['salida','','살리다','출구',False],
    ['entrada','','엔트라다','입구',False],['servicios','','세르비시오스','화장실',False],
    ['farmacia','','파르마시아','약국',False],['hospital','','오스피탈','병원',False],
    ['banco','','반코','은행',False],['mercado','','메르카도','시장',False],
    ['empujar','','엠푸하르','미시오',True],['tirar','','티라르','당기시오',True]],
    'ex':[['¿De qué andén sale el tren?','데 케 안덴 살레 엘 트렌','기차는 몇 번 승강장에서 떠나요?'],
          ['¿Hay una farmacia por aquí?','아이 우나 파르마시아 포르 아키','근처에 약국 있나요?']]},
   {'label':'바르 · 식당에서','items':[
    ['mesa','','메사','테이블',False],['la carta','','라 카르타','메뉴판',False],
    ['menú del día','','메누 델 디아','오늘의 세트 (점심 특가)',True],
    ['tapa','','타파','작은 안주 한 접시',True],['ración','','라시온','큰 접시',True],
    ['agua del grifo','','아구아 델 그리포','수돗물 (무료)',True],
    ['caña','','카냐','생맥주 작은 잔',True],['en la barra','','엔 라 바라','바 카운터에서',False],
    ['primero','','프리메로','첫 번째 접시',False],['segundo','','세군도','두 번째 접시',False],
    ['postre','','포스트레','디저트',False],['para llevar','','파라 예바르','포장',False]],
    'ex':[['Una caña y una tapa, por favor.','우나 카냐 이 우나 타파, 포르 파보르','생맥주 한 잔이랑 타파 하나요.'],
          ['¿Tienen menú del día?','티에넨 메누 델 디아','오늘의 세트 있나요?'],
          ['Agua del grifo, por favor.','아구아 델 그리포, 포르 파보르','수돗물로 주세요.']]},
  ],
 }
}

LANG['data']['verbRules'] = [
 ['RULE 1','주어를 쓰지 않습니다','<span class="fr">yo</span>(나)를 굳이 붙이지 않습니다. <b>동사 어미가 이미 누구인지 말해주기</b> 때문입니다. <span class="fr">Soy coreano</span> = (나는) 한국인입니다. 강조할 때만 주어를 붙입니다.'],
 ['RULE 2','어미는 세 가지','<span class="fr">-ar</span>(hablar) · <span class="fr">-er</span>(comer) · <span class="fr">-ir</span>(vivir). <b>-ar가 압도적으로 많습니다.</b> 세 유형의 「나」꼴은 모두 <em>-o</em>로 끝나니 우선 그것만 잡으세요.'],
 ['RULE 3','ser와 estar가 갈립니다','스페인어 최대의 관문. <span class="fr"><em>ser</em></span>는 <b>변하지 않는 것</b>(국적·직업·성격), <span class="fr"><em>estar</em></span>는 <b>지금 상태와 위치</b>. <span class="fr">Soy coreano</span>(한국인이다) / <span class="fr">Estoy cansado</span>(피곤하다) / <span class="fr">¿Dónde está?</span>(어디 있어요?).'],
 ['RULE 4','quisiera 하나면 됩니다','<span class="fr"><em>Quisiera...</em></span> 키시에라 = 「~을 원해요」의 정중한 꼴. <span class="fr">Quiero</span>(원한다)는 조금 직설적이니, 가게에서는 <span class="fr">Quisiera</span>나 <span class="fr">Me pone...</span>(하나 주세요) 쪽이 부드럽습니다.'],
 ['TIP','허락은 「¿Puedo...?」','푸에도 = 「~해도 되나요?」. 뒤에 동사 원형만 붙입니다 — <span class="fr">¿Puedo pagar con tarjeta?</span> / <span class="fr">¿Puedo entrar?</span>'],
 ['TIP','과거는 「he + 과거분사」','<span class="fr">he comido</span>(먹었어요) · <span class="fr">he perdido</span>(잃어버렸어요). <b>he</b>에 동사만 갈아 끼우면 됩니다. 중남미에서는 <span class="fr">comí · perdí</span> 꼴을 더 씁니다 — <em>둘 다 통합니다.</em>'],
]

LANG['data']['verbSets'] = [
 {'n':'ser <i>↔</i> estar', 'tip':'<b>스페인어에서 가장 중요한 구분.</b> <span class="fr">ser</span>는 바뀌지 않는 것 — 국적·직업·성격. <span class="fr">estar</span>는 지금의 상태와 위치. <em>같은 「~이다」인데 뜻이 완전히 달라집니다.</em>', 'items':[
  ['ser','세르','~이다 (본질)','불규칙','soy 소이','es 에스','Soy coreano.','소이 코레아노','저는 한국인입니다.',True],
  ['estar','에스타르','~이다 · 있다 (상태 · 위치)','불규칙','estoy 에스토이','está 에스타','¿Dónde está el baño?','돈데 에스타 엘 바뇨','화장실이 어디 있어요?',True]]},
 {'n':'tener <i>·</i> hay', 'tip':'<span class="fr">tener</span>는 <b>내가 가진 것</b>, <span class="fr">hay</span>는 <b>거기에 있는 것</b>. 나이도 tener로 말합니다 — <span class="fr">Tengo treinta años</span>(서른입니다). <span class="fr">hay</span>는 <b>모양이 하나뿐</b>이라 외울 게 없습니다.', 'items':[
  ['tener','테네르','가지다','불규칙','tengo 텡고','tiene 티에네','Tengo una reserva.','텡고 우나 레세르바','예약이 있어요.',True],
  ['haber','아베르','있다 (존재)','불규칙','hay 아이','hay 아이','¿Hay wifi?','아이 위피','와이파이 있나요?',True]]},
 {'n':'ir <i>·</i> venir <i>·</i> volver', 'tip':'방향 삼총사. 나에게서 <b>멀어지면</b> ir, <b>다가오면</b> venir, <b>원래 자리로</b> 돌아가면 volver. <span class="fr">ir</span>는 원형과 활용이 전혀 안 닮은 <em>극단적 불규칙</em>이라 소리째로 외웁니다.', 'items':[
  ['ir','이르','가다','불규칙','voy 보이','va 바','Voy a Madrid.','보이 아 마드리드','마드리드에 갑니다.',True],
  ['venir','베니르','오다','불규칙','vengo 벵고','viene 비에네','¿Cuándo viene el bus?','쿠안도 비에네 엘 부스','버스는 언제 오나요?',True],
  ['volver','볼베르','돌아가다','-er','vuelvo 부엘보','vuelve 부엘베','Vuelvo mañana.','부엘보 마냐나','내일 돌아갑니다.',True]]},
 {'n':'querer <i>·</i> poder <i>·</i> tener que', 'tip':'뒤에 <b>동사 원형</b>을 그대로 붙이는 셋. <span class="fr">Quisiera</span>(원해요) · <span class="fr">¿Puedo?</span>(해도 되나요) · <span class="fr">Tengo que</span>(해야 해요). <em>이 셋이면 웬만한 부탁과 질문이 끝납니다.</em>', 'items':[
  ['querer','케레르','원하다','불규칙','quisiera 키시에라','quiere 키에레','Quisiera un café.','키시에라 운 카페','커피 한 잔 주세요.',True],
  ['poder','포데르','할 수 있다','불규칙','puedo 푸에도','puede 푸에데','¿Puedo entrar?','푸에도 엔트라르','들어가도 되나요?',True],
  ['tener que','테네르 케','해야 한다','불규칙','tengo que 텡고 케','tiene que 티에네 케','Tengo que irme.','텡고 케 이르메','가봐야 해요.',True]]},
 {'n':'comer <i>·</i> beber <i>·</i> tomar', 'tip':'식당 삼총사. 주문할 때는 <span class="fr">tomar</span>(취하다 → 먹다·마시다)를 아주 많이 씁니다 — <span class="fr">Voy a tomar la paella</span>(파에야로 할게요). 영어의 「I\'ll have」 자리입니다.', 'items':[
  ['comer','코메르','먹다','-er','como 코모','come 코메','No como carne.','노 코모 카르네','고기는 안 먹어요.',False],
  ['beber','베베르','마시다','-er','bebo 베보','bebe 베베','Solo bebo agua.','솔로 베보 아구아','물만 마셔요.',False],
  ['tomar','토마르','먹다 · 마시다 · 타다','-ar','tomo 토모','toma 토마','Voy a tomar la paella.','보이 아 토마르 라 파에야','파에야로 할게요.',False]]},
 {'n':'comprar <i>·</i> pagar <i>·</i> costar', 'tip':'계산대 세트. <span class="fr">costar</span>는 <b>물건이 주어</b>라 3인칭만 씁니다 — 하나면 <span class="fr">cuesta</span>, 여럿이면 <span class="fr">cuestan</span>.', 'items':[
  ['comprar','콤프라르','사다','-ar','compro 콤프로','compra 콤프라','Quisiera comprar esto.','키시에라 콤프라르 에스토','이걸 사고 싶어요.',False],
  ['pagar','파가르','지불하다','-ar','pago 파고','paga 파가','¿Puedo pagar con tarjeta?','푸에도 파가르 콘 타르헤타','카드로 낼 수 있나요?',False],
  ['costar','코스타르','값이 나가다','-ar','cuesta 쿠에스타','cuestan 쿠에스탄','¿Cuánto cuesta?','쿠안토 쿠에스타','얼마예요?',True]]},
 {'n':'hablar <i>·</i> entender <i>·</i> saber', 'tip':'말이 안 통할 때의 세 개. <span class="fr">No entiendo</span>(못 알아듣겠어요)와 <span class="fr">No sé</span>(모르겠어요)는 <b>통째로</b> 외우세요. 앞에 <span class="fr">no</span>만 붙이면 부정문이 됩니다.', 'items':[
  ['hablar','아블라르','말하다','-ar','hablo 아블로','habla 아블라','¿Habla inglés?','아블라 잉글레스','영어 하세요?',False],
  ['entender','엔텐데르','이해하다','-er','entiendo 엔티엔도','entiende 엔티엔데','No entiendo.','노 엔티엔도','못 알아듣겠어요.',True],
  ['saber','사베르','알다','불규칙','sé 세','sabe 사베','No sé.','노 세','모르겠어요.',True]]},
 {'n':'buscar <i>·</i> encontrar <i>·</i> perder', 'tip':'잃어버렸을 때의 3연타. <span class="fr">He perdido</span>(잃어버렸어요) → <span class="fr">Busco</span>(찾고 있어요) → <span class="fr">Lo he encontrado</span>(찾았어요). 이 순서로 말하면 상황 설명이 끝납니다.', 'items':[
  ['buscar','부스카르','찾다','-ar','busco 부스코','busca 부스카','Busco esta dirección.','부스코 에스타 디렉시온','이 주소를 찾고 있어요.',False],
  ['encontrar','엔콘트라르','발견하다','-ar','encuentro 엔쿠엔트로','encuentra 엔쿠엔트라','No encuentro mi hotel.','노 엔쿠엔트로 미 오텔','호텔을 못 찾겠어요.',True],
  ['perder','페르데르','잃다 · 놓치다','-er','pierdo 피에르도','pierde 피에르데','He perdido el tren.','에 페르디도 엘 트렌','기차를 놓쳤어요.',True]]},
 {'n':'esperar <i>·</i> llegar <i>·</i> salir', 'tip':'이동 세트. 역 전광판에 <span class="fr">llegadas</span>(도착)와 <span class="fr">salidas</span>(출발)로 그대로 적혀 있습니다. <b>동사를 알면 표지판이 읽힙니다.</b>', 'items':[
  ['esperar','에스페라르','기다리다','-ar','espero 에스페로','espera 에스페라','Un momento, ¡espere!','운 모멘토, 에스페레','잠깐만 기다려주세요!',False],
  ['llegar','예가르','도착하다','-ar','llego 예고','llega 예가','¿A qué hora llega?','아 케 오라 예가','몇 시에 도착해요?',False],
  ['salir','살리르','나가다 · 출발하다','-ir','salgo 살고','sale 살레','El tren sale a las ocho.','엘 트렌 살레 아 라스 오초','기차는 8시에 떠나요.',True]]},
 {'n':'abrir <i>·</i> cerrar <i>·</i> hacer', 'tip':'가게 앞에서. <span class="fr">abierto</span>(영업 중) / <span class="fr">cerrado</span>(닫힘)는 <b>문에 붙은 팻말</b> 그대로입니다. <span class="fr">hacer</span>는 날씨에도 씁니다 — <span class="fr">Hace calor</span>(덥다).', 'items':[
  ['abrir','아브리르','열다','-ir','abro 아브로','abre 아브레','¿A qué hora abren?','아 케 오라 아브렌','몇 시에 열어요?',False],
  ['cerrar','세라르','닫다','-ar','cierro 시에로','cierra 시에라','¿Cuándo cierran?','쿠안도 시에란','언제 닫아요?',True],
  ['hacer','아세르','하다 · 만들다','불규칙','hago 아고','hace 아세','¿A qué se dedica?','아 케 세 데디카','무슨 일 하세요?',True]]},
 {'n':'gustar <i>·</i> ver <i>·</i> decir', 'tip':'<span class="fr">gustar</span>는 <b>거꾸로 된 동사</b>입니다 — 「내가 좋아한다」가 아니라 「그것이 내 마음에 든다」. 그래서 <span class="fr">Me gusta</span>(단수) / <span class="fr">Me gustan</span>(복수)로 갈립니다.', 'items':[
  ['gustar','구스타르','마음에 들다','-ar','me gusta 메 구스타','le gusta 레 구스타','¡Me gusta mucho!','메 구스타 무초','정말 좋아요!',True],
  ['ver','베르','보다','불규칙','veo 베오','ve 베','Quisiera ver esto.','키시에라 베르 에스토','이거 보고 싶어요.',True],
  ['decir','데시르','말하다','불규칙','digo 디고','dice 디세','¿Cómo se dice en español?','코모 세 디세 엔 에스파뇰','스페인어로 뭐라고 해요?',True]]},
]

LANG['data']['talkRules'] = [
 ['RULE 1','인사부터, 그리고 크게','<span class="fr">Buenos días</span>(아침) / <span class="fr">Buenas tardes</span>(오후) / <span class="fr">Buenas noches</span>(밤). 바르나 가게에 들어서면 <b>먼저 인사</b>합니다. 스페인 사람들은 목소리가 큰 편이라, <em>작게 말하면 오히려 안 들립니다.</em>'],
 ['RULE 2','Vale 하나로 절반은 됩니다','<span class="fr"><em>Vale</em></span> 발레 = 「좋아요 · 알겠어요 · 그래요」. 스페인에서 <b>하루에 수백 번</b> 듣게 되는 말입니다. 맞장구, 동의, 마무리에 전부 씁니다. <b>이 한 단어부터 외우세요.</b>'],
 ['RULE 3','Tú와 Usted','스페인은 <b>격식이 덜한 편</b>이라 가게에서도 <span class="fr">tú</span>(반말)로 말을 걸어옵니다. 놀라지 마세요 — 무례한 게 아닙니다. 그래도 <b>내가 먼저 쓸 때는</b> <span class="fr">usted</span>(정중)이 안전합니다.'],
 ['TIP','손과 목소리가 같이 말합니다','단어가 막히면 <b>손으로 가리키고 표정을 쓰세요.</b> 스페인어권에서는 그게 자연스럽습니다. <em>발음이 서툴러도 적극적이면 훨씬 잘 통합니다.</em>'],
]

LANG['data']['talkGroups'] = [
 {'label':'첫 마디 — 입을 떼는 순간','items':[
  ['Buenos días.','부에노스 디아스','안녕하세요. (아침~오후 2시)','가게·식당·호텔 어디서든 <b>첫 마디</b>.',True],
  ['Buenas tardes.','부에나스 타르데스','안녕하세요. (오후~해질 무렵)','스페인은 점심이 늦어서 <b>오후 2시 이후</b>부터 씁니다.',False],
  ['Hola.','올라','안녕.','시간과 상관없이 무난합니다. 조금 가벼운 느낌.',False],
  ['Perdón. / Disculpe.','페르돈 · 디스쿨페','실례합니다.','모르는 사람에게 말을 걸 때. <span class="fr">Disculpe</span> 쪽이 더 정중합니다.',True],
  ['No hablo español.','노 아블로 에스파뇰','스페인어를 못해요.','먼저 밝히면 상대가 <b>속도를 늦춰줍니다</b>. 가성비 최고의 문장.',True],
  ['¿Habla inglés?','아블라 잉글레스','영어 하세요?','관광지에서는 대개 통합니다. 안 되면 손짓과 숫자로.',False],
  ['¿Puede hablar más despacio?','푸에데 아블라르 마스 데스파시오','좀 더 천천히 말씀해 주실래요?','<span class="fr">No entiendo</span>보다 이쪽이 <b>대화를 이어줍니다</b>.',True],
  ['Soy coreano. / coreana.','소이 코레아노 · 코레아나','한국 사람이에요.','남자는 <span class="fr">-o</span>, 여자는 <span class="fr">-a</span>. 대화의 절반이 여기서 시작됩니다.',True]]},
 {'label':'부탁하기 — 이 네 틀이면 끝','items':[
  ['Quisiera...','키시에라','~을 원해요 (정중)','<b>가장 많이 쓰게 될 한 마디.</b> 뒤에 명사든 동사 원형이든 붙입니다.',True],
  ['¿Puedo... ?','푸에도','~해도 되나요?','뒤에 동사 원형만. <span class="fr">¿Puedo entrar? / ¿Puedo pagar?</span>',True],
  ['Por favor.','포르 파보르','부탁합니다.','문장 끝에 붙이면 뭐든 정중해집니다.',True],
  ['¿Hay... ?','아이','~이 있나요?','가게에서 물건을 찾을 때. <span class="fr">¿Hay wifi?</span>',False],
  ['Me pone...','메 포네','~ 하나 주세요','바르에서 주문할 때 <b>현지인들이 실제로 쓰는</b> 말. <span class="fr">Me pone una caña.</span>',True],
  ['¿Me ayuda, por favor?','메 아유다, 포르 파보르','좀 도와주시겠어요?','정말 곤란할 때. 대부분 발 벗고 나서 줍니다.',False]]},
 {'label':'맞장구 — 대화를 굴리는 말','items':[
  ['Vale.','발레','좋아요 · 알겠어요.','<b>스페인에서 가장 많이 듣는 단어.</b> 이것 하나면 대화가 굴러갑니다.',True],
  ['Claro.','클라로','물론이죠.','확실하게 긍정할 때.',False],
  ['¿En serio?','엔 세리오','정말요?','놀랐을 때. 살짝 올려서 말하면 리액션이 삽니다.',True],
  ['¡Qué bonito!','케 보니토','정말 예쁘네요!','풍경·물건·가게 무엇에든.',False],
  ['¡Está buenísimo!','에스타 부에니시모','정말 맛있어요!','<b>먹자마자, 크게.</b> 주방까지 들리면 분위기가 달라집니다.',True],
  ['Me gusta mucho.','메 구스타 무초','아주 마음에 들어요.','물건이든 음식이든 장소든.',False],
  ['Ya veo.','야 베오','아, 그렇군요.','설명을 듣고 이해했을 때.',False],
  ['No sé.','노 세','모르겠어요.','모를 때 솔직하게. 침묵보다 낫습니다.',False]]},
 {'label':'말을 트는 질문','items':[
  ['¿Cómo se llama?','코모 세 야마','성함이 어떻게 되세요?','조금 친해진 다음에. 이름을 주고받으면 분위기가 바뀝니다.',False],
  ['¿Es de aquí?','에스 데 아키','여기 분이세요?','현지인인지 묻는 가벼운 질문.',False],
  ['¿Qué me recomienda?','케 메 레코미엔다','뭘 추천해 주시겠어요?','<b>바르에서 이 한마디면</b> 주인이 신나서 설명합니다.',True],
  ['¿Cuál es el plato típico?','쿠알 에스 엘 플라토 티피코','이 지역 대표 요리가 뭐예요?','관광객 메뉴 말고 진짜를 알려줍니다.',True],
  ['¿Ha estado en Corea?','아 에스타도 엔 코레아','한국에 가보신 적 있어요?','거의 실패하지 않는 질문. 이야기가 이어집니다.',False],
  ['¿Puedo hacer una foto?','푸에도 아세르 우나 포토','사진 찍어도 될까요?','가게 안이나 음식을 찍기 전에.',False]]},
 {'label':'마무리 — 자리를 뜰 때','items':[
  ['¡Muchas gracias!','무차스 그라시아스','정말 고맙습니다!','<span class="fr">gracias</span>보다 한 단계 따뜻합니다.',True],
  ['De nada.','데 나다','천만에요.','Gracias를 받으면 이걸로.',True],
  ['Ha sido un placer.','아 시도 운 플라세르','즐거웠습니다.','사람과 헤어질 때.',False],
  ['Adiós.','아디오스','안녕히 계세요.','정중한 작별.',False],
  ['¡Hasta luego!','아스타 루에고','또 봐요!','<b>실제로는 이쪽을 훨씬 많이 씁니다.</b> 가게를 나서며 가볍게.',True],
  ['¡Buen día!','부엔 디아','좋은 하루 되세요!','헤어지며 건네는 한 마디.',False]]},
]

LANG['data']['conjRules'] = [
 ['RULE 1','문장을 짧게 끊고 앞에 얹으세요','긴 문장을 만들려 하지 말고 <b>짧게 끊은 뒤 앞에 한 단어</b>를 붙이세요. <span class="fr">Es caro. Pero lo compro.</span>(비싸요. 그래도 살게요.) 이게 실제로 말이 되는 방식입니다.'],
 ['RULE 2','y가 e로 바뀔 때','뒤에 오는 단어가 <span class="fr">i-</span>나 <span class="fr">hi-</span>로 시작하면 <span class="fr">y</span>가 <span class="fr"><em>e</em></span>로 바뀝니다 — <span class="fr">España <em>e</em> Italia</span>. 소리가 겹치는 걸 피하려는 것입니다. <b>o도 마찬가지</b>로 <span class="fr">o-</span> 앞에서 <span class="fr">u</span>가 됩니다.'],
 ['TRAP','「그런데」가 두 갈래','앞말을 뒤집는 역접이면 <span class="fr"><em>pero</em></span>, 화제를 바꾸는 「그건 그렇고」면 <span class="fr"><em>por cierto</em></span>. 한국어 「그런데」 하나가 스페인어에서는 둘로 갈립니다.'],
 ['TIP','o sea와 es que','<span class="fr">o sea</span> 오 세아 = 「그러니까 즉」, <span class="fr">es que</span> 에스 케 = 「그게 말이죠」. 둘 다 <b>현지인이 하루에 수십 번</b> 쓰는데 교과서에는 잘 안 나옵니다. 특히 <span class="fr">es que</span>는 <em>변명을 시작하는 신호</em>입니다.'],
]

LANG['data']['conjGroups'] = [
 {'label':'그리고 — 덧붙이기','items':[
  ['y / e','이 · 에','그리고','기본은 <span class="fr">y</span>. <b>i-, hi-로 시작하는 말 앞에서만</b> <span class="fr">e</span>가 됩니다.','Pan y vino.','판 이 비노','빵과 와인.',False],
  ['luego','루에고','그러고 나서','<b>순서</b>가 있을 때. 「그 다음에」.','Un café, y luego me voy.','운 카페, 이 루에고 메 보이','커피 마시고, 그 다음에 갈게요.',True],
  ['también','탐비엔','또한 · ~도','「나도」는 <span class="fr">yo también</span> 요 탐비엔.','Para mí también, gracias.','파라 미 탐비엔, 그라시아스','저도 같은 걸로요.',True],
  ['además','아데마스','게다가','이유를 보태 강조할 때.','Está bueno y además es barato.','에스타 부에노 이 아데마스 에스 바라토','맛있고, 게다가 싸요.',False]]},
 {'label':'그런데 · 하지만 — 뒤집기','items':[
  ['pero','페로','하지만','<b>1순위.</b> 회화의 역접은 pero 하나로 거의 다 됩니다. <em>perro(개)와 헷갈리지 않게</em> r은 하나만.','Es caro, pero lo compro.','에스 카로, 페로 로 콤프로','비싸요, 그래도 살게요.',True],
  ['sin embargo','신 엠바르고','그러나','조금 격식 있는 역접. 글에서 더 자주 보입니다.','Sin embargo, está cerrado.','신 엠바르고, 에스타 세라도','그러나 닫혀 있어요.',False],
  ['en cambio','엔 캄비오','반면에','두 가지를 대비할 때.','El tinto no, en cambio el blanco sí.','엘 틴토 노, 엔 캄비오 엘 블랑코 시','레드 말고 화이트로요.',False],
  ['por cierto','포르 시에르토','그런데 (화제 전환)','앞말을 뒤집는 게 아니라 <b>화제를 바꿀 때만</b>.','Por cierto, ¿a qué hora cierran?','포르 시에르토, 아 케 오라 시에란','그런데, 몇 시에 닫으세요?',True]]},
 {'label':'그래서 · 그러니까','items':[
  ['entonces','엔톤세스','그럼 · 그러니까','<b>결정을 내리는 순간</b>, 그리고 <b>말이 막혔을 때</b> 둘 다.','Entonces, me llevo esto.','엔톤세스, 메 예보 에스토','그럼 이걸로 할게요.',True],
  ['así que','아시 케','그래서','앞의 일 때문에 벌어진 결과. 회화에서 아주 흔합니다.','Es tarde, así que me voy.','에스 타르데, 아시 케 메 보이','늦었으니 갈게요.',True],
  ['porque','포르케','왜냐하면','이유를 답니다. 「왜?」라는 질문은 <span class="fr">¿Por qué?</span> — <b>띄어쓰기와 악센트로</b> 구별합니다.','Porque está cerrado.','포르케 에스타 세라도','닫혀 있어서요.',True],
  ['por eso','포르 에소','그래서 · 그 때문에','앞말을 이유로 받아 결론을 냅니다.','Por eso no fuimos.','포르 에소 노 푸이모스','그래서 안 갔어요.',False]]},
 {'label':'정리 · 되짚기','items':[
  ['por ejemplo','포르 에헴플로','예를 들면','추천을 받았는데 감이 안 올 때. <span class="fr">¿Por ejemplo?</span> 한 마디면 구체적으로 말해줍니다.','¿Por ejemplo?','포르 에헴플로','예를 들면요?',True],
  ['o sea','오 세아','그러니까 즉','상대 말을 <b>내가 이해한 대로 되짚을 때</b>. 현지인이 정말 자주 씁니다.','O sea, ¿hoy está cerrado?','오 세아, 오이 에스타 세라도','그러니까, 오늘 닫는다고요?',True],
  ['en fin','엔 핀','결국 · 아무튼','이야기를 접고 넘어갈 때.','En fin, está bien así.','엔 핀, 에스타 비엔 아시','아무튼 이걸로 괜찮아요.',False],
  ['a lo mejor','아 로 메호르','어쩌면','확신이 없을 때. 부드럽게 거절할 때도.','A lo mejor mañana.','아 로 메호르 마냐나','어쩌면 내일요.',True]]},
 {'label':'말이 막혔을 때','items':[
  ['Pues...','푸에스','음… 그러니까…','다음 말을 고르는 사이. <b>스페인어의 「음…」</b>입니다.','Pues... ¿cuánto cuesta?','푸에스... 쿠안토 쿠에스타','음… 얼마예요?',True],
  ['Bueno...','부에노','글쎄요 · 자 그럼','생각을 정리하며. 화제를 넘길 때도 씁니다.','Bueno, vamos.','부에노, 바모스','자, 그럼 갑시다.',True],
  ['Es que...','에스 케','그게 말이죠…','<b>변명이나 사정을 꺼내는 신호.</b> 이 말이 나오면 뒤에 이유가 따라옵니다.','Es que no hablo español.','에스 케 노 아블로 에스파뇰','그게, 제가 스페인어를 못해서요.',True],
  ['¿Cómo?','코모','네? · 뭐라고요?','못 알아들었을 때. <b>이 한 마디를 아끼지 마세요.</b>','¿Cómo? Más despacio.','코모? 마스 데스파시오','네? 좀 더 천천히요.',True]]},
]
