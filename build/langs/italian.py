# -*- coding: utf-8 -*-
LANG = {
 'order':1, 'nav':('ITALIANO','이탈리아어'),
 'file':'italian.html', 'serif':'Playfair Display',
 'grid':'#2E6144', 'gl':'rgba(46,97,68,.30)', 'glh':'rgba(46,97,68,.55)',
 'title':'이탈리아어 첫 일주일',
 'eyebrow':'ITALIANO · FIRST WEEK',
 'h1':'이탈리아어 일주일', 'h1sub':'italiano in una settimana',
 'lede':'이탈리아어는 <b>쓰인 대로 읽습니다.</b> 영어처럼 묵음 규칙을 외울 필요가 없고, 모음 다섯 개는 한국어와 거의 같은 소리입니다. 규칙 몇 개만 잡으면 처음 보는 단어도 읽힙니다.',
 's1':'읽는 법 — 규칙이 거의 전부', 's1sub':'이탈리아어에 묵음은 <b>h 하나뿐</b>입니다. 아래 규칙만 알면 메뉴판이든 표지판이든 소리 내어 읽을 수 있습니다.',
 's8':'꼭 외워야 할 동사 28', 's8sub':'이탈리아어는 <b>주어를 생략합니다.</b> 동사 어미가 누구인지 말해주기 때문입니다. 그래서 동사 하나를 두 가지 꼴(나 / 정중한 상대)로 외우면 바로 문장이 됩니다.',
 'foot':'8일째부터는 새 규칙 없이, 카페 메뉴판과 거리 간판을 <b>소리 내어</b> 읽으세요. 이탈리아어는 쓰기보다 <b>읽는 속도</b>가 실력입니다. 틀리게 읽어도 대부분 알아듣습니다 — 침묵보다 낫습니다.',
 'data':{
  'p1':'IO · 나', 'p2':'LEI · 정중',

  'soundRules':[
   ['RULE 1','쓰인 대로 읽습니다','이탈리아어에 묵음은 <b>h 하나뿐</b>입니다. <span class="fr">ho</span> 오, <span class="fr">hotel</span> 오텔. 영어처럼 「이 단어는 이렇게 읽는다」를 외울 일이 없습니다. <b>규칙을 알면 처음 보는 단어도 읽힙니다.</b>'],
   ['RULE 2','c와 g는 뒤 모음이 정합니다','<span class="fr">c·g + a·o·u</span> = 카·가. <span class="fr">c·g + e·i</span> = 체·제. <span class="fr">casa</span> 카사 / <span class="fr">cena</span> 체나. 딱딱한 소리로 되돌리려면 <b>h를 끼웁니다</b> — <span class="fr">che</span> <em>케</em>, <span class="fr">spaghetti</span> <em>스파게티</em>.'],
   ['RULE 3','모음 다섯 개가 절대 안 변합니다','<span class="fr">a 아 · e 에 · i 이 · o 오 · u 우</span>. 위치가 어디든 이 소리 그대로입니다. 영어를 배운 사람에게 가장 낯설고, <b>한국인에게는 가장 유리한</b> 지점입니다.'],
   ['RULE 4','겹자음은 한 박 쉽니다','<span class="fr">nonno</span>(논노, 할아버지)와 <span class="fr">nono</span>(노노, 아홉 번째)는 <b>다른 단어</b>입니다. 일본어 촉음(っ)과 같은 원리로, <em>길이가 뜻을 바꿉니다</em>. 겹자음 앞에서 살짝 멈추세요.'],
   ['RULE 5','강세는 뒤에서 두 번째','<span class="fr">piz-ze-RI-a</span>, <span class="fr">ge-LA-to</span>, <span class="fr">SPA-ghet-ti</span>. 대부분 뒤에서 두 번째 음절에 힘이 갑니다. 예외는 <b>악센트 표시</b>가 알려줍니다 — <span class="fr">città</span> 치<em>타</em>, <span class="fr">caffè</span> 카<em>페</em>.'],
   ['TIP','r은 혀끝을 한 번 튕깁니다','한국어 <b>ㄹ과 ㄷ의 중간</b>. 굴리지 못해도 통합니다. <span class="fr">rr</span>은 길게 굴리며 <span class="fr">caro</span>(비싼)와 <span class="fr">carro</span>(수레)를 가릅니다. 못 굴리겠으면 <b>그냥 ㄹ로</b> 말하세요 — 알아듣습니다.'],
  ],
  'soundGroups':[
   {'label':'모음 다섯 — 끝까지 이 소리 그대로','items':[
    ['a','아','casa','집',False],['e','에','bene','좋게',False],['i','이','vino','와인',False],
    ['o','오','sole','해',False],['u','우','luna','달',False]],
    'ex':[['Una birra, per favore.','우나 비라, 페르 파보레','맥주 한 잔 주세요.'],
          ['Che bello!','케 벨로','정말 멋지네요!']]},
   {'label':'c · g — 뒤에 오는 모음이 소리를 정합니다','items':[
    ['ca / co / cu','카 · 코 · 쿠','casa · cosa','집 · 것',False],
    ['ce / ci','체 · 치','cena · ciao','저녁 · 안녕',True],
    ['che / chi','케 · 키','che · chiave','무엇 · 열쇠',True],
    ['ga / go / gu','가 · 고 · 구','gatto','고양이',False],
    ['ge / gi','제 · 지','gelato · giro','젤라토 · 한 바퀴',True],
    ['ghe / ghi','게 · 기','spaghetti','스파게티',True]],
    'ex':[['Un gelato al cioccolato.','운 젤라토 알 초콜라토','초콜릿 젤라토 하나요.'],
          ['Che cosa è questo?','케 코자 에 퀘스토','이게 뭔가요?']]},
   {'label':'특별 조합 — 이 여섯만 알면 됩니다','items':[
    ['gn','뉴 (ㄴ+ㅣ)','gnocchi · bagno','뇨키 · 화장실',True],
    ['gli','리 (혀를 입천장에)','famiglia','가족',True],
    ['sce / sci','셰 · 시','pesce · sciare','생선 · 스키타다',True],
    ['z','츠 · 드즈','pizza · zero','피자 · 0',True],
    ['qu','쿠','quanto','얼마',False],
    ['h','묵음','ho · hotel','가지다 · 호텔',True]],
    'ex':[['Il bagno, per favore?','일 바뇨, 페르 파보레','화장실이 어디예요?'],
          ['Ho una prenotazione.','오 우나 프레노타치오네','예약이 있어요.']]},
   {'label':'악센트 표시 — 그 자리에 힘을 줍니다','items':[
    ['città','치타','città','도시',False],['caffè','카페','caffè','커피',False],
    ['perché','페르케','perché','왜 · 왜냐하면',False],['però','페로','però','그런데',False],
    ['più','피우','più','더',False],['è','에','è','~이다',True]],
    'ex':[['Un caffè, per favore.','운 카페, 페르 파보레','커피 한 잔 주세요.'],
          ['Perché no?','페르케 노','왜 안 되겠어요?']]},
  ],
  'pairs':[
   ['cena <em>/</em> che','둘 다 c로 시작하지만 <b>뒤 모음</b>이 다릅니다. <span class="fr">ce</span>는 <em>체</em>, <span class="fr">che</span>는 <em>케</em>. <b>h가 끼면 딱딱한 소리</b>로 되돌아간다고 기억하세요.'],
   ['gelato <em>/</em> spaghetti','g도 똑같습니다. <span class="fr">ge</span>는 <em>제</em>, <span class="fr">ghe</span>는 <em>게</em>. 이미 아는 두 단어라 이 짝으로 외우면 평생 안 헷갈립니다.'],
   ['gnocchi <em>/</em> famiglia','<span class="fr">gn</span>은 <em>뉴</em>(스페인어 ñ), <span class="fr">gli</span>는 <em>리</em>(혀를 입천장에 붙였다 떼며). 둘 다 한국어에 없는 소리라 <b>나란히</b> 연습하세요.'],
   ['nonno <em>/</em> nono','겹자음 하나로 <b>할아버지</b>와 <b>아홉 번째</b>가 갈립니다. <span class="fr">nn</span> 앞에서 한 박 멈추세요. 일본어 촉음과 완전히 같습니다.'],
   ['e <em>/</em> è','악센트 하나가 전부입니다. <span class="fr">e</span>는 <b>그리고</b>, <span class="fr">è</span>는 <b>~이다</b>. <span class="fr">pane e vino</span>(빵과 와인) / <span class="fr">è buono</span>(맛있다).'],
   ['pesce <em>/</em> scuola','<span class="fr">sc + e·i</span>는 <em>시</em> 소리, <span class="fr">sc + a·o·u</span>는 <em>스크</em>. c·g와 <b>완전히 같은 규칙</b>이니 하나로 묶어 외우세요.'],
   ['pizza <em>/</em> zero','같은 z인데 <span class="fr">pizza</span>는 <em>핏차</em>(무성), <span class="fr">zero</span>는 <em>제로</em>(유성). 규칙이 딱 떨어지지 않으니 <b>단어째로</b> 외웁니다.'],
   ['caro <em>/</em> carro','<span class="fr">r</span> 하나면 <b>비싼</b>, <span class="fr">rr</span>이면 <b>수레</b>. 못 굴려도 대화는 되지만, 겹자음은 <b>길게</b> 낸다는 감각은 잡아두세요.'],
  ],
  'notes':[
   ['h','이탈리아어의 <b>유일한 묵음</b>입니다. 절대 소리 내지 않습니다. <span class="fr">ho</span>는 <b>오</b>, <span class="fr">hanno</span>는 <b>안노</b>. 대신 c·g 뒤에 붙어 <b>소리를 딱딱하게</b> 되돌리는 일을 합니다.'],
   ['r','한국어 <b>ㄹ과 ㄷ의 중간</b>으로 혀끝을 한 번 튕깁니다. 굴리는 <b>rr</b>은 연습이 필요하지만, <em>못 굴려도 다 알아듣습니다</em>. 발음보다 말을 거는 게 중요합니다.'],
   ['모음','<b>절대 흐려지지 않습니다.</b> 영어는 강세 없는 모음을 「어」로 뭉개지만 이탈리아어는 끝까지 또렷합니다. <span class="fr">momento</span>는 「머멘트」가 아니라 <b>모멘토</b>.'],
   ['겹자음','<span class="fr">nonno · pizza · bello</span>. <b>한 박 멈춘 뒤</b> 소리를 냅니다. 한국인은 이걸 자주 빼먹는데, 이탈리아 사람에게는 <em>다른 단어로 들립니다</em>.'],
   ['강세','대부분 <b>뒤에서 두 번째 음절</b>. 이것만 지켜도 억양이 확 자연스러워집니다. 자신 없으면 <b>끝에서 두 번째를 조금 길게</b> 발음하세요.'],
   ['s','모음 사이에서는 <b>ㅈ에 가깝게</b> 울립니다. <span class="fr">rosa</span> 로자, <span class="fr">musica</span> 무지카. 북부일수록 뚜렷하고 남부는 ㅅ에 가깝습니다 — <b>어느 쪽이든 통합니다</b>.'],
   ['남성 · 여성','명사가 대개 <b>-o(남성) / -a(여성)</b>로 끝나고, 형용사가 여기에 맞춰 변합니다. <span class="fr">un caffè buono</span> / <span class="fr">una pizza buona</span>. <em>틀려도 다 알아듣습니다</em> — 겁내지 마세요.'],
   ['-i / -e','복수형은 <b>-o → -i</b>, <b>-a → -e</b>로 끝만 바뀝니다. <span class="fr">panino → panini</span>, <span class="fr">pizza → pizze</span>. 영어처럼 s를 붙이지 않습니다.'],
  ],
  'quiz':[
   {'label':'c · g','items':[
    ['casa','카사','집'],['cena','체나','저녁'],['ciao','차오','안녕'],['chiave','키아베','열쇠'],
    ['che','케','무엇'],['gatto','가토','고양이'],['gelato','젤라토','젤라토'],['giro','지로','한 바퀴'],
    ['spaghetti','스파게티','스파게티'],['cucina','쿠치나','부엌 · 요리']]},
   {'label':'특별 조합','items':[
    ['gnocchi','뇨키','뇨키'],['bagno','바뇨','화장실'],['famiglia','파밀리아','가족'],
    ['pesce','페셰','생선'],['pizza','핏차','피자'],['zero','제로','0'],
    ['quanto','콴토','얼마'],['hotel','오텔','호텔'],['sciare','시아레','스키 타다'],['aglio','알리오','마늘']]},
   {'label':'자주 보는 단어','items':[
    ['grazie','그라치에','고맙습니다'],['prego','프레고','천만에요'],['scusi','스쿠지','실례합니다'],
    ['acqua','아콰','물'],['vino','비노','와인'],['conto','콘토','계산서'],
    ['stazione','스타치오네','역'],['biglietto','빌리에토','표'],['uscita','우시타','출구'],['aperto','아페르토','영업 중']]},
   {'label':'악센트 · 겹자음','items':[
    ['città','치타','도시'],['caffè','카페','커피'],['perché','페르케','왜'],['più','피우','더'],
    ['nonno','논노','할아버지'],['bello','벨로','아름다운'],['freddo','프레도','차가운'],
    ['formaggio','포르마조','치즈'],['prosciutto','프로슈토','생햄'],['spiaggia','스피아자','해변']]},
  ],

  'numRules':[
   ['RULE 1','11~16만 따로 외웁니다','<span class="fr">undici · dodici · tredici · quattordici · quindici · sedici</span>. 여기까지는 <b>숫자 + dici</b> 꼴입니다. 17부터는 뒤집혀서 <span class="fr">dici + 숫자</span> — <span class="fr">diciassette(17) · diciotto(18) · diciannove(19)</span>.'],
   ['RULE 2','20 이상은 붙여 씁니다','<span class="fr">venti + uno = ventuno</span>, <span class="fr">trenta + tre = trentatré</span>. 앞말의 <b>끝 모음이 떨어지는</b> 자리가 있습니다. 규칙보다 <em>몇 개 소리째로</em> 외우는 게 빠릅니다.'],
   ['RULE 3','값은 「Quanto costa?」 하나','<span class="fr">Quanto costa?</span> 콴토 코스타 = 얼마예요? 물건이 여러 개면 <span class="fr">Quanto costano?</span>. 못 알아들으면 <span class="fr">Lo scriva, per favore</span>(써 주세요)로 넘기면 됩니다.'],
   ['TIP','카페는 서서 마시면 쌉니다','바에 서서(<span class="fr">al banco</span>) 마시면 1유로대, 앉으면(<span class="fr">al tavolo</span>) 두세 배입니다. <b>같은 커피인데 자릿값이 붙습니다.</b> 메뉴판에 값이 두 줄로 적혀 있으면 이 뜻입니다.'],
  ],
  'numGroups':[
   {'label':'0 ~ 10','items':[
    ['zero','','제로','0',False],['uno','','우노','1',False],['due','','두에','2',False],
    ['tre','','트레','3',False],['quattro','','콰트로','4',False],['cinque','','친퀘','5',False],
    ['sei','','세이','6',False],['sette','','세테','7',False],['otto','','오토','8',False],
    ['nove','','노베','9',False],['dieci','','디에치','10',False]],
    'ex':[['Siamo in due.','시아모 인 두에','두 명이에요.'],
          ['Un caffè e due cornetti.','운 카페 에 두에 코르네티','커피 하나랑 크루아상 둘이요.']]},
   {'label':'11 ~ 20 — 17에서 방향이 바뀝니다','items':[
    ['undici','','운디치','11',False],['dodici','','도디치','12',False],['tredici','','트레디치','13',False],
    ['quattordici','','콰토르디치','14',False],['quindici','','퀸디치','15',False],['sedici','','세디치','16',False],
    ['diciassette','','디차세테','17',True],['diciotto','','디초토','18',True],
    ['diciannove','','디챤노베','19',True],['venti','','벤티','20',False]],
    'ex':[['Sono le quindici.','소노 레 퀸디치','15시(오후 3시)입니다.'],
          ['Il diciotto, per favore.','일 디초토, 페르 파보레','18번으로 주세요.']]},
   {'label':'수십 · 백 · 천','items':[
    ['trenta','','트렌타','30',False],['quaranta','','콰란타','40',False],['cinquanta','','친콴타','50',False],
    ['sessanta','','세산타','60',False],['settanta','','세탄타','70',False],['ottanta','','오탄타','80',False],
    ['novanta','','노반타','90',False],['cento','','첸토','100',False],['mille','','밀레','1,000',False],
    ['duemila','','두에밀라','2,000',True]],
    'ex':[['Quanto costa?','콴토 코스타','얼마예요?'],
          ['Sono venticinque euro.','소노 벤티친퀘 에우로','25유로입니다.']]},
   {'label':'계산에 쓰는 말','items':[
    ['quanto','','콴토','얼마 · 몇',False],['euro','','에우로','유로',False],['prezzo','','프레초','가격',False],
    ['caro','','카로','비싼',False],['economico','','에코노미코','싼',False],
    ['il conto','','일 콘토','계산서',False],['scontrino','','스콘트리노','영수증',False],
    ['contanti','','콘탄티','현금',False],['carta','','카르타','카드',False],
    ['coperto','','코페르토','자릿세',True],['resto','','레스토','거스름돈',False],['sconto','','스콘토','할인',False]],
    'ex':[['Il conto, per favore.','일 콘토, 페르 파보레','계산서 주세요.'],
          ['Posso pagare con la carta?','포소 파가레 콘 라 카르타','카드로 낼 수 있나요?'],
          ["C'è il coperto?",'체 일 코페르토','자릿세가 있나요?']]},
  ],

  'timeRules':[
   ['RULE 1','시간은 「Sono le + 숫자」','<span class="fr">Sono le tre</span> = 3시입니다. <b>1시만</b> 예외로 <span class="fr">È l\'una</span>. 「몇 시예요?」는 <span class="fr"><em>Che ore sono?</em></span> 케 오레 소노.'],
   ['RULE 2','24시간제로 말합니다','기차표, 영업시간, 공연은 거의 <b>24시간제</b>입니다. <span class="fr">le quindici</span>(15시) = 오후 3시. 표를 볼 때 12를 빼면 됩니다.'],
   ['RULE 3','오후에는 가게가 닫습니다','<span class="fr">riposo</span>(리포조) — 대략 <b>13시부터 16시까지</b> 문을 닫는 가게가 많습니다. 특히 소도시. <em>일정을 이 시간대로 잡으면 허탕</em>입니다.'],
   ['TIP','요일과 달은 소문자','영어와 달리 <span class="fr">lunedì · gennaio</span>처럼 <b>소문자</b>로 씁니다. 그리고 요일 앞에 <span class="fr">il</span>을 붙이면 「매주 ~요일」이 됩니다 — <span class="fr">il lunedì</span> 매주 월요일.'],
  ],
  'timeGroups':[
   {'label':'몇 시 — ora','items':[
    ['Che ore sono?','','케 오레 소노','몇 시예요?',False],["È l'una",'','에 루나','1시입니다',True],
    ['Sono le due','','소노 레 두에','2시입니다',False],['e mezzo','','에 메조','30분',False],
    ['e un quarto','','에 운 콰르토','15분',False],['mezzogiorno','','메조조르노','정오',False],
    ['mezzanotte','','메자노테','자정',False],['minuto','','미누토','분',False],['ora','','오라','시간',False]],
    'ex':[['Che ore sono?','케 오레 소노','몇 시예요?'],
          ['Sono le sette e mezzo.','소노 레 세테 에 메조','7시 반이에요.'],
          ['A che ora apre?','아 케 오라 아프레','몇 시에 열어요?']]},
   {'label':'오늘 · 내일 · 하루의 때','items':[
    ['oggi','','오지','오늘',False],['domani','','도마니','내일',False],['ieri','','이에리','어제',False],
    ['adesso','','아데소','지금',False],['dopo','','도포','나중에',False],['presto','','프레스토','일찍',False],
    ['tardi','','타르디','늦게',False],['mattina','','마티나','아침',False],
    ['pomeriggio','','포메리조','오후',False],['sera','','세라','저녁',False],['notte','','노테','밤',False],
    ['stasera','','스타세라','오늘 저녁',False]],
    'ex':[['Partiamo domani mattina.','파르티아모 도마니 마티나','내일 아침에 떠나요.'],
          ['A stasera!','아 스타세라','오늘 저녁에 봐요!']]},
   {'label':'요일 — 소문자로 씁니다','items':[
    ['lunedì','','루네디','월요일',False],['martedì','','마르테디','화요일',False],
    ['mercoledì','','메르콜레디','수요일',False],['giovedì','','조베디','목요일',False],
    ['venerdì','','베네르디','금요일',False],['sabato','','사바토','토요일',False],
    ['domenica','','도메니카','일요일',False],['weekend','','위켄드','주말',False],
    ['chiuso','','키우조','휴무 · 닫힘',True],['aperto','','아페르토','영업 중',False]],
    'ex':[['È aperto domenica?','에 아페르토 도메니카','일요일에 여나요?'],
          ['Chiuso il lunedì.','키우조 일 루네디','매주 월요일 휴무.']]},
   {'label':'계절과 그때의 말','items':[
    ['primavera','','프리마베라','봄',False],['estate','','에스타테','여름',False],
    ['autunno','','아우툰노','가을',False],['inverno','','인베르노','겨울',False],
    ['caldo','','칼도','더운',False],['freddo','','프레도','추운',False],
    ['sole','','솔레','해',False],['pioggia','','피오자','비',False],
    ['ferragosto','','페라고스토','8월 15일 휴가철',True],['festa','','페스타','축제 · 공휴일',False]],
    'ex':[['Fa caldo oggi.','파 칼도 오지','오늘 덥네요.'],
          ["D'estate è pieno di turisti.",'데스타테 에 피에노 디 투리스티','여름엔 관광객으로 가득해요.']]},
  ],

  'placeRules':[
   ['RULE 1','1층은 「piano terra」입니다','이탈리아의 <span class="fr"><em>primo piano</em></span>는 <b>한국식 2층</b>입니다. 지상층은 <span class="fr">piano terra</span>(피아노 테라). 엘리베이터 버튼의 <b>T 또는 0</b>이 1층이니, 무심코 1을 누르면 한 층 위로 갑니다.'],
   ['RULE 2','길 안내는 네 단어면 됩니다','<span class="fr">destra</span>(오른쪽) · <span class="fr">sinistra</span>(왼쪽) · <span class="fr">dritto</span>(직진) · <span class="fr">qui vicino</span>(이 근처). <span class="fr">Dov\'è...?</span>(도베 = 어디예요?) 앞에 붙이면 길 찾기는 끝납니다.'],
   ['RULE 3','표는 타기 전에 각인합니다','버스·기차표는 <span class="fr">convalidare</span>(각인) — 승강장의 <b>작은 노란 기계</b>에 넣어야 유효합니다. 안 하면 표가 있어도 <em>벌금</em>입니다. 「각인했나요?」 = <span class="fr">Ha convalidato?</span>'],
   ['TIP','표지판 단어만 알아도','<span class="fr">uscita</span>(출구) · <span class="fr">entrata</span>(입구) · <span class="fr">spingere</span>(미시오) · <span class="fr">tirare</span>(당기시오) · <span class="fr">vietato</span>(금지). <b>읽기만 하면</b> 헤맬 일이 없습니다.'],
  ],
  'placeGroups':[
   {'label':'층 — piano','items':[
    ['piano terra','','피아노 테라','지상층 (한국 1층)',True],
    ['primo piano','','프리모 피아노','2층',True],
    ['secondo piano','','세콘도 피아노','3층',False],
    ['ultimo piano','','울티모 피아노','꼭대기 층',False],
    ['scale','','스칼레','계단',False],['ascensore','','아셴소레','엘리베이터',False],
    ['seminterrato','','세민테라토','지하',False]],
    'ex':[["Dov'è il bagno?",'도베 일 바뇨','화장실이 어디예요?'],
          ['È al primo piano.','에 알 프리모 피아노','2층에 있어요.']]},
   {'label':'방향과 위치','items':[
    ['dove','','도베','어디',False],['qui','','퀴','여기',False],['lì','','리','저기',False],
    ['a destra','','아 데스트라','오른쪽으로',False],['a sinistra','','아 시니스트라','왼쪽으로',False],
    ['sempre dritto','','셈프레 드리토','계속 직진',False],['vicino','','비치노','가까이',False],
    ['lontano','','론타노','멀리',False],['davanti','','다반티','앞',False],
    ['dietro','','디에트로','뒤',False],['accanto','','아칸토','옆',False],['angolo','','안골로','모퉁이',False]],
    'ex':[["Dov'è la stazione?",'도베 라 스타치오네','역이 어디예요?'],
          ['Sempre dritto, poi a destra.','셈프레 드리토, 포이 아 데스트라','계속 직진하다가 오른쪽이요.'],
          ['È qui vicino?','에 퀴 비치노','여기서 가까워요?']]},
   {'label':'시설 · 표지판','items':[
    ['stazione','','스타치오네','역',False],['aeroporto','','아에로포르토','공항',False],
    ['fermata','','페르마타','정류장',False],['biglietto','','빌리에토','표',False],
    ['binario','','비나리오','승강장',False],['uscita','','우시타','출구',False],
    ['entrata','','엔트라타','입구',False],['bagno','','바뇨','화장실',False],
    ['farmacia','','파르마치아','약국',False],['ospedale','','오스페달레','병원',False],
    ['banca','','반카','은행',False],['supermercato','','수페르메르카토','슈퍼마켓',False],
    ['spingere','','스핀제레','미시오',True],['tirare','','티라레','당기시오',True]],
    'ex':[['Da che binario parte?','다 케 비나리오 파르테','몇 번 승강장에서 떠나요?'],
          ["C'è una farmacia qui vicino?",'체 우나 파르마치아 퀴 비치노','근처에 약국 있나요?']]},
   {'label':'식당에서','items':[
    ['tavolo','','타볼로','테이블',False],['menù','','메누','메뉴',False],
    ['acqua','','아콰','물',False],['naturale','','나투랄레','생수 (무탄산)',False],
    ['frizzante','','프리찬테','탄산수',True],['primo','','프리모','첫 번째 코스 (파스타)',False],
    ['secondo','','세콘도','두 번째 코스 (고기·생선)',False],['contorno','','콘토르노','곁들임',False],
    ['dolce','','돌체','디저트',False],['vino della casa','','비노 델라 카자','하우스 와인',False]],
    'ex':[['Un tavolo per due, per favore.','운 타볼로 페르 두에, 페르 파보레','두 명 자리 부탁합니다.'],
          ['Acqua naturale, per favore.','아콰 나투랄레, 페르 파보레','무탄산 생수로 주세요.']]},
  ],
 }
}

