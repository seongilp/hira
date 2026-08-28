# -*- coding: utf-8 -*-
LANG = {
 'order':2, 'nav':('FRANCAIS','프랑스어'),
 'file':'french.html', 'serif':'EB Garamond',
 'grid':'#2F4A6D', 'gl':'rgba(47,74,109,.30)', 'glh':'rgba(47,74,109,.55)',
 'title':'프랑스어 첫 일주일',
 'eyebrow':'FRANCAIS · FIRST WEEK',
 'h1':'프랑스어 일주일', 'h1sub':'le français en une semaine',
 'lede':'프랑스어의 어려움은 문법이 아니라 <b>「쓰인 것과 읽는 것이 다르다」</b>는 데 있습니다. 그런데 그 차이에도 규칙이 있습니다. <b>끝 자음을 버리고, 모음 조합을 묶어 읽고, 콧소리 네 개를 익히면</b> 대부분 읽힙니다.',
 's1':'읽는 법 — 끝소리를 버립니다', 's1sub':'프랑스어는 <b>글자를 다 읽지 않습니다.</b> 무엇을 버리고 무엇을 묶는지, 그 규칙 다섯 개가 이 언어의 8할입니다.',
 's8':'꼭 외워야 할 동사 27', 's8sub':'프랑스어는 <b>주어를 반드시 씁니다.</b> 동사 어미가 대부분 같은 소리로 뭉개지기 때문입니다. 그래서 <b>「je + 동사」</b>를 한 덩어리로 외우는 편이 빠릅니다.',
 'foot':'8일째부터는 새 규칙 없이, 카페 메뉴판과 지하철 표지판을 <b>소리 내어</b> 읽으세요. 그리고 가게에 들어갈 때 반드시 <b>Bonjour</b>. 프랑스에서 이 한 마디의 유무가 대접을 가릅니다.',
 'data':{
  'p1':'JE · 나', 'p2':'VOUS · 정중',

  'soundRules':[
   ['RULE 1','끝 자음은 대개 버립니다','<span class="fr">Paris</span> 파리, <span class="fr">petit</span> 프티, <span class="fr">beaucoup</span> 보쿠. 단어 끝의 자음은 <b>거의 안 읽습니다</b>. 읽는 건 대체로 <span class="fr"><em>c · r · f · l</em></span> 넷 — 영어 단어 <b>CaReFuL</b>로 외우세요.'],
   ['RULE 2','끝의 e도 안 읽습니다','<span class="fr">porte</span> 포르트, <span class="fr">France</span> 프랑스. 끝의 <span class="fr">-e</span>는 소리가 없고, <b>앞 자음을 살려내는</b> 역할만 합니다. 그래서 <span class="fr">grand</span>(그랑)과 <span class="fr">grande</span>(그랑드)가 갈립니다.'],
   ['RULE 3','모음은 조합으로 읽습니다','글자 하나씩 읽으면 안 됩니다. <span class="fr">ou</span> 우 · <span class="fr">au·eau</span> 오 · <span class="fr">ai·ei</span> 에 · <span class="fr">oi</span> 와 · <span class="fr">eu</span> 외 · <span class="fr">ui</span> 위. <b>이 여섯 묶음이 전부</b>입니다.'],
   ['RULE 4','콧소리 네 개','<span class="fr">an·en</span> 앙 · <span class="fr">on</span> 옹 · <span class="fr">in·ain·ein</span> 앵 · <span class="fr">un</span> 욍. <b>입은 그대로 두고 코로</b> 소리를 보냅니다. 뒤에 모음이나 n이 더 오면 <em>비음이 풀립니다</em> — <span class="fr">bon</span> 봉 / <span class="fr">bonne</span> 본.'],
   ['RULE 5','연음 — 죽은 자음이 살아납니다','앞 단어의 묵음 끝자음이 <b>뒤 모음에 붙어</b> 되살아납니다. <span class="fr">vous avez</span> 부<em>자</em>베, <span class="fr">les amis</span> 레<em>자</em>미, <span class="fr">c\'est un</span> 세<em>탕</em>. 안 해도 통하지만, <b>하면 확 프랑스어처럼 들립니다.</b>'],
   ['TIP','강세는 마지막 음절','영어처럼 특정 음절을 세게 치지 않고, <b>구절 끝을 살짝 올리며</b> 끝냅니다. <span class="fr">bonjour</span>는 「<b>봉</b>주르」가 아니라 「봉<b>주르</b>」. 이것만 바꿔도 억양이 달라집니다.'],
  ],
  'soundGroups':[
   {'label':'모음 조합 — 이 여섯이 전부','items':[
    ['ou','우','vous · bonjour','당신 · 안녕하세요',False],
    ['au / eau','오','au · beau · eau','~에 · 아름다운 · 물',False],
    ['ai / ei','에','mais · seize','하지만 · 16',False],
    ['oi','와','moi · trois','나 · 3',True],
    ['eu / œu','외','deux · sœur','2 · 누이',True],
    ['ui','위','oui · huit','네 · 8',True],
    ['u','위 (입술 오므리고 이)','tu · rue','너 · 거리',True],
    ['é','에','café · été','카페 · 여름',False]],
    'ex':[["S'il vous plaît.",'실 부 플레','부탁합니다.'],
          ['Trois cafés, merci.','트루아 카페, 메르시','커피 세 잔이요, 고맙습니다.']]},
   {'label':'콧소리 넷 — 입은 그대로, 코로','items':[
    ['an / en','앙','grand · comment','큰 · 어떻게',True],
    ['on','옹','bon · bonjour','좋은 · 안녕하세요',True],
    ['in / ain / ein','앵','vin · pain · plein','와인 · 빵 · 가득한',True],
    ['un','욍 (앵에 가깝게)','un · lundi','하나 · 월요일',True],
    ['bonne','본 (비음 풀림)','bonne · bonne nuit','좋은(여성) · 잘 자요',False],
    ['-tion','시옹','addition · station','계산서 · 역',True]],
    'ex':[["L'addition, s'il vous plaît.",'라디시옹, 실 부 플레','계산서 주세요.'],
          ['Un verre de vin rouge.','앙 베르 드 뱅 루주','레드와인 한 잔이요.']]},
   {'label':'자음 — 영어와 다른 것만','items':[
    ['ch','슈','chat · chercher','고양이 · 찾다',True],
    ['j / ge','즈','je · rouge','나 · 빨간',True],
    ['gn','뉴','montagne · champagne','산 · 샴페인',False],
    ['qu','크','qui · quatre','누구 · 4',True],
    ['ç','스','ça · français','그것 · 프랑스의',False],
    ['ill','이유','famille · billet','가족 · 표',True],
    ['h','묵음','hôtel · heure','호텔 · 시간',True],
    ['r','목 안쪽에서','Paris · merci','파리 · 고마워요',True]],
    'ex':[["Je cherche l'hôtel.",'즈 셰르슈 로텔','호텔을 찾고 있어요.'],
          ['Un billet, s\'il vous plaît.','앙 비예, 실 부 플레','표 한 장 주세요.']]},
   {'label':'끝소리 — 무엇을 버리는가','items':[
    ['-e','묵음','porte · France','문 · 프랑스',False],
    ['-s','묵음','Paris · vous','파리 · 당신',False],
    ['-t / -d','묵음','petit · grand','작은 · 큰',False],
    ['-er','에','parler · manger','말하다 · 먹다',True],
    ['-ez','에','vous avez','당신은 가지고 있다',True],
    ['-ent (동사)','묵음','ils parlent','그들이 말한다',True],
    ['c · r · f · l','읽습니다','avec · bonjour · chef · hôtel','~와 · 안녕 · 셰프 · 호텔',True]],
    'ex':[['Vous parlez anglais ?','부 파를레 앙글레','영어 하세요?'],
          ["C'est très bon !",'세 트레 봉','정말 맛있어요!']]},
  ],
  'pairs':[
   ['vous <em>/</em> tu','<b>한국인 최대 난관.</b> <span class="fr">ou</span>는 입술을 동그랗게 <em>우</em>, <span class="fr">u</span>는 입술은 우 모양 그대로 두고 <em>이</em>를 냅니다. 이 둘이 안 갈리면 <span class="fr">dessous</span>(아래)와 <span class="fr">dessus</span>(위)가 같아집니다.'],
   ['bon <em>/</em> banc','<span class="fr">on</span>은 <em>옹</em>, <span class="fr">an</span>은 <em>앙</em>. 입을 얼마나 벌리느냐의 차이입니다. <b>on은 오무리고, an은 벌리고.</b>'],
   ['vin <em>/</em> vent','<span class="fr">in</span>은 <em>앵</em>(와인), <span class="fr">en</span>은 <em>앙</em>(바람). 콧소리 넷 중 이 짝이 가장 자주 부딪힙니다.'],
   ['bon <em>/</em> bonne','뒤에 <span class="fr">-ne</span>가 붙으면 <b>비음이 풀립니다</b>. 봉 → 본. <span class="fr">Bonne nuit</span>는 「봉 뉘」가 아니라 <em>본 뉘</em>.'],
   ['grand <em>/</em> grande','끝의 <span class="fr">-e</span>가 <b>죽어 있던 d를 살립니다</b>. 그랑 → 그랑드. 남성형·여성형의 소리 차이가 대부분 이 원리입니다.'],
   ['é <em>/</em> è <em>/</em> e','<span class="fr">é</span>는 <em>에</em>(입을 좁게), <span class="fr">è</span>는 <em>에</em>(입을 넓게), 표시 없는 끝의 <span class="fr">e</span>는 <b>소리 없음</b>. 악센트가 소리를 지정합니다.'],
   ['ch <em>/</em> qu','<span class="fr">ch</span>는 <em>슈</em>(chat 샤), <span class="fr">qu</span>는 <em>크</em>(qui 키). 영어와 정반대라 자주 뒤집힙니다.'],
   ['les amis <em>/</em> les livres','앞은 <b>연음</b>이 일어나 레<em>자</em>미, 뒤는 자음으로 시작해 그냥 레 리브르. <b>뒤가 모음이면 붙는다</b>고만 기억하세요.'],
  ],
  'notes':[
   ['r','<b>혀가 아니라 목</b>에서 냅니다. 가래 뱉듯 목젖을 살짝 떨죠. 안 되면 <b>ㅎ에 가깝게</b> 내세요 — <span class="fr">merci</span> 메흐시. <em>못해도 다 알아듣습니다.</em>'],
   ['u','한국어에 없는 소리입니다. <b>「우」 입 모양에서 「이」를 소리 내면</b> 됩니다. <span class="fr">tu</span> 튀, <span class="fr">rue</span> 뤼, <span class="fr">salut</span> 살뤼.'],
   ['연음','<span class="fr">vous avez</span> 부자베처럼 <b>붙여 읽습니다</b>. 안 해도 통하지만, 하면 훨씬 자연스럽습니다. 다만 <span class="fr">et</span>(그리고) 뒤에는 <em>절대 연음하지 않습니다</em>.'],
   ['묵음 h','h는 <b>어디서든 소리가 없습니다</b>. <span class="fr">hôtel</span> 오텔, <span class="fr">heure</span> 외르. 앞말과 연음까지 일어납니다 — <span class="fr">deux heures</span> 되<b>죄</b>르.'],
   ['숫자 소리 변화','<span class="fr">six</span>는 혼자면 <b>시스</b>, 뒤에 자음이 오면 <b>시</b>, 모음이 오면 <b>시즈</b>. <span class="fr">dix</span>도 같습니다. <em>규칙보다 자주 쓰는 조합으로</em> 익히세요.'],
   ['남성 · 여성','명사마다 <span class="fr">le</span>(남성) / <span class="fr">la</span>(여성)가 정해져 있고 규칙이 없습니다. <b>틀려도 다 알아듣습니다</b> — 헷갈리면 <span class="fr">un</span>이나 <span class="fr">le</span>로 밀고 가세요.'],
   ['부정문','<span class="fr">ne ... pas</span>로 동사를 감쌉니다. <span class="fr">Je ne sais pas</span>(모르겠어요). 회화에서는 <b>ne를 빼고</b> <span class="fr">Je sais pas</span>라고도 많이 합니다.'],
   ['억양','단어마다 힘을 주지 않고 <b>구절 전체를 하나로</b> 흘린 뒤 끝을 살짝 올립니다. 한국어처럼 또박또박 끊으면 어색하게 들립니다.'],
  ],
  'quiz':[
   {'label':'모음 조합','items':[
    ['vous','부','당신'],['beaucoup','보쿠','많이'],['moi','무아','나'],['deux','되','2'],
    ['oui','위','네'],['café','카페','커피'],['eau','오','물'],['mais','메','하지만'],
    ['tu','튀','너'],['rue','뤼','거리']]},
   {'label':'콧소리','items':[
    ['bonjour','봉주르','안녕하세요'],['vin','뱅','와인'],['pain','팽','빵'],['grand','그랑','큰'],
    ['comment','코망','어떻게'],['bonne','본','좋은(여성)'],['addition','라디시옹','계산서'],
    ['un','앙','하나'],['lundi','룅디','월요일'],['plein','플랭','가득한']]},
   {'label':'자음','items':[
    ['chat','샤','고양이'],['je','즈','나'],['rouge','루주','빨간'],['qui','키','누구'],
    ['ça','사','그것'],['famille','파미유','가족'],['billet','비예','표'],
    ['hôtel','오텔','호텔'],['merci','메르시','고마워요'],['champagne','샹파뉴','샴페인']]},
   {'label':'끝소리 · 자주 보는 단어','items':[
    ['Paris','파리','파리'],['petit','프티','작은'],['porte','포르트','문'],['parler','파를레','말하다'],
    ['sortie','소르티','출구'],['entrée','앙트레','입구'],['gare','가르','역'],
    ['toilettes','투알레트','화장실'],['ouvert','우베르','영업 중'],['fermé','페르메','닫힘']]},
  ],

  'numRules':[
   ['RULE 1','70 · 80 · 90은 계산입니다','<span class="fr"><em>soixante-dix</em></span> = 60+10 = <b>70</b>. <span class="fr"><em>quatre-vingts</em></span> = 4×20 = <b>80</b>. <span class="fr"><em>quatre-vingt-dix</em></span> = 4×20+10 = <b>90</b>. 프랑스어의 악명 높은 부분이지만, <b>이 셋뿐</b>입니다.'],
   ['RULE 2','71~79는 60대에 얹습니다','<span class="fr">soixante et onze</span>(71) = 60 + 11. 마찬가지로 <span class="fr">quatre-vingt-onze</span>(91) = 80 + 11. <b>11~19를 알면</b> 여기가 자동으로 풀립니다.'],
   ['RULE 3','값은 「Ça fait combien ?」','사 페 콩비앙 = 전부 얼마예요? 물건 하나면 <span class="fr">C\'est combien ?</span> 세 콩비앙. <b>둘 다 통합니다.</b>'],
   ['TIP','1은 남성·여성이 갈립니다','<span class="fr">un</span>(남성) / <span class="fr">une</span>(여성). <span class="fr">un café</span> / <span class="fr">une bière</span>. 2부터는 구별이 없으니 <b>1만 신경 쓰면</b> 됩니다.'],
  ],
  'numGroups':[
   {'label':'0 ~ 10','items':[
    ['zéro','','제로','0',False],['un / une','','앙 · 윈','1',True],['deux','','되','2',False],
    ['trois','','트루아','3',False],['quatre','','카트르','4',False],['cinq','','생크','5',False],
    ['six','','시스','6',True],['sept','','세트','7',False],['huit','','위트','8',False],
    ['neuf','','뇌프','9',False],['dix','','디스','10',True]],
    'ex':[['Une table pour deux.','윈 타블 푸르 되','두 명 자리요.'],
          ['Un café et deux croissants.','앙 카페 에 되 크루아상','커피 하나랑 크루아상 둘이요.']]},
   {'label':'11 ~ 20','items':[
    ['onze','','옹즈','11',False],['douze','','두즈','12',False],['treize','','트레즈','13',False],
    ['quatorze','','카토르즈','14',False],['quinze','','캥즈','15',False],['seize','','세즈','16',False],
    ['dix-sept','','디세트','17',False],['dix-huit','','디즈위트','18',False],
    ['dix-neuf','','디즈뇌프','19',False],['vingt','','뱅','20',False]],
    'ex':[['Il est quinze heures.','일 레 캥즈 외르','15시(오후 3시)입니다.'],
          ['Chambre dix-huit.','샹브르 디즈위트','18호실이요.']]},
   {'label':'수십 — 70·80·90이 계산입니다','items':[
    ['trente','','트랑트','30',False],['quarante','','카랑트','40',False],
    ['cinquante','','생캉트','50',False],['soixante','','수아상트','60',False],
    ['soixante-dix','','수아상트 디스','70 (60+10)',True],
    ['quatre-vingts','','카트르 뱅','80 (4×20)',True],
    ['quatre-vingt-dix','','카트르 뱅 디스','90 (4×20+10)',True],
    ['cent','','상','100',False],['mille','','밀','1,000',False]],
    'ex':[['Ça fait combien ?','사 페 콩비앙','전부 얼마예요?'],
          ['Vingt-cinq euros.','뱅생크 외로','25유로입니다.']]},
   {'label':'계산에 쓰는 말','items':[
    ['combien','','콩비앙','얼마 · 몇',False],['euro','','외로','유로',False],
    ['prix','','프리','가격',False],['cher','','셰르','비싼',False],
    ["pas cher",'','파 셰르','싼',False],["l'addition",'','라디시옹','계산서',False],
    ['reçu','','르쉬','영수증',False],['espèces','','에스페스','현금',False],
    ['carte','','카르트','카드',False],['monnaie','','모네','잔돈',False],
    ['pourboire','','푸르부아르','팁',False],['service compris','','세르비스 콩프리','서비스료 포함',True]],
    'ex':[["L'addition, s'il vous plaît.",'라디시옹, 실 부 플레','계산서 주세요.'],
          ['Je peux payer par carte ?','즈 푀 페이예 파르 카르트','카드로 낼 수 있나요?']]},
  ],

  'timeRules':[
   ['RULE 1','시간은 「Il est + 숫자 + heures」','<span class="fr">Il est trois heures</span> = 3시입니다. <b>1시만</b> <span class="fr">une heure</span>. 「몇 시예요?」는 <span class="fr"><em>Quelle heure est-il ?</em></span> 켈 뢰르 에틸.'],
   ['RULE 2','24시간제로 적습니다','기차표·영업시간·공연은 거의 24시간제입니다. <span class="fr">15h30</span> = 오후 3시 반. 말할 때도 <span class="fr">quinze heures trente</span>라고 그대로 읽습니다.'],
   ['RULE 3','일요일엔 많이 닫습니다','상점·슈퍼가 <b>일요일에 문을 닫는</b> 곳이 많고, 작은 가게는 <span class="fr">lundi</span>(월요일)도 쉽니다. <em>일정을 짜기 전에 영업일을 확인하세요.</em>'],
   ['TIP','요일과 달은 소문자','영어와 달리 <span class="fr">lundi · janvier</span>처럼 <b>소문자</b>입니다. 요일 앞에 <span class="fr">le</span>를 붙이면 「매주 ~요일」 — <span class="fr">le lundi</span> 매주 월요일.'],
  ],
  'timeGroups':[
   {'label':'몇 시 — heure','items':[
    ['Quelle heure est-il ?','','켈 뢰르 에틸','몇 시예요?',False],
    ['Il est une heure','','일 레 튄 뢰르','1시입니다',True],
    ['deux heures','','되죄르','2시',True],['et demie','','에 드미','30분',False],
    ['et quart','','에 카르','15분',False],['midi','','미디','정오',False],
    ['minuit','','미뉘','자정',False],['minute','','미뉘트','분',False],['heure','','외르','시간',False]],
    'ex':[['Quelle heure est-il ?','켈 뢰르 에틸','몇 시예요?'],
          ['Il est sept heures et demie.','일 레 세 뢰르 에 드미','7시 반이에요.'],
          ['Ça ouvre à quelle heure ?','사 우브르 아 켈 뢰르','몇 시에 열어요?']]},
   {'label':'오늘 · 내일 · 하루의 때','items':[
    ["aujourd'hui",'','오주르뒤','오늘',True],['demain','','드맹','내일',False],
    ['hier','','이에르','어제',False],['maintenant','','맹트낭','지금',False],
    ['plus tard','','플뤼 타르','나중에',False],['tôt','','토','일찍',False],
    ['tard','','타르','늦게',False],['matin','','마탱','아침',False],
    ['après-midi','','아프레 미디','오후',False],['soir','','수아르','저녁',False],
    ['nuit','','뉘','밤',False],['ce soir','','스 수아르','오늘 저녁',False]],
    'ex':[['On part demain matin.','옹 파르 드맹 마탱','내일 아침에 떠나요.'],
          ['À ce soir !','아 스 수아르','오늘 저녁에 봐요!']]},
   {'label':'요일 — 소문자로 씁니다','items':[
    ['lundi','','룅디','월요일',False],['mardi','','마르디','화요일',False],
    ['mercredi','','메르크르디','수요일',False],['jeudi','','죄디','목요일',False],
    ['vendredi','','방드르디','금요일',False],['samedi','','삼디','토요일',False],
    ['dimanche','','디망슈','일요일',False],['week-end','','위켄드','주말',False],
    ['ouvert','','우베르','영업 중',False],['fermé','','페르메','휴무 · 닫힘',True]],
    'ex':[["C'est ouvert dimanche ?",'세 투베르 디망슈','일요일에 여나요?'],
          ['Fermé le lundi.','페르메 르 룅디','매주 월요일 휴무.']]},
   {'label':'계절과 그때의 말','items':[
    ['printemps','','프랭탕','봄',False],['été','','에테','여름',False],
    ['automne','','오톤','가을',True],['hiver','','이베르','겨울',False],
    ['chaud','','쇼','더운',False],['froid','','프루아','추운',False],
    ['soleil','','솔레유','해',False],['pluie','','플뤼이','비',False],
    ['grève','','그레브','파업',True],['jour férié','','주르 페리에','공휴일',False]],
    'ex':[["Il fait chaud aujourd'hui.",'일 페 쇼 오주르뒤','오늘 덥네요.'],
          ["Il y a une grève aujourd'hui ?",'일리 아 윈 그레브 오주르뒤','오늘 파업이 있나요?']]},
  ],

  'placeRules':[
   ['RULE 1','1층은 「rez-de-chaussée」','프랑스의 <span class="fr"><em>premier étage</em></span>는 <b>한국식 2층</b>입니다. 지상층은 <span class="fr">rez-de-chaussée</span>(레드쇼세), 엘리베이터 버튼의 <b>RC 또는 0</b>. 무심코 1을 누르면 한 층 위로 갑니다.'],
   ['RULE 2','길 안내는 네 단어','<span class="fr">à droite</span>(오른쪽) · <span class="fr">à gauche</span>(왼쪽) · <span class="fr">tout droit</span>(직진) · <span class="fr">près d\'ici</span>(이 근처). 앞에 <span class="fr">Où est... ?</span>(우 에 = 어디예요?)만 붙이면 됩니다.'],
   ['RULE 3','화장실은 항상 복수','<span class="fr"><em>les toilettes</em></span> — 늘 복수형입니다. <span class="fr">Où sont les toilettes ?</span> 우 송 레 투알레트. 카페에서는 <b>주문한 손님만</b> 쓸 수 있는 곳이 많습니다.'],
   ['TIP','표지판 단어만 읽어도','<span class="fr">sortie</span>(출구) · <span class="fr">entrée</span>(입구) · <span class="fr">poussez</span>(미시오) · <span class="fr">tirez</span>(당기시오) · <span class="fr">interdit</span>(금지). <b>읽기만 하면</b> 헤맬 일이 없습니다.'],
  ],
  'placeGroups':[
   {'label':'층 — étage','items':[
    ['rez-de-chaussée','','레드쇼세','지상층 (한국 1층)',True],
    ['premier étage','','프르미에 에타주','2층',True],
    ['deuxième étage','','되지엠 에타주','3층',False],
    ['dernier étage','','데르니에 에타주','꼭대기 층',False],
    ['sous-sol','','수 솔','지하',False],['escalier','','에스칼리에','계단',False],
    ['ascenseur','','아상쇠르','엘리베이터',False]],
    'ex':[['Où sont les toilettes ?','우 송 레 투알레트','화장실이 어디예요?'],
          ["C'est au premier étage.",'세 토 프르미에 에타주','2층에 있어요.']]},
   {'label':'방향과 위치','items':[
    ['où','','우','어디',False],['ici','','이시','여기',False],['là','','라','저기',False],
    ['à droite','','아 드루아트','오른쪽으로',False],['à gauche','','아 고슈','왼쪽으로',False],
    ['tout droit','','투 드루아','계속 직진',False],['près','','프레','가까이',False],
    ['loin','','루앙','멀리',False],['devant','','드방','앞',False],
    ['derrière','','데리에르','뒤',False],['à côté','','아 코테','옆',False],['coin','','쿠앙','모퉁이',False]],
    'ex':[['Où est la gare ?','우 에 라 가르','역이 어디예요?'],
          ['Tout droit, puis à droite.','투 드루아, 퓌 아 드루아트','계속 직진하다가 오른쪽이요.'],
          ["C'est près d'ici ?",'세 프레 디시','여기서 가까워요?']]},
   {'label':'시설 · 표지판','items':[
    ['gare','','가르','역',False],['aéroport','','아에로포르','공항',False],
    ['arrêt','','아레','정류장',False],['billet','','비예','표',False],
    ['quai','','케','승강장',False],['sortie','','소르티','출구',False],
    ['entrée','','앙트레','입구',False],['toilettes','','투알레트','화장실',False],
    ['pharmacie','','파르마시','약국',False],['hôpital','','오피탈','병원',False],
    ['banque','','방크','은행',False],['boulangerie','','불랑주리','빵집',False],
    ['poussez','','푸세','미시오',True],['tirez','','티레','당기시오',True]],
    'ex':[['De quel quai part le train ?','드 켈 케 파르 르 트랭','기차는 몇 번 승강장에서 떠나요?'],
          ["Il y a une pharmacie près d'ici ?",'일리 아 윈 파르마시 프레 디시','근처에 약국 있나요?']]},
   {'label':'카페 · 식당에서','items':[
    ['une table','','윈 타블','테이블 하나',False],['la carte','','라 카르트','메뉴판',True],
    ['le menu','','르 므뉘','세트 메뉴',True],["une carafe d'eau",'','윈 카라프 도','수돗물 한 병 (무료)',True],
    ['en terrasse','','앙 테라스','테라스 자리',False],['entrée','','앙트레','전채',False],
    ['plat','','플라','메인',False],['dessert','','데세르','디저트',False],
    ['saignant','','세냥','레어',False],['à point','','아 푸앙','미디엄',False],
    ['bien cuit','','비앙 퀴','웰던',False],['emporter','','앙포르테','포장',False]],
    'ex':[["Une carafe d'eau, s'il vous plaît.",'윈 카라프 도, 실 부 플레','물 한 병 주세요. (무료 수돗물)'],
          ['La carte, s\'il vous plaît.','라 카르트, 실 부 플레','메뉴판 주세요.'],
          ["C'est à emporter.",'세 타 앙포르테','포장이요.']]},
  ],
 }
}

