from __future__ import annotations

EXTRA_LETTER_INDEX_PACKS: list[dict] = [
    {
        "id": f"base_{index:03d}",
        "file": f"base/pack_{index:03d}.json",
        "count": 32 if index < 16 else 28,
        "constellations": [
            "AND", "AQL", "AQR", "ARI", "AUR", "BOO", "CAS", "CEN", "CEP", "CMA", "CYG", "DRA", "GEM",
            "HER", "LEO", "LYR", "ORI", "PEG", "PER", "SCO", "SGR", "TAU", "UMA", "UMI", "VIR",
        ],
        "languages": ["ja", "en"],
    }
    for index in range(8, 17)
]

_CONSTELLATIONS: tuple[tuple[str, tuple[int, ...], str, str], ...] = (
    ("AND", (677,), "アンドロメダ座", "Andromeda"), ("AQL", (97649,), "わし座", "Aquila"),
    ("AQR", (109074,), "みずがめ座", "Aquarius"), ("ARI", (13209,), "おひつじ座", "Aries"),
    ("AUR", (24608,), "ぎょしゃ座", "Auriga"), ("BOO", (69673,), "うしかい座", "Bootes"),
    ("CAS", (3179, 4427), "カシオペヤ座", "Cassiopeia"), ("CEN", (71683,), "ケンタウルス座", "Centaurus"),
    ("CEP", (106032,), "ケフェウス座", "Cepheus"), ("CMA", (32349,), "おおいぬ座", "Canis Major"),
    ("CYG", (102098,), "はくちょう座", "Cygnus"), ("DRA", (87833,), "りゅう座", "Draco"),
    ("GEM", (37826, 36850), "ふたご座", "Gemini"), ("HER", (80816,), "ヘルクレス座", "Hercules"),
    ("LEO", (49669,), "しし座", "Leo"), ("LYR", (91262,), "こと座", "Lyra"),
    ("ORI", (27989, 24436), "オリオン座", "Orion"), ("PEG", (113963,), "ペガスス座", "Pegasus"),
    ("PER", (15863,), "ペルセウス座", "Perseus"), ("SCO", (80763,), "さそり座", "Scorpius"),
    ("SGR", (90185, 92855), "いて座", "Sagittarius"), ("TAU", (21421,), "おうし座", "Taurus"),
    ("UMA", (54061,), "おおぐま座", "Ursa Major"), ("UMI", (11767,), "北極星", "Polaris"),
    ("VIR", (65474,), "おとめ座", "Virgo"),
)

_PLACES: tuple[tuple[str, str, str], ...] = (
    ("JP", "Ibaraki", "Mito"), ("JP", "Nara", "Ikoma"), ("JP", "Ehime", "Matsuyama"), ("JP", "Iwate", "Morioka"),
    ("JP", "Tokyo", "Kokubunji"), ("JP", "Aichi", "Okazaki"), ("JP", "Kumamoto", "Amakusa"), ("JP", "Tottori", "Yonago"),
    ("JP", "Fukui", "Sabae"), ("JP", "Kochi", "Shimanto"), ("JP", "Yamanashi", "Kofu"), ("JP", "Akita", "Yokote"),
    ("US", "Oregon", "Eugene"), ("US", "Vermont", "Burlington"), ("US", "Arizona", "Tucson"), ("US", "Michigan", "Ann Arbor"),
    ("CA", "Nova Scotia", "Halifax"), ("CA", "Quebec", "Sherbrooke"), ("GB", "Scotland", "Dundee"), ("IE", "Galway", "Galway"),
    ("AU", "Tasmania", "Hobart"), ("NZ", "Otago", "Dunedin"), ("FR", "Occitanie", "Nimes"), ("DE", "Saxony", "Dresden"),
    ("IT", "Liguria", "Genoa"), ("ES", "Andalusia", "Granada"), ("PT", "Porto", "Porto"), ("NL", "Groningen", "Groningen"),
    ("SE", "Vasterbotten", "Umea"), ("NO", "Vestland", "Bergen"), ("FI", "Pirkanmaa", "Tampere"), ("DK", "Jutland", "Aarhus"),
    ("PL", "Lesser Poland", "Krakow"), ("CZ", "Bohemia", "Ceske Budejovice"), ("AT", "Tyrol", "Innsbruck"), ("GR", "Crete", "Heraklion"),
    ("TR", "Izmir", "Izmir"), ("KR", "Busan", "Busan"), ("TW", "Hualien", "Hualien"), ("SG", "Central", "Singapore"),
    ("TH", "Chiang Mai", "Chiang Mai"), ("VN", "Da Nang", "Da Nang"), ("ID", "Bali", "Denpasar"), ("IN", "Kerala", "Kochi"),
    ("PH", "Iloilo", "Iloilo City"), ("BR", "Bahia", "Salvador"), ("AR", "Santa Fe", "Rosario"), ("CL", "Valparaiso", "Valparaiso"),
    ("PE", "Arequipa", "Arequipa"), ("MX", "Oaxaca", "Oaxaca"), ("CO", "Antioquia", "Medellin"), ("ZA", "Western Cape", "Stellenbosch"),
    ("EG", "Alexandria", "Alexandria"), ("MA", "Fes-Meknes", "Fes"), ("KE", "Nairobi", "Nairobi"), ("UY", "Montevideo", "Montevideo"),
    ("IS", "Capital Region", "Reykjavik"), ("CH", "Bern", "Bern"), ("BE", "Flanders", "Ghent"), ("MY", "Penang", "George Town"),
)