# V(원형, 발음, 뜻, 유형, io형, Lei형, 예문, 예문발음, 예문뜻, 불규칙)
LANG['data']['verbRules'] = [
 ['RULE 1','주어를 씁니다? 안 씁니다','<span class="fr">io</span>(나)를 굳이 붙이지 않습니다. <b>동사 어미가 이미 누구인지 말해주기</b> 때문입니다. <span class="fr">Sono coreano</span> = (나는) 한국인입니다. 강조할 때만 주어를 붙입니다.'],
 ['RULE 2','어미는 세 가지','<span class="fr">-are</span>(parlare) · <span class="fr">-ere</span>(prendere) · <span class="fr">-ire</span>(partire). <b>-are가 압도적으로 많습니다.</b> 세 유형의 「나」꼴은 모두 <em>-o</em>로 끝나니, 우선 그것만 잡으세요.'],
 ['RULE 3','두 꼴만 외우면 됩니다','여행에서 필요한 건 <b>「나」꼴</b>과 <b>「정중한 상대」꼴</b> 둘입니다. 내 얘기는 <span class="fr">io</span>꼴, 상대에게 묻는 건 <span class="fr">Lei</span>꼴. 아래 카드가 이 두 칸입니다.'],
 ['RULE 4','vorrei 하나면 다 됩니다','<span class="fr"><em>Vorrei...</em></span> 보레이 = 「~을 원해요」의 정중한 꼴. 뒤에 <b>명사든 동사든</b> 붙입니다 — <span class="fr">Vorrei un caffè</span> / <span class="fr">Vorrei prenotare</span>. 이 한 마디가 여행 회화의 절반입니다.'],
 ['TIP','posso? 는 만능 허락','<span class="fr">Posso...?</span> 포소 = 「~해도 되나요?」. 뒤에 동사 원형만 붙이면 됩니다 — <span class="fr">Posso pagare con la carta?</span> / <span class="fr">Posso entrare?</span>'],
 ['TIP','과거는 「ho + 과거분사」','<span class="fr">ho mangiato</span>(먹었어요) · <span class="fr">ho perso</span>(잃어버렸어요). <b>ho</b>에 동사만 갈아 끼우면 과거가 됩니다. 완벽하지 않아도 <em>다 알아듣습니다</em>.'],
]