LANG['data']['verbRules'] = [
 ['RULE 1','주어를 반드시 씁니다','이탈리아어와 정반대입니다. <span class="fr">je · vous</span>를 <b>빼면 안 됩니다</b>. 동사 어미가 대부분 같은 소리로 뭉개져서 주어가 없으면 누구인지 알 수 없기 때문입니다.'],
 ['RULE 2','어미는 -er가 90%','<span class="fr">parler · manger · aimer · chercher</span>. <b>-er 동사는 규칙이 하나</b>입니다 — <span class="fr">je parle</span> / <span class="fr">vous parlez</span>. 나머지 <span class="fr">-ir · -re</span>와 불규칙만 따로 챙기면 됩니다.'],
 ['RULE 3','두 꼴만 외우면 됩니다','여행에서 필요한 건 <b>「나」꼴</b>과 <b>「정중한 상대」꼴</b> 둘입니다. 내 얘기는 <span class="fr">je</span>, 상대에게 묻는 건 <span class="fr">vous</span>. 아래 카드가 이 두 칸입니다.'],
 ['RULE 4','je voudrais 하나면 됩니다','<span class="fr"><em>Je voudrais...</em></span> 즈 부드레 = 「~을 원해요」의 정중한 꼴. <span class="fr">Je veux</span>(원한다)는 <b>아이 말투로 무례하게</b> 들리니, 반드시 voudrais 쪽으로.'],
 ['TIP','허락은 「Je peux...?」','즈 푀 = 「~해도 되나요?」. 뒤에 동사 원형만 붙입니다 — <span class="fr">Je peux payer par carte ?</span> / <span class="fr">Je peux entrer ?</span>'],
 ['TIP','과거는 「j\'ai + 과거분사」','<span class="fr">j\'ai mangé</span>(먹었어요) · <span class="fr">j\'ai perdu</span>(잃어버렸어요). <b>j\'ai</b>에 동사만 갈아 끼우면 과거가 됩니다. <em>정확하지 않아도 다 알아듣습니다.</em>'],
]