_OBJECTS: tuple[tuple[str, str], ...] = (
    ("a blue umbrella", "青い傘"), ("a paper cup", "紙コップ"), ("a warm rice ball", "あたたかいおにぎり"),
    ("a wrinkled receipt", "しわのあるレシート"), ("one mismatched sock", "片方だけ違うくつした"), ("a borrowed pen", "借りたペン"),
    ("a cold tea bottle", "冷たいお茶"), ("the last bread roll", "最後のパン"), ("a bent train ticket", "曲がった切符"),
    ("a small packet of seeds", "小さな種の袋"), ("a chipped mug", "欠けたマグ"), ("a folded map", "折った地図"),
    ("a loose button", "取れかけのボタン"), ("a pharmacy bag", "薬局の袋"), ("a red scarf", "赤いマフラー"),
    ("a notebook with no title", "題名のないノート"), ("a damp towel", "少しぬれたタオル"), ("a pear from work", "職場でもらった梨"),
    ("a half-empty snack bag", "半分だけ残ったお菓子"), ("a quiet radio", "小さく鳴るラジオ"), ("a cracked phone case", "ひびの入ったスマホケース"),
    ("a library card", "図書館カード"), ("a loose shoelace", "ほどけたくつひも"), ("a tiny flower pot", "小さな植木鉢"),
    ("a ferry ticket", "フェリーの切符"), ("a supermarket basket", "スーパーのかご"), ("a room key", "部屋の鍵"),
    ("a pencil stub", "短いえんぴつ"), ("a lunch box lid", "弁当箱のふた"), ("a packet of screws", "ネジの袋"),
    ("a towel from the hostel", "宿のタオル"), ("an old postcard", "古いはがき"), ("a cheap pair of gloves", "安い手袋"),
    ("a plastic spoon", "プラスチックのスプーン"), ("a loose bookmark", "はさみっぱなしのしおり"), ("a guitar pick", "ギターのピック"),
    ("a rain-dark jacket", "雨で黒くなった上着"), ("a bag of plums", "すももの袋"), ("a small flashlight", "小さなライト"),
    ("a subway transfer slip", "地下鉄の乗り換え券"), ("a cup of soup", "スープのカップ"), ("a white envelope", "白い封筒"),
    ("a loose coin", "小銭"), ("a half-read comic", "読みかけの漫画"), ("a takeout box", "持ち帰りの箱"),
    ("a scratched water bottle", "傷のある水筒"), ("a ticket stub", "半券"), ("a paper lantern", "紙のランタン"),
    ("a jar of basil", "バジルのびん"), ("a phone charger", "充電コード"), ("a melon bread wrapper", "メロンパンの袋"),
    ("a grocery coupon", "割引券"), ("a tiny screwdriver", "小さなドライバー"), ("a postcard stamp", "はがきの切手"),
    ("a ferry rope", "フェリーのロープ"), ("a bowl from the sink", "流しの茶わん"), ("a red pencil mark", "赤い鉛筆の印"),
    ("a small stone", "小さな石"), ("a key ring", "鍵の輪"), ("a packet of instant noodles", "カップめん"),
    ("a clean fork", "きれいなフォーク"), ("a window latch", "まどの留め金"), ("a delivery sticker", "配達のシール"),
    ("a folded sweater", "たたんだセーター"), ("a torn grocery list", "破れた買い物メモ"), ("a bus pass", "バスの定期"),
    ("a theater flyer", "映画館のちらし"), ("a chess bishop", "チェスのビショップ"), ("a warm paper bag", "あたたかい紙袋"),
    ("a museum postcard", "美術館のはがき"), ("a red sock", "赤いくつした"), ("a clinic number slip", "病院の番号札"),
    ("a small bottle of ink", "小さなインクびん"), ("a travel-size toothbrush", "旅行用の歯ブラシ"), ("a cracked ruler", "ひびの入った定規"),
    ("a bowl of cereal", "シリアルの茶わん"), ("a train-window reflection", "電車のまどに映る顔"), ("a half-melted ice cream", "少し溶けたアイス"),
    ("a packet of cough drops", "のどあめの袋"), ("a cold bicycle lock", "冷たい自転車の鍵"), ("a handwritten label", "手書きのラベル"),
)