LANG['data']['verbSets'] = [
 {'n':'essere <i>·</i> avere', 'tip':'모든 문장의 뼈대. <span class="fr">essere</span>는 <b>~이다 · 있다</b>, <span class="fr">avere</span>는 <b>가지다</b>. 나이도 avere로 말합니다 — <span class="fr">Ho trent\'anni</span>(서른입니다).', 'items':[
  ['essere','에세레','~이다 · 있다','불규칙','sono 소노','è 에',"Sono coreano.",'소노 코레아노','저는 한국인입니다.',True],
  ['avere','아베레','가지다 · 있다','불규칙','ho 오','ha 아','Ho una prenotazione.','오 우나 프레노타치오네','예약이 있어요.',True]]},
 {'n':'andare <i>·</i> venire <i>·</i> tornare', 'tip':'방향 삼총사. 나에게서 <b>멀어지면</b> andare, <b>다가오면</b> venire, <b>원래 자리로</b> 돌아가면 tornare. 앞의 둘은 불규칙이라 소리째로 외웁니다.', 'items':[
  ['andare','안다레','가다','불규칙','vado 바도','va 바','Vado a Roma.','바도 아 로마','로마에 갑니다.',True],
  ['venire','베니레','오다','불규칙','vengo 벤고','viene 비에네','Quando viene il bus?','콴도 비에네 일 부스','버스는 언제 오나요?',True],
  ['tornare','토르나레','돌아가다','-are','torno 토르노','torna 토르나','Torno domani.','토르노 도마니','내일 돌아갑니다.',False]]},
 {'n':'volere <i>·</i> potere <i>·</i> dovere', 'tip':'뒤에 <b>동사 원형</b>을 그대로 붙이는 세 개. <span class="fr">Vorrei</span>(원해요) · <span class="fr">Posso</span>(해도 되나요) · <span class="fr">Devo</span>(해야 해요). <em>이 셋이면 웬만한 부탁과 질문이 끝납니다.</em>', 'items':[
  ['volere','볼레레','원하다','불규칙','vorrei 보레이','vuole 부올레','Vorrei un caffè.','보레이 운 카페','커피 한 잔 주세요.',True],
  ['potere','포테레','할 수 있다','불규칙','posso 포소','può 푸오','Posso entrare?','포소 엔트라레','들어가도 되나요?',True],
  ['dovere','도베레','해야 한다','불규칙','devo 데보','deve 데베','Devo andare.','데보 안다레','가봐야 해요.',True]]},
 {'n':'mangiare <i>·</i> bere <i>·</i> prendere', 'tip':'식당 삼총사. 주문할 때는 대개 <span class="fr">prendere</span>(잡다 → 시키다)를 씁니다 — <span class="fr">Prendo la pizza</span>(피자로 할게요). 영어의 「I\'ll have」와 같은 자리입니다.', 'items':[
  ['mangiare','만자레','먹다','-are','mangio 만조','mangia 만자','Non mangio carne.','논 만조 카르네','고기는 안 먹어요.',False],
  ['bere','베레','마시다','불규칙','bevo 베보','beve 베베','Bevo solo acqua.','베보 솔로 아콰','물만 마셔요.',True],
  ['prendere','프렌데레','잡다 · 주문하다','-ere','prendo 프렌도','prende 프렌데','Prendo la pizza.','프렌도 라 핏차','피자로 할게요.',False]]},
 {'n':'comprare <i>·</i> pagare <i>·</i> costare', 'tip':'계산대 세트. <span class="fr">costare</span>는 <b>물건이 주어</b>라 3인칭만 씁니다 — 하나면 <span class="fr">costa</span>, 여럿이면 <span class="fr">costano</span>.', 'items':[
  ['comprare','콤프라레','사다','-are','compro 콤프로','compra 콤프라','Vorrei comprare questo.','보레이 콤프라레 퀘스토','이걸 사고 싶어요.',False],
  ['pagare','파가레','지불하다','-are','pago 파고','paga 파가','Posso pagare con la carta?','포소 파가레 콘 라 카르타','카드로 낼 수 있나요?',False],
  ['costare','코스타레','값이 나가다','-are','costa 코스타','costano 코스타노','Quanto costa?','콴토 코스타','얼마예요?',False]]},
 {'n':'parlare <i>·</i> capire <i>·</i> sapere', 'tip':'말이 안 통할 때의 세 개. <span class="fr">capire</span>는 <b>-isc-</b>가 끼어드는 유형이라 <span class="fr">capisco</span>가 됩니다. <span class="fr">Non capisco</span>(못 알아듣겠어요)를 통째로 외우세요.', 'items':[
  ['parlare','파를라레','말하다','-are','parlo 파를로','parla 파를라','Parla inglese?','파를라 인글레제','영어 하세요?',False],
  ['capire','카피레','이해하다','-ire','capisco 카피스코','capisce 카피셰','Non capisco.','논 카피스코','못 알아듣겠어요.',True],
  ['sapere','사페레','알다','불규칙','so 소','sa 사','Non lo so.','논 로 소','그건 모르겠어요.',True]]},
 {'n':'cercare <i>·</i> trovare <i>·</i> perdere', 'tip':'잃어버렸을 때의 3연타. <span class="fr">Ho perso</span>(잃어버렸어요) → <span class="fr">Cerco</span>(찾고 있어요) → <span class="fr">Ho trovato</span>(찾았어요). 이 순서로 말하면 상황 설명이 끝납니다.', 'items':[
  ['cercare','체르카레','찾다','-are','cerco 체르코','cerca 체르카','Cerco questo indirizzo.','체르코 퀘스토 인디리초','이 주소를 찾고 있어요.',False],
  ['trovare','트로바레','발견하다','-are','trovo 트로보','trova 트로바','Non trovo il mio hotel.','논 트로보 일 미오 오텔','호텔을 못 찾겠어요.',False],
  ['perdere','페르데레','잃다 · 놓치다','-ere','perdo 페르도','perde 페르데','Ho perso il treno.','오 페르소 일 트레노','기차를 놓쳤어요.',False]]},
 {'n':'aspettare <i>·</i> arrivare <i>·</i> partire', 'tip':'이동 세트. 기차역 전광판에 <span class="fr">arrivi</span>(도착)와 <span class="fr">partenze</span>(출발)로 그대로 적혀 있습니다. <b>동사를 알면 표지판이 읽힙니다.</b>', 'items':[
  ['aspettare','아스페타레','기다리다','-are','aspetto 아스페토','aspetta 아스페타','Un momento, aspetti!','운 모멘토, 아스페티','잠깐만 기다려주세요!',False],
  ['arrivare','아리바레','도착하다','-are','arrivo 아리보','arriva 아리바','A che ora arriva?','아 케 오라 아리바','몇 시에 도착해요?',False],
  ['partire','파르티레','출발하다','-ire','parto 파르토','parte 파르테','Il treno parte alle otto.','일 트레노 파르테 알레 오토','기차는 8시에 떠나요.',False]]},
 {'n':'aprire <i>·</i> chiudere <i>·</i> fare', 'tip':'가게 앞에서. <span class="fr">aperto</span>(영업 중) / <span class="fr">chiuso</span>(닫힘)는 <b>문에 붙은 팻말</b> 그대로입니다. <span class="fr">fare</span>는 「하다·만들다」로 쓰임이 아주 넓습니다.', 'items':[
  ['aprire','아프리레','열다','-ire','apro 아프로','apre 아프레','A che ora apre?','아 케 오라 아프레','몇 시에 열어요?',False],
  ['chiudere','키우데레','닫다','-ere','chiudo 키우도','chiude 키우데','Quando chiude?','콴도 키우데','언제 닫아요?',False],
  ['fare','파레','하다 · 만들다','불규칙','faccio 파초','fa 파','Che lavoro fa?','케 라보로 파','무슨 일 하세요?',True]]},
 {'n':'piacere <i>·</i> vedere <i>·</i> dire', 'tip':'<span class="fr">piacere</span>는 <b>거꾸로 된 동사</b>입니다 — 「내가 좋아한다」가 아니라 「그것이 내 마음에 든다」. 그래서 <span class="fr">Mi piace</span>(단수) / <span class="fr">Mi piacciono</span>(복수)로 갈립니다.', 'items':[
  ['piacere','피아체레','마음에 들다','불규칙','mi piace 미 피아체','le piace 레 피아체','Mi piace molto!','미 피아체 몰토','정말 좋아요!',True],
  ['vedere','베데레','보다','-ere','vedo 베도','vede 베데','Vorrei vedere questo.','보레이 베데레 퀘스토','이거 보고 싶어요.',False],
  ['dire','디레','말하다','불규칙','dico 디코','dice 디체','Come si dice in italiano?','코메 시 디체 인 이탈리아노','이탈리아어로 뭐라고 해요?',True]]},
]