LANG['data']['verbSets'] = [
 {'n':'être <i>·</i> avoir', 'tip':'모든 문장의 뼈대. <span class="fr">être</span>는 <b>~이다</b>, <span class="fr">avoir</span>는 <b>가지다</b>. 나이도 avoir로 말합니다 — <span class="fr">J\'ai trente ans</span>(서른입니다).', 'items':[
  ['être','에트르','~이다','불규칙','je suis 즈 쉬','vous êtes 부 제트','Je suis coréen.','즈 쉬 코레앙','저는 한국인입니다.',True],
  ['avoir','아부아르','가지다','불규칙',"j'ai 제",'vous avez 부 자베',"J'ai une réservation.",'제 윈 레제르바시옹','예약이 있어요.',True]]},
 {'n':'aller <i>·</i> venir <i>·</i> rentrer', 'tip':'방향 삼총사. <span class="fr">aller</span>는 <b>-er로 끝나는데 불규칙</b>이라 조심. 인사말 <span class="fr">Ça va ?</span>도 이 동사입니다 — 직역하면 「(일이) 잘 가나요?」.', 'items':[
  ['aller','알레','가다','불규칙','je vais 즈 베','vous allez 부 잘레','Je vais à Lyon.','즈 베 아 리옹','리옹에 갑니다.',True],
  ['venir','브니르','오다','불규칙','je viens 즈 비앙','vous venez 부 브네','Le bus vient quand ?','르 뷔스 비앙 캉','버스는 언제 오나요?',True],
  ['rentrer','랑트레','돌아가다','-er','je rentre 즈 랑트르','vous rentrez 부 랑트레','Je rentre demain.','즈 랑트르 드맹','내일 돌아갑니다.',False]]},
 {'n':'vouloir <i>·</i> pouvoir <i>·</i> devoir', 'tip':'뒤에 <b>동사 원형</b>을 그대로 붙이는 세 개. <span class="fr">Je voudrais</span>(원해요) · <span class="fr">Je peux</span>(해도 되나요) · <span class="fr">Je dois</span>(해야 해요). <em>이 셋이면 부탁과 질문이 거의 끝납니다.</em>', 'items':[
  ['vouloir','불루아르','원하다','불규칙','je voudrais 즈 부드레','vous voulez 부 불레','Je voudrais un café.','즈 부드레 앙 카페','커피 한 잔 주세요.',True],
  ['pouvoir','푸부아르','할 수 있다','불규칙','je peux 즈 푀','vous pouvez 부 푸베','Je peux entrer ?','즈 푀 앙트레','들어가도 되나요?',True],
  ['devoir','드부아르','해야 한다','불규칙','je dois 즈 두아','vous devez 부 드베','Je dois partir.','즈 두아 파르티르','가봐야 해요.',True]]},
 {'n':'manger <i>·</i> boire <i>·</i> prendre', 'tip':'식당 삼총사. 주문할 때는 대개 <span class="fr">prendre</span>(잡다 → 시키다)를 씁니다 — <span class="fr">Je prends le menu</span>(세트로 할게요). 영어의 「I\'ll have」 자리입니다.', 'items':[
  ['manger','망제','먹다','-er','je mange 즈 망주','vous mangez 부 망제','Je ne mange pas de viande.','즈 느 망주 파 드 비앙드','고기는 안 먹어요.',False],
  ['boire','부아르','마시다','불규칙','je bois 즈 부아','vous buvez 부 뷔베',"Je bois juste de l'eau.",'즈 부아 쥐스트 드 로','물만 마셔요.',True],
  ['prendre','프랑드르','잡다 · 주문하다','불규칙','je prends 즈 프랑','vous prenez 부 프르네','Je prends le menu.','즈 프랑 르 므뉘','세트로 할게요.',True]]},
 {'n':'acheter <i>·</i> payer <i>·</i> coûter', 'tip':'계산대 세트. <span class="fr">coûter</span>는 <b>물건이 주어</b>라 3인칭만 씁니다. 값을 물을 땐 <span class="fr">Ça coûte combien ?</span> 또는 더 흔하게 <span class="fr">Ça fait combien ?</span>', 'items':[
  ['acheter','아슈테','사다','-er',"j'achète 자셰트",'vous achetez 부 자슈테',"Je voudrais acheter ça.",'즈 부드레 아슈테 사','이걸 사고 싶어요.',False],
  ['payer','페이예','지불하다','-er','je paie 즈 페','vous payez 부 페이예','Je peux payer par carte ?','즈 푀 페이예 파르 카르트','카드로 낼 수 있나요?',False],
  ['coûter','쿠테','값이 나가다','-er','ça coûte 사 쿠트','ça fait 사 페','Ça fait combien ?','사 페 콩비앙','전부 얼마예요?',False]]},
 {'n':'parler <i>·</i> comprendre <i>·</i> savoir', 'tip':'말이 안 통할 때의 세 개. <span class="fr">Je ne comprends pas</span>(못 알아듣겠어요)와 <span class="fr">Je ne sais pas</span>(모르겠어요)는 <b>통째로</b> 외우세요.', 'items':[
  ['parler','파를레','말하다','-er','je parle 즈 파를','vous parlez 부 파를레','Vous parlez anglais ?','부 파를레 앙글레','영어 하세요?',False],
  ['comprendre','콩프랑드르','이해하다','불규칙','je comprends 즈 콩프랑','vous comprenez 부 콩프르네','Je ne comprends pas.','즈 느 콩프랑 파','못 알아듣겠어요.',True],
  ['savoir','사부아르','알다','불규칙','je sais 즈 세','vous savez 부 사베','Je ne sais pas.','즈 느 세 파','모르겠어요.',True]]},
 {'n':'chercher <i>·</i> trouver <i>·</i> perdre', 'tip':'잃어버렸을 때의 3연타. <span class="fr">J\'ai perdu</span>(잃어버렸어요) → <span class="fr">Je cherche</span>(찾고 있어요) → <span class="fr">J\'ai trouvé</span>(찾았어요). 이 순서로 말하면 상황 설명이 끝납니다.', 'items':[
  ['chercher','셰르셰','찾다','-er','je cherche 즈 셰르슈','vous cherchez 부 셰르셰','Je cherche cette adresse.','즈 셰르슈 세트 아드레스','이 주소를 찾고 있어요.',False],
  ['trouver','트루베','발견하다','-er','je trouve 즈 트루브','vous trouvez 부 트루베',"Je ne trouve pas mon hôtel.",'즈 느 트루브 파 몽 오텔','호텔을 못 찾겠어요.',False],
  ['perdre','페르드르','잃다 · 놓치다','-re','je perds 즈 페르','vous perdez 부 페르데',"J'ai perdu mon passeport.",'제 페르뒤 몽 파스포르','여권을 잃어버렸어요.',False]]},
 {'n':'attendre <i>·</i> arriver <i>·</i> partir', 'tip':'이동 세트. 역 전광판에 <span class="fr">arrivées</span>(도착)와 <span class="fr">départs</span>(출발)로 그대로 적혀 있습니다. <b>동사를 알면 표지판이 읽힙니다.</b>', 'items':[
  ['attendre','아탕드르','기다리다','-re',"j'attends 자탕",'vous attendez 부 자탕데','Un instant, attendez !','앙 낭스탕, 아탕데','잠깐만 기다려주세요!',False],
  ['arriver','아리베','도착하다','-er',"j'arrive 자리브",'vous arrivez 부 자리베','Ça arrive à quelle heure ?','사 아리브 아 켈 뢰르','몇 시에 도착해요?',False],
  ['partir','파르티르','출발하다','-ir','je pars 즈 파르','vous partez 부 파르테','Le train part à huit heures.','르 트랭 파르 아 위 뢰르','기차는 8시에 떠나요.',False]]},
 {'n':'ouvrir <i>·</i> fermer <i>·</i> faire', 'tip':'가게 앞에서. <span class="fr">ouvert</span>(영업 중) / <span class="fr">fermé</span>(닫힘)는 <b>문에 붙은 팻말</b> 그대로입니다. <span class="fr">faire</span>는 날씨에도 씁니다 — <span class="fr">Il fait chaud</span>(덥다).', 'items':[
  ['ouvrir','우브리르','열다','-ir',"j'ouvre 주브르",'vous ouvrez 부 주브레','Ça ouvre à quelle heure ?','사 우브르 아 켈 뢰르','몇 시에 열어요?',False],
  ['fermer','페르메','닫다','-er','je ferme 즈 페름','vous fermez 부 페르메','Vous fermez quand ?','부 페르메 캉','언제 닫아요?',False],
  ['faire','페르','하다 · 만들다','불규칙','je fais 즈 페','vous faites 부 페트','Vous faites quoi dans la vie ?','부 페트 쿠아 당 라 비','무슨 일 하세요?',True]]},
 {'n':'aimer <i>·</i> voir <i>·</i> dire', 'tip':'<span class="fr">aimer</span>는 <b>사람에게 쓰면 「사랑한다」</b>가 되니 조심. 사물·음식이면 그냥 「좋아한다」입니다. 그래서 사람에겐 보통 <span class="fr">J\'aime bien</span>으로 눌러 말합니다.', 'items':[
  ['aimer','에메','좋아하다','-er',"j'aime 젬",'vous aimez 부 제메',"J'aime beaucoup !",'젬 보쿠','정말 좋아요!',False],
  ['voir','부아르','보다','불규칙','je vois 즈 부아','vous voyez 부 부아예','Je voudrais voir ça.','즈 부드레 부아르 사','이거 보고 싶어요.',True],
  ['dire','디르','말하다','불규칙','je dis 즈 디','vous dites 부 디트','Comment on dit en français ?','코망 옹 디 앙 프랑세','프랑스어로 뭐라고 해요?',True]]},
]