_ACTIONS: tuple[tuple[str, str], ...] = (
    ("waited beside", "の横で待っていた"), ("rolled under", "の下へ転がった"), ("sat quietly on", "の上で静かにしていた"),
    ("kept knocking against", "に何度も当たっていた"), ("made a small corner in", "の中で小さな角になっていた"),
    ("looked more serious than", "よりまじめそうに見えた"), ("fell out near", "の近くで落ちた"), ("warmed my hand near", "の近くで手をあたためた"),
    ("stayed forgotten by", "のそばで忘れられていた"), ("squeezed into", "の中へ押し込まれていた"),
    ("became the main event at", "で主役みたいになった"), ("survived the walk past", "を通る道をなんとか生きのびた"),
    ("made me stop before", "の前で私を止めた"), ("waited in the shadow of", "の影で待っていた"),
    ("clicked once beside", "の横で一度だけ鳴った"), ("smelled faintly of", "の匂いを少し持っていた"),
    ("took up too much room on", "の上で場所を取りすぎていた"), ("looked newly important under", "の下で急に大事そうに見えた"),
    ("made the bench near", "の近くのベンチを少し変えた"), ("reminded me of", "を思い出させた"),
    ("kept its balance on", "の上でなんとか立っていた"), ("turned ordinary beside", "の横でふつうに戻った"),
    ("made a quiet sound against", "に当たって小さな音を出した"), ("waited for permission near", "の近くで許可を待っているみたいだった"),
)

_BACKDROPS: tuple[tuple[str, str], ...] = (
    ("the station wall", "駅の壁"), ("the laundromat door", "コインランドリーのドア"), ("the closed bakery", "閉まったパン屋"),
    ("the harbor fence", "港のフェンス"), ("the office sink", "会社の流し"), ("the apartment stairs", "アパートの階段"),
    ("the bus shelter", "バス停の屋根"), ("the campus gate", "学校の門"), ("the clinic window", "病院のまど"),
    ("the supermarket light", "スーパーの明かり"), ("the old bridge", "古い橋"), ("the hostel desk", "宿の机"),
    ("the kitchen table", "台所の机"), ("the tram stop", "電車の停留所"), ("the river railing", "川の手すり"),
    ("the vending machine", "自販機"), ("the elevator mirror", "エレベーターの鏡"), ("the lecture hall", "講義室"),
    ("the noodle shop curtain", "ラーメン屋ののれん"), ("the rooftop door", "屋上のドア"), ("the bicycle racks", "自転車置き場"),
    ("the library steps", "図書館の階段"), ("the night market", "夜の市場"), ("the ferry deck", "フェリーの甲板"),
    ("the quiet courtyard", "静かな中庭"), ("the ticket gate", "改札"), ("the balcony rail", "ベランダの手すり"),
    ("the tiny shrine", "小さな神社"), ("the cinema lobby", "映画館のロビー"), ("the flower shop shutter", "花屋のシャッター"),
    ("the dorm kitchen", "寮の台所"), ("the parking lot", "駐車場"), ("the old stone steps", "古い石段"),
)