LANG['data']['talkRules'] = [
 ['RULE 1','가게에 들어가면 인사부터','<span class="fr">Buongiorno</span>(아침~오후) / <span class="fr">Buonasera</span>(저녁). <b>말없이 물건부터 보면 무례합니다.</b> 나올 때는 <span class="fr">Arrivederci</span> 또는 <span class="fr">Buona giornata</span>. 이 두 마디로 대접이 달라집니다.'],
 ['RULE 2','Ciao는 아는 사이에만','<span class="fr">Ciao</span>는 <b>반말</b>입니다. 친구·또래에게는 좋지만, 가게 주인이나 처음 보는 어른에게는 <span class="fr"><em>Buongiorno</em></span>가 맞습니다. 헷갈리면 무조건 Buongiorno.'],
 ['RULE 3','손이 같이 말합니다','이탈리아어는 <b>제스처가 문장의 일부</b>입니다. 단어가 막히면 손으로 가리키고 표정을 쓰세요. <em>말이 서툴러도 적극적이면 훨씬 잘 통합니다.</em>'],
 ['TIP','Prego는 만능','<b>천만에요 · 들어오세요 · 말씀하세요 · 먼저 가세요</b>가 전부 <span class="fr">Prego</span>입니다. 상대가 Grazie라고 하면 Prego로 받으세요. 이 한 단어가 여러 자리를 메웁니다.'],
]