LANG['data']['talkRules'] = [
 ['RULE 1','Bonjour 없이 시작하면 무례합니다','프랑스에서는 <b>가게에 들어서는 순간</b> <span class="fr"><em>Bonjour</em></span>가 먼저입니다. 이걸 빼고 용건부터 꺼내면 <b>대접이 눈에 띄게 달라집니다.</b> 나올 때는 <span class="fr">Au revoir</span> 또는 <span class="fr">Bonne journée</span>.'],
 ['RULE 2','Salut는 아는 사이에만','<span class="fr">Salut</span>는 <b>반말</b>입니다. 친구·또래에게만. 처음 보는 사람, 가게 주인, 나이 든 분에게는 무조건 <span class="fr"><em>Bonjour</em></span>. 저녁이면 <span class="fr">Bonsoir</span>.'],
 ['RULE 3','서툴러도 프랑스어로 시작하세요','영어부터 들이밀면 차갑게 나오는 일이 있지만, <span class="fr">Bonjour, je ne parle pas français...</span>로 <b>먼저 프랑스어로 시도하면</b> 대부분 웃으며 영어로 도와줍니다. <em>순서가 전부입니다.</em>'],
 ['TIP','Je vous en prie가 한 급 위','<span class="fr">De rien</span>(별말씀을)보다 <span class="fr">Je vous en prie</span> 쪽이 <b>정중합니다</b>. 「먼저 가세요」의 뜻으로도 씁니다. 문을 잡아주며 이 말을 건네면 딱입니다.'],
]