_DETAILS: tuple[tuple[str, str], ...] = (
    ("Nobody noticed it, which made the scene easier to keep.", "だれも気づかないので、覚えておきやすかった。"),
    ("I laughed once and pretended it was a cough.", "一度笑って、それを咳のふりにした。"),
    ("The night had no opinion, and that helped.", "夜には意見がなくて、それが少し助かった。"),
    ("I counted to seven for no practical reason.", "理由もなく七まで数えた。"),
    ("The phone stayed quiet like it had been warned.", "スマホは注意されたみたいに静かだった。"),
    ("A little wind moved through at exactly the right time.", "ちょうどいい時に、小さな風が通った。"),
    ("I almost sent a message and then spared everyone.", "連絡しそうになって、みんなを助けた。"),
    ("The floor was cold enough to make my socks honest.", "床が冷たくて、くつしたの薄さが分かった。"),
    ("For a second the whole errand felt planned.", "一瞬だけ、用事が全部予定通りに見えた。"),
    ("The smell of soap arrived before the person did.", "人より先に、せっけんの匂いが来た。"),
    ("I did not solve anything, but I changed location.", "何も解決していないけど、場所だけは変えた。"),
    ("The quiet after the scooter passed felt almost clean.", "スクーターが過ぎた後の静けさは、少しきれいだった。"),
    ("My pocket held one more useless proof of the day.", "ポケットには、今日の役に立たない証拠が一つ増えた。"),
    ("The smallest success was still a success.", "いちばん小さい成功も、成功ではあった。"),
    ("I decided not to improve the moment by explaining it.", "説明してよくするのは、やめておいた。"),
    ("Somebody upstairs dropped something and ended the silence.", "上の階で何かが落ちて、静けさが終わった。"),
    ("It was only funny after I stopped being annoyed.", "腹が立つのをやめたら、少しだけ面白かった。"),
    ("I remembered the wrong song and hummed it anyway.", "違う曲を思い出して、そのまま鼻歌にした。"),
    ("The receipt proved less than I wanted it to prove.", "レシートは、思ったほど何も証明してくれなかった。"),
    ("A dog barked once, then left the matter there.", "犬が一度だけ鳴いて、その件は終わった。"),
    ("The tea had cooled into something more responsible.", "お茶は冷めて、少しまじめな飲みものになっていた。"),
    ("I took the long way because the short way knew too much.", "近道はいろいろ知りすぎているので、遠回りした。"),
    ("My hands were busy, so my thoughts slowed down.", "手がふさがると、考えごとも少し遅くなった。"),
    ("The answer I wanted did not arrive, but the bus did.", "ほしい答えは来なかったけど、バスは来た。"),
    ("The whole thing was tiny and somehow complete.", "全部小さいのに、なぜか足りていた。"),
    ("I would not call it a miracle, but I did look twice.", "奇跡とは言わないけど、二度見はした。"),
    ("The old clock nearby sounded too confident.", "近くの古い時計が、妙に自信のある音を立てた。"),
    ("A stranger smiled at the wrong timing and saved the mood.", "知らない人が変なタイミングで笑って、空気が助かった。"),
    ("The page in my bag bent around the corner of a book.", "かばんの紙が、本の角にそって曲がった。"),
    ("I stepped around a puddle and felt briefly skilled.", "水たまりをよけて、一瞬だけ上手に生きた気がした。"),
    ("The light changed before my excuse was ready.", "言い訳ができる前に、信号が変わった。"),
    ("Nothing spooky happened, except the door opening by itself.", "ドアが勝手に開いた以外、こわいことは何もない。"),
    ("I thought, this is a little ridiculous, and kept smiling.", "これは少しだけ草だと思って、そのまま笑っていた。"),
    ("The radio caught a town I have never visited.", "ラジオが、行ったことのない町を拾った。"),
    ("One meteor appeared while everyone checked a different patch of sky.", "みんなが違う空を見ている時に、ひとつ流れた。"),
    ("The promised meteor shower mostly taught me patience.", "流星群は、ほとんど待つ練習だった。"),
    ("I lost count of airplanes before seeing the meteor.", "流れ星を見る前に、飛行機の数を忘れた。"),
    ("The silence after the streak felt wider than the streak itself.", "光った線より、その後の静けさのほうが広かった。"),
    ("Someone's laughter crossed the street before the people did.", "人より先に、笑い声が道を渡った。"),
    ("I saved the last bite for no one in particular.", "最後のひと口を、だれでもない人のために残した。"),
)