LANG['data']['talkGroups'] = [
 {'label':'첫 마디 — 입을 떼는 순간','items':[
  ['Buongiorno.','부온조르노','안녕하세요. (아침~오후)','가게·식당·호텔 어디서든 <b>첫 마디</b>. 이것부터 하고 용건을 꺼냅니다.',True],
  ['Buonasera.','부오나세라','안녕하세요. (저녁)','대략 <b>오후 4~5시 이후</b>. 헷갈리면 Buongiorno로도 무난합니다.',False],
  ['Scusi.','스쿠지','실례합니다.','모르는 사람에게 말을 걸 때. 존댓말 꼴입니다(반말은 scusa).',True],
  ['Non parlo italiano.','논 파를로 이탈리아노','이탈리아어를 못해요.','먼저 밝히면 상대가 <b>속도를 늦춰줍니다</b>. 가성비 최고의 문장.',True],
  ['Parla inglese?','파를라 인글레제','영어 하세요?','관광지에서는 대개 통합니다. 안 되면 손짓과 숫자로.',False],
  ['Può parlare più lentamente?','푸오 파를라레 피우 렌타멘테','좀 더 천천히 말씀해 주실래요?','<span class="fr">Non capisco</span>보다 이쪽이 <b>대화를 이어줍니다</b>.',True],
  ['Sono coreano. / coreana.','소노 코레아노 · 코레아나','한국 사람이에요.','남자는 <span class="fr">-o</span>, 여자는 <span class="fr">-a</span>. 대화의 절반이 여기서 시작됩니다.',True]]},
 {'label':'부탁하기 — 이 세 틀이면 끝','items':[
  ['Vorrei...','보레이','~을 원해요 (정중)','<b>가장 많이 쓰게 될 한 마디.</b> 뒤에 명사든 동사 원형이든 붙입니다.',True],
  ['Posso...?','포소','~해도 되나요?','뒤에 동사 원형만. <span class="fr">Posso entrare? / Posso pagare?</span>',True],
  ["C'è...? / Ci sono...?",'체 · 치 소노','~이 있나요?','가게에서 물건을 찾을 때. <span class="fr">C\'è il wifi?</span>',False],
  ['Per favore.','페르 파보레','부탁합니다.','문장 끝에 붙이면 뭐든 정중해집니다.',True],
  ['Quanto costa?','콴토 코스타','얼마예요?','값을 묻는 기본. 여러 개면 <span class="fr">Quanto costano?</span>',False],
  ['Mi aiuti, per favore.','미 아이우티, 페르 파보레','좀 도와주세요.','정말 곤란할 때. 대부분 발 벗고 나서 줍니다.',False]]},
 {'label':'맞장구 — 대화를 굴리는 말','items':[
  ['Sì, certo.','시, 체르토','네, 물론이죠.','기본 긍정. 확신을 담아서.',False],
  ['Davvero?','다베로','정말요?','놀랐을 때. 살짝 올려서 말하면 리액션이 삽니다.',True],
  ['Che bello!','케 벨로','정말 멋지네요!','풍경·물건·이야기 무엇에든. 이탈리아 사람이 하루에 몇 번씩 쓰는 말.',True],
  ['Buonissimo!','부오니시모','정말 맛있어요!','<b>먹자마자, 크게.</b> 주방까지 들리면 분위기가 달라집니다.',True],
  ['Mi piace molto.','미 피아체 몰토','아주 마음에 들어요.','물건이든 음식이든 장소든.',False],
  ['Va bene.','바 베네','좋아요 · 괜찮아요.','제안을 받아들일 때의 기본 응답.',False],
  ['Non lo so.','논 로 소','그건 모르겠어요.','모를 때 솔직하게. 침묵보다 낫습니다.',False],
  ['Ho capito.','오 카피토','알겠어요.','설명을 듣고 이해했을 때.',False]]},
 {'label':'말을 트는 질문','items':[
  ['Come si chiama?','코메 시 키아마','성함이 어떻게 되세요?','조금 친해진 다음에. 이름을 주고받으면 분위기가 바뀝니다.',False],
  ['È di qui?','에 디 퀴','여기 분이세요?','현지인인지 묻는 가벼운 질문.',False],
  ['Cosa mi consiglia?','코자 미 콘실리아','뭘 추천해 주시겠어요?','<b>식당에서 이 한마디면</b> 주인이 신나서 설명합니다.',True],
  ['Qual è il piatto tipico?','콸 에 일 피아토 티피코','이 지역 대표 요리가 뭐예요?','관광객 메뉴 말고 진짜를 알려줍니다.',True],
  ['È mai stato in Corea?','에 마이 스타토 인 코레아','한국에 가보신 적 있어요?','거의 실패하지 않는 질문. 이야기가 이어집니다.',False],
  ['Posso fare una foto?','포소 파레 우나 포토','사진 찍어도 될까요?','가게 내부나 음식을 찍기 전에.',False]]},
 {'label':'마무리 — 자리를 뜰 때','items':[
  ['Grazie mille!','그라치에 밀레','정말 고맙습니다!','<span class="fr">grazie</span>보다 한 단계 따뜻합니다.',True],
  ['Prego.','프레고','천만에요 · 그러세요.','만능 응답. Grazie를 받으면 이걸로.',True],
  ['È stato un piacere.','에 스타토 운 피아체레','즐거웠습니다.','사람과 헤어질 때.',False],
  ['Arrivederci.','아리베데르치','안녕히 계세요.','가게를 나서며. 정중한 작별.',False],
  ['Buona giornata!','부오나 조르나타','좋은 하루 되세요!','낮에. 저녁이면 <span class="fr">Buona serata!</span>',True],
  ['A presto!','아 프레스토','또 봐요!','다시 올 것 같을 때. 빈말이어도 좋아합니다.',False]]},
]