LANG['data']['talkGroups'] = [
 {'label':'첫 마디 — 이것부터, 반드시','items':[
  ['Bonjour.','봉주르','안녕하세요.','<b>가게·식당·호텔에 들어서는 순간.</b> 프랑스에서 가장 중요한 한 마디입니다.',True],
  ['Bonsoir.','봉수아르','안녕하세요. (저녁)','대략 <b>저녁 6시 이후</b>. 헷갈리면 Bonjour로도 무난합니다.',False],
  ['Excusez-moi.','엑스퀴제 무아','실례합니다.','모르는 사람에게 말을 걸 때. 존댓말 꼴입니다.',True],
  ['Je ne parle pas français.','즈 느 파를 파 프랑세','프랑스어를 못해요.','먼저 밝히면 <b>상대가 태도를 바꿉니다</b>. 가성비 최고의 문장.',True],
  ['Vous parlez anglais ?','부 파를레 앙글레','영어 하세요?','Bonjour <b>다음에</b> 물으세요. 순서를 지키면 대부분 도와줍니다.',True],
  ['Pouvez-vous parler plus lentement ?','푸베 부 파를레 플뤼 랑트망','좀 더 천천히 말씀해 주실래요?','<span class="fr">Je ne comprends pas</span>보다 이쪽이 <b>대화를 이어줍니다</b>.',True],
  ['Je suis coréen. / coréenne.','즈 쉬 코레앙 · 코레엔','한국 사람이에요.','남자는 <span class="fr">-éen</span>, 여자는 <span class="fr">-éenne</span>.',False]]},
 {'label':'부탁하기 — 이 네 틀이면 끝','items':[
  ['Je voudrais...','즈 부드레','~을 원해요 (정중)','<b>가장 많이 쓰게 될 한 마디.</b> <span class="fr">Je veux</span>는 무례하게 들리니 쓰지 마세요.',True],
  ['Je peux... ?','즈 푀','~해도 되나요?','뒤에 동사 원형만. <span class="fr">Je peux entrer ? / Je peux payer ?</span>',True],
  ["S'il vous plaît.",'실 부 플레','부탁합니다.','문장 끝에 붙이면 뭐든 정중해집니다. <b>거의 반사적으로</b> 붙이세요.',True],
  ["Est-ce qu'il y a... ?",'에스킬 리 아','~이 있나요?','가게에서 물건을 찾을 때. 줄여서 <span class="fr">Il y a... ?</span>로도 통합니다.',False],
  ['Ça fait combien ?','사 페 콩비앙','전부 얼마예요?','값을 묻는 기본. 하나면 <span class="fr">C\'est combien ?</span>',False],
  ['Vous pouvez m\'aider ?','부 푸베 메데','좀 도와주실 수 있어요?','정말 곤란할 때.',False]]},
 {'label':'맞장구 — 대화를 굴리는 말','items':[
  ["D'accord.",'다코르','알겠어요 · 좋아요.','가장 기본적인 동의. 아주 자주 씁니다.',True],
  ['Bien sûr.','비앙 쉬르','물론이죠.','확실하게 긍정할 때.',False],
  ['Vraiment ?','브레망','정말요?','놀랐을 때. 살짝 올려서.',True],
  ["C'est magnifique !",'세 마니피크','정말 멋져요!','풍경·건물·작품에.',False],
  ["C'est délicieux !",'세 델리시외','정말 맛있어요!','<b>먹자마자, 크게.</b> 분위기가 확 달라집니다.',True],
  ["J'aime beaucoup.",'젬 보쿠','아주 마음에 들어요.','사물·음식·장소에. 사람에게는 뜻이 달라지니 주의.',False],
  ['Voilà.','부알라','자, 됐어요 · 바로 그거예요.','건네줄 때, 맞장구칠 때, 마무리할 때 — <b>만능</b>입니다.',True],
  ["Je ne sais pas.",'즈 느 세 파','모르겠어요.','모를 때 솔직하게. 침묵보다 낫습니다.',False]]},
 {'label':'말을 트는 질문','items':[
  ['Comment vous appelez-vous ?','코망 부 자플레 부','성함이 어떻게 되세요?','조금 친해진 다음에.',False],
  ['Vous êtes d\'ici ?','부 제트 디시','여기 분이세요?','현지인인지 묻는 가벼운 질문.',False],
  ['Qu\'est-ce que vous me conseillez ?','케스크 부 므 콩세이예','뭘 추천해 주시겠어요?','<b>식당에서 이 한마디면</b> 주인이 신나서 설명합니다.',True],
  ['Quelle est la spécialité ?','켈 에 라 스페시알리테','여기 대표 메뉴가 뭐예요?','관광객 메뉴 말고 진짜를 알려줍니다.',True],
  ['Vous êtes déjà allé en Corée ?','부 제트 데자 알레 앙 코레','한국에 가보신 적 있어요?','거의 실패하지 않는 질문.',False],
  ['Je peux prendre une photo ?','즈 푀 프랑드르 윈 포토','사진 찍어도 될까요?','가게 안이나 음식을 찍기 전에.',False]]},
 {'label':'마무리 — 자리를 뜰 때','items':[
  ['Merci beaucoup !','메르시 보쿠','정말 고맙습니다!','<span class="fr">merci</span>보다 한 단계 따뜻합니다.',True],
  ['Je vous en prie.','즈 부 장 프리','천만에요 · 그러세요.','<span class="fr">De rien</span>보다 정중합니다.',True],
  ["C'était très agréable.",'세테 트레 자그레아블','정말 즐거웠어요.','사람과 헤어질 때.',False],
  ['Au revoir.','오 르부아르','안녕히 계세요.','가게를 나서며. <b>이것도 빠뜨리면 안 됩니다.</b>',True],
  ['Bonne journée !','본 주르네','좋은 하루 되세요!','낮에. 저녁이면 <span class="fr">Bonne soirée !</span>',True],
  ['À bientôt !','아 비앙토','또 봐요!','다시 올 것 같을 때.',False]]},
]