_SKY_LINES: tuple[tuple[str, str], ...] = (
    ("{en_const} fitted between two roofs above {backdrop_en}.", "{backdrop_ja}の上で、{ja_const}が屋根の間に入っていた。"),
    ("I found {en_const} after the light on {backdrop_en} blinked once.", "{backdrop_ja}の明かりが一度またたいてから、{ja_const}を見つけた。"),
    ("Over {backdrop_en}, {en_const} looked less far than usual.", "{backdrop_ja}の上では、{ja_const}がいつもより近く見えた。"),
    ("{en_const} waited past the edge of {backdrop_en}.", "{backdrop_ja}の端の向こうで、{ja_const}が待っていた。"),
    ("A thin gap above {backdrop_en} was just enough for {en_const}.", "{backdrop_ja}の上の細いすきまに、{ja_const}がちょうど入った。"),
    ("When I looked up from {backdrop_en}, {en_const} was already there.", "{backdrop_ja}から顔を上げると、{ja_const}はもうそこにいた。"),
    ("{en_const} made the dark around {backdrop_en} feel arranged.", "{ja_const}のせいで、{backdrop_ja}のまわりの暗さが少し並んで見えた。"),
    ("Past {backdrop_en}, {en_const} held its shape without hurry.", "{backdrop_ja}の向こうで、{ja_const}は急がず形を保っていた。"),
    ("{en_const} was clearer than the sign beside {backdrop_en}.", "{backdrop_ja}のそばの看板より、{ja_const}のほうがはっきりしていた。"),
    ("I used {en_const} above {backdrop_en} as a reason to pause.", "{backdrop_ja}の上の{ja_const}を、立ち止まる理由にした。"),
    ("Near {backdrop_en}, {en_const} looked like part of the errand.", "{backdrop_ja}の近くでは、{ja_const}まで用事の一部みたいだった。"),
    ("{en_const} returned when the clouds left {backdrop_en} alone.", "雲が{backdrop_ja}を離れると、{ja_const}が戻ってきた。"),
    ("The space above {backdrop_en} opened, and {en_const} took it quietly.", "{backdrop_ja}の上が開いて、{ja_const}が静かにそこへ入った。"),
    ("{en_const} stayed visible past the wires near {backdrop_en}.", "{backdrop_ja}の近くの電線の向こうに、{ja_const}はまだ見えていた。"),
    ("I checked the time, then looked back at {en_const} over {backdrop_en}.", "時間を見てから、{backdrop_ja}の上の{ja_const}をもう一度見た。"),
    ("{en_const} gave the corner by {backdrop_en} a little depth.", "{ja_const}のおかげで、{backdrop_ja}の角に少し奥行きが出た。"),
)

_FINALS: tuple[tuple[str, str], ...] = (
    ("I went in before making it too meaningful.", "意味を持たせすぎる前に、中へ入った。"),
    ("The door closed softly enough to count as an answer.", "ドアは答えみたいに静かに閉まった。"),
    ("My phone stayed in my pocket, which improved the ending.", "スマホを出さなかったので、終わり方は少しましだった。"),
    ("Tomorrow could wait outside for one more minute.", "明日は、もう一分だけ外で待てそうだった。"),
    ("The room looked slightly rearranged when I returned.", "戻った部屋は、少しだけ並び方が変わって見えた。"),
    ("I kept the quiet without giving it a name.", "名前をつけないまま、その静けさを持って帰った。"),
    ("For no good reason, I felt less unfinished.", "理由はないのに、少しだけ途中ではなくなった。"),
    ("The next ordinary thing waited indoors.", "次のふつうのことは、部屋の中で待っていた。"),
    ("I remembered my keys and forgot the time.", "鍵は思い出して、時間は忘れた。"),
    ("The night did not become better; it became more specific.", "夜がよくなったというより、少し具体的になった。"),
    ("I saved the receipt, though it proved almost nothing.", "ほとんど何の証拠にもならないけど、レシートは残した。"),
    ("The hallway smelled of dust and somebody's dinner.", "廊下は、ほこりとだれかの夕飯の匂いがした。"),
)