LANG['data']['conjRules'] = [
 ['RULE 1','문장을 짧게 끊고 앞에 얹으세요','긴 문장을 만들려 하지 말고, <b>짧게 끊은 뒤 앞에 한 단어</b>를 붙이세요. <span class="fr">È caro. Però lo compro.</span>(비싸요. 그래도 살게요.) 이게 실제로 말이 되는 방식입니다.'],
 ['RULE 2','ma와 però는 자리가 다릅니다','<span class="fr">ma</span>는 <b>문장 중간</b>을 잇고, <span class="fr">però</span>는 <b>문장 맨 앞이나 끝</b>에 옵니다. <span class="fr">È buono ma caro</span> / <span class="fr">Però è caro</span>. 회화에서는 però가 더 자주 들립니다.'],
 ['TRAP','perché는 두 가지','<span class="fr">Perché?</span>는 <b>왜?</b>, 문장 중간의 <span class="fr">perché</span>는 <b>왜냐하면</b>입니다. <em>같은 단어가 질문도 되고 대답도 됩니다</em> — <span class="fr">Perché? Perché è tardi.</span>'],
 ['TIP','allora는 시간 벌기','<span class="fr">Allora...</span> 알로라 = 「그러니까…」. 다음 말을 고르는 사이에 넣는 <b>이탈리아어의 「음…」</b>입니다. 침묵보다 훨씬 자연스럽습니다.'],
]