LANG['data']['conjRules'] = [
 ['RULE 1','문장을 짧게 끊고 앞에 얹으세요','긴 문장을 만들려 하지 말고 <b>짧게 끊은 뒤 앞에 한 단어</b>를 붙이세요. <span class="fr">C\'est cher. Mais je le prends.</span>(비싸요. 그래도 살게요.) 이게 실제로 말이 되는 방식입니다.'],
 ['RULE 2','회화체와 문어체','<b>말할 때</b>는 <span class="fr">mais · alors · donc · du coup</span>, <b>글에서</b>는 <span class="fr">cependant · néanmoins · par conséquent</span>. 여행 중에 cependant를 쓰면 <em>논설문처럼</em> 들립니다.'],
 ['TRAP','「그런데」가 두 갈래','앞말을 뒤집는 역접이면 <span class="fr"><em>mais</em></span>, 화제를 바꾸는 「그건 그렇고」면 <span class="fr"><em>au fait</em></span>. 한국어 「그런데」 하나가 프랑스어에서는 둘로 갈립니다.'],
 ['TIP','du coup은 요즘 말','<span class="fr">du coup</span> 뒤 쿠 = 「그래서」. 젊은 사람들이 <b>하루에 수십 번</b> 씁니다. 이걸 쓰면 교과서 프랑스어가 아니라 <em>실제로 들리는 프랑스어</em>가 됩니다.'],
]