_SPECIALS: tuple[tuple[str, str, str, str], ...] = (
    ("PER", "I came out for the Perseids and first found my missing earbud. One meteor arrived after that. I accepted both discoveries.", "ペルセウス座流星群を見に出て、最初に落としたイヤホンを見つけた。そのあと流れ星がひとつ来た。どちらの発見も受け取った。", "PER"),
    ("GEM", "The Geminids were quiet for twenty minutes, then one line cut over the roof. Everyone said something different at once. That felt correct.", "ふたご座流星群は二十分しずかで、そのあと屋根の上を一本切った。みんなが一度に違うことを言った。それで合っている気がした。", "GEM"),
    ("LYR", "I was not expecting the Lyrids to be patient with me. The tea went cold before anything moved. Then the sky answered too briefly to quote.", "こと座流星群に、こちらを待ってくれる感じはなかった。お茶が冷めてから、やっとひとつ動いた。引用できないくらい短い返事だった。", "LYR"),
    ("ORI", "The Orionids made me stand outside longer than my jacket wanted. I saw one streak and two satellites. My jacket filed a complaint.", "オリオン座流星群のせいで、上着が望むより長く外にいた。流れ星をひとつ、人工衛星をふたつ見た。上着は不満そうだった。", "ORI"),
    ("DRA", "The old clock in the hall loses two minutes only after midnight. I have no theory, which is rare for me. Draco was outside the window like a witness.", "廊下の古い時計は、真夜中のあとだけ二分遅れる。めずらしく、私には仮説がない。まどの外のりゅう座は、証人みたいだった。", ""),
    ("CEP", "A small bell rang once where there was no door. Maybe it was someone's key downstairs. Cepheus kept quiet, which did not help the case.", "ドアのない場所で、小さな鈴が一度鳴った。たぶん下の階の鍵だと思う。ケフェウス座は黙っていて、事件の役には立たなかった。", ""),
    ("ORI", "I lost the game so badly that even the loading screen felt concerned. Orion was above the gate when I cooled down. It was a little ridiculous, lol.", "ゲームに負けすぎて、ロード画面まで心配している気がした。落ち着いたころ、門の上にオリオン座があった。ちょっと草だった。", ""),
    ("UMA", "My friend sent a photo of soup with the caption, dinner has entered politics. I laughed on the station stairs. Ursa Major was tipped over the roof.", "友達が、夕飯が政治になった、という一文つきでスープの写真を送ってきた。駅の階段で笑った。屋根の上で、おおぐま座が傾いていた。", ""),
)


def _season_for_constellation(constellation_id: str) -> list[str]:
    if constellation_id in {"ORI", "CMA", "GEM", "TAU", "AUR"}:
        return ["winter"]
    if constellation_id in {"LEO", "VIR", "BOO", "UMA"}:
        return ["spring"]
    if constellation_id in {"CYG", "LYR", "AQL", "SCO", "SGR", "HER"}:
        return ["summer"]
    if constellation_id in {"AND", "PEG", "CAS", "AQR", "ARI", "PER", "CEP"}:
        return ["autumn"]
    return ["spring", "summer", "autumn", "winter"]


def _sentence_count(index: int) -> int:
    if index % 29 == 0:
        return 2
    if index % 23 == 0:
        return 5
    if index % 6 in (0, 4):
        return 4
    return 3