LANG['data']['conjGroups'] = [
 {'label':'그리고 — 덧붙이기','items':[
  ['e','에','그리고','가장 기본. 모음 앞에서는 <span class="fr">ed</span>가 되기도 합니다.','Pane e vino.','파네 에 비노','빵과 와인.',False],
  ['poi','포이','그러고 나서','<b>순서</b>가 있을 때. 「그 다음에」.','Prendo un caffè, poi vado.','프렌도 운 카페, 포이 바도','커피 마시고, 그 다음에 갈게요.',True],
  ['anche','안케','또한 · ~도','「나도」는 <span class="fr">anch\'io</span> 안키오.','Anche per me, grazie.','안케 페르 메, 그라치에','저도 같은 걸로요.',True],
  ['inoltre','인올트레','게다가','이유를 보태 강조할 때. 조금 격식 있는 느낌.',"È buono, inoltre è economico.",'에 부오노, 인올트레 에 에코노미코','맛있고, 게다가 싸요.',False]]},
 {'label':'그런데 · 하지만 — 뒤집기','items':[
  ['ma','마','하지만','<b>문장 중간</b>을 잇습니다. 가장 기본적인 역접.','È buono ma caro.','에 부오노 마 카로','맛있는데 비싸요.',True],
  ['però','페로','그런데 · 그래도','<b>문장 앞이나 끝</b>에 옵니다. 회화에서 더 자주 들립니다.','È caro. Però lo prendo.','에 카로. 페로 로 프렌도','비싸요. 그래도 살게요.',True],
  ['invece','인베체','반면에 · ~ 대신','두 가지를 대비할 때.','Non il rosso, invece il bianco.','논 일 로소, 인베체 일 비안코','레드 말고 화이트로요.',False],
  ['comunque','코문퀘','어쨌든','이야기를 정리하고 넘어갈 때.','Comunque, grazie.','코문퀘, 그라치에','어쨌든 고마워요.',False]]},
 {'label':'그래서 · 그러니까','items':[
  ['allora','알로라','그럼 · 그러니까','<b>결정을 내리는 순간</b>, 그리고 <b>말이 막혔을 때</b> 둘 다.','Allora, prendo questo.','알로라, 프렌도 퀘스토','그럼 이걸로 할게요.',True],
  ['quindi','퀸디','그래서','앞의 일 때문에 벌어진 결과.','È tardi, quindi vado.','에 타르디, 퀸디 바도','늦었으니 갈게요.',False],
  ['perché','페르케','왜 · 왜냐하면','<b>질문도 되고 대답도 됩니다.</b> 억양으로 구별합니다.','Perché è chiuso.','페르케 에 키우조','닫혀 있어서요.',True],
  ['siccome','시코메','~이니까','<b>문장 맨 앞</b>에서만 이유를 답니다.','Siccome piove, restiamo.','시코메 피오베, 레스티아모','비가 오니까 여기 있죠.',False]]},
 {'label':'정리 · 되짚기','items':[
  ['per esempio','페르 에젬피오','예를 들면','추천을 받았는데 감이 안 올 때. <span class="fr">Per esempio?</span> 한 마디면 구체적으로 말해줍니다.','Per esempio?','페르 에젬피오','예를 들면요?',True],
  ['cioè','초에','그러니까 즉','상대 말을 <b>내가 이해한 대로 되짚을 때</b>.','Cioè, è chiuso oggi?','초에, 에 키우조 오지','그러니까, 오늘 닫는다고요?',False],
  ['insomma','인솜마','결국 · 그저 그래요','정리할 때도, <b>「그저 그렇다」</b>는 평가로도 씁니다.','Insomma, va bene così.','인솜마, 바 베네 코지','결국 이걸로 괜찮아요.',False],
  ['magari','마가리','어쩌면 · 그러면 좋겠다','<b>「그럴 수 있으면 좋겠다」</b>는 아쉬움까지 담는 이탈리아 특유의 말.','Magari domani.','마가리 도마니','어쩌면 내일요.',True]]},
 {'label':'말이 막혔을 때','items':[
  ['Allora...','알로라','음…','다음 말을 고르는 사이. <b>이탈리아어의 「음…」</b>입니다.','Allora... quanto costa?','알로라... 콴토 코스타','음… 얼마예요?',True],
  ['Senta,','센타','저기요,','말을 걸 때. <span class="fr">Scusi</span>보다 부드럽습니다.','Senta, dov\'è la stazione?','센타, 도베 라 스타치오네','저기요, 역이 어디예요?',True],
  ['Ecco','에코','자, 여기','물건을 건네며. <b>「여기 있어요」</b>의 자리.','Ecco a lei.','에코 아 레이','여기 있습니다.',False],
  ['Boh','보','글쎄요','<b>어깨를 으쓱하며.</b> 모르겠다는 뜻의 아주 구어적인 소리.','Boh, non lo so.','보, 논 로 소','글쎄요, 모르겠어요.',False]]},
]