LANG['data']['conjGroups'] = [
 {'label':'그리고 — 덧붙이기','items':[
  ['et','에','그리고','가장 기본. <b>et 뒤에는 절대 연음하지 않습니다.</b>','Un café et un croissant.','앙 카페 에 앙 크루아상','커피 하나랑 크루아상 하나요.',False],
  ['puis','퓌','그러고 나서','<b>순서</b>가 있을 때. 「그 다음에」.','Tout droit, puis à gauche.','투 드루아, 퓌 아 고슈','직진하고, 그 다음에 왼쪽이요.',True],
  ['aussi','오시','또한 · ~도','「나도」는 <span class="fr">moi aussi</span> 무아 오시.','Pour moi aussi, merci.','푸르 무아 오시, 메르시','저도 같은 걸로요.',True],
  ['en plus','앙 플뤼','게다가','이유를 보태 강조할 때.',"C'est bon, et en plus pas cher.",'세 봉, 에 앙 플뤼 파 셰르','맛있고, 게다가 싸요.',False]]},
 {'label':'그런데 · 하지만 — 뒤집기','items':[
  ['mais','메','하지만','<b>1순위.</b> 회화의 역접은 mais 하나로 거의 다 됩니다.',"C'est cher, mais je le prends.",'세 셰르, 메 즈 르 프랑','비싸요, 그래도 살게요.',True],
  ['par contre','파르 콩트르','반면에','두 가지를 대비할 때. 회화에서 아주 흔합니다.','Par contre, ça je n\'aime pas.','파르 콩트르, 사 즈 넴 파','반면에 그건 별로예요.',True],
  ['quand même','캉 멤','그래도 · 어쨌든','아쉬움이나 놀람이 섞인 <b>「그래도」</b>. 프랑스어다운 말투.',"C'est cher quand même.",'세 셰르 캉 멤','그래도 좀 비싸네요.',True],
  ['au fait','오 페','그런데 (화제 전환)','앞말을 뒤집는 게 아니라 <b>화제를 바꿀 때만</b>.','Au fait, vous fermez quand ?','오 페, 부 페르메 캉','그런데, 언제 닫으세요?',True]]},
 {'label':'그래서 · 그러니까','items':[
  ['alors','알로르','그럼 · 그러니까','<b>결정을 내리는 순간</b>, 그리고 <b>말이 막혔을 때</b> 둘 다.','Alors, je prends ça.','알로르, 즈 프랑 사','그럼 이걸로 할게요.',True],
  ['donc','동크','그래서','앞의 일 때문에 벌어진 결과. 조금 논리적인 어감.',"Il est tard, donc j'y vais.",'일 레 타르, 동크 지 베','늦었으니 갈게요.',False],
  ['du coup','뒤 쿠','그래서 (구어)','<b>요즘 프랑스 사람이 가장 많이 쓰는 접속어.</b> 교과서에는 잘 안 나옵니다.','Du coup, on fait quoi ?','뒤 쿠, 옹 페 쿠아','그래서 뭐 할까요?',True],
  ['parce que','파르스 크','왜냐하면','이유를 답니다. 「왜?」라는 질문은 <span class="fr">Pourquoi ?</span>.',"Parce que c'est fermé.",'파르스 크 세 페르메','닫혀 있어서요.',False]]},
 {'label':'정리 · 되짚기','items':[
  ['par exemple','파르 에그장플','예를 들면','추천을 받았는데 감이 안 올 때. <span class="fr">Par exemple ?</span> 한 마디면 구체적으로 말해줍니다.','Par exemple ?','파르 에그장플','예를 들면요?',True],
  ["c'est-à-dire",'세타디르','그러니까 즉','상대 말을 <b>내가 이해한 대로 되짚을 때</b>.',"C'est-à-dire, c'est fermé aujourd'hui ?",'세타디르, 세 페르메 오주르뒤','그러니까, 오늘 닫는다고요?',False],
  ['enfin','앙팽','결국 · 아무튼','정리할 때도, <b>말을 고쳐 말할 때</b>도 씁니다.','Enfin, ça va.','앙팽, 사 바','뭐 아무튼 괜찮아요.',False],
  ['peut-être','푀 테트르','어쩌면','확신이 없을 때. 부드럽게 거절할 때도.','Peut-être demain.','푀 테트르 드맹','어쩌면 내일요.',True]]},
 {'label':'말이 막혔을 때','items':[
  ['Euh...','외','음…','다음 말을 고르는 사이. <b>프랑스어의 「음…」</b>입니다.','Euh... c\'est combien ?','외... 세 콩비앙','음… 얼마예요?',True],
  ['Alors...','알로르','그러니까…','생각을 정리하며. 문장 첫머리에서 시간을 법니다.','Alors, je voudrais...','알로르, 즈 부드레','그러니까, 저는…',True],
  ['Pardon ?','파르동','네? · 다시 말씀해 주세요','못 알아들었을 때. <b>이 한 마디를 아끼지 마세요.</b>','Pardon ? Plus lentement.','파르동? 플뤼 랑트망','네? 좀 더 천천히요.',True],
  ['Voilà','부알라','자, 그거예요','건네줄 때, 맞장구칠 때, 문장을 닫을 때 — <b>만능</b>.','Voilà, c\'est ça.','부알라, 세 사','네, 바로 그거예요.',True]]},
]