def _build_generated_pair(index: int) -> tuple[str, str, str, tuple[str, ...], tuple[int, ...], list[str], list[str], float]:
    constellation_id, star_ids, ja_const, en_const = _CONSTELLATIONS[(index * 7 + index // 9) % len(_CONSTELLATIONS)]
    obj_en, obj_ja = _OBJECTS[(index * 17 + 3) % len(_OBJECTS)]
    action_en, action_ja = _ACTIONS[(index * 5 + index // 11) % len(_ACTIONS)]
    backdrop_en, backdrop_ja = _BACKDROPS[(index * 13 + 5) % len(_BACKDROPS)]
    detail_en, detail_ja = _DETAILS[(index * 19 + index // 7) % len(_DETAILS)]
    detail_en = detail_en[:-1] + f" near {backdrop_en}, with {obj_en}."
    detail_ja = detail_ja[:-1] + f"、{backdrop_ja}で、{obj_ja}といっしょに。"
    sky_en, sky_ja = _SKY_LINES[(index * 11 + index // 3) % len(_SKY_LINES)]
    final_en, final_ja = _FINALS[(index * 7 + index // 5) % len(_FINALS)]
    first_en = f"{obj_en.capitalize()} {action_en} {backdrop_en}."
    first_ja = f"{obj_ja}が{backdrop_ja}{action_ja}。"
    sky_en = sky_en.format(en_const=en_const, backdrop_en=backdrop_en)
    sky_ja = sky_ja.format(ja_const=ja_const, backdrop_ja=backdrop_ja)
    if index % 3 == 0:
        sky_en = sky_en[:-1] + f", near {obj_en}."
        sky_ja = sky_ja[:-1] + f"、近くには{obj_ja}。"
    elif index % 3 == 1:
        sky_en = sky_en[:-1] + f", just past {obj_en}."
        sky_ja = sky_ja[:-1] + f"、その先には{obj_ja}。"
    else:
        sky_en = sky_en[:-1] + f", while I held {obj_en}."
        sky_ja = sky_ja[:-1] + f"、手には{obj_ja}。"
    sentence_count = _sentence_count(index)
    en_parts = [first_en, detail_en, sky_en]
    ja_parts = [first_ja, detail_ja, sky_ja]
    if sentence_count >= 4:
        if index % 4 == 0:
            final_en = final_en[:-1] + f", beside {backdrop_en}."
            final_ja = final_ja[:-1] + f"、そばには{backdrop_ja}。"
        elif index % 4 == 1:
            final_en = final_en[:-1] + f", with {obj_en}."
            final_ja = final_ja[:-1] + f"、そこには{obj_ja}。"
        elif index % 4 == 2:
            final_en = final_en[:-1] + f", after noticing {obj_en}."
            final_ja = final_ja[:-1] + f"、目に入ったのは{obj_ja}。"
        else:
            final_en = final_en[:-1] + f", because of {obj_en}."
            final_ja = final_ja[:-1] + f"、理由は{obj_ja}。"
        en_parts.append(final_en)
        ja_parts.append(final_ja)
    if sentence_count >= 5:
        more_en, more_ja = _DETAILS[(index * 23 + 9) % len(_DETAILS)]
        more_en = more_en[:-1] + f" after {backdrop_en}."
        more_ja = more_ja[:-1] + f"、{backdrop_ja}のあとで。"
        en_parts.append(more_en)
        ja_parts.append(more_ja)
    event_tags: tuple[str, ...] = ()
    weight = 1.0
    if constellation_id in {"PER", "GEM", "ORI", "LYR"} and index % 34 == 0:
        event_tags = (constellation_id,)
        weight = 1.18
    return " ".join(en_parts[:sentence_count]), "".join(ja_parts[:sentence_count]), constellation_id, star_ids, _season_for_constellation(constellation_id), list(event_tags), weight


def _build_packs() -> dict[str, tuple[dict, ...]]:
    packs: dict[str, list[dict]] = {f"base_{index:03d}": [] for index in range(8, 17)}
    special_index = 0
    for index in range(284):
        pack_number = min(16, 8 + index // 32)
        pack_id = f"base_{pack_number:03d}"
        item_number = len(packs[pack_id]) + 1
        country_code, region, city = _PLACES[(index * 11 + index // 5) % len(_PLACES)]
        if index % 41 == 0 and special_index < len(_SPECIALS):
            constellation_id, en_text, ja_text, event_tag = _SPECIALS[special_index]
            special_index += 1
            star_ids = next(stars for cid, stars, _ja, _en in _CONSTELLATIONS if cid == constellation_id)
            seasons = _season_for_constellation(constellation_id)
            event_tags = [event_tag] if event_tag else []
            weight = 1.15 if event_tags else 1.0
        else:
            en_text, ja_text, constellation_id, star_ids, seasons, event_tags, weight = _build_generated_pair(index)
        original_language = "ja" if (country_code == "JP" or index % 5 == 0) else "en"
        original_text = ja_text if original_language == "ja" else en_text
        translation_language = "en" if original_language == "ja" else "ja"
        translation_text = en_text if original_language == "ja" else ja_text
        packs[pack_id].append({
            "id": f"{pack_id}_{item_number:03d}",
            "country_code": country_code,
            "region": region,
            "city": city,
            "original_language": original_language,
            "original_text": original_text,
            "translations": {translation_language: translation_text},
            "constellation_ids": [constellation_id],
            "anchor_star_ids": list(star_ids),
            "season_tags": seasons,
            "time_tags": ["night" if index % 4 else "late"],
            "event_tags": event_tags,
            "weight": weight,
        })
    return {pack_id: tuple(items) for pack_id, items in packs.items()}


EXTRA_PRESET_LETTER_PACKS = _build_packs()
