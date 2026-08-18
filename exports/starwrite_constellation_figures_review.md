# Starwrite Constellation Figure Review

This file lists the constellation stick figures currently implemented in Starwrite.
Use it to compare each figure against common modern star-chart patterns.

## Review Checklist

- Mark each constellation as `acceptable`, `questionable`, or `likely_wrong`.
- Check whether the main outline matches common references closely enough for Starwrite.
- Check whether branches or repeated path points create odd shapes.
- If a correction is needed, propose replacement polylines or edges using HIP ids.
- Do not mix feature/asterism lines into constellation body lines.

## Data Notes

- Generated from commit: `d1d1499`
- Constellations: 88
- Edges: 685
- Endpoint stars: 694
- Endpoint stars without display names: 322

## AND -- Andromeda / アンドロメダ座

Counts: stars 16, edges 16, polylines 5, branch points 4, stars without display names 12

### Polylines

1. Alpheratz -> Delta Andromedae -> Mirach -> Almach
2. HIP 113726 -> HIP 116631 -> HIP 116805 -> HIP 116584
3. HIP 116631 -> HIP 2912 -> Delta Andromedae
4. HIP 2912 -> Mirach -> HIP 4436 -> HIP 3881 -> HIP 5434 -> HIP 7607
5. Delta Andromedae -> HIP 3031 -> HIP 3693 -> HIP 4463

### Edges

- Alpheratz -- Delta Andromedae  |  アルフェラッツ -- デルタ・アンドロメダ
- HIP 2912 -- Delta Andromedae  |  HIP 2912 -- デルタ・アンドロメダ
- HIP 2912 -- Mirach  |  HIP 2912 -- ミラク
- HIP 2912 -- HIP 116631  |  HIP 2912 -- HIP 116631
- HIP 3031 -- Delta Andromedae  |  HIP 3031 -- デルタ・アンドロメダ
- HIP 3031 -- HIP 3693  |  HIP 3031 -- HIP 3693
- Delta Andromedae -- Mirach  |  デルタ・アンドロメダ -- ミラク
- HIP 3693 -- HIP 4463  |  HIP 3693 -- HIP 4463
- HIP 3881 -- HIP 4436  |  HIP 3881 -- HIP 4436
- HIP 3881 -- HIP 5434  |  HIP 3881 -- HIP 5434
- HIP 4436 -- Mirach  |  HIP 4436 -- ミラク
- HIP 5434 -- HIP 7607  |  HIP 5434 -- HIP 7607
- Mirach -- Almach  |  ミラク -- アルマク
- HIP 113726 -- HIP 116631  |  HIP 113726 -- HIP 116631
- HIP 116584 -- HIP 116805  |  HIP 116584 -- HIP 116805
- HIP 116631 -- HIP 116805  |  HIP 116631 -- HIP 116805

### Branch Points

- HIP 2912 / HIP 2912 (HIP 2912): degree 3
- Delta Andromedae / デルタ・アンドロメダ (HIP 3092): degree 4
- Mirach / ミラク (HIP 5447): degree 4
- HIP 116631 / HIP 116631 (HIP 116631): degree 3

### Stars

- Alpheratz / アルフェラッツ (HIP 677, mag 2.06, RA 0.1398h, Dec 29.0904deg)
- HIP 2912 / HIP 2912 (HIP 2912, mag 4.34, RA 0.6147h, Dec 33.7193deg) [no display name]
- HIP 3031 / HIP 3031 (HIP 3031, mag 4.34, RA 0.6426h, Dec 29.3118deg) [no display name]
- Delta Andromedae / デルタ・アンドロメダ (HIP 3092, mag 3.27, RA 0.6555h, Dec 30.8610deg)
- HIP 3693 / HIP 3693 (HIP 3693, mag 4.08, RA 0.7890h, Dec 24.2672deg) [no display name]
- HIP 3881 / HIP 3881 (HIP 3881, mag 4.53, RA 0.8302h, Dec 41.0789deg) [no display name]
- HIP 4436 / HIP 4436 (HIP 4436, mag 3.86, RA 0.9459h, Dec 38.4993deg) [no display name]
- HIP 4463 / HIP 4463 (HIP 4463, mag 4.40, RA 0.9534h, Dec 23.4176deg) [no display name]
- HIP 5434 / HIP 5434 (HIP 5434, mag 4.26, RA 1.1584h, Dec 47.2418deg) [no display name]
- Mirach / ミラク (HIP 5447, mag 2.07, RA 1.1622h, Dec 35.6206deg)
- HIP 7607 / HIP 7607 (HIP 7607, mag 3.59, RA 1.6332h, Dec 48.6282deg) [no display name]
- Almach / アルマク (HIP 9640, mag 2.10, RA 2.0649h, Dec 42.3297deg)
- HIP 113726 / HIP 113726 (HIP 113726, mag 3.62, RA 23.0320h, Dec 42.3260deg) [no display name]
- HIP 116584 / HIP 116584 (HIP 116584, mag 3.81, RA 23.6261h, Dec 46.4582deg) [no display name]
- HIP 116631 / HIP 116631 (HIP 116631, mag 4.29, RA 23.6356h, Dec 43.2681deg) [no display name]
- HIP 116805 / HIP 116805 (HIP 116805, mag 4.15, RA 23.6735h, Dec 44.3339deg) [no display name]

## ANT -- Antlia / ポンプ座

Counts: stars 3, edges 2, polylines 1, branch points 0, stars without display names 1

### Polylines

1. Iota Antliae -> Alpha Antliae -> HIP 46515

### Edges

- HIP 46515 -- Alpha Antliae  |  HIP 46515 -- アルファ・ポンプ
- Alpha Antliae -- Iota Antliae  |  アルファ・ポンプ -- イオタ・ポンプ

### Stars

- HIP 46515 / HIP 46515 (HIP 46515, mag 4.51, RA 9.4874h, Dec -35.9513deg) [no display name]
- Alpha Antliae / アルファ・ポンプ (HIP 51172, mag 4.25, RA 10.4525h, Dec -31.0678deg)
- Iota Antliae / イオタ・ポンプ (HIP 53502, mag 4.60, RA 10.9453h, Dec -37.1378deg)

## APS -- Apus / ふうちょう座

Counts: stars 4, edges 3, polylines 2, branch points 0, stars without display names 0

### Polylines

1. Alpha Apodis -> Gamma Apodis
2. Delta Apodis -> Beta Apodis -> Gamma Apodis

### Edges

- Alpha Apodis -- Gamma Apodis  |  アルファ・ふうちょう -- ガンマ・ふうちょう
- Delta Apodis -- Beta Apodis  |  デルタ・ふうちょう -- ベータ・ふうちょう
- Gamma Apodis -- Beta Apodis  |  ガンマ・ふうちょう -- ベータ・ふうちょう

### Stars

- Alpha Apodis / アルファ・ふうちょう (HIP 72370, mag 3.83, RA 14.7977h, Dec -79.0447deg)
- Delta Apodis / デルタ・ふうちょう (HIP 80047, mag 4.68, RA 16.3391h, Dec -78.6957deg)
- Gamma Apodis / ガンマ・ふうちょう (HIP 81065, mag 3.87, RA 16.5575h, Dec -78.8971deg)
- Beta Apodis / ベータ・ふうちょう (HIP 81852, mag 4.24, RA 16.7179h, Dec -77.5166deg)

## AQR -- Aquarius / みずがめ座

Counts: stars 16, edges 17, polylines 2, branch points 5, stars without display names 7

### Polylines

1. Albali -> Sadalsuud -> Sadalmelik -> Sadachbia -> Zeta Aquarii -> Eta Aquarii -> Zeta Aquarii -> Pi Aquarii -> Sadalmelik
2. HIP 109139 -> Sadalsuud -> Sadalmelik -> Ancha -> HIP 112961 -> HIP 114724 -> HIP 115033 -> HIP 115438 -> HIP 115033 -> HIP 114341 -> HIP 115033 -> Skat -> HIP 112716 -> HIP 112961

### Edges

- Albali -- Sadalsuud  |  アルバリ -- サダルスウド
- Sadalsuud -- Sadalmelik  |  サダルスウド -- サダルメリク
- Sadalsuud -- HIP 109139  |  サダルスウド -- HIP 109139
- Sadalmelik -- Ancha  |  サダルメリク -- アンカ
- Sadalmelik -- Sadachbia  |  サダルメリク -- サダクビア
- Sadalmelik -- Pi Aquarii  |  サダルメリク -- パイ・みずがめ
- Ancha -- HIP 112961  |  アンカ -- HIP 112961
- Sadachbia -- Zeta Aquarii  |  サダクビア -- ゼータ・みずがめ
- Pi Aquarii -- Zeta Aquarii  |  パイ・みずがめ -- ゼータ・みずがめ
- Zeta Aquarii -- Eta Aquarii  |  ゼータ・みずがめ -- イータ・みずがめ
- HIP 112716 -- HIP 112961  |  HIP 112716 -- HIP 112961
- HIP 112716 -- Skat  |  HIP 112716 -- スカト
- HIP 112961 -- HIP 114724  |  HIP 112961 -- HIP 114724
- Skat -- HIP 115033  |  スカト -- HIP 115033
- HIP 114341 -- HIP 115033  |  HIP 114341 -- HIP 115033
- HIP 114724 -- HIP 115033  |  HIP 114724 -- HIP 115033
- HIP 115033 -- HIP 115438  |  HIP 115033 -- HIP 115438

### Branch Points

- Sadalsuud / サダルスウド (HIP 106278): degree 3
- Sadalmelik / サダルメリク (HIP 109074): degree 4
- Zeta Aquarii / ゼータ・みずがめ (HIP 110960): degree 3
- HIP 112961 / HIP 112961 (HIP 112961): degree 3
- HIP 115033 / HIP 115033 (HIP 115033): degree 4

### Stars

- Albali / アルバリ (HIP 102618, mag 3.77, RA 20.7946h, Dec -9.4958deg)
- Sadalsuud / サダルスウド (HIP 106278, mag 2.87, RA 21.5260h, Dec -5.5712deg)
- Sadalmelik / サダルメリク (HIP 109074, mag 2.94, RA 22.0964h, Dec -0.3199deg)
- HIP 109139 / HIP 109139 (HIP 109139, mag 4.29, RA 22.1073h, Dec -13.8697deg) [no display name]
- Ancha / アンカ (HIP 110003, mag 4.17, RA 22.2806h, Dec -7.7833deg)
- Sadachbia / サダクビア (HIP 110395, mag 3.84, RA 22.3609h, Dec -1.3873deg)
- Pi Aquarii / パイ・みずがめ (HIP 110672, mag 4.66, RA 22.4213h, Dec 1.3774deg)
- Zeta Aquarii / ゼータ・みずがめ (HIP 110960, mag 3.65, RA 22.4805h, Dec -0.0199deg)
- Eta Aquarii / イータ・みずがめ (HIP 111497, mag 4.04, RA 22.5893h, Dec -0.1175deg)
- HIP 112716 / HIP 112716 (HIP 112716, mag 4.05, RA 22.8265h, Dec -13.5926deg) [no display name]
- HIP 112961 / HIP 112961 (HIP 112961, mag 3.73, RA 22.8769h, Dec -7.5796deg) [no display name]
- Skat / スカト (HIP 113136, mag 3.27, RA 22.9108h, Dec -15.8208deg)
- HIP 114341 / HIP 114341 (HIP 114341, mag 3.68, RA 23.1574h, Dec -21.1724deg) [no display name]
- HIP 114724 / HIP 114724 (HIP 114724, mag 4.22, RA 23.2387h, Dec -6.0490deg) [no display name]
- HIP 115033 / HIP 115033 (HIP 115033, mag 4.41, RA 23.2984h, Dec -9.1825deg) [no display name]
- HIP 115438 / HIP 115438 (HIP 115438, mag 3.96, RA 23.3828h, Dec -20.1006deg) [no display name]

## AQL -- Aquila / わし座

Counts: stars 9, edges 8, polylines 1, branch points 1, stars without display names 5

### Polylines

1. Alshain -> Altair -> Tarazed -> Deneb el Okab -> HIP 93747 -> Deneb el Okab -> HIP 97804 -> HIP 99473 -> HIP 97804 -> Deneb el Okab -> HIP 93805 -> HIP 93429

### Edges

- Alshain -- Altair  |  アルシャイン -- アルタイル
- Altair -- Tarazed  |  アルタイル -- タラゼド
- Tarazed -- Deneb el Okab  |  タラゼド -- デネブ・エル・オカブ
- Deneb el Okab -- HIP 93747  |  デネブ・エル・オカブ -- HIP 93747
- Deneb el Okab -- HIP 97804  |  デネブ・エル・オカブ -- HIP 97804
- HIP 97804 -- HIP 99473  |  HIP 97804 -- HIP 99473
- Deneb el Okab -- HIP 93805  |  デネブ・エル・オカブ -- HIP 93805
- HIP 93805 -- HIP 93429  |  HIP 93805 -- HIP 93429

### Branch Points

- Deneb el Okab / デネブ・エル・オカブ (HIP 95501): degree 4

### Stars

- HIP 93429 / HIP 93429 (HIP 93429, mag 4.02, RA 19.0280h, Dec -5.7391deg) [no display name]
- HIP 93747 / HIP 93747 (HIP 93747, mag 2.99, RA 19.0902h, Dec 13.8635deg) [no display name]
- HIP 93805 / HIP 93805 (HIP 93805, mag 3.43, RA 19.1042h, Dec -4.8826deg) [no display name]
- Deneb el Okab / デネブ・エル・オカブ (HIP 95501, mag 3.36, RA 19.4249h, Dec 3.1148deg)
- Tarazed / タラゼド (HIP 97278, mag 2.72, RA 19.7710h, Dec 10.6133deg)
- Altair / アルタイル (HIP 97649, mag 0.77, RA 19.8464h, Dec 8.8683deg)
- HIP 97804 / HIP 97804 (HIP 97804, mag 3.87, RA 19.8745h, Dec 1.0057deg) [no display name]
- Alshain / アルシャイン (HIP 98036, mag 3.71, RA 19.9219h, Dec 6.4068deg)
- HIP 99473 / HIP 99473 (HIP 99473, mag 3.24, RA 20.1884h, Dec -0.8215deg) [no display name]

## ARA -- Ara / さいだん座

Counts: stars 8, edges 8, polylines 1, branch points 3, stars without display names 1

### Polylines

1. Theta Arae -> Alpha Arae -> Beta Arae -> Gamma Arae -> Delta Arae -> Gamma Arae -> Zeta Arae -> Eta Arae -> Zeta Arae -> HIP 83153 -> Alpha Arae

### Edges

- Theta Arae -- Alpha Arae  |  シータ・さいだん -- アルファ・さいだん
- Alpha Arae -- Beta Arae  |  アルファ・さいだん -- ベータ・さいだん
- Beta Arae -- Gamma Arae  |  ベータ・さいだん -- ガンマ・さいだん
- Gamma Arae -- Delta Arae  |  ガンマ・さいだん -- デルタ・さいだん
- Gamma Arae -- Zeta Arae  |  ガンマ・さいだん -- ゼータ・さいだん
- Zeta Arae -- Eta Arae  |  ゼータ・さいだん -- イータ・さいだん
- Zeta Arae -- HIP 83153  |  ゼータ・さいだん -- HIP 83153
- HIP 83153 -- Alpha Arae  |  HIP 83153 -- アルファ・さいだん

### Branch Points

- Zeta Arae / ゼータ・さいだん (HIP 83081): degree 3
- Gamma Arae / ガンマ・さいだん (HIP 85267): degree 3
- Alpha Arae / アルファ・さいだん (HIP 85792): degree 3

### Stars

- Eta Arae / イータ・さいだん (HIP 82363, mag 3.77, RA 16.8298h, Dec -59.0414deg)
- Zeta Arae / ゼータ・さいだん (HIP 83081, mag 3.12, RA 16.9770h, Dec -55.9901deg)
- HIP 83153 / HIP 83153 (HIP 83153, mag 4.06, RA 16.9931h, Dec -53.1604deg) [no display name]
- Beta Arae / ベータ・さいだん (HIP 85258, mag 2.84, RA 17.4217h, Dec -55.5299deg)
- Gamma Arae / ガンマ・さいだん (HIP 85267, mag 3.31, RA 17.4232h, Dec -56.3777deg)
- Delta Arae / デルタ・さいだん (HIP 85727, mag 3.60, RA 17.5183h, Dec -60.6838deg)
- Alpha Arae / アルファ・さいだん (HIP 85792, mag 2.84, RA 17.5307h, Dec -49.8761deg)
- Theta Arae / シータ・さいだん (HIP 88714, mag 3.65, RA 18.1105h, Dec -50.0915deg)

## ARI -- Aries / おひつじ座

Counts: stars 4, edges 3, polylines 1, branch points 0, stars without display names 1

### Polylines

1. Mesarthim -> Sheratan -> Hamal -> HIP 13209

### Edges

- Mesarthim -- Sheratan  |  メサルティム -- シェラタン
- Sheratan -- Hamal  |  シェラタン -- ハマル
- Hamal -- HIP 13209  |  ハマル -- HIP 13209

### Stars

- Mesarthim / メサルティム (HIP 8832, mag 3.88, RA 1.8922h, Dec 19.2939deg)
- Sheratan / シェラタン (HIP 8903, mag 2.64, RA 1.9107h, Dec 20.8080deg)
- Hamal / ハマル (HIP 9884, mag 2.00, RA 2.1195h, Dec 23.4624deg)
- HIP 13209 / HIP 13209 (HIP 13209, mag 3.61, RA 2.8331h, Dec 27.2605deg) [no display name]

## AUR -- Auriga / ぎょしゃ座

Counts: stars 8, edges 8, polylines 1, branch points 0, stars without display names 2

### Polylines

1. Capella -> Menkalinan -> Mahasim -> Elnath -> Hassaleh -> HIP 23453 -> HIP 23767 -> Almaaz -> Capella

### Edges

- Capella -- Menkalinan  |  カペラ -- メンカリナン
- Menkalinan -- Mahasim  |  メンカリナン -- マハシム
- Mahasim -- Elnath  |  マハシム -- エルナト
- Elnath -- Hassaleh  |  エルナト -- ハッサレ
- Hassaleh -- HIP 23453  |  ハッサレ -- HIP 23453
- HIP 23453 -- HIP 23767  |  HIP 23453 -- HIP 23767
- HIP 23767 -- Almaaz  |  HIP 23767 -- アルマーズ
- Almaaz -- Capella  |  アルマーズ -- カペラ

### Stars

- Hassaleh / ハッサレ (HIP 23015, mag 2.69, RA 4.9499h, Dec 33.1661deg)
- Almaaz / アルマーズ (HIP 23416, mag 3.03, RA 5.0328h, Dec 43.8233deg)
- HIP 23453 / HIP 23453 (HIP 23453, mag 3.69, RA 5.0413h, Dec 41.0758deg) [no display name]
- HIP 23767 / HIP 23767 (HIP 23767, mag 3.18, RA 5.1086h, Dec 41.2345deg) [no display name]
- Capella / カペラ (HIP 24608, mag 0.08, RA 5.2782h, Dec 45.9980deg)
- Elnath / エルナト (HIP 25428, mag 1.65, RA 5.4382h, Dec 28.6075deg)
- Menkalinan / メンカリナン (HIP 28360, mag 1.90, RA 5.9921h, Dec 44.9474deg)
- Mahasim / マハシム (HIP 28380, mag 2.62, RA 5.9954h, Dec 37.2126deg)

## BOO -- Bootes / うしかい座

Counts: stars 9, edges 10, polylines 1, branch points 2, stars without display names 5

### Polylines

1. Seginus -> HIP 71053 -> Arcturus -> Izar -> HIP 74666 -> Nekkar -> Seginus -> HIP 69732 -> HIP 70497 -> HIP 69483 -> HIP 69732

### Edges

- Seginus -- HIP 71053  |  セギヌス -- HIP 71053
- HIP 71053 -- Arcturus  |  HIP 71053 -- アークトゥルス
- Arcturus -- Izar  |  アークトゥルス -- イザール
- Izar -- HIP 74666  |  イザール -- HIP 74666
- HIP 74666 -- Nekkar  |  HIP 74666 -- ネッカル
- Nekkar -- Seginus  |  ネッカル -- セギヌス
- Seginus -- HIP 69732  |  セギヌス -- HIP 69732
- HIP 69732 -- HIP 70497  |  HIP 69732 -- HIP 70497
- HIP 70497 -- HIP 69483  |  HIP 70497 -- HIP 69483
- HIP 69483 -- HIP 69732  |  HIP 69483 -- HIP 69732

### Branch Points

- HIP 69732 / HIP 69732 (HIP 69732): degree 3
- Seginus / セギヌス (HIP 71075): degree 3

### Stars

- HIP 69483 / HIP 69483 (HIP 69483, mag 4.53, RA 14.2247h, Dec 51.7900deg) [no display name]
- Arcturus / アークトゥルス (HIP 69673, mag -0.05, RA 14.2610h, Dec 19.1824deg)
- HIP 69732 / HIP 69732 (HIP 69732, mag 4.18, RA 14.2731h, Dec 46.0883deg) [no display name]
- HIP 70497 / HIP 70497 (HIP 70497, mag 4.04, RA 14.4200h, Dec 51.8507deg) [no display name]
- HIP 71053 / HIP 71053 (HIP 71053, mag 3.57, RA 14.5305h, Dec 30.3714deg) [no display name]
- Seginus / セギヌス (HIP 71075, mag 3.03, RA 14.5346h, Dec 38.3079deg)
- Izar / イザール (HIP 72105, mag 2.37, RA 14.7498h, Dec 27.0742deg)
- Nekkar / ネッカル (HIP 73555, mag 3.49, RA 15.0324h, Dec 40.3906deg)
- HIP 74666 / HIP 74666 (HIP 74666, mag 3.46, RA 15.2584h, Dec 33.3148deg) [no display name]

## CAE -- Caelum / ちょうこくぐ座

Counts: stars 3, edges 2, polylines 1, branch points 0, stars without display names 1

### Polylines

1. HIP 21060 -> Alpha Caeli -> Beta Caeli

### Edges

- HIP 21060 -- Alpha Caeli  |  HIP 21060 -- アルファ・ちょうこくぐ
- Alpha Caeli -- Beta Caeli  |  アルファ・ちょうこくぐ -- ベータ・ちょうこくぐ

### Stars

- HIP 21060 / HIP 21060 (HIP 21060, mag 5.07, RA 4.5139h, Dec -44.9537deg) [no display name]
- Alpha Caeli / アルファ・ちょうこくぐ (HIP 21770, mag 4.45, RA 4.6760h, Dec -41.8638deg)
- Beta Caeli / ベータ・ちょうこくぐ (HIP 21861, mag 5.04, RA 4.7009h, Dec -37.1443deg)

## CAM -- Camelopardalis / きりん座

Counts: stars 7, edges 6, polylines 1, branch points 0, stars without display names 4

### Polylines

1. HIP 16281 -> HIP 16228 -> HIP 17884 -> Gamma Camelopardalis -> Alpha Camelopardalis -> Beta Camelopardalis -> HIP 23040

### Edges

- HIP 16281 -- HIP 16228  |  HIP 16281 -- HIP 16228
- HIP 16228 -- HIP 17884  |  HIP 16228 -- HIP 17884
- HIP 17884 -- Gamma Camelopardalis  |  HIP 17884 -- ガンマ・きりん
- Gamma Camelopardalis -- Alpha Camelopardalis  |  ガンマ・きりん -- アルファ・きりん
- Alpha Camelopardalis -- Beta Camelopardalis  |  アルファ・きりん -- ベータ・きりん
- Beta Camelopardalis -- HIP 23040  |  ベータ・きりん -- HIP 23040

### Stars

- HIP 16228 / HIP 16228 (HIP 16228, mag 4.21, RA 3.4845h, Dec 59.9403deg) [no display name]
- HIP 16281 / HIP 16281 (HIP 16281, mag 4.55, RA 3.4985h, Dec 58.8787deg) [no display name]
- HIP 17884 / HIP 17884 (HIP 17884, mag 4.39, RA 3.8254h, Dec 65.5260deg) [no display name]
- Gamma Camelopardalis / ガンマ・きりん (HIP 17959, mag 4.59, RA 3.8393h, Dec 71.3323deg)
- Alpha Camelopardalis / アルファ・きりん (HIP 22783, mag 4.29, RA 4.9008h, Dec 66.3427deg)
- HIP 23040 / HIP 23040 (HIP 23040, mag 4.43, RA 4.9548h, Dec 53.7521deg) [no display name]
- Beta Camelopardalis / ベータ・きりん (HIP 23522, mag 4.03, RA 5.0569h, Dec 60.4422deg)

## CNC -- Cancer / かに座

Counts: stars 5, edges 4, polylines 1, branch points 1, stars without display names 0

### Polylines

1. Acubens -> Asellus Australis -> Tarf -> Asellus Australis -> Asellus Borealis -> Iota Cancri

### Edges

- Acubens -- Asellus Australis  |  アクベンス -- アセルス・アウストラリス
- Asellus Australis -- Tarf  |  アセルス・アウストラリス -- タルフ
- Asellus Australis -- Asellus Borealis  |  アセルス・アウストラリス -- アセルス・ボレアリス
- Asellus Borealis -- Iota Cancri  |  アセルス・ボレアリス -- イオタ・かに

### Branch Points

- Asellus Australis / アセルス・アウストラリス (HIP 42911): degree 3

### Stars

- Tarf / タルフ (HIP 40526, mag 3.53, RA 8.2753h, Dec 9.1855deg)
- Asellus Borealis / アセルス・ボレアリス (HIP 42806, mag 4.66, RA 8.7214h, Dec 21.4685deg)
- Asellus Australis / アセルス・アウストラリス (HIP 42911, mag 3.94, RA 8.7447h, Dec 18.1543deg)
- Iota Cancri / イオタ・かに (HIP 43103, mag 4.03, RA 8.7783h, Dec 28.7599deg)
- Acubens / アクベンス (HIP 44066, mag 4.26, RA 8.9748h, Dec 11.8577deg)

## CVN -- Canes Venatici / りょうけん座

Counts: stars 2, edges 1, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Cor Caroli -> Chara

### Edges

- Cor Caroli -- Chara  |  コル・カロリ -- カーラ

### Stars

- Chara / カーラ (HIP 61317, mag 4.24, RA 12.5624h, Dec 41.3575deg)
- Cor Caroli / コル・カロリ (HIP 63125, mag 2.89, RA 12.9338h, Dec 38.3184deg)

## CMA -- Canis Major / おおいぬ座

Counts: stars 10, edges 11, polylines 3, branch points 3, stars without display names 5

### Polylines

1. Mirzam -> Sirius -> Wezen -> Adhara -> Wezen -> Aludra
2. Mirzam -> HIP 31592 -> HIP 33152 -> Adhara
3. Sirius -> HIP 33347 -> HIP 34045 -> HIP 33160 -> HIP 33347

### Edges

- Mirzam -- HIP 31592  |  ミルザム -- HIP 31592
- Mirzam -- Sirius  |  ミルザム -- シリウス
- HIP 31592 -- HIP 33152  |  HIP 31592 -- HIP 33152
- Sirius -- HIP 33347  |  シリウス -- HIP 33347
- Sirius -- Wezen  |  シリウス -- ウェゼン
- HIP 33152 -- Adhara  |  HIP 33152 -- アダーラ
- HIP 33160 -- HIP 33347  |  HIP 33160 -- HIP 33347
- HIP 33160 -- HIP 34045  |  HIP 33160 -- HIP 34045
- HIP 33347 -- HIP 34045  |  HIP 33347 -- HIP 34045
- Adhara -- Wezen  |  アダーラ -- ウェゼン
- Wezen -- Aludra  |  ウェゼン -- アルドラ

### Branch Points

- Sirius / シリウス (HIP 32349): degree 3
- HIP 33347 / HIP 33347 (HIP 33347): degree 3
- Wezen / ウェゼン (HIP 34444): degree 3

### Stars

- Mirzam / ミルザム (HIP 30324, mag 1.98, RA 6.3783h, Dec -17.9559deg)
- HIP 31592 / HIP 31592 (HIP 31592, mag 3.95, RA 6.6114h, Dec -19.2559deg) [no display name]
- Sirius / シリウス (HIP 32349, mag -1.46, RA 6.7525h, Dec -16.7161deg)
- HIP 33152 / HIP 33152 (HIP 33152, mag 3.89, RA 6.9022h, Dec -24.1842deg) [no display name]
- HIP 33160 / HIP 33160 (HIP 33160, mag 4.08, RA 6.9032h, Dec -12.0386deg) [no display name]
- HIP 33347 / HIP 33347 (HIP 33347, mag 4.36, RA 6.9356h, Dec -17.0542deg) [no display name]
- Adhara / アダーラ (HIP 33579, mag 1.50, RA 6.9771h, Dec -28.9721deg)
- HIP 34045 / HIP 34045 (HIP 34045, mag 4.11, RA 7.0626h, Dec -15.6333deg) [no display name]
- Wezen / ウェゼン (HIP 34444, mag 1.83, RA 7.1399h, Dec -26.3932deg)
- Aludra / アルドラ (HIP 35904, mag 2.45, RA 7.4016h, Dec -29.3031deg)

## CMI -- Canis Minor / こいぬ座

Counts: stars 2, edges 1, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Procyon -> Gomeisa

### Edges

- Procyon -- Gomeisa  |  プロキオン -- ゴメイサ

### Stars

- Gomeisa / ゴメイサ (HIP 36188, mag 2.89, RA 7.4525h, Dec 8.2893deg)
- Procyon / プロキオン (HIP 37279, mag 0.40, RA 7.6550h, Dec 5.2250deg)

## CAP -- Capricornus / やぎ座

Counts: stars 9, edges 9, polylines 1, branch points 0, stars without display names 4

### Polylines

1. Algedi -> Dabih -> HIP 102485 -> HIP 102978 -> HIP 105881 -> HIP 106723 -> Deneb Algedi -> Nashira -> Psi Capricorni -> Algedi

### Edges

- Algedi -- Dabih  |  アルゲディ -- ダビー
- Algedi -- Psi Capricorni  |  アルゲディ -- プサイ・カプリコルニ
- Dabih -- HIP 102485  |  ダビー -- HIP 102485
- HIP 102485 -- HIP 102978  |  HIP 102485 -- HIP 102978
- HIP 102978 -- HIP 105881  |  HIP 102978 -- HIP 105881
- Psi Capricorni -- Nashira  |  プサイ・カプリコルニ -- ナシラ
- HIP 105881 -- HIP 106723  |  HIP 105881 -- HIP 106723
- HIP 106723 -- Deneb Algedi  |  HIP 106723 -- デネブ・アルゲディ
- Nashira -- Deneb Algedi  |  ナシラ -- デネブ・アルゲディ

### Stars

- Algedi / アルゲディ (HIP 100064, mag 3.58, RA 20.3009h, Dec -12.5449deg)
- Dabih / ダビー (HIP 100345, mag 3.05, RA 20.3502h, Dec -14.7814deg)
- HIP 102485 / HIP 102485 (HIP 102485, mag 4.13, RA 20.7683h, Dec -25.2709deg) [no display name]
- HIP 102978 / HIP 102978 (HIP 102978, mag 4.12, RA 20.8637h, Dec -26.9191deg) [no display name]
- Psi Capricorni / プサイ・カプリコルニ (HIP 104139, mag 4.13, RA 21.0991h, Dec -17.2329deg)
- HIP 105881 / HIP 105881 (HIP 105881, mag 3.77, RA 21.4445h, Dec -22.4113deg) [no display name]
- HIP 106723 / HIP 106723 (HIP 106723, mag 4.51, RA 21.6180h, Dec -19.4660deg) [no display name]
- Nashira / ナシラ (HIP 106985, mag 3.69, RA 21.6682h, Dec -16.6623deg)
- Deneb Algedi / デネブ・アルゲディ (HIP 107556, mag 2.85, RA 21.7840h, Dec -16.1273deg)

## CAR -- Carina / りゅうこつ座

Counts: stars 8, edges 7, polylines 1, branch points 0, stars without display names 5

### Polylines

1. Canopus -> Miaplacidus -> HIP 50099 -> HIP 52419 -> HIP 51576 -> HIP 50371 -> Aspidiske -> HIP 43238

### Edges

- Canopus -- Miaplacidus  |  カノープス -- ミアプラキドゥス
- HIP 43238 -- Aspidiske  |  HIP 43238 -- アスピディスケ
- Miaplacidus -- HIP 50099  |  ミアプラキドゥス -- HIP 50099
- Aspidiske -- HIP 50371  |  アスピディスケ -- HIP 50371
- HIP 50099 -- HIP 52419  |  HIP 50099 -- HIP 52419
- HIP 50371 -- HIP 51576  |  HIP 50371 -- HIP 51576
- HIP 51576 -- HIP 52419  |  HIP 51576 -- HIP 52419

### Stars

- Canopus / カノープス (HIP 30438, mag -0.74, RA 6.3992h, Dec -52.6957deg)
- HIP 43238 / HIP 43238 (HIP 43238, mag 7.71, RA 8.8079h, Dec -55.4492deg) [no display name]
- Miaplacidus / ミアプラキドゥス (HIP 45238, mag 1.67, RA 9.2200h, Dec -69.7172deg)
- Aspidiske / アスピディスケ (HIP 45556, mag 2.21, RA 9.2848h, Dec -59.2752deg)
- HIP 50099 / HIP 50099 (HIP 50099, mag 3.29, RA 10.2290h, Dec -70.0379deg) [no display name]
- HIP 50371 / HIP 50371 (HIP 50371, mag 3.39, RA 10.2847h, Dec -61.3323deg) [no display name]
- HIP 51576 / HIP 51576 (HIP 51576, mag 3.30, RA 10.5337h, Dec -61.6853deg) [no display name]
- HIP 52419 / HIP 52419 (HIP 52419, mag 2.74, RA 10.7159h, Dec -64.3945deg) [no display name]

## CAS -- Cassiopeia / カシオペヤ座

Counts: stars 5, edges 4, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Segin -> Ruchbah -> Gamma Cassiopeiae -> Schedar -> Caph

### Edges

- Segin -- Ruchbah  |  セギン -- ルクバー
- Ruchbah -- Gamma Cassiopeiae  |  ルクバー -- ガンマ・カシオペヤ
- Gamma Cassiopeiae -- Schedar  |  ガンマ・カシオペヤ -- シェダル
- Schedar -- Caph  |  シェダル -- カフ

### Stars

- Caph / カフ (HIP 746, mag 2.27, RA 0.1529h, Dec 59.1498deg)
- Schedar / シェダル (HIP 3179, mag 2.24, RA 0.6751h, Dec 56.5373deg)
- Gamma Cassiopeiae / ガンマ・カシオペヤ (HIP 4427, mag 2.15, RA 0.9451h, Dec 60.7167deg)
- Ruchbah / ルクバー (HIP 6686, mag 2.68, RA 1.4302h, Dec 60.2353deg)
- Segin / セギン (HIP 8886, mag 3.35, RA 1.9066h, Dec 63.6700deg)

## CEN -- Centaurus / ケンタウルス座

Counts: stars 12, edges 13, polylines 1, branch points 3, stars without display names 9

### Polylines

1. HIP 61932 -> HIP 66657 -> Hadar -> HIP 71681 -> Hadar -> HIP 66657 -> Theta Centauri -> HIP 61932 -> Theta Centauri -> HIP 68323 -> HIP 68245 -> HIP 71352 -> HIP 68245 -> HIP 68862 -> HIP 70090 -> Menkent -> HIP 67347 -> Theta Centauri

### Edges

- HIP 61932 -- HIP 66657  |  HIP 61932 -- HIP 66657
- HIP 61932 -- Theta Centauri  |  HIP 61932 -- シータ・ケンタウリ
- HIP 66657 -- Theta Centauri  |  HIP 66657 -- シータ・ケンタウリ
- HIP 66657 -- Hadar  |  HIP 66657 -- ハダル
- HIP 67347 -- Theta Centauri  |  HIP 67347 -- シータ・ケンタウリ
- HIP 67347 -- Menkent  |  HIP 67347 -- メンケント
- Theta Centauri -- HIP 68323  |  シータ・ケンタウリ -- HIP 68323
- HIP 68245 -- HIP 68323  |  HIP 68245 -- HIP 68323
- HIP 68245 -- HIP 68862  |  HIP 68245 -- HIP 68862
- HIP 68245 -- HIP 71352  |  HIP 68245 -- HIP 71352
- Hadar -- HIP 71681  |  ハダル -- HIP 71681
- HIP 68862 -- HIP 70090  |  HIP 68862 -- HIP 70090
- Menkent -- HIP 70090  |  メンケント -- HIP 70090

### Branch Points

- HIP 66657 / HIP 66657 (HIP 66657): degree 3
- Theta Centauri / シータ・ケンタウリ (HIP 68002): degree 4
- HIP 68245 / HIP 68245 (HIP 68245): degree 3

### Stars

- HIP 61932 / HIP 61932 (HIP 61932, mag 2.20, RA 12.6920h, Dec -48.9599deg) [no display name]
- HIP 66657 / HIP 66657 (HIP 66657, mag 2.29, RA 13.6648h, Dec -53.4664deg) [no display name]
- HIP 67347 / HIP 67347 (HIP 67347, mag 7.99, RA 13.8034h, Dec -42.1847deg) [no display name]
- Theta Centauri / シータ・ケンタウリ (HIP 68002, mag 2.30, RA 13.9257h, Dec -47.2884deg)
- HIP 68245 / HIP 68245 (HIP 68245, mag 3.83, RA 13.9712h, Dec -42.1008deg) [no display name]
- HIP 68323 / HIP 68323 (HIP 68323, mag 7.38, RA 13.9860h, Dec -45.4690deg) [no display name]
- Hadar / ハダル (HIP 68702, mag 0.61, RA 14.0637h, Dec -60.3730deg)
- HIP 68862 / HIP 68862 (HIP 68862, mag 4.36, RA 14.1008h, Dec -41.1796deg) [no display name]
- Menkent / メンケント (HIP 68933, mag 2.06, RA 14.1114h, Dec -36.3700deg)
- HIP 70090 / HIP 70090 (HIP 70090, mag 4.05, RA 14.3426h, Dec -37.8853deg) [no display name]
- HIP 71352 / HIP 71352 (HIP 71352, mag 2.33, RA 14.5918h, Dec -42.1578deg) [no display name]
- HIP 71681 / HIP 71681 (HIP 71681, mag 1.35, RA 14.6603h, Dec -60.8383deg) [no display name]

## CEP -- Cepheus / ケフェウス座

Counts: stars 10, edges 11, polylines 2, branch points 3, stars without display names 6

### Polylines

1. HIP 102422 -> Alderamin -> Alfirk -> HIP 112724 -> Alfirk -> Errai -> HIP 112724 -> HIP 110991 -> Zeta Cephei -> HIP 109857 -> HIP 107259 -> Alderamin
2. HIP 101093 -> HIP 102422

### Edges

- HIP 101093 -- HIP 102422  |  HIP 101093 -- HIP 102422
- HIP 102422 -- Alderamin  |  HIP 102422 -- アルデラミン
- Alderamin -- Alfirk  |  アルデラミン -- アルフィルク
- Alderamin -- HIP 107259  |  アルデラミン -- HIP 107259
- Alfirk -- HIP 112724  |  アルフィルク -- HIP 112724
- Alfirk -- Errai  |  アルフィルク -- エライ
- HIP 107259 -- HIP 109857  |  HIP 107259 -- HIP 109857
- Zeta Cephei -- HIP 109857  |  ゼータ・ケフェイ -- HIP 109857
- Zeta Cephei -- HIP 110991  |  ゼータ・ケフェイ -- HIP 110991
- HIP 110991 -- HIP 112724  |  HIP 110991 -- HIP 112724
- HIP 112724 -- Errai  |  HIP 112724 -- エライ

### Branch Points

- Alderamin / アルデラミン (HIP 105199): degree 3
- Alfirk / アルフィルク (HIP 106032): degree 3
- HIP 112724 / HIP 112724 (HIP 112724): degree 3

### Stars

- HIP 101093 / HIP 101093 (HIP 101093, mag 4.21, RA 20.4930h, Dec 62.9941deg) [no display name]
- HIP 102422 / HIP 102422 (HIP 102422, mag 3.41, RA 20.7548h, Dec 61.8388deg) [no display name]
- Alderamin / アルデラミン (HIP 105199, mag 2.45, RA 21.3096h, Dec 62.5856deg)
- Alfirk / アルフィルク (HIP 106032, mag 3.23, RA 21.4777h, Dec 70.5607deg)
- HIP 107259 / HIP 107259 (HIP 107259, mag 4.23, RA 21.7251h, Dec 58.7800deg) [no display name]
- Zeta Cephei / ゼータ・ケフェイ (HIP 109492, mag 3.35, RA 22.1809h, Dec 58.2012deg)
- HIP 109857 / HIP 109857 (HIP 109857, mag 4.18, RA 22.2505h, Dec 57.0436deg) [no display name]
- HIP 110991 / HIP 110991 (HIP 110991, mag 4.07, RA 22.4862h, Dec 58.4152deg) [no display name]
- HIP 112724 / HIP 112724 (HIP 112724, mag 3.50, RA 22.8280h, Dec 66.2004deg) [no display name]
- Errai / エライ (HIP 116727, mag 3.21, RA 23.6558h, Dec 77.6323deg)

## CET -- Cetus / くじら座 REVIEW PRIORITY

Counts: stars 13, edges 14, polylines 1, branch points 2, stars without display names 9

### Polylines

1. Baten Kaitos -> Menkar -> HIP 13954 -> HIP 12828 -> HIP 11484 -> Baten Kaitos -> HIP 12387 -> Mira -> HIP 8645 -> HIP 8102 -> Diphda -> HIP 1562 -> HIP 5364 -> HIP 6537 -> HIP 8645

### Edges

- HIP 1562 -- Diphda  |  HIP 1562 -- ディフダ
- HIP 1562 -- HIP 5364  |  HIP 1562 -- HIP 5364
- Diphda -- HIP 8102  |  ディフダ -- HIP 8102
- HIP 5364 -- HIP 6537  |  HIP 5364 -- HIP 6537
- HIP 6537 -- HIP 8645  |  HIP 6537 -- HIP 8645
- HIP 8102 -- HIP 8645  |  HIP 8102 -- HIP 8645
- HIP 8645 -- Mira  |  HIP 8645 -- ミラ
- Mira -- HIP 12387  |  ミラ -- HIP 12387
- HIP 11484 -- Baten Kaitos  |  HIP 11484 -- バテン・カイトス
- HIP 11484 -- HIP 12828  |  HIP 11484 -- HIP 12828
- HIP 12387 -- Baten Kaitos  |  HIP 12387 -- バテン・カイトス
- Baten Kaitos -- Menkar  |  バテン・カイトス -- メンカル
- HIP 12828 -- HIP 13954  |  HIP 12828 -- HIP 13954
- HIP 13954 -- Menkar  |  HIP 13954 -- メンカル

### Branch Points

- HIP 8645 / HIP 8645 (HIP 8645): degree 3
- Baten Kaitos / バテン・カイトス (HIP 12706): degree 3

### Stars

- HIP 1562 / HIP 1562 (HIP 1562, mag 3.56, RA 0.3238h, Dec -8.8239deg) [no display name]
- Diphda / ディフダ (HIP 3419, mag 2.04, RA 0.7265h, Dec -17.9866deg)
- HIP 5364 / HIP 5364 (HIP 5364, mag 3.46, RA 1.1432h, Dec -10.1823deg) [no display name]
- HIP 6537 / HIP 6537 (HIP 6537, mag 3.60, RA 1.4004h, Dec -8.1833deg) [no display name]
- HIP 8102 / HIP 8102 (HIP 8102, mag 3.49, RA 1.7345h, Dec -15.9375deg) [no display name]
- HIP 8645 / HIP 8645 (HIP 8645, mag 3.74, RA 1.8577h, Dec -10.3350deg) [no display name]
- Mira / ミラ (HIP 10826, mag 3.00, RA 2.3224h, Dec -2.9776deg)
- HIP 11484 / HIP 11484 (HIP 11484, mag 4.30, RA 2.4693h, Dec 8.4601deg) [no display name]
- HIP 12387 / HIP 12387 (HIP 12387, mag 4.08, RA 2.6580h, Dec 0.3285deg) [no display name]
- Baten Kaitos / バテン・カイトス (HIP 12706, mag 3.73, RA 2.7217h, Dec -10.6780deg)
- HIP 12828 / HIP 12828 (HIP 12828, mag 4.27, RA 2.7490h, Dec 10.1141deg) [no display name]
- HIP 13954 / HIP 13954 (HIP 13954, mag 4.71, RA 2.9952h, Dec 8.9074deg) [no display name]
- Menkar / メンカル (HIP 14135, mag 2.54, RA 3.0379h, Dec 4.0897deg)

## CHA -- Chamaeleon / カメレオン座

Counts: stars 5, edges 5, polylines 1, branch points 1, stars without display names 1

### Polylines

1. Alpha Chamaeleontis -> Gamma Chamaeleontis -> Delta Chamaeleontis -> Beta Chamaeleontis -> HIP 58484 -> Gamma Chamaeleontis

### Edges

- Alpha Chamaeleontis -- Gamma Chamaeleontis  |  アルファ・カメレオン -- ガンマ・カメレオン
- Gamma Chamaeleontis -- Delta Chamaeleontis  |  ガンマ・カメレオン -- デルタ・カメレオン
- Gamma Chamaeleontis -- HIP 58484  |  ガンマ・カメレオン -- HIP 58484
- Delta Chamaeleontis -- Beta Chamaeleontis  |  デルタ・カメレオン -- ベータ・カメレオン
- HIP 58484 -- Beta Chamaeleontis  |  HIP 58484 -- ベータ・カメレオン

### Branch Points

- Gamma Chamaeleontis / ガンマ・カメレオン (HIP 51839): degree 3

### Stars

- Alpha Chamaeleontis / アルファ・カメレオン (HIP 40702, mag 4.07, RA 8.3088h, Dec -76.9197deg)
- Gamma Chamaeleontis / ガンマ・カメレオン (HIP 51839, mag 4.11, RA 10.5920h, Dec -78.6078deg)
- Delta Chamaeleontis / デルタ・カメレオン (HIP 52633, mag 4.45, RA 10.7630h, Dec -80.5402deg)
- HIP 58484 / HIP 58484 (HIP 58484, mag 4.88, RA 11.9938h, Dec -78.2218deg) [no display name]
- Beta Chamaeleontis / ベータ・カメレオン (HIP 60000, mag 4.24, RA 12.3058h, Dec -79.3122deg)

## CIR -- Circinus / コンパス座

Counts: stars 3, edges 2, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Beta Circini -> Alpha Circini -> Gamma Circini

### Edges

- Beta Circini -- Alpha Circini  |  ベータ・コンパス -- アルファ・コンパス
- Alpha Circini -- Gamma Circini  |  アルファ・コンパス -- ガンマ・コンパス

### Stars

- Alpha Circini / アルファ・コンパス (HIP 71908, mag 3.19, RA 14.7085h, Dec -64.9751deg)
- Beta Circini / ベータ・コンパス (HIP 74824, mag 4.07, RA 15.2919h, Dec -58.8012deg)
- Gamma Circini / ガンマ・コンパス (HIP 75323, mag 4.48, RA 15.3896h, Dec -59.3207deg)

## COL -- Columba / はと座

Counts: stars 6, edges 5, polylines 3, branch points 1, stars without display names 0

### Polylines

1. Phact -> Wazn
2. Epsilon Columbae -> Phact
3. Eta Columbae -> Wazn -> Gamma Columbae -> Delta Columbae

### Edges

- Epsilon Columbae -- Phact  |  イプシロン・はと -- ファクト
- Phact -- Wazn  |  ファクト -- ワズン
- Wazn -- Gamma Columbae  |  ワズン -- ガンマ・はと
- Wazn -- Eta Columbae  |  ワズン -- イータ・はと
- Gamma Columbae -- Delta Columbae  |  ガンマ・はと -- デルタ・はと

### Branch Points

- Wazn / ワズン (HIP 27628): degree 3

### Stars

- Epsilon Columbae / イプシロン・はと (HIP 25859, mag 3.86, RA 5.5202h, Dec -35.4705deg)
- Phact / ファクト (HIP 26634, mag 2.65, RA 5.6608h, Dec -34.0741deg)
- Wazn / ワズン (HIP 27628, mag 3.12, RA 5.8493h, Dec -35.7683deg)
- Gamma Columbae / ガンマ・はと (HIP 28199, mag 4.36, RA 5.9589h, Dec -35.2833deg)
- Eta Columbae / イータ・はと (HIP 28328, mag 3.96, RA 5.9858h, Dec -42.8151deg)
- Delta Columbae / デルタ・はと (HIP 30277, mag 3.85, RA 6.3686h, Dec -33.4364deg)

## COM -- Coma Berenices / かみのけ座

Counts: stars 3, edges 2, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Diadem -> Beta Comae Berenices -> Gamma Comae Berenices

### Edges

- Diadem -- Beta Comae Berenices  |  ディアデム -- ベータ・かみのけ
- Beta Comae Berenices -- Gamma Comae Berenices  |  ベータ・かみのけ -- ガンマ・かみのけ

### Stars

- Gamma Comae Berenices / ガンマ・かみのけ (HIP 60742, mag 4.35, RA 12.4490h, Dec 28.2684deg)
- Diadem / ディアデム (HIP 64241, mag 4.32, RA 13.1665h, Dec 17.5294deg)
- Beta Comae Berenices / ベータ・かみのけ (HIP 64394, mag 4.23, RA 13.1979h, Dec 27.8782deg)

## CRA -- Corona Australis / みなみのかんむり座

Counts: stars 5, edges 4, polylines 1, branch points 0, stars without display names 2

### Polylines

1. Gamma Coronae Australis -> Alpha Coronae Australis -> Beta Coronae Australis -> HIP 94005 -> HIP 90982

### Edges

- HIP 90982 -- HIP 94005  |  HIP 90982 -- HIP 94005
- Gamma Coronae Australis -- Alpha Coronae Australis  |  ガンマ・みなみのかんむり -- アルファ・みなみのかんむり
- HIP 94005 -- Beta Coronae Australis  |  HIP 94005 -- ベータ・みなみのかんむり
- Alpha Coronae Australis -- Beta Coronae Australis  |  アルファ・みなみのかんむり -- ベータ・みなみのかんむり

### Stars

- HIP 90982 / HIP 90982 (HIP 90982, mag 4.62, RA 18.5584h, Dec -42.3125deg) [no display name]
- Gamma Coronae Australis / ガンマ・みなみのかんむり (HIP 93825, mag 4.23, RA 19.1069h, Dec -37.0634deg)
- HIP 94005 / HIP 94005 (HIP 94005, mag 4.57, RA 19.1392h, Dec -40.4967deg) [no display name]
- Alpha Coronae Australis / アルファ・みなみのかんむり (HIP 94114, mag 4.10, RA 19.1579h, Dec -37.9045deg)
- Beta Coronae Australis / ベータ・みなみのかんむり (HIP 94160, mag 4.11, RA 19.1671h, Dec -39.3407deg)

## CRB -- Corona Borealis / かんむり座

Counts: stars 7, edges 6, polylines 1, branch points 0, stars without display names 3

### Polylines

1. HIP 78493 -> HIP 78159 -> Delta Coronae Borealis -> Gamma Coronae Borealis -> Alphecca -> Nusakan -> HIP 76127

### Edges

- HIP 78493 -- HIP 78159  |  HIP 78493 -- HIP 78159
- HIP 78159 -- Delta Coronae Borealis  |  HIP 78159 -- デルタ・かんむり
- Delta Coronae Borealis -- Gamma Coronae Borealis  |  デルタ・かんむり -- ガンマ・かんむり
- Gamma Coronae Borealis -- Alphecca  |  ガンマ・かんむり -- アルフェッカ
- Alphecca -- Nusakan  |  アルフェッカ -- ヌサカン
- Nusakan -- HIP 76127  |  ヌサカン -- HIP 76127

### Stars

- Nusakan / ヌサカン (HIP 75695, mag 3.68, RA 15.4638h, Dec 29.1057deg)
- HIP 76127 / HIP 76127 (HIP 76127, mag 4.14, RA 15.5488h, Dec 31.3591deg) [no display name]
- Alphecca / アルフェッカ (HIP 76267, mag 2.22, RA 15.5781h, Dec 26.7147deg)
- Gamma Coronae Borealis / ガンマ・かんむり (HIP 76952, mag 3.84, RA 15.7124h, Dec 26.2956deg)
- Delta Coronae Borealis / デルタ・かんむり (HIP 77512, mag 4.63, RA 15.8266h, Dec 26.0685deg)
- HIP 78159 / HIP 78159 (HIP 78159, mag 4.14, RA 15.9598h, Dec 26.8779deg) [no display name]
- HIP 78493 / HIP 78493 (HIP 78493, mag 4.98, RA 16.0240h, Dec 29.8511deg) [no display name]

## CRV -- Corvus / からす座

Counts: stars 5, edges 5, polylines 1, branch points 1, stars without display names 1

### Polylines

1. HIP 59199 -> Minkar -> Gienah Corvi -> Algorab -> Kraz -> Minkar

### Edges

- HIP 59199 -- Minkar  |  HIP 59199 -- ミンカル
- Minkar -- Gienah Corvi  |  ミンカル -- ギェナー・からす
- Gienah Corvi -- Algorab  |  ギェナー・からす -- アルゴラブ
- Algorab -- Kraz  |  アルゴラブ -- クラズ
- Kraz -- Minkar  |  クラズ -- ミンカル

### Branch Points

- Minkar / ミンカル (HIP 59316): degree 3

### Stars

- HIP 59199 / HIP 59199 (HIP 59199, mag 4.02, RA 12.1402h, Dec -24.7289deg) [no display name]
- Minkar / ミンカル (HIP 59316, mag 3.02, RA 12.1687h, Dec -22.6198deg)
- Gienah Corvi / ギェナー・からす (HIP 59803, mag 2.59, RA 12.2634h, Dec -17.5419deg)
- Algorab / アルゴラブ (HIP 60965, mag 2.95, RA 12.4977h, Dec -16.5154deg)
- Kraz / クラズ (HIP 61359, mag 2.65, RA 12.5731h, Dec -23.3968deg)

## CRT -- Crater / コップ座

Counts: stars 8, edges 8, polylines 1, branch points 2, stars without display names 4

### Polylines

1. HIP 58188 -> HIP 57283 -> Gamma Crateris -> Beta Crateris -> Alpha Crateris -> Delta Crateris -> Gamma Crateris -> Delta Crateris -> HIP 55687 -> HIP 56633

### Edges

- HIP 58188 -- HIP 57283  |  HIP 58188 -- HIP 57283
- HIP 57283 -- Gamma Crateris  |  HIP 57283 -- ガンマ・コップ
- Gamma Crateris -- Beta Crateris  |  ガンマ・コップ -- ベータ・コップ
- Beta Crateris -- Alpha Crateris  |  ベータ・コップ -- アルファ・コップ
- Alpha Crateris -- Delta Crateris  |  アルファ・コップ -- デルタ・コップ
- Delta Crateris -- Gamma Crateris  |  デルタ・コップ -- ガンマ・コップ
- Delta Crateris -- HIP 55687  |  デルタ・コップ -- HIP 55687
- HIP 55687 -- HIP 56633  |  HIP 55687 -- HIP 56633

### Branch Points

- Delta Crateris / デルタ・コップ (HIP 55282): degree 3
- Gamma Crateris / ガンマ・コップ (HIP 55705): degree 3

### Stars

- Alpha Crateris / アルファ・コップ (HIP 53740, mag 4.07, RA 10.9962h, Dec -18.2988deg)
- Beta Crateris / ベータ・コップ (HIP 54682, mag 4.46, RA 11.1943h, Dec -22.8256deg)
- Delta Crateris / デルタ・コップ (HIP 55282, mag 3.56, RA 11.3223h, Dec -14.7785deg)
- HIP 55687 / HIP 55687 (HIP 55687, mag 4.81, RA 11.4102h, Dec -10.8593deg) [no display name]
- Gamma Crateris / ガンマ・コップ (HIP 55705, mag 4.08, RA 11.4147h, Dec -17.6840deg)
- HIP 56633 / HIP 56633 (HIP 56633, mag 4.70, RA 11.6114h, Dec -9.8022deg) [no display name]
- HIP 57283 / HIP 57283 (HIP 57283, mag 4.71, RA 11.7460h, Dec -18.3507deg) [no display name]
- HIP 58188 / HIP 58188 (HIP 58188, mag 5.17, RA 11.9336h, Dec -17.1508deg) [no display name]

## CRU -- Crux / みなみじゅうじ座

Counts: stars 4, edges 2, polylines 3, branch points 0, stars without display names 0

### Polylines

1. Acrux -> Gacrux
2. Mimosa -> Delta Crucis
3. Mimosa -> Delta Crucis

### Edges

- Delta Crucis -- Mimosa  |  デルタ・クルキス -- ミモザ
- Acrux -- Gacrux  |  アクルックス -- ガクルックス

### Stars

- Delta Crucis / デルタ・クルキス (HIP 59747, mag 2.79, RA 12.2524h, Dec -58.7489deg)
- Acrux / アクルックス (HIP 60718, mag 0.77, RA 12.4433h, Dec -63.0991deg)
- Gacrux / ガクルックス (HIP 61084, mag 1.63, RA 12.5194h, Dec -57.1132deg)
- Mimosa / ミモザ (HIP 62434, mag 1.25, RA 12.7953h, Dec -59.6888deg)

## CYG -- Cygnus / はくちょう座

Counts: stars 10, edges 11, polylines 1, branch points 3, stars without display names 5

### Polylines

1. Deneb -> Sadr -> Gienah -> Sadr -> Albireo -> Sadr -> Delta Cygni -> HIP 95853 -> HIP 94779 -> HIP 95853 -> HIP 99848 -> Deneb -> HIP 103413 -> HIP 104732 -> Gienah

### Edges

- HIP 94779 -- HIP 95853  |  HIP 94779 -- HIP 95853
- HIP 95853 -- Delta Cygni  |  HIP 95853 -- デルタ・キグニ
- HIP 95853 -- HIP 99848  |  HIP 95853 -- HIP 99848
- Albireo -- Sadr  |  アルビレオ -- サドル
- Delta Cygni -- Sadr  |  デルタ・キグニ -- サドル
- HIP 99848 -- Deneb  |  HIP 99848 -- デネブ
- Sadr -- Deneb  |  サドル -- デネブ
- Sadr -- Gienah  |  サドル -- ギェナー
- Deneb -- HIP 103413  |  デネブ -- HIP 103413
- Gienah -- HIP 104732  |  ギェナー -- HIP 104732
- HIP 103413 -- HIP 104732  |  HIP 103413 -- HIP 104732

### Branch Points

- HIP 95853 / HIP 95853 (HIP 95853): degree 3
- Sadr / サドル (HIP 100453): degree 4
- Deneb / デネブ (HIP 102098): degree 3

### Stars

- HIP 94779 / HIP 94779 (HIP 94779, mag 3.80, RA 19.2850h, Dec 53.3685deg) [no display name]
- HIP 95853 / HIP 95853 (HIP 95853, mag 3.76, RA 19.4951h, Dec 51.7298deg) [no display name]
- Albireo / アルビレオ (HIP 95947, mag 3.08, RA 19.5120h, Dec 27.9597deg)
- Delta Cygni / デルタ・キグニ (HIP 97165, mag 2.87, RA 19.7494h, Dec 45.1308deg)
- HIP 99848 / HIP 99848 (HIP 99848, mag 3.96, RA 20.2579h, Dec 47.7142deg) [no display name]
- Sadr / サドル (HIP 100453, mag 2.23, RA 20.3705h, Dec 40.2567deg)
- Deneb / デネブ (HIP 102098, mag 1.25, RA 20.6905h, Dec 45.2803deg)
- Gienah / ギェナー (HIP 102488, mag 2.48, RA 20.7702h, Dec 33.9703deg)
- HIP 103413 / HIP 103413 (HIP 103413, mag 3.94, RA 20.9529h, Dec 41.1671deg) [no display name]
- HIP 104732 / HIP 104732 (HIP 104732, mag 3.21, RA 21.2156h, Dec 30.2269deg) [no display name]

## DEL -- Delphinus / いるか座

Counts: stars 5, edges 5, polylines 1, branch points 1, stars without display names 3

### Polylines

1. HIP 101421 -> Rotanev -> Sualocin -> HIP 102532 -> HIP 102281 -> Rotanev

### Edges

- HIP 101421 -- Rotanev  |  HIP 101421 -- ロタネブ
- Rotanev -- Sualocin  |  ロタネブ -- スアロキン
- Sualocin -- HIP 102532  |  スアロキン -- HIP 102532
- HIP 102532 -- HIP 102281  |  HIP 102532 -- HIP 102281
- HIP 102281 -- Rotanev  |  HIP 102281 -- ロタネブ

### Branch Points

- Rotanev / ロタネブ (HIP 101769): degree 3

### Stars

- HIP 101421 / HIP 101421 (HIP 101421, mag 4.03, RA 20.5535h, Dec 11.3033deg) [no display name]
- Rotanev / ロタネブ (HIP 101769, mag 3.64, RA 20.6258h, Dec 14.5951deg)
- Sualocin / スアロキン (HIP 101958, mag 3.77, RA 20.6606h, Dec 15.9119deg)
- HIP 102281 / HIP 102281 (HIP 102281, mag 4.43, RA 20.7243h, Dec 15.0746deg) [no display name]
- HIP 102532 / HIP 102532 (HIP 102532, mag 4.27, RA 20.7776h, Dec 16.1243deg) [no display name]

## DOR -- Dorado / かじき座

Counts: stars 6, edges 5, polylines 1, branch points 1, stars without display names 2

### Polylines

1. Gamma Doradus -> Alpha Doradus -> HIP 23693 -> Beta Doradus -> Delta Doradus -> Beta Doradus -> HIP 27890

### Edges

- Gamma Doradus -- Alpha Doradus  |  ガンマ・かじき -- アルファ・かじき
- Alpha Doradus -- HIP 23693  |  アルファ・かじき -- HIP 23693
- HIP 23693 -- Beta Doradus  |  HIP 23693 -- ベータ・かじき
- Beta Doradus -- Delta Doradus  |  ベータ・かじき -- デルタ・かじき
- Beta Doradus -- HIP 27890  |  ベータ・かじき -- HIP 27890

### Branch Points

- Beta Doradus / ベータ・かじき (HIP 26069): degree 3

### Stars

- Gamma Doradus / ガンマ・かじき (HIP 19893, mag 4.25, RA 4.2671h, Dec -51.4867deg)
- Alpha Doradus / アルファ・かじき (HIP 21281, mag 3.27, RA 4.5666h, Dec -55.0450deg)
- HIP 23693 / HIP 23693 (HIP 23693, mag 4.71, RA 5.0919h, Dec -57.4727deg) [no display name]
- Beta Doradus / ベータ・かじき (HIP 26069, mag 3.76, RA 5.5604h, Dec -62.4898deg)
- Delta Doradus / デルタ・かじき (HIP 27100, mag 4.35, RA 5.7462h, Dec -65.7355deg)
- HIP 27890 / HIP 27890 (HIP 27890, mag 4.65, RA 5.9017h, Dec -63.0896deg) [no display name]

## DRA -- Draco / りゅう座

Counts: stars 15, edges 15, polylines 1, branch points 3, stars without display names 11

### Polylines

1. HIP 56211 -> HIP 61281 -> Thuban -> Edasich -> HIP 78527 -> HIP 80331 -> HIP 83895 -> HIP 89908 -> HIP 89937 -> HIP 89908 -> HIP 94376 -> HIP 97433 -> HIP 94376 -> HIP 87585 -> HIP 85829 -> Rastaban -> Eltanin -> HIP 87585 -> HIP 94376

### Edges

- HIP 56211 -- HIP 61281  |  HIP 56211 -- HIP 61281
- HIP 61281 -- Thuban  |  HIP 61281 -- トゥバン
- Thuban -- Edasich  |  トゥバン -- エダシク
- Edasich -- HIP 78527  |  エダシク -- HIP 78527
- HIP 78527 -- HIP 80331  |  HIP 78527 -- HIP 80331
- HIP 80331 -- HIP 83895  |  HIP 80331 -- HIP 83895
- HIP 83895 -- HIP 89908  |  HIP 83895 -- HIP 89908
- Rastaban -- HIP 85829  |  ラスタバン -- HIP 85829
- Rastaban -- Eltanin  |  ラスタバン -- エルタニン
- HIP 85829 -- HIP 87585  |  HIP 85829 -- HIP 87585
- HIP 87585 -- Eltanin  |  HIP 87585 -- エルタニン
- HIP 87585 -- HIP 94376  |  HIP 87585 -- HIP 94376
- HIP 89908 -- HIP 89937  |  HIP 89908 -- HIP 89937
- HIP 89908 -- HIP 94376  |  HIP 89908 -- HIP 94376
- HIP 94376 -- HIP 97433  |  HIP 94376 -- HIP 97433

### Branch Points

- HIP 87585 / HIP 87585 (HIP 87585): degree 3
- HIP 89908 / HIP 89908 (HIP 89908): degree 3
- HIP 94376 / HIP 94376 (HIP 94376): degree 3

### Stars

- HIP 56211 / HIP 56211 (HIP 56211, mag 3.82, RA 11.5234h, Dec 69.3311deg) [no display name]
- HIP 61281 / HIP 61281 (HIP 61281, mag 3.85, RA 12.5581h, Dec 69.7882deg) [no display name]
- Thuban / トゥバン (HIP 68756, mag 3.65, RA 14.0732h, Dec 64.3759deg)
- Edasich / エダシク (HIP 75458, mag 3.29, RA 15.4155h, Dec 58.9661deg)
- HIP 78527 / HIP 78527 (HIP 78527, mag 4.01, RA 16.0315h, Dec 58.5653deg) [no display name]
- HIP 80331 / HIP 80331 (HIP 80331, mag 2.73, RA 16.3999h, Dec 61.5142deg) [no display name]
- HIP 83895 / HIP 83895 (HIP 83895, mag 3.17, RA 17.1464h, Dec 65.7147deg) [no display name]
- Rastaban / ラスタバン (HIP 85670, mag 2.79, RA 17.5072h, Dec 52.3014deg)
- HIP 85829 / HIP 85829 (HIP 85829, mag 4.86, RA 17.5378h, Dec 55.1730deg) [no display name]
- HIP 87585 / HIP 87585 (HIP 87585, mag 3.73, RA 17.8921h, Dec 56.8726deg) [no display name]
- Eltanin / エルタニン (HIP 87833, mag 2.24, RA 17.9434h, Dec 51.4889deg)
- HIP 89908 / HIP 89908 (HIP 89908, mag 4.22, RA 18.3460h, Dec 71.3378deg) [no display name]
- HIP 89937 / HIP 89937 (HIP 89937, mag 3.55, RA 18.3507h, Dec 72.7328deg) [no display name]
- HIP 94376 / HIP 94376 (HIP 94376, mag 3.07, RA 19.2092h, Dec 67.6615deg) [no display name]
- HIP 97433 / HIP 97433 (HIP 97433, mag 3.84, RA 19.8028h, Dec 70.2679deg) [no display name]

## EQU -- Equuleus / こうま座

Counts: stars 3, edges 2, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Alpha Equulei -> Delta Equulei -> Gamma Equulei

### Edges

- Gamma Equulei -- Delta Equulei  |  ガンマ・こうま -- デルタ・こうま
- Delta Equulei -- Alpha Equulei  |  デルタ・こうま -- アルファ・こうま

### Stars

- Gamma Equulei / ガンマ・こうま (HIP 104521, mag 4.69, RA 21.1724h, Dec 10.1316deg)
- Delta Equulei / デルタ・こうま (HIP 104858, mag 4.49, RA 21.2413h, Dec 10.0069deg)
- Alpha Equulei / アルファ・こうま (HIP 104987, mag 3.92, RA 21.2637h, Dec 5.2479deg)

## ERI -- Eridanus / エリダヌス座

Counts: stars 31, edges 30, polylines 1, branch points 0, stars without display names 27

### Polylines

1. Cursa -> HIP 22701 -> HIP 22109 -> HIP 21444 -> HIP 19587 -> Zaurak -> HIP 17378 -> HIP 16537 -> HIP 13701 -> HIP 12770 -> HIP 12843 -> HIP 14146 -> HIP 15474 -> HIP 16611 -> HIP 17651 -> HIP 18216 -> HIP 18673 -> HIP 21393 -> HIP 20535 -> HIP 20042 -> HIP 17874 -> HIP 17797 -> HIP 16870 -> HIP 15510 -> Acamar -> HIP 12486 -> HIP 12413 -> HIP 11407 -> HIP 10602 -> HIP 9007 -> Achernar

### Edges

- Cursa -- HIP 22701  |  クルサ -- HIP 22701
- HIP 22701 -- HIP 22109  |  HIP 22701 -- HIP 22109
- HIP 22109 -- HIP 21444  |  HIP 22109 -- HIP 21444
- HIP 21444 -- HIP 19587  |  HIP 21444 -- HIP 19587
- HIP 19587 -- Zaurak  |  HIP 19587 -- ザウラク
- Zaurak -- HIP 17378  |  ザウラク -- HIP 17378
- HIP 17378 -- HIP 16537  |  HIP 17378 -- HIP 16537
- HIP 16537 -- HIP 13701  |  HIP 16537 -- HIP 13701
- HIP 13701 -- HIP 12770  |  HIP 13701 -- HIP 12770
- HIP 12770 -- HIP 12843  |  HIP 12770 -- HIP 12843
- HIP 12843 -- HIP 14146  |  HIP 12843 -- HIP 14146
- HIP 14146 -- HIP 15474  |  HIP 14146 -- HIP 15474
- HIP 15474 -- HIP 16611  |  HIP 15474 -- HIP 16611
- HIP 16611 -- HIP 17651  |  HIP 16611 -- HIP 17651
- HIP 17651 -- HIP 18216  |  HIP 17651 -- HIP 18216
- HIP 18216 -- HIP 18673  |  HIP 18216 -- HIP 18673
- HIP 18673 -- HIP 21393  |  HIP 18673 -- HIP 21393
- HIP 21393 -- HIP 20535  |  HIP 21393 -- HIP 20535
- HIP 20535 -- HIP 20042  |  HIP 20535 -- HIP 20042
- HIP 20042 -- HIP 17874  |  HIP 20042 -- HIP 17874
- HIP 17874 -- HIP 17797  |  HIP 17874 -- HIP 17797
- HIP 17797 -- HIP 16870  |  HIP 17797 -- HIP 16870
- HIP 16870 -- HIP 15510  |  HIP 16870 -- HIP 15510
- HIP 15510 -- Acamar  |  HIP 15510 -- アカマル
- Acamar -- HIP 12486  |  アカマル -- HIP 12486
- HIP 12486 -- HIP 12413  |  HIP 12486 -- HIP 12413
- HIP 12413 -- HIP 11407  |  HIP 12413 -- HIP 11407
- HIP 11407 -- HIP 10602  |  HIP 11407 -- HIP 10602
- HIP 10602 -- HIP 9007  |  HIP 10602 -- HIP 9007
- HIP 9007 -- Achernar  |  HIP 9007 -- アケルナル

### Stars

- Achernar / アケルナル (HIP 7588, mag 0.46, RA 1.6286h, Dec -57.2368deg)
- HIP 9007 / HIP 9007 (HIP 9007, mag 3.69, RA 1.9326h, Dec -51.6089deg) [no display name]
- HIP 10602 / HIP 10602 (HIP 10602, mag 3.56, RA 2.2752h, Dec -51.5122deg) [no display name]
- HIP 11407 / HIP 11407 (HIP 11407, mag 4.24, RA 2.4498h, Dec -47.7038deg) [no display name]
- HIP 12413 / HIP 12413 (HIP 12413, mag 4.74, RA 2.6633h, Dec -42.8917deg) [no display name]
- HIP 12486 / HIP 12486 (HIP 12486, mag 4.11, RA 2.6778h, Dec -39.8554deg) [no display name]
- HIP 12770 / HIP 12770 (HIP 12770, mag 4.24, RA 2.7354h, Dec -13.8587deg) [no display name]
- HIP 12843 / HIP 12843 (HIP 12843, mag 4.47, RA 2.7517h, Dec -18.5726deg) [no display name]
- HIP 13701 / HIP 13701 (HIP 13701, mag 3.89, RA 2.9405h, Dec -8.8981deg) [no display name]
- Acamar / アカマル (HIP 13847, mag 3.24, RA 2.9710h, Dec -40.3047deg)
- HIP 14146 / HIP 14146 (HIP 14146, mag 4.08, RA 3.0399h, Dec -23.6245deg) [no display name]
- HIP 15474 / HIP 15474 (HIP 15474, mag 3.70, RA 3.3253h, Dec -21.7579deg) [no display name]
- HIP 15510 / HIP 15510 (HIP 15510, mag 4.26, RA 3.3319h, Dec -43.0698deg) [no display name]
- HIP 16537 / HIP 16537 (HIP 16537, mag 3.72, RA 3.5488h, Dec -9.4583deg) [no display name]
- HIP 16611 / HIP 16611 (HIP 16611, mag 4.26, RA 3.5631h, Dec -21.6329deg) [no display name]
- HIP 16870 / HIP 16870 (HIP 16870, mag 4.57, RA 3.6182h, Dec -40.2745deg) [no display name]
- HIP 17378 / HIP 17378 (HIP 17378, mag 3.52, RA 3.7208h, Dec -9.7634deg) [no display name]
- HIP 17651 / HIP 17651 (HIP 17651, mag 4.22, RA 3.7808h, Dec -23.2497deg) [no display name]
- HIP 17797 / HIP 17797 (HIP 17797, mag 4.30, RA 3.8100h, Dec -37.6202deg) [no display name]
- HIP 17874 / HIP 17874 (HIP 17874, mag 4.17, RA 3.8242h, Dec -36.2002deg) [no display name]
- HIP 18216 / HIP 18216 (HIP 18216, mag 4.64, RA 3.8952h, Dec -24.6122deg) [no display name]
- Zaurak / ザウラク (HIP 18543, mag 2.97, RA 3.9672h, Dec -13.5085deg)
- HIP 18673 / HIP 18673 (HIP 18673, mag 4.62, RA 3.9987h, Dec -24.0162deg) [no display name]
- HIP 19587 / HIP 19587 (HIP 19587, mag 4.04, RA 4.1978h, Dec -6.8376deg) [no display name]
- HIP 20042 / HIP 20042 (HIP 20042, mag 3.55, RA 4.2982h, Dec -33.7983deg) [no display name]
- HIP 20535 / HIP 20535 (HIP 20535, mag 3.97, RA 4.4006h, Dec -34.0168deg) [no display name]
- HIP 21393 / HIP 21393 (HIP 21393, mag 3.81, RA 4.5925h, Dec -30.5623deg) [no display name]
- HIP 21444 / HIP 21444 (HIP 21444, mag 3.93, RA 4.6053h, Dec -3.3525deg) [no display name]
- HIP 22109 / HIP 22109 (HIP 22109, mag 4.01, RA 4.7584h, Dec -3.2547deg) [no display name]
- HIP 22701 / HIP 22701 (HIP 22701, mag 4.36, RA 4.8816h, Dec -5.4527deg) [no display name]
- Cursa / クルサ (HIP 23875, mag 2.79, RA 5.1308h, Dec -5.0864deg)

## FOR -- Fornax / ろ座

Counts: stars 3, edges 2, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Alpha Fornacis -> Beta Fornacis -> Nu Fornacis

### Edges

- Alpha Fornacis -- Beta Fornacis  |  アルファ・ろ -- ベータ・ろ
- Beta Fornacis -- Nu Fornacis  |  ベータ・ろ -- ニュー・ろ

### Stars

- Nu Fornacis / ニュー・ろ (HIP 9677, mag 4.69, RA 2.0748h, Dec -29.2968deg)
- Beta Fornacis / ベータ・ろ (HIP 13147, mag 4.46, RA 2.8182h, Dec -32.4059deg)
- Alpha Fornacis / アルファ・ろ (HIP 14879, mag 3.87, RA 3.2012h, Dec -28.9869deg)

## GEM -- Gemini / ふたご座

Counts: stars 18, edges 17, polylines 1, branch points 4, stars without display names 12

### Polylines

1. HIP 28734 -> HIP 29655 -> HIP 30343 -> Mebsuta -> HIP 30883 -> Mebsuta -> HIP 34693 -> HIP 36366 -> Castor -> HIP 36366 -> HIP 34693 -> HIP 33018 -> HIP 34693 -> HIP 36046 -> HIP 36962 -> Pollux -> HIP 36962 -> HIP 37740 -> HIP 36962 -> Wasat -> Mekbuda -> Alhena -> Mekbuda -> Wasat -> HIP 35350 -> HIP 32362

### Edges

- HIP 28734 -- HIP 29655  |  HIP 28734 -- HIP 29655
- HIP 29655 -- HIP 30343  |  HIP 29655 -- HIP 30343
- HIP 30343 -- Mebsuta  |  HIP 30343 -- メブスタ
- Mebsuta -- HIP 30883  |  メブスタ -- HIP 30883
- Mebsuta -- HIP 34693  |  メブスタ -- HIP 34693
- HIP 34693 -- HIP 36366  |  HIP 34693 -- HIP 36366
- HIP 36366 -- Castor  |  HIP 36366 -- カストル
- HIP 34693 -- HIP 33018  |  HIP 34693 -- HIP 33018
- HIP 34693 -- HIP 36046  |  HIP 34693 -- HIP 36046
- HIP 36046 -- HIP 36962  |  HIP 36046 -- HIP 36962
- HIP 36962 -- Pollux  |  HIP 36962 -- ポルックス
- HIP 36962 -- HIP 37740  |  HIP 36962 -- HIP 37740
- HIP 36962 -- Wasat  |  HIP 36962 -- ワサト
- Wasat -- Mekbuda  |  ワサト -- メクブダ
- Mekbuda -- Alhena  |  メクブダ -- アルヘナ
- Wasat -- HIP 35350  |  ワサト -- HIP 35350
- HIP 35350 -- HIP 32362  |  HIP 35350 -- HIP 32362

### Branch Points

- Mebsuta / メブスタ (HIP 32246): degree 3
- HIP 34693 / HIP 34693 (HIP 34693): degree 4
- Wasat / ワサト (HIP 35550): degree 3
- HIP 36962 / HIP 36962 (HIP 36962): degree 4

### Stars

- HIP 28734 / HIP 28734 (HIP 28734, mag 4.16, RA 6.0687h, Dec 23.2633deg) [no display name]
- HIP 29655 / HIP 29655 (HIP 29655, mag 3.31, RA 6.2480h, Dec 22.5068deg) [no display name]
- HIP 30343 / HIP 30343 (HIP 30343, mag 2.87, RA 6.3827h, Dec 22.5136deg) [no display name]
- HIP 30883 / HIP 30883 (HIP 30883, mag 4.13, RA 6.4827h, Dec 20.2121deg) [no display name]
- Alhena / アルヘナ (HIP 31681, mag 1.93, RA 6.6285h, Dec 16.3993deg)
- Mebsuta / メブスタ (HIP 32246, mag 3.06, RA 6.7322h, Dec 25.1311deg)
- HIP 32362 / HIP 32362 (HIP 32362, mag 3.35, RA 6.7548h, Dec 12.8956deg) [no display name]
- HIP 33018 / HIP 33018 (HIP 33018, mag 3.60, RA 6.8798h, Dec 33.9613deg) [no display name]
- Mekbuda / メクブダ (HIP 34088, mag 4.01, RA 7.0685h, Dec 20.5703deg)
- HIP 34693 / HIP 34693 (HIP 34693, mag 4.41, RA 7.1857h, Dec 30.2452deg) [no display name]
- HIP 35350 / HIP 35350 (HIP 35350, mag 3.58, RA 7.3015h, Dec 16.5404deg) [no display name]
- Wasat / ワサト (HIP 35550, mag 3.53, RA 7.3354h, Dec 21.9823deg)
- HIP 36046 / HIP 36046 (HIP 36046, mag 3.78, RA 7.4288h, Dec 27.7981deg) [no display name]
- HIP 36366 / HIP 36366 (HIP 36366, mag 4.16, RA 7.4852h, Dec 31.7845deg) [no display name]
- Castor / カストル (HIP 36850, mag 1.58, RA 7.5766h, Dec 31.8886deg)
- HIP 36962 / HIP 36962 (HIP 36962, mag 4.06, RA 7.5987h, Dec 26.8957deg) [no display name]
- HIP 37740 / HIP 37740 (HIP 37740, mag 3.57, RA 7.7408h, Dec 24.3980deg) [no display name]
- Pollux / ポルックス (HIP 37826, mag 1.14, RA 7.5767h, Dec 31.8883deg)

## GRU -- Grus / つる座

Counts: stars 7, edges 7, polylines 1, branch points 2, stars without display names 2

### Polylines

1. Aldhanab -> HIP 109111 -> Delta Gruis -> Alnair -> Tiaki -> Delta Gruis -> Tiaki -> Epsilon Gruis -> HIP 113638

### Edges

- Aldhanab -- HIP 109111  |  アルダナブ -- HIP 109111
- HIP 109111 -- Delta Gruis  |  HIP 109111 -- デルタ・つる
- Alnair -- Delta Gruis  |  アルナイル -- デルタ・つる
- Alnair -- Tiaki  |  アルナイル -- ティアキ
- Delta Gruis -- Tiaki  |  デルタ・つる -- ティアキ
- Tiaki -- Epsilon Gruis  |  ティアキ -- イプシロン・つる
- Epsilon Gruis -- HIP 113638  |  イプシロン・つる -- HIP 113638

### Branch Points

- Delta Gruis / デルタ・つる (HIP 110997): degree 3
- Tiaki / ティアキ (HIP 112122): degree 3

### Stars

- Aldhanab / アルダナブ (HIP 108085, mag 3.00, RA 21.8988h, Dec -37.3649deg)
- HIP 109111 / HIP 109111 (HIP 109111, mag 4.47, RA 22.1019h, Dec -39.5434deg) [no display name]
- Alnair / アルナイル (HIP 109268, mag 1.73, RA 22.1372h, Dec -46.9610deg)
- Delta Gruis / デルタ・つる (HIP 110997, mag 3.97, RA 22.4878h, Dec -43.4956deg)
- Tiaki / ティアキ (HIP 112122, mag 2.07, RA 22.7111h, Dec -46.8846deg)
- Epsilon Gruis / イプシロン・つる (HIP 112623, mag 3.49, RA 22.8092h, Dec -51.3169deg)
- HIP 113638 / HIP 113638 (HIP 113638, mag 4.11, RA 23.0147h, Dec -52.7541deg) [no display name]

## HER -- Hercules / ヘルクレス座

Counts: stars 17, edges 18, polylines 1, branch points 6, stars without display names 9

### Polylines

1. Maasym -> Rasalgethi -> Kornephoros -> Sarin -> Kornephoros -> Zeta Herculis -> Epsilon Herculis -> Zeta Herculis -> Eta Herculis -> HIP 81126 -> HIP 79992 -> HIP 81126 -> Eta Herculis -> Pi Herculis -> HIP 85112 -> HIP 87808 -> HIP 86414 -> HIP 87808 -> HIP 85112 -> Pi Herculis -> Epsilon Herculis -> Maasym -> HIP 85693 -> HIP 86974 -> HIP 87933 -> HIP 88794

### Edges

- HIP 79992 -- HIP 81126  |  HIP 79992 -- HIP 81126
- Sarin -- Kornephoros  |  サリン -- コルネフォロス
- Kornephoros -- Zeta Herculis  |  コルネフォロス -- ゼータ・ヘルクレス
- Kornephoros -- Rasalgethi  |  コルネフォロス -- ラスアルゲティ
- HIP 81126 -- Eta Herculis  |  HIP 81126 -- イータ・ヘルクレス
- Zeta Herculis -- Eta Herculis  |  ゼータ・ヘルクレス -- イータ・ヘルクレス
- Zeta Herculis -- Epsilon Herculis  |  ゼータ・ヘルクレス -- イプシロン・ヘルクレス
- Eta Herculis -- Pi Herculis  |  イータ・ヘルクレス -- パイ・ヘルクレス
- Epsilon Herculis -- Maasym  |  イプシロン・ヘルクレス -- マーシム
- Epsilon Herculis -- Pi Herculis  |  イプシロン・ヘルクレス -- パイ・ヘルクレス
- Rasalgethi -- Maasym  |  ラスアルゲティ -- マーシム
- Maasym -- HIP 85693  |  マーシム -- HIP 85693
- Pi Herculis -- HIP 85112  |  パイ・ヘルクレス -- HIP 85112
- HIP 85112 -- HIP 87808  |  HIP 85112 -- HIP 87808
- HIP 85693 -- HIP 86974  |  HIP 85693 -- HIP 86974
- HIP 86414 -- HIP 87808  |  HIP 86414 -- HIP 87808
- HIP 86974 -- HIP 87933  |  HIP 86974 -- HIP 87933
- HIP 87933 -- HIP 88794  |  HIP 87933 -- HIP 88794

### Branch Points

- Kornephoros / コルネフォロス (HIP 80816): degree 3
- Zeta Herculis / ゼータ・ヘルクレス (HIP 81693): degree 3
- Eta Herculis / イータ・ヘルクレス (HIP 81833): degree 3
- Epsilon Herculis / イプシロン・ヘルクレス (HIP 83207): degree 3
- Maasym / マーシム (HIP 84379): degree 3
- Pi Herculis / パイ・ヘルクレス (HIP 84380): degree 3

### Stars

- HIP 79992 / HIP 79992 (HIP 79992, mag 3.91, RA 16.3290h, Dec 46.3134deg) [no display name]
- Sarin / サリン (HIP 80170, mag 3.13, RA 16.3290h, Dec 19.1530deg)
- Kornephoros / コルネフォロス (HIP 80816, mag 2.77, RA 16.5037h, Dec 21.4896deg)
- HIP 81126 / HIP 81126 (HIP 81126, mag 4.20, RA 16.5684h, Dec 42.4370deg) [no display name]
- Zeta Herculis / ゼータ・ヘルクレス (HIP 81693, mag 2.81, RA 16.6881h, Dec 31.6031deg)
- Eta Herculis / イータ・ヘルクレス (HIP 81833, mag 3.48, RA 16.7149h, Dec 38.9223deg)
- Epsilon Herculis / イプシロン・ヘルクレス (HIP 83207, mag 3.91, RA 17.0048h, Dec 30.9264deg)
- Rasalgethi / ラスアルゲティ (HIP 84345, mag 3.35, RA 17.2441h, Dec 14.3903deg)
- Maasym / マーシム (HIP 84379, mag 4.41, RA 17.2505h, Dec 24.8392deg)
- Pi Herculis / パイ・ヘルクレス (HIP 84380, mag 3.16, RA 17.2508h, Dec 36.8092deg)
- HIP 85112 / HIP 85112 (HIP 85112, mag 4.15, RA 17.3947h, Dec 37.1459deg) [no display name]
- HIP 85693 / HIP 85693 (HIP 85693, mag 4.41, RA 17.5123h, Dec 26.1106deg) [no display name]
- HIP 86414 / HIP 86414 (HIP 86414, mag 3.82, RA 17.6577h, Dec 46.0063deg) [no display name]
- HIP 86974 / HIP 86974 (HIP 86974, mag 3.42, RA 17.7743h, Dec 27.7207deg) [no display name]
- HIP 87808 / HIP 87808 (HIP 87808, mag 3.86, RA 17.9376h, Dec 37.2505deg) [no display name]
- HIP 87933 / HIP 87933 (HIP 87933, mag 3.70, RA 17.9627h, Dec 29.2479deg) [no display name]
- HIP 88794 / HIP 88794 (HIP 88794, mag 3.84, RA 18.1257h, Dec 28.7625deg) [no display name]

## HOR -- Horologium / とけい座

Counts: stars 6, edges 5, polylines 1, branch points 0, stars without display names 3

### Polylines

1. Alpha Horologii -> HIP 12653 -> Eta Horologii -> HIP 12484 -> HIP 14240 -> Beta Horologii

### Edges

- Eta Horologii -- HIP 12484  |  イータ・とけい -- HIP 12484
- Eta Horologii -- HIP 12653  |  イータ・とけい -- HIP 12653
- HIP 12484 -- HIP 14240  |  HIP 12484 -- HIP 14240
- HIP 12653 -- Alpha Horologii  |  HIP 12653 -- アルファ・とけい
- Beta Horologii -- HIP 14240  |  ベータ・とけい -- HIP 14240

### Stars

- Eta Horologii / イータ・とけい (HIP 12225, mag 5.31, RA 2.6234h, Dec -52.5431deg)
- HIP 12484 / HIP 12484 (HIP 12484, mag 5.21, RA 2.6777h, Dec -54.5499deg) [no display name]
- HIP 12653 / HIP 12653 (HIP 12653, mag 5.40, RA 2.7093h, Dec -50.8003deg) [no display name]
- Beta Horologii / ベータ・とけい (HIP 13884, mag 4.98, RA 2.9793h, Dec -64.0713deg)
- HIP 14240 / HIP 14240 (HIP 14240, mag 5.12, RA 3.0602h, Dec -59.7378deg) [no display name]
- Alpha Horologii / アルファ・とけい (HIP 19747, mag 3.86, RA 4.2334h, Dec -42.2944deg)

## HYA -- Hydra / うみへび座

Counts: stars 17, edges 17, polylines 1, branch points 1, stars without display names 13

### Polylines

1. HIP 43234 -> HIP 43109 -> HIP 42313 -> HIP 42402 -> HIP 42799 -> HIP 43234 -> Zeta Hydrae -> HIP 45336 -> HIP 47431 -> Alphard -> HIP 48356 -> HIP 49841 -> HIP 51069 -> Nu Hydrae -> HIP 56343 -> HIP 57936 -> Gamma Hydrae -> HIP 68895

### Edges

- HIP 43234 -- HIP 43109  |  HIP 43234 -- HIP 43109
- HIP 43109 -- HIP 42313  |  HIP 43109 -- HIP 42313
- HIP 42313 -- HIP 42402  |  HIP 42313 -- HIP 42402
- HIP 42402 -- HIP 42799  |  HIP 42402 -- HIP 42799
- HIP 42799 -- HIP 43234  |  HIP 42799 -- HIP 43234
- HIP 43234 -- Zeta Hydrae  |  HIP 43234 -- ゼータ・うみへび
- Zeta Hydrae -- HIP 45336  |  ゼータ・うみへび -- HIP 45336
- HIP 45336 -- HIP 47431  |  HIP 45336 -- HIP 47431
- HIP 47431 -- Alphard  |  HIP 47431 -- アルファルド
- Alphard -- HIP 48356  |  アルファルド -- HIP 48356
- HIP 48356 -- HIP 49841  |  HIP 48356 -- HIP 49841
- HIP 49841 -- HIP 51069  |  HIP 49841 -- HIP 51069
- HIP 51069 -- Nu Hydrae  |  HIP 51069 -- ニュー・うみへび
- Nu Hydrae -- HIP 56343  |  ニュー・うみへび -- HIP 56343
- HIP 56343 -- HIP 57936  |  HIP 56343 -- HIP 57936
- HIP 57936 -- Gamma Hydrae  |  HIP 57936 -- ガンマ・うみへび
- Gamma Hydrae -- HIP 68895  |  ガンマ・うみへび -- HIP 68895

### Branch Points

- HIP 43234 / HIP 43234 (HIP 43234): degree 3

### Stars

- HIP 42313 / HIP 42313 (HIP 42313, mag 4.14, RA 8.6276h, Dec 5.7038deg) [no display name]
- HIP 42402 / HIP 42402 (HIP 42402, mag 4.45, RA 8.6460h, Dec 3.3414deg) [no display name]
- HIP 42799 / HIP 42799 (HIP 42799, mag 4.30, RA 8.7204h, Dec 3.3987deg) [no display name]
- HIP 43109 / HIP 43109 (HIP 43109, mag 3.38, RA 8.7796h, Dec 6.4188deg) [no display name]
- HIP 43234 / HIP 43234 (HIP 43234, mag 4.35, RA 8.8072h, Dec 5.8378deg) [no display name]
- Zeta Hydrae / ゼータ・うみへび (HIP 43813, mag 3.10, RA 8.9232h, Dec 5.9456deg)
- HIP 45336 / HIP 45336 (HIP 45336, mag 3.89, RA 9.2394h, Dec 2.3143deg) [no display name]
- Alphard / アルファルド (HIP 46390, mag 1.99, RA 9.4598h, Dec -8.6586deg)
- HIP 47431 / HIP 47431 (HIP 47431, mag 3.90, RA 9.6643h, Dec -1.1428deg) [no display name]
- HIP 48356 / HIP 48356 (HIP 48356, mag 4.11, RA 9.8580h, Dec -14.8466deg) [no display name]
- HIP 49841 / HIP 49841 (HIP 49841, mag 3.61, RA 10.1765h, Dec -12.3541deg) [no display name]
- HIP 51069 / HIP 51069 (HIP 51069, mag 3.83, RA 10.4348h, Dec -16.8363deg) [no display name]
- Nu Hydrae / ニュー・うみへび (HIP 52943, mag 3.11, RA 10.8271h, Dec -16.1937deg)
- HIP 56343 / HIP 56343 (HIP 56343, mag 3.54, RA 11.5500h, Dec -31.8576deg) [no display name]
- HIP 57936 / HIP 57936 (HIP 57936, mag 4.29, RA 11.8818h, Dec -33.9081deg) [no display name]
- Gamma Hydrae / ガンマ・うみへび (HIP 64962, mag 2.99, RA 13.3153h, Dec -23.1715deg)
- HIP 68895 / HIP 68895 (HIP 68895, mag 3.25, RA 14.1062h, Dec -26.6824deg) [no display name]

## HYI -- Hydrus / みずへび座

Counts: stars 4, edges 4, polylines 1, branch points 0, stars without display names 1

### Polylines

1. Beta Hydri -> Gamma Hydri -> HIP 11001 -> Alpha Hydri -> Beta Hydri

### Edges

- Beta Hydri -- Alpha Hydri  |  ベータ・みずへび -- アルファ・みずへび
- Beta Hydri -- Gamma Hydri  |  ベータ・みずへび -- ガンマ・みずへび
- Alpha Hydri -- HIP 11001  |  アルファ・みずへび -- HIP 11001
- HIP 11001 -- Gamma Hydri  |  HIP 11001 -- ガンマ・みずへび

### Stars

- Beta Hydri / ベータ・みずへび (HIP 2021, mag 2.80, RA 0.4276h, Dec -77.2542deg)
- Alpha Hydri / アルファ・みずへび (HIP 9236, mag 2.86, RA 1.9795h, Dec -61.5699deg)
- HIP 11001 / HIP 11001 (HIP 11001, mag 4.08, RA 2.3625h, Dec -68.6594deg) [no display name]
- Gamma Hydri / ガンマ・みずへび (HIP 17678, mag 3.26, RA 3.7873h, Dec -74.2390deg)

## IND -- Indus / インディアン座

Counts: stars 5, edges 5, polylines 1, branch points 0, stars without display names 1

### Polylines

1. Beta Indi -> HIP 102333 -> Alpha Indi -> Theta Indi -> Delta Indi -> Beta Indi

### Edges

- Alpha Indi -- HIP 102333  |  アルファ・インディアン -- HIP 102333
- Alpha Indi -- Theta Indi  |  アルファ・インディアン -- シータ・インディアン
- HIP 102333 -- Beta Indi  |  HIP 102333 -- ベータ・インディアン
- Beta Indi -- Delta Indi  |  ベータ・インディアン -- デルタ・インディアン
- Theta Indi -- Delta Indi  |  シータ・インディアン -- デルタ・インディアン

### Stars

- Alpha Indi / アルファ・インディアン (HIP 101772, mag 3.11, RA 20.6261h, Dec -47.2915deg)
- HIP 102333 / HIP 102333 (HIP 102333, mag 4.51, RA 20.7340h, Dec -51.9210deg) [no display name]
- Beta Indi / ベータ・インディアン (HIP 103227, mag 3.67, RA 20.9135h, Dec -58.4541deg)
- Theta Indi / シータ・インディアン (HIP 105319, mag 4.39, RA 21.3311h, Dec -53.4494deg)
- Delta Indi / デルタ・インディアン (HIP 108431, mag 4.40, RA 21.9653h, Dec -54.9926deg)

## LAC -- Lacerta / とかげ座 REVIEW PRIORITY

Counts: stars 9, edges 10, polylines 1, branch points 2, stars without display names 4

### Polylines

1. 5 Lacertae -> Alpha Lacertae -> Beta Lacertae -> HIP 110609 -> 5 Lacertae -> HIP 110351 -> HIP 111104 -> 11 Lacertae -> HIP 111104 -> 11 Lacertae -> 5 Lacertae -> 11 Lacertae -> HIP 111104 -> HIP 109754 -> 1 Lacertae

### Edges

- HIP 109754 -- 1 Lacertae  |  HIP 109754 -- 1・とかげ
- HIP 109754 -- HIP 111104  |  HIP 109754 -- HIP 111104
- HIP 110351 -- 5 Lacertae  |  HIP 110351 -- 5・とかげ
- HIP 110351 -- HIP 111104  |  HIP 110351 -- HIP 111104
- Beta Lacertae -- HIP 110609  |  ベータ・とかげ -- HIP 110609
- Beta Lacertae -- Alpha Lacertae  |  ベータ・とかげ -- アルファ・とかげ
- HIP 110609 -- 5 Lacertae  |  HIP 110609 -- 5・とかげ
- 5 Lacertae -- Alpha Lacertae  |  5・とかげ -- アルファ・とかげ
- 5 Lacertae -- 11 Lacertae  |  5・とかげ -- 11・とかげ
- HIP 111104 -- 11 Lacertae  |  HIP 111104 -- 11・とかげ

### Branch Points

- 5 Lacertae / 5・とかげ (HIP 111022): degree 4
- HIP 111104 / HIP 111104 (HIP 111104): degree 3

### Stars

- HIP 109754 / HIP 109754 (HIP 109754, mag 4.50, RA 22.2313h, Dec 39.7149deg) [no display name]
- 1 Lacertae / 1・とかげ (HIP 109937, mag 4.14, RA 22.2662h, Dec 37.7487deg)
- HIP 110351 / HIP 110351 (HIP 110351, mag 4.55, RA 22.3504h, Dec 46.5366deg) [no display name]
- Beta Lacertae / ベータ・とかげ (HIP 110538, mag 4.42, RA 22.3927h, Dec 52.2290deg)
- HIP 110609 / HIP 110609 (HIP 110609, mag 4.55, RA 22.4086h, Dec 49.4764deg) [no display name]
- 5 Lacertae / 5・とかげ (HIP 111022, mag 4.34, RA 22.4922h, Dec 47.7069deg)
- HIP 111104 / HIP 111104 (HIP 111104, mag 4.52, RA 22.5081h, Dec 43.1234deg) [no display name]
- Alpha Lacertae / アルファ・とかげ (HIP 111169, mag 3.76, RA 22.5215h, Dec 50.2825deg)
- 11 Lacertae / 11・とかげ (HIP 111944, mag 4.50, RA 22.6752h, Dec 44.2763deg)

## LEO -- Leo / しし座

Counts: stars 12, edges 12, polylines 1, branch points 3, stars without display names 3

### Polylines

1. Epsilon Leonis -> Mu Leonis -> Zeta Leonis -> Algieba -> Eta Leonis -> Regulus -> HIP 47508 -> Regulus -> Chertan -> HIP 55642 -> HIP 55434 -> HIP 55642 -> Chertan -> Denebola -> Zosma -> Algieba

### Edges

- Epsilon Leonis -- Mu Leonis  |  イプシロン・しし -- ミュー・しし
- Mu Leonis -- Zeta Leonis  |  ミュー・しし -- ゼータ・しし
- Zeta Leonis -- Algieba  |  ゼータ・しし -- アルギエバ
- Algieba -- Eta Leonis  |  アルギエバ -- エータ・しし
- Eta Leonis -- Regulus  |  エータ・しし -- レグルス
- Regulus -- HIP 47508  |  レグルス -- HIP 47508
- Regulus -- Chertan  |  レグルス -- チェルタン
- Chertan -- HIP 55642  |  チェルタン -- HIP 55642
- HIP 55642 -- HIP 55434  |  HIP 55642 -- HIP 55434
- Chertan -- Denebola  |  チェルタン -- デネボラ
- Denebola -- Zosma  |  デネボラ -- ゾスマ
- Zosma -- Algieba  |  ゾスマ -- アルギエバ

### Branch Points

- Regulus / レグルス (HIP 49669): degree 3
- Algieba / アルギエバ (HIP 50583): degree 3
- Chertan / チェルタン (HIP 54879): degree 3

### Stars

- HIP 47508 / HIP 47508 (HIP 47508, mag 3.52, RA 9.6858h, Dec 9.8923deg) [no display name]
- Epsilon Leonis / イプシロン・しし (HIP 47908, mag 2.98, RA 9.7642h, Dec 23.7743deg)
- Mu Leonis / ミュー・しし (HIP 48455, mag 3.88, RA 9.8794h, Dec 26.0069deg)
- Eta Leonis / エータ・しし (HIP 49583, mag 3.52, RA 10.1222h, Dec 16.7627deg)
- Regulus / レグルス (HIP 49669, mag 1.35, RA 10.1395h, Dec 11.9672deg)
- Zeta Leonis / ゼータ・しし (HIP 50335, mag 3.44, RA 10.2782h, Dec 23.4173deg)
- Algieba / アルギエバ (HIP 50583, mag 2.28, RA 10.3330h, Dec 19.8415deg)
- Zosma / ゾスマ (HIP 54872, mag 2.56, RA 11.2351h, Dec 20.5237deg)
- Chertan / チェルタン (HIP 54879, mag 3.33, RA 11.2373h, Dec 15.4296deg)
- HIP 55434 / HIP 55434 (HIP 55434, mag 4.05, RA 11.3523h, Dec 6.0293deg) [no display name]
- HIP 55642 / HIP 55642 (HIP 55642, mag 4.00, RA 11.3987h, Dec 10.5295deg) [no display name]
- Denebola / デネボラ (HIP 57632, mag 2.14, RA 11.8177h, Dec 14.5721deg)

## LMI -- Leo Minor / こじし座

Counts: stars 5, edges 5, polylines 1, branch points 1, stars without display names 2

### Polylines

1. HIP 46952 -> 21 Leonis Minoris -> Beta Leonis Minoris -> Praecipua -> HIP 51056 -> 21 Leonis Minoris

### Edges

- HIP 46952 -- 21 Leonis Minoris  |  HIP 46952 -- 21・こじし
- 21 Leonis Minoris -- HIP 51056  |  21・こじし -- HIP 51056
- 21 Leonis Minoris -- Beta Leonis Minoris  |  21・こじし -- ベータ・こじし
- HIP 51056 -- Praecipua  |  HIP 51056 -- プレキプア
- Beta Leonis Minoris -- Praecipua  |  ベータ・こじし -- プレキプア

### Branch Points

- 21 Leonis Minoris / 21・こじし (HIP 49593): degree 3

### Stars

- HIP 46952 / HIP 46952 (HIP 46952, mag 4.54, RA 9.5704h, Dec 36.3976deg) [no display name]
- 21 Leonis Minoris / 21・こじし (HIP 49593, mag 4.48, RA 10.1238h, Dec 35.2447deg)
- HIP 51056 / HIP 51056 (HIP 51056, mag 4.72, RA 10.4319h, Dec 33.7961deg) [no display name]
- Beta Leonis Minoris / ベータ・こじし (HIP 51233, mag 4.21, RA 10.4647h, Dec 36.7072deg)
- Praecipua / プレキプア (HIP 53229, mag 3.83, RA 10.8885h, Dec 34.2149deg)

## LEP -- Lepus / うさぎ座

Counts: stars 11, edges 12, polylines 3, branch points 3, stars without display names 4

### Polylines

1. Epsilon Leporis -> Mu Leporis -> Arneb -> Nihal -> Epsilon Leporis
2. HIP 24845 -> Mu Leporis -> HIP 24327
3. Nihal -> Gamma Leporis -> Delta Leporis -> HIP 28910 -> HIP 28103 -> Zeta Leporis -> Arneb

### Edges

- Epsilon Leporis -- Mu Leporis  |  イプシロン・うさぎ -- ミュー・うさぎ
- Epsilon Leporis -- Nihal  |  イプシロン・うさぎ -- ニハル
- Mu Leporis -- HIP 24327  |  ミュー・うさぎ -- HIP 24327
- Mu Leporis -- HIP 24845  |  ミュー・うさぎ -- HIP 24845
- Mu Leporis -- Arneb  |  ミュー・うさぎ -- アルネブ
- Nihal -- Arneb  |  ニハル -- アルネブ
- Nihal -- Gamma Leporis  |  ニハル -- ガンマ・うさぎ
- Arneb -- Zeta Leporis  |  アルネブ -- ゼータ・うさぎ
- Gamma Leporis -- Delta Leporis  |  ガンマ・うさぎ -- デルタ・うさぎ
- Zeta Leporis -- HIP 28103  |  ゼータ・うさぎ -- HIP 28103
- Delta Leporis -- HIP 28910  |  デルタ・うさぎ -- HIP 28910
- HIP 28103 -- HIP 28910  |  HIP 28103 -- HIP 28910

### Branch Points

- Mu Leporis / ミュー・うさぎ (HIP 24305): degree 4
- Nihal / ニハル (HIP 25606): degree 3
- Arneb / アルネブ (HIP 25985): degree 3

### Stars

- Epsilon Leporis / イプシロン・うさぎ (HIP 23685, mag 3.19, RA 5.0910h, Dec -22.3710deg)
- Mu Leporis / ミュー・うさぎ (HIP 24305, mag 3.29, RA 5.2155h, Dec -16.2055deg)
- HIP 24327 / HIP 24327 (HIP 24327, mag 4.36, RA 5.2205h, Dec -12.9413deg) [no display name]
- HIP 24845 / HIP 24845 (HIP 24845, mag 4.29, RA 5.3263h, Dec -13.1768deg) [no display name]
- Nihal / ニハル (HIP 25606, mag 2.81, RA 5.4708h, Dec -20.7594deg)
- Arneb / アルネブ (HIP 25985, mag 2.58, RA 5.5455h, Dec -17.8223deg)
- Gamma Leporis / ガンマ・うさぎ (HIP 27072, mag 3.59, RA 5.7411h, Dec -22.4484deg)
- Zeta Leporis / ゼータ・うさぎ (HIP 27288, mag 3.55, RA 5.7826h, Dec -14.8219deg)
- Delta Leporis / デルタ・うさぎ (HIP 27654, mag 3.76, RA 5.8554h, Dec -20.8791deg)
- HIP 28103 / HIP 28103 (HIP 28103, mag 3.71, RA 5.9401h, Dec -14.1677deg) [no display name]
- HIP 28910 / HIP 28910 (HIP 28910, mag 4.67, RA 6.1026h, Dec -14.9353deg) [no display name]

## LIB -- Libra / てんびん座

Counts: stars 6, edges 6, polylines 3, branch points 2, stars without display names 3

### Polylines

1. Zubenelgenubi -> Zubeneschamali
2. Zubenelgenubi -> Brachium
3. Zubeneschamali -> HIP 76333 -> Zubenelgenubi -> HIP 76333 -> HIP 76470 -> HIP 76600

### Edges

- Zubenelgenubi -- Brachium  |  ズベンエルゲヌビ -- ブラキウム
- Zubenelgenubi -- Zubeneschamali  |  ズベンエルゲヌビ -- ズベンエスカマリ
- Zubenelgenubi -- HIP 76333  |  ズベンエルゲヌビ -- HIP 76333
- Zubeneschamali -- HIP 76333  |  ズベンエスカマリ -- HIP 76333
- HIP 76333 -- HIP 76470  |  HIP 76333 -- HIP 76470
- HIP 76470 -- HIP 76600  |  HIP 76470 -- HIP 76600

### Branch Points

- Zubenelgenubi / ズベンエルゲヌビ (HIP 72622): degree 3
- HIP 76333 / HIP 76333 (HIP 76333): degree 3

### Stars

- Zubenelgenubi / ズベンエルゲヌビ (HIP 72622, mag 2.75, RA 14.8479h, Dec -16.0418deg)
- Brachium / ブラキウム (HIP 73714, mag 3.25, RA 15.0678h, Dec -25.2819deg)
- Zubeneschamali / ズベンエスカマリ (HIP 74785, mag 2.61, RA 15.2834h, Dec -9.3831deg)
- HIP 76333 / HIP 76333 (HIP 76333, mag 3.91, RA 15.5921h, Dec -14.7895deg) [no display name]
- HIP 76470 / HIP 76470 (HIP 76470, mag 3.60, RA 15.6171h, Dec -28.1351deg) [no display name]
- HIP 76600 / HIP 76600 (HIP 76600, mag 3.66, RA 15.6443h, Dec -29.7778deg) [no display name]

## LUP -- Lupus / おおかみ座 REVIEW PRIORITY

Counts: stars 9, edges 10, polylines 1, branch points 3, stars without display names 4

### Polylines

1. Men -> HIP 74395 -> HIP 75264 -> Gamma Lupi -> Delta Lupi -> Beta Lupi -> Delta Lupi -> Gamma Lupi -> HIP 78384 -> Upsilon Librae -> HIP 77634 -> HIP 78384 -> HIP 74395

### Edges

- Men -- HIP 74395  |  メン -- HIP 74395
- Beta Lupi -- Delta Lupi  |  ベータ・おおかみ -- デルタ・おおかみ
- HIP 74395 -- HIP 75264  |  HIP 74395 -- HIP 75264
- HIP 74395 -- HIP 78384  |  HIP 74395 -- HIP 78384
- Delta Lupi -- Gamma Lupi  |  デルタ・おおかみ -- ガンマ・おおかみ
- Upsilon Librae -- HIP 77634  |  ウプシロン・てんびん -- HIP 77634
- Upsilon Librae -- HIP 78384  |  ウプシロン・てんびん -- HIP 78384
- HIP 75264 -- Gamma Lupi  |  HIP 75264 -- ガンマ・おおかみ
- Gamma Lupi -- HIP 78384  |  ガンマ・おおかみ -- HIP 78384
- HIP 77634 -- HIP 78384  |  HIP 77634 -- HIP 78384

### Branch Points

- HIP 74395 / HIP 74395 (HIP 74395): degree 3
- Gamma Lupi / ガンマ・おおかみ (HIP 76297): degree 3
- HIP 78384 / HIP 78384 (HIP 78384): degree 4

### Stars

- Men / メン (HIP 71860, mag 2.30, RA 14.6988h, Dec -47.3882deg)
- Beta Lupi / ベータ・おおかみ (HIP 73273, mag 2.68, RA 14.9755h, Dec -43.1339deg)
- HIP 74395 / HIP 74395 (HIP 74395, mag 3.41, RA 15.2048h, Dec -52.0992deg) [no display name]
- Delta Lupi / デルタ・おおかみ (HIP 75141, mag 3.22, RA 15.3027h, Dec -40.6475deg)
- Upsilon Librae / ウプシロン・てんびん (HIP 75177, mag 3.60, RA 15.3089h, Dec -28.1351deg)
- HIP 75264 / HIP 75264 (HIP 75264, mag 3.37, RA 15.3780h, Dec -44.6896deg) [no display name]
- Gamma Lupi / ガンマ・おおかみ (HIP 76297, mag 2.78, RA 15.5857h, Dec -41.1668deg)
- HIP 77634 / HIP 77634 (HIP 77634, mag 3.97, RA 15.8493h, Dec -33.6272deg) [no display name]
- HIP 78384 / HIP 78384 (HIP 78384, mag 3.42, RA 16.0020h, Dec -38.3967deg) [no display name]

## LYN -- Lynx / やまねこ座

Counts: stars 8, edges 7, polylines 1, branch points 0, stars without display names 3

### Polylines

1. Alpha Lyncis -> 38 Lyncis -> HIP 44700 -> HIP 44248 -> Alsciaukat -> 21 Lyncis -> 15 Lyncis -> HIP 30060

### Edges

- Alpha Lyncis -- 38 Lyncis  |  アルファ・やまねこ -- 38・やまねこ
- 38 Lyncis -- HIP 44700  |  38・やまねこ -- HIP 44700
- HIP 44700 -- HIP 44248  |  HIP 44700 -- HIP 44248
- HIP 44248 -- Alsciaukat  |  HIP 44248 -- アルシアウカト
- Alsciaukat -- 21 Lyncis  |  アルシアウカト -- 21・やまねこ
- 21 Lyncis -- 15 Lyncis  |  21・やまねこ -- 15・やまねこ
- 15 Lyncis -- HIP 30060  |  15・やまねこ -- HIP 30060

### Stars

- HIP 30060 / HIP 30060 (HIP 30060, mag 4.44, RA 6.3271h, Dec 59.0110deg) [no display name]
- 15 Lyncis / 15・やまねこ (HIP 33449, mag 4.35, RA 6.9546h, Dec 58.4228deg)
- 21 Lyncis / 21・やまねこ (HIP 36145, mag 4.61, RA 7.4452h, Dec 49.2115deg)
- Alsciaukat / アルシアウカト (HIP 41075, mag 4.25, RA 8.3806h, Dec 43.1881deg)
- HIP 44248 / HIP 44248 (HIP 44248, mag 3.96, RA 9.0107h, Dec 41.7829deg) [no display name]
- HIP 44700 / HIP 44700 (HIP 44700, mag 4.56, RA 9.1088h, Dec 38.4522deg) [no display name]
- 38 Lyncis / 38・やまねこ (HIP 45688, mag 3.82, RA 9.3141h, Dec 36.8026deg)
- Alpha Lyncis / アルファ・やまねこ (HIP 45860, mag 3.14, RA 9.3509h, Dec 34.3926deg)

## LYR -- Lyra / こと座

Counts: stars 5, edges 5, polylines 1, branch points 1, stars without display names 1

### Polylines

1. Vega -> HIP 91971 -> Sheliak -> Sulafat -> Delta Lyrae -> HIP 91971

### Edges

- Vega -- HIP 91971  |  ベガ -- HIP 91971
- HIP 91971 -- Sheliak  |  HIP 91971 -- シェリアク
- Sheliak -- Sulafat  |  シェリアク -- スラファト
- Sulafat -- Delta Lyrae  |  スラファト -- デルタ・リラ
- Delta Lyrae -- HIP 91971  |  デルタ・リラ -- HIP 91971

### Branch Points

- HIP 91971 / HIP 91971 (HIP 91971): degree 3

### Stars

- Vega / ベガ (HIP 91262, mag 0.03, RA 18.6156h, Dec 38.7837deg)
- HIP 91971 / HIP 91971 (HIP 91971, mag 4.34, RA 18.7462h, Dec 37.6051deg) [no display name]
- Sheliak / シェリアク (HIP 92420, mag 3.52, RA 18.8347h, Dec 33.3627deg)
- Delta Lyrae / デルタ・リラ (HIP 92791, mag 4.30, RA 18.9084h, Dec 36.8986deg)
- Sulafat / スラファト (HIP 93194, mag 3.24, RA 18.9824h, Dec 32.6896deg)

## MEN -- Mensa / テーブルさん座

Counts: stars 2, edges 1, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Alpha Mensae -> Beta Mensae

### Edges

- Beta Mensae -- Alpha Mensae  |  ベータ・テーブルさん -- アルファ・テーブルさん

### Stars

- Beta Mensae / ベータ・テーブルさん (HIP 23467, mag 5.31, RA 5.0453h, Dec -71.3143deg)
- Alpha Mensae / アルファ・テーブルさん (HIP 29271, mag 5.09, RA 6.1707h, Dec -74.7530deg)

## MIC -- Microscopium / けんびきょう座

Counts: stars 2, edges 1, polylines 1, branch points 0, stars without display names 1

### Polylines

1. Alpha Microscopii -> HIP 102989

### Edges

- Alpha Microscopii -- HIP 102989  |  アルファ・けんびきょう -- HIP 102989

### Stars

- Alpha Microscopii / アルファ・けんびきょう (HIP 102831, mag 4.88, RA 20.8328h, Dec -33.7797deg)
- HIP 102989 / HIP 102989 (HIP 102989, mag 6.06, RA 20.8663h, Dec -33.1780deg) [no display name]

## MON -- Monoceros / いっかくじゅう座

Counts: stars 9, edges 9, polylines 1, branch points 3, stars without display names 6

### Polylines

1. HIP 31978 -> HIP 31216 -> Epsilon Monocerotis -> Epsilon Monocerotis -> HIP 32578 -> HIP 31216 -> HIP 32578 -> Delta Monocerotis -> Beta Monocerotis -> HIP 29651 -> Beta Monocerotis -> Delta Monocerotis -> HIP 39863 -> HIP 37447

### Edges

- HIP 29651 -- Beta Monocerotis  |  HIP 29651 -- ベータ・いっかくじゅう
- Epsilon Monocerotis -- HIP 31216  |  イプシロン・いっかくじゅう -- HIP 31216
- Epsilon Monocerotis -- HIP 32578  |  イプシロン・いっかくじゅう -- HIP 32578
- Beta Monocerotis -- Delta Monocerotis  |  ベータ・いっかくじゅう -- デルタ・いっかくじゅう
- HIP 31216 -- HIP 31978  |  HIP 31216 -- HIP 31978
- HIP 31216 -- HIP 32578  |  HIP 31216 -- HIP 32578
- HIP 32578 -- Delta Monocerotis  |  HIP 32578 -- デルタ・いっかくじゅう
- Delta Monocerotis -- HIP 39863  |  デルタ・いっかくじゅう -- HIP 39863
- HIP 37447 -- HIP 39863  |  HIP 37447 -- HIP 39863

### Branch Points

- HIP 31216 / HIP 31216 (HIP 31216): degree 3
- HIP 32578 / HIP 32578 (HIP 32578): degree 3
- Delta Monocerotis / デルタ・いっかくじゅう (HIP 34769): degree 3

### Stars

- HIP 29651 / HIP 29651 (HIP 29651, mag 3.99, RA 6.2476h, Dec -6.2748deg) [no display name]
- Epsilon Monocerotis / イプシロン・いっかくじゅう (HIP 30419, mag 4.39, RA 6.3961h, Dec 4.5929deg)
- Beta Monocerotis / ベータ・いっかくじゅう (HIP 30867, mag 3.76, RA 6.4803h, Dec -7.0329deg)
- HIP 31216 / HIP 31216 (HIP 31216, mag 4.47, RA 6.5484h, Dec 7.3330deg) [no display name]
- HIP 31978 / HIP 31978 (HIP 31978, mag 4.66, RA 6.6830h, Dec 9.8958deg) [no display name]
- HIP 32578 / HIP 32578 (HIP 32578, mag 4.48, RA 6.7977h, Dec 2.4122deg) [no display name]
- Delta Monocerotis / デルタ・いっかくじゅう (HIP 34769, mag 4.15, RA 7.1977h, Dec -0.4928deg)
- HIP 37447 / HIP 37447 (HIP 37447, mag 3.94, RA 7.6875h, Dec -9.5511deg) [no display name]
- HIP 39863 / HIP 39863 (HIP 39863, mag 4.36, RA 8.1432h, Dec -2.9838deg) [no display name]

## MUS -- Musca / はえ座

Counts: stars 6, edges 6, polylines 1, branch points 1, stars without display names 2

### Polylines

1. HIP 57363 -> HIP 59929 -> Alpha Muscae -> Beta Muscae -> Delta Muscae -> Gamma Muscae -> Alpha Muscae

### Edges

- HIP 57363 -- HIP 59929  |  HIP 57363 -- HIP 59929
- HIP 59929 -- Alpha Muscae  |  HIP 59929 -- アルファ・はえ
- Gamma Muscae -- Alpha Muscae  |  ガンマ・はえ -- アルファ・はえ
- Gamma Muscae -- Delta Muscae  |  ガンマ・はえ -- デルタ・はえ
- Alpha Muscae -- Beta Muscae  |  アルファ・はえ -- ベータ・はえ
- Beta Muscae -- Delta Muscae  |  ベータ・はえ -- デルタ・はえ

### Branch Points

- Alpha Muscae / アルファ・はえ (HIP 61585): degree 3

### Stars

- HIP 57363 / HIP 57363 (HIP 57363, mag 3.63, RA 11.7601h, Dec -66.7288deg) [no display name]
- HIP 59929 / HIP 59929 (HIP 59929, mag 4.06, RA 12.2929h, Dec -67.9607deg) [no display name]
- Gamma Muscae / ガンマ・はえ (HIP 61199, mag 3.84, RA 12.5411h, Dec -72.1329deg)
- Alpha Muscae / アルファ・はえ (HIP 61585, mag 2.69, RA 12.6197h, Dec -69.1355deg)
- Beta Muscae / ベータ・はえ (HIP 62322, mag 3.04, RA 12.7714h, Dec -68.1081deg)
- Delta Muscae / デルタ・はえ (HIP 63613, mag 3.61, RA 13.0378h, Dec -71.5489deg)

## NOR -- Norma / じょうぎ座

Counts: stars 4, edges 4, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Eta Normae -> Gamma2 Normae -> Epsilon Normae -> Delta Normae -> Eta Normae

### Edges

- Eta Normae -- Delta Normae  |  イータ・じょうぎ -- デルタ・じょうぎ
- Eta Normae -- Gamma2 Normae  |  イータ・じょうぎ -- ガンマ2・じょうぎ
- Delta Normae -- Epsilon Normae  |  デルタ・じょうぎ -- イプシロン・じょうぎ
- Gamma2 Normae -- Epsilon Normae  |  ガンマ2・じょうぎ -- イプシロン・じょうぎ

### Stars

- Eta Normae / イータ・じょうぎ (HIP 78639, mag 4.65, RA 16.0536h, Dec -49.2297deg)
- Delta Normae / デルタ・じょうぎ (HIP 78914, mag 4.73, RA 16.1082h, Dec -45.1733deg)
- Gamma2 Normae / ガンマ2・じょうぎ (HIP 80000, mag 4.02, RA 16.3307h, Dec -50.1554deg)
- Epsilon Normae / イプシロン・じょうぎ (HIP 80582, mag 4.47, RA 16.4531h, Dec -47.5547deg)

## OCT -- Octans / はちぶんぎ座

Counts: stars 3, edges 3, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Beta Octantis -> Delta Octantis -> Nu Octantis -> Beta Octantis

### Edges

- Beta Octantis -- Delta Octantis  |  ベータ・はちぶんぎ -- デルタ・はちぶんぎ
- Delta Octantis -- Nu Octantis  |  デルタ・はちぶんぎ -- ニュー・はちぶんぎ
- Nu Octantis -- Beta Octantis  |  ニュー・はちぶんぎ -- ベータ・はちぶんぎ

### Stars

- Delta Octantis / デルタ・はちぶんぎ (HIP 70638, mag 4.32, RA 14.4489h, Dec -83.6679deg)
- Nu Octantis / ニュー・はちぶんぎ (HIP 107089, mag 3.76, RA 21.6913h, Dec -77.3895deg)
- Beta Octantis / ベータ・はちぶんぎ (HIP 112405, mag 4.13, RA 22.7677h, Dec -81.3816deg)

## OPH -- Ophiuchus / へびつかい座

Counts: stars 11, edges 12, polylines 1, branch points 3, stars without display names 7

### Polylines

1. Rasalhague -> HIP 83000 -> HIP 80883 -> Yed Prior -> HIP 79882 -> HIP 80628 -> HIP 81377 -> HIP 80628 -> HIP 79882 -> Yed Prior -> HIP 80883 -> HIP 83000 -> HIP 81377 -> Sabik -> Cebalrai -> HIP 87108 -> HIP 88048 -> HIP 87108 -> Cebalrai -> Rasalhague

### Edges

- Yed Prior -- HIP 79882  |  イェド・プリオル -- HIP 79882
- Yed Prior -- HIP 80883  |  イェド・プリオル -- HIP 80883
- HIP 79882 -- HIP 80628  |  HIP 79882 -- HIP 80628
- HIP 80628 -- HIP 81377  |  HIP 80628 -- HIP 81377
- HIP 80883 -- HIP 83000  |  HIP 80883 -- HIP 83000
- HIP 81377 -- HIP 83000  |  HIP 81377 -- HIP 83000
- HIP 81377 -- Sabik  |  HIP 81377 -- サビク
- HIP 83000 -- Rasalhague  |  HIP 83000 -- ラスアルハゲ
- Sabik -- Cebalrai  |  サビク -- ケバルライ
- Rasalhague -- Cebalrai  |  ラスアルハゲ -- ケバルライ
- Cebalrai -- HIP 87108  |  ケバルライ -- HIP 87108
- HIP 87108 -- HIP 88048  |  HIP 87108 -- HIP 88048

### Branch Points

- HIP 81377 / HIP 81377 (HIP 81377): degree 3
- HIP 83000 / HIP 83000 (HIP 83000): degree 3
- Cebalrai / ケバルライ (HIP 86742): degree 3

### Stars

- Yed Prior / イェド・プリオル (HIP 79593, mag 2.73, RA 16.2391h, Dec -3.6943deg)
- HIP 79882 / HIP 79882 (HIP 79882, mag 3.23, RA 16.3054h, Dec -4.6925deg) [no display name]
- HIP 80628 / HIP 80628 (HIP 80628, mag 4.62, RA 16.4634h, Dec -8.3717deg) [no display name]
- HIP 80883 / HIP 80883 (HIP 80883, mag 3.82, RA 16.5152h, Dec 1.9839deg) [no display name]
- HIP 81377 / HIP 81377 (HIP 81377, mag 2.54, RA 16.6193h, Dec -10.5671deg) [no display name]
- HIP 83000 / HIP 83000 (HIP 83000, mag 3.19, RA 16.9611h, Dec 9.3750deg) [no display name]
- Sabik / サビク (HIP 84012, mag 2.43, RA 17.1729h, Dec -15.7249deg)
- Rasalhague / ラスアルハゲ (HIP 86032, mag 2.08, RA 17.5822h, Dec 12.5600deg)
- Cebalrai / ケバルライ (HIP 86742, mag 2.76, RA 17.7245h, Dec 4.5673deg)
- HIP 87108 / HIP 87108 (HIP 87108, mag 3.75, RA 17.7982h, Dec 2.7073deg) [no display name]
- HIP 88048 / HIP 88048 (HIP 88048, mag 3.32, RA 17.9838h, Dec -9.7736deg) [no display name]

## ORI -- Orion / オリオン座

Counts: stars 22, edges 23, polylines 5, branch points 5, stars without display names 14

### Polylines

1. Betelgeuse -> Alnitak -> Saiph -> Alnitak -> Alnilam -> Mintaka -> Bellatrix -> Mintaka -> HIP 25281 -> Rigel
2. Betelgeuse -> Bellatrix -> Meissa -> Meissa -> Betelgeuse
3. HIP 23607 -> HIP 22957 -> HIP 22845 -> HIP 22509 -> HIP 22449 -> Bellatrix -> HIP 22449 -> HIP 22549 -> HIP 22797 -> HIP 23123
4. Betelgeuse -> HIP 28614 -> HIP 29038
5. HIP 29426 -> HIP 28716 -> HIP 27913 -> HIP 29038

### Edges

- HIP 22449 -- HIP 22509  |  HIP 22449 -- HIP 22509
- HIP 22449 -- HIP 22549  |  HIP 22449 -- HIP 22549
- HIP 22449 -- Bellatrix  |  HIP 22449 -- ベラトリックス
- HIP 22509 -- HIP 22845  |  HIP 22509 -- HIP 22845
- HIP 22549 -- HIP 22797  |  HIP 22549 -- HIP 22797
- HIP 22797 -- HIP 23123  |  HIP 22797 -- HIP 23123
- HIP 22845 -- HIP 22957  |  HIP 22845 -- HIP 22957
- HIP 22957 -- HIP 23607  |  HIP 22957 -- HIP 23607
- Rigel -- HIP 25281  |  リゲル -- HIP 25281
- HIP 25281 -- Mintaka  |  HIP 25281 -- ミンタカ
- Bellatrix -- Mintaka  |  ベラトリックス -- ミンタカ
- Bellatrix -- Meissa  |  ベラトリックス -- メイサ
- Bellatrix -- Betelgeuse  |  ベラトリックス -- ベテルギウス
- Mintaka -- Alnilam  |  ミンタカ -- アルニラム
- Meissa -- Betelgeuse  |  メイサ -- ベテルギウス
- Alnilam -- Alnitak  |  アルニラム -- アルニタク
- Alnitak -- Saiph  |  アルニタク -- サイフ
- Alnitak -- Betelgeuse  |  アルニタク -- ベテルギウス
- HIP 27913 -- HIP 28716  |  HIP 27913 -- HIP 28716
- HIP 27913 -- HIP 29038  |  HIP 27913 -- HIP 29038
- Betelgeuse -- HIP 28614  |  ベテルギウス -- HIP 28614
- HIP 28614 -- HIP 29038  |  HIP 28614 -- HIP 29038
- HIP 28716 -- HIP 29426  |  HIP 28716 -- HIP 29426

### Branch Points

- HIP 22449 / HIP 22449 (HIP 22449): degree 3
- Bellatrix / ベラトリックス (HIP 25336): degree 4
- Mintaka / ミンタカ (HIP 25930): degree 3
- Alnitak / アルニタク (HIP 26727): degree 3
- Betelgeuse / ベテルギウス (HIP 27989): degree 4

### Stars

- HIP 22449 / HIP 22449 (HIP 22449, mag 3.19, RA 4.8307h, Dec 6.9613deg) [no display name]
- HIP 22509 / HIP 22509 (HIP 22509, mag 4.35, RA 4.8435h, Dec 8.9002deg) [no display name]
- HIP 22549 / HIP 22549 (HIP 22549, mag 3.68, RA 4.8534h, Dec 5.6051deg) [no display name]
- HIP 22797 / HIP 22797 (HIP 22797, mag 3.71, RA 4.9042h, Dec 2.4407deg) [no display name]
- HIP 22845 / HIP 22845 (HIP 22845, mag 4.64, RA 4.9149h, Dec 10.1508deg) [no display name]
- HIP 22957 / HIP 22957 (HIP 22957, mag 4.06, RA 4.9395h, Dec 13.5145deg) [no display name]
- HIP 23123 / HIP 23123 (HIP 23123, mag 4.47, RA 4.9758h, Dec 1.7140deg) [no display name]
- HIP 23607 / HIP 23607 (HIP 23607, mag 4.65, RA 5.0762h, Dec 15.4041deg) [no display name]
- Rigel / リゲル (HIP 24436, mag 0.13, RA 5.2423h, Dec -8.2016deg)
- HIP 25281 / HIP 25281 (HIP 25281, mag 3.35, RA 5.4079h, Dec -2.3971deg) [no display name]
- Bellatrix / ベラトリックス (HIP 25336, mag 1.64, RA 5.4188h, Dec 6.3497deg)
- Mintaka / ミンタカ (HIP 25930, mag 2.23, RA 5.5334h, Dec -0.2991deg)
- Meissa / メイサ (HIP 26207, mag 3.39, RA 5.5856h, Dec 9.9342deg)
- Alnilam / アルニラム (HIP 26311, mag 1.69, RA 5.6036h, Dec -1.2019deg)
- Alnitak / アルニタク (HIP 26727, mag 1.74, RA 5.6793h, Dec -1.9426deg)
- Saiph / サイフ (HIP 27366, mag 2.06, RA 5.7959h, Dec -9.6696deg)
- HIP 27913 / HIP 27913 (HIP 27913, mag 4.39, RA 5.9064h, Dec 20.2762deg) [no display name]
- Betelgeuse / ベテルギウス (HIP 27989, mag 0.50, RA 5.9195h, Dec 7.4071deg)
- HIP 28614 / HIP 28614 (HIP 28614, mag 4.12, RA 6.0397h, Dec 9.6473deg) [no display name]
- HIP 28716 / HIP 28716 (HIP 28716, mag 4.64, RA 6.0653h, Dec 20.1385deg) [no display name]
- HIP 29038 / HIP 29038 (HIP 29038, mag 4.42, RA 6.1262h, Dec 14.7685deg) [no display name]
- HIP 29426 / HIP 29426 (HIP 29426, mag 4.45, RA 6.1990h, Dec 14.2088deg) [no display name]

## PAV -- Pavo / くじゃく座

Counts: stars 11, edges 12, polylines 3, branch points 2, stars without display names 6

### Polylines

1. Peacock -> Delta Pavonis -> Beta Pavonis
2. Peacock -> Gamma Pavonis -> Beta Pavonis
3. HIP 91792 -> Delta Pavonis -> HIP 98495 -> Delta Pavonis -> HIP 93015 -> HIP 88866 -> Eta Pavonis -> HIP 88866 -> HIP 90098 -> HIP 92609 -> Delta Pavonis

### Edges

- Eta Pavonis -- HIP 88866  |  イータ・くじゃく -- HIP 88866
- HIP 88866 -- HIP 90098  |  HIP 88866 -- HIP 90098
- HIP 88866 -- HIP 93015  |  HIP 88866 -- HIP 93015
- HIP 90098 -- HIP 92609  |  HIP 90098 -- HIP 92609
- HIP 91792 -- Delta Pavonis  |  HIP 91792 -- デルタ・くじゃく
- HIP 92609 -- Delta Pavonis  |  HIP 92609 -- デルタ・くじゃく
- HIP 93015 -- Delta Pavonis  |  HIP 93015 -- デルタ・くじゃく
- HIP 98495 -- Delta Pavonis  |  HIP 98495 -- デルタ・くじゃく
- Delta Pavonis -- Peacock  |  デルタ・くじゃく -- ピーコック
- Delta Pavonis -- Beta Pavonis  |  デルタ・くじゃく -- ベータ・くじゃく
- Peacock -- Gamma Pavonis  |  ピーコック -- ガンマ・くじゃく
- Beta Pavonis -- Gamma Pavonis  |  ベータ・くじゃく -- ガンマ・くじゃく

### Branch Points

- HIP 88866 / HIP 88866 (HIP 88866): degree 3
- Delta Pavonis / デルタ・くじゃく (HIP 99240): degree 6

### Stars

- Eta Pavonis / イータ・くじゃく (HIP 86929, mag 3.61, RA 17.7622h, Dec -64.7239deg)
- HIP 88866 / HIP 88866 (HIP 88866, mag 4.33, RA 18.1430h, Dec -63.6686deg) [no display name]
- HIP 90098 / HIP 90098 (HIP 90098, mag 4.35, RA 18.3871h, Dec -61.4939deg) [no display name]
- HIP 91792 / HIP 91792 (HIP 91792, mag 4.01, RA 18.7173h, Dec -71.4281deg) [no display name]
- HIP 92609 / HIP 92609 (HIP 92609, mag 4.22, RA 18.8703h, Dec -62.1876deg) [no display name]
- HIP 93015 / HIP 93015 (HIP 93015, mag 4.40, RA 18.9492h, Dec -67.2335deg) [no display name]
- HIP 98495 / HIP 98495 (HIP 98495, mag 3.97, RA 20.0098h, Dec -72.9105deg) [no display name]
- Delta Pavonis / デルタ・くじゃく (HIP 99240, mag 3.55, RA 20.1452h, Dec -66.1821deg)
- Peacock / ピーコック (HIP 100751, mag 1.94, RA 20.4275h, Dec -56.7351deg)
- Beta Pavonis / ベータ・くじゃく (HIP 102395, mag 3.42, RA 20.7493h, Dec -66.2032deg)
- Gamma Pavonis / ガンマ・くじゃく (HIP 105858, mag 4.21, RA 21.4407h, Dec -65.3662deg)

## PEG -- Pegasus / ペガスス座

Counts: stars 9, edges 9, polylines 1, branch points 2, stars without display names 4

### Polylines

1. HIP 109410 -> HIP 112158 -> Scheat -> Alpheratz -> Scheat -> Markab -> Algenib -> Alpheratz -> Algenib -> Markab -> HIP 112029 -> HIP 109427 -> Enif

### Edges

- HIP 109410 -- HIP 112158  |  HIP 109410 -- HIP 112158
- HIP 112158 -- Scheat  |  HIP 112158 -- シェアト
- Scheat -- Alpheratz  |  シェアト -- アルフェラッツ
- Scheat -- Markab  |  シェアト -- マルカブ
- Markab -- Algenib  |  マルカブ -- アルゲニブ
- Algenib -- Alpheratz  |  アルゲニブ -- アルフェラッツ
- Markab -- HIP 112029  |  マルカブ -- HIP 112029
- HIP 112029 -- HIP 109427  |  HIP 112029 -- HIP 109427
- HIP 109427 -- Enif  |  HIP 109427 -- エニフ

### Branch Points

- Scheat / シェアト (HIP 113881): degree 3
- Markab / マルカブ (HIP 113963): degree 3

### Stars

- Alpheratz / アルフェラッツ (HIP 677, mag 2.06, RA 0.1398h, Dec 29.0904deg)
- Algenib / アルゲニブ (HIP 1067, mag 2.83, RA 0.2206h, Dec 15.1836deg)
- Enif / エニフ (HIP 107315, mag 2.39, RA 21.7364h, Dec 9.8750deg)
- HIP 109410 / HIP 109410 (HIP 109410, mag 4.28, RA 22.1665h, Dec 33.1782deg) [no display name]
- HIP 109427 / HIP 109427 (HIP 109427, mag 3.52, RA 22.1700h, Dec 6.1979deg) [no display name]
- HIP 112029 / HIP 112029 (HIP 112029, mag 3.41, RA 22.6910h, Dec 10.8314deg) [no display name]
- HIP 112158 / HIP 112158 (HIP 112158, mag 2.93, RA 22.7167h, Dec 30.2212deg) [no display name]
- Scheat / シェアト (HIP 113881, mag 2.42, RA 23.0629h, Dec 28.0828deg)
- Markab / マルカブ (HIP 113963, mag 2.49, RA 23.0793h, Dec 15.2053deg)

## PER -- Perseus / ペルセウス座

Counts: stars 13, edges 15, polylines 1, branch points 6, stars without display names 9

### Polylines

1. Atik -> HIP 18246 -> HIP 18614 -> HIP 18532 -> HIP 17358 -> Mirfak -> Gamma Persei -> HIP 13268 -> HIP 13531 -> Gamma Persei -> HIP 13531 -> HIP 14632 -> Mirfak -> HIP 14632 -> HIP 14668 -> Algol -> HIP 18532 -> Algol -> HIP 14354

### Edges

- HIP 13268 -- HIP 13531  |  HIP 13268 -- HIP 13531
- HIP 13268 -- Gamma Persei  |  HIP 13268 -- ガンマ・ペルセイ
- HIP 13531 -- Gamma Persei  |  HIP 13531 -- ガンマ・ペルセイ
- HIP 13531 -- HIP 14632  |  HIP 13531 -- HIP 14632
- Gamma Persei -- Mirfak  |  ガンマ・ペルセイ -- ミルファク
- HIP 14354 -- Algol  |  HIP 14354 -- アルゴル
- Algol -- HIP 14668  |  アルゴル -- HIP 14668
- Algol -- HIP 18532  |  アルゴル -- HIP 18532
- HIP 14632 -- HIP 14668  |  HIP 14632 -- HIP 14668
- HIP 14632 -- Mirfak  |  HIP 14632 -- ミルファク
- Mirfak -- HIP 17358  |  ミルファク -- HIP 17358
- HIP 17358 -- HIP 18532  |  HIP 17358 -- HIP 18532
- Atik -- HIP 18246  |  アティク -- HIP 18246
- HIP 18246 -- HIP 18614  |  HIP 18246 -- HIP 18614
- HIP 18532 -- HIP 18614  |  HIP 18532 -- HIP 18614

### Branch Points

- HIP 13531 / HIP 13531 (HIP 13531): degree 3
- Gamma Persei / ガンマ・ペルセイ (HIP 14328): degree 3
- Algol / アルゴル (HIP 14576): degree 3
- HIP 14632 / HIP 14632 (HIP 14632): degree 3
- Mirfak / ミルファク (HIP 15863): degree 3
- HIP 18532 / HIP 18532 (HIP 18532): degree 3

### Stars

- HIP 13268 / HIP 13268 (HIP 13268, mag 3.77, RA 2.8449h, Dec 55.8955deg) [no display name]
- HIP 13531 / HIP 13531 (HIP 13531, mag 3.93, RA 2.9043h, Dec 52.7625deg) [no display name]
- Gamma Persei / ガンマ・ペルセイ (HIP 14328, mag 2.93, RA 3.0799h, Dec 53.5064deg)
- HIP 14354 / HIP 14354 (HIP 14354, mag 3.32, RA 3.0863h, Dec 38.8403deg) [no display name]
- Algol / アルゴル (HIP 14576, mag 2.09, RA 3.1361h, Dec 40.9556deg)
- HIP 14632 / HIP 14632 (HIP 14632, mag 4.05, RA 3.1510h, Dec 49.6133deg) [no display name]
- HIP 14668 / HIP 14668 (HIP 14668, mag 3.79, RA 3.1583h, Dec 44.8575deg) [no display name]
- Mirfak / ミルファク (HIP 15863, mag 1.79, RA 3.4054h, Dec 49.8612deg)
- HIP 17358 / HIP 17358 (HIP 17358, mag 3.01, RA 3.7154h, Dec 47.7876deg) [no display name]
- Atik / アティク (HIP 17448, mag 3.84, RA 3.7387h, Dec 32.2883deg)
- HIP 18246 / HIP 18246 (HIP 18246, mag 2.84, RA 3.9022h, Dec 31.8836deg) [no display name]
- HIP 18532 / HIP 18532 (HIP 18532, mag 2.90, RA 3.9642h, Dec 40.0102deg) [no display name]
- HIP 18614 / HIP 18614 (HIP 18614, mag 3.98, RA 3.9827h, Dec 35.7910deg) [no display name]

## PHE -- Phoenix / ほうおう座

Counts: stars 6, edges 7, polylines 2, branch points 1, stars without display names 0

### Polylines

1. Ankaa -> Beta Phoenicis -> Gamma Phoenicis
2. Ankaa -> Epsilon Phoenicis -> Beta Phoenicis -> Wurren -> Delta Phoenicis -> Gamma Phoenicis

### Edges

- Epsilon Phoenicis -- Ankaa  |  イプシロン・ほうおう -- アンカー
- Epsilon Phoenicis -- Beta Phoenicis  |  イプシロン・ほうおう -- ベータ・ほうおう
- Ankaa -- Beta Phoenicis  |  アンカー -- ベータ・ほうおう
- Beta Phoenicis -- Wurren  |  ベータ・ほうおう -- ウレン
- Beta Phoenicis -- Gamma Phoenicis  |  ベータ・ほうおう -- ガンマ・ほうおう
- Wurren -- Delta Phoenicis  |  ウレン -- デルタ・ほうおう
- Gamma Phoenicis -- Delta Phoenicis  |  ガンマ・ほうおう -- デルタ・ほうおう

### Branch Points

- Beta Phoenicis / ベータ・ほうおう (HIP 5165): degree 4

### Stars

- Epsilon Phoenicis / イプシロン・ほうおう (HIP 765, mag 3.88, RA 0.1568h, Dec -45.7474deg)
- Ankaa / アンカー (HIP 2081, mag 2.40, RA 0.4381h, Dec -42.3060deg)
- Beta Phoenicis / ベータ・ほうおう (HIP 5165, mag 3.32, RA 1.1014h, Dec -46.7184deg)
- Wurren / ウレン (HIP 5348, mag 3.94, RA 1.1397h, Dec -55.2458deg)
- Gamma Phoenicis / ガンマ・ほうおう (HIP 6867, mag 3.41, RA 1.4728h, Dec -43.3182deg)
- Delta Phoenicis / デルタ・ほうおう (HIP 7083, mag 3.93, RA 1.5209h, Dec -49.0727deg)

## PIC -- Pictor / がか座

Counts: stars 3, edges 2, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Alpha Pictoris -> Gamma Pictoris -> Beta Pictoris

### Edges

- Alpha Pictoris -- Gamma Pictoris  |  アルファ・がか -- ガンマ・がか
- Gamma Pictoris -- Beta Pictoris  |  ガンマ・がか -- ベータ・がか

### Stars

- Beta Pictoris / ベータ・がか (HIP 27321, mag 3.85, RA 5.7881h, Dec -51.0665deg)
- Gamma Pictoris / ガンマ・がか (HIP 27530, mag 4.50, RA 5.8305h, Dec -56.1667deg)
- Alpha Pictoris / アルファ・がか (HIP 32607, mag 3.27, RA 6.8032h, Dec -61.9414deg)

## PSC -- Pisces / うお座

Counts: stars 17, edges 18, polylines 1, branch points 2, stars without display names 7

### Polylines

1. HIP 5742 -> HIP 6193 -> HIP 5586 -> HIP 5742 -> Kullat Nunu -> Torcular -> Alrescha -> HIP 7884 -> HIP 4906 -> HIP 3786 -> Omega Piscium -> Iota Piscium -> Theta Piscium -> 7 Piscium -> Gamma Piscium -> HIP 115738 -> Lambda Piscium -> 19 Piscium -> Iota Piscium

### Edges

- HIP 5742 -- HIP 6193  |  HIP 5742 -- HIP 6193
- HIP 6193 -- HIP 5586  |  HIP 6193 -- HIP 5586
- HIP 5586 -- HIP 5742  |  HIP 5586 -- HIP 5742
- HIP 5742 -- Kullat Nunu  |  HIP 5742 -- クラット・ヌヌ
- Kullat Nunu -- Torcular  |  クラット・ヌヌ -- トルクラー
- Torcular -- Alrescha  |  トルクラー -- アルレシャ
- Alrescha -- HIP 7884  |  アルレシャ -- HIP 7884
- HIP 7884 -- HIP 4906  |  HIP 7884 -- HIP 4906
- HIP 4906 -- HIP 3786  |  HIP 4906 -- HIP 3786
- HIP 3786 -- Omega Piscium  |  HIP 3786 -- オメガ・うお
- Omega Piscium -- Iota Piscium  |  オメガ・うお -- イオタ・うお
- Iota Piscium -- Theta Piscium  |  イオタ・うお -- シータ・うお
- Theta Piscium -- 7 Piscium  |  シータ・うお -- 7・うお
- 7 Piscium -- Gamma Piscium  |  7・うお -- ガンマ・うお
- Gamma Piscium -- HIP 115738  |  ガンマ・うお -- HIP 115738
- HIP 115738 -- Lambda Piscium  |  HIP 115738 -- ラムダ・うお
- Lambda Piscium -- 19 Piscium  |  ラムダ・うお -- 19・うお
- 19 Piscium -- Iota Piscium  |  19・うお -- イオタ・うお

### Branch Points

- HIP 5742 / HIP 5742 (HIP 5742): degree 3
- Iota Piscium / イオタ・うお (HIP 116771): degree 3

### Stars

- HIP 3786 / HIP 3786 (HIP 3786, mag 4.44, RA 0.8114h, Dec 7.5851deg) [no display name]
- HIP 4906 / HIP 4906 (HIP 4906, mag 4.27, RA 1.0491h, Dec 7.8901deg) [no display name]
- HIP 5586 / HIP 5586 (HIP 5586, mag 4.51, RA 1.1943h, Dec 30.0896deg) [no display name]
- HIP 5742 / HIP 5742 (HIP 5742, mag 4.67, RA 1.2292h, Dec 24.5837deg) [no display name]
- HIP 6193 / HIP 6193 (HIP 6193, mag 4.74, RA 1.3244h, Dec 27.2641deg) [no display name]
- Kullat Nunu / クラット・ヌヌ (HIP 7097, mag 4.27, RA 1.5247h, Dec 15.3458deg)
- HIP 7884 / HIP 7884 (HIP 7884, mag 4.45, RA 1.6905h, Dec 5.4876deg) [no display name]
- Torcular / トルクラー (HIP 8198, mag 4.27, RA 1.7566h, Dec 9.1577deg)
- Alrescha / アルレシャ (HIP 9487, mag 3.82, RA 2.0341h, Dec 2.7638deg)
- Gamma Piscium / ガンマ・うお (HIP 114971, mag 3.70, RA 23.2861h, Dec 3.2823deg)
- 7 Piscium / 7・うお (HIP 115227, mag 5.05, RA 23.3390h, Dec 5.3813deg)
- HIP 115738 / HIP 115738 (HIP 115738, mag 4.95, RA 23.4489h, Dec 1.2556deg) [no display name]
- Theta Piscium / シータ・うお (HIP 115830, mag 4.27, RA 23.4661h, Dec 6.3791deg)
- Iota Piscium / イオタ・うお (HIP 116771, mag 4.13, RA 23.6658h, Dec 5.6263deg)
- Lambda Piscium / ラムダ・うお (HIP 116928, mag 4.50, RA 23.7008h, Dec 1.7800deg)
- 19 Piscium / 19・うお (HIP 117245, mag 5.04, RA 23.7732h, Dec 3.4868deg)
- Omega Piscium / オメガ・うお (HIP 118268, mag 4.01, RA 23.9885h, Dec 6.8633deg)

## PSA -- Piscis Austrinus / みなみのうお座

Counts: stars 8, edges 9, polylines 1, branch points 1, stars without display names 4

### Polylines

1. Fomalhaut -> Delta Piscis Austrini -> Gamma Piscis Austrini -> Beta Piscis Austrini -> HIP 109285 -> HIP 107380 -> HIP 107608 -> HIP 109285 -> HIP 111954 -> Fomalhaut

### Edges

- HIP 107380 -- HIP 107608  |  HIP 107380 -- HIP 107608
- HIP 107380 -- HIP 109285  |  HIP 107380 -- HIP 109285
- HIP 107608 -- HIP 109285  |  HIP 107608 -- HIP 109285
- HIP 109285 -- Beta Piscis Austrini  |  HIP 109285 -- ベータ・みなみのうお
- HIP 109285 -- HIP 111954  |  HIP 109285 -- HIP 111954
- Beta Piscis Austrini -- Gamma Piscis Austrini  |  ベータ・みなみのうお -- ガンマ・みなみのうお
- HIP 111954 -- Fomalhaut  |  HIP 111954 -- フォーマルハウト
- Gamma Piscis Austrini -- Delta Piscis Austrini  |  ガンマ・みなみのうお -- デルタ・みなみのうお
- Delta Piscis Austrini -- Fomalhaut  |  デルタ・みなみのうお -- フォーマルハウト

### Branch Points

- HIP 109285 / HIP 109285 (HIP 109285): degree 4

### Stars

- HIP 107380 / HIP 107380 (HIP 107380, mag 4.35, RA 21.7491h, Dec -33.0258deg) [no display name]
- HIP 107608 / HIP 107608 (HIP 107608, mag 5.02, RA 21.7956h, Dec -30.8983deg) [no display name]
- HIP 109285 / HIP 109285 (HIP 109285, mag 4.50, RA 22.1397h, Dec -32.9885deg) [no display name]
- Beta Piscis Austrini / ベータ・みなみのうお (HIP 111188, mag 4.29, RA 22.5251h, Dec -32.3460deg)
- HIP 111954 / HIP 111954 (HIP 111954, mag 4.18, RA 22.6776h, Dec -27.0436deg) [no display name]
- Gamma Piscis Austrini / ガンマ・みなみのうお (HIP 112948, mag 4.46, RA 22.8754h, Dec -32.8754deg)
- Delta Piscis Austrini / デルタ・みなみのうお (HIP 113246, mag 4.20, RA 22.9325h, Dec -32.5396deg)
- Fomalhaut / フォーマルハウト (HIP 113368, mag 1.16, RA 22.9608h, Dec -29.6222deg)

## PUP -- Puppis / とも座

Counts: stars 9, edges 8, polylines 1, branch points 0, stars without display names 6

### Polylines

1. HIP 39855 -> Naos -> Tureis -> HIP 38170 -> HIP 37229 -> HIP 36917 -> Azmidi -> HIP 31685 -> HIP 30581

### Edges

- HIP 30581 -- HIP 31685  |  HIP 30581 -- HIP 31685
- HIP 31685 -- Azmidi  |  HIP 31685 -- アズミディ
- Azmidi -- HIP 36917  |  アズミディ -- HIP 36917
- HIP 36917 -- HIP 37229  |  HIP 36917 -- HIP 37229
- HIP 37229 -- HIP 38170  |  HIP 37229 -- HIP 38170
- HIP 38170 -- Tureis  |  HIP 38170 -- トゥレイス
- Naos -- Tureis  |  ナオス -- トゥレイス
- Naos -- HIP 39855  |  ナオス -- HIP 39855

### Stars

- HIP 30581 / HIP 30581 (HIP 30581, mag 8.69, RA 6.4278h, Dec -51.1342deg) [no display name]
- HIP 31685 / HIP 31685 (HIP 31685, mag 3.17, RA 6.6294h, Dec -43.1959deg) [no display name]
- Azmidi / アズミディ (HIP 35264, mag 3.25, RA 7.2857h, Dec -37.0975deg)
- HIP 36917 / HIP 36917 (HIP 36917, mag 4.65, RA 7.5897h, Dec -28.3693deg) [no display name]
- HIP 37229 / HIP 37229 (HIP 37229, mag 3.80, RA 7.6472h, Dec -26.8038deg) [no display name]
- HIP 38170 / HIP 38170 (HIP 38170, mag 3.34, RA 7.8216h, Dec -24.8598deg) [no display name]
- Naos / ナオス (HIP 39429, mag 2.21, RA 8.0597h, Dec -40.0031deg)
- Tureis / トゥレイス (HIP 39757, mag 2.83, RA 8.1257h, Dec -24.3043deg)
- HIP 39855 / HIP 39855 (HIP 39855, mag 8.81, RA 8.1424h, Dec -46.2605deg) [no display name]

## PYX -- Pyxis / らしんばん座

Counts: stars 3, edges 2, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Beta Pyxidis -> Alpha Pyxidis -> Gamma Pyxidis

### Edges

- Beta Pyxidis -- Alpha Pyxidis  |  ベータ・らしんばん -- アルファ・らしんばん
- Alpha Pyxidis -- Gamma Pyxidis  |  アルファ・らしんばん -- ガンマ・らしんばん

### Stars

- Beta Pyxidis / ベータ・らしんばん (HIP 42515, mag 3.97, RA 8.6684h, Dec -35.3083deg)
- Alpha Pyxidis / アルファ・らしんばん (HIP 42828, mag 3.68, RA 8.7265h, Dec -33.1864deg)
- Gamma Pyxidis / ガンマ・らしんばん (HIP 43409, mag 4.01, RA 8.8422h, Dec -27.7101deg)

## RET -- Reticulum / レチクル座

Counts: stars 4, edges 4, polylines 1, branch points 0, stars without display names 1

### Polylines

1. Alpha Reticuli -> Beta Reticuli -> HIP 18597 -> Epsilon Reticuli -> Alpha Reticuli

### Edges

- Beta Reticuli -- HIP 18597  |  ベータ・レチクル -- HIP 18597
- Beta Reticuli -- Alpha Reticuli  |  ベータ・レチクル -- アルファ・レチクル
- HIP 18597 -- Epsilon Reticuli  |  HIP 18597 -- イプシロン・レチクル
- Alpha Reticuli -- Epsilon Reticuli  |  アルファ・レチクル -- イプシロン・レチクル

### Stars

- Beta Reticuli / ベータ・レチクル (HIP 17440, mag 3.84, RA 3.7367h, Dec -64.8069deg)
- HIP 18597 / HIP 18597 (HIP 18597, mag 4.56, RA 3.9791h, Dec -61.4002deg) [no display name]
- Alpha Reticuli / アルファ・レチクル (HIP 19780, mag 3.35, RA 4.2404h, Dec -62.4739deg)
- Epsilon Reticuli / イプシロン・レチクル (HIP 19921, mag 4.44, RA 4.2747h, Dec -59.3017deg)

## SGE -- Sagitta / や座

Counts: stars 4, edges 3, polylines 1, branch points 1, stars without display names 1

### Polylines

1. Gamma Sagittae -> Delta Sagittae -> HIP 96757 -> Delta Sagittae -> Sham

### Edges

- Gamma Sagittae -- Delta Sagittae  |  ガンマ・や -- デルタ・や
- Delta Sagittae -- HIP 96757  |  デルタ・や -- HIP 96757
- Delta Sagittae -- Sham  |  デルタ・や -- シャム

### Branch Points

- Delta Sagittae / デルタ・や (HIP 97365): degree 3

### Stars

- HIP 96757 / HIP 96757 (HIP 96757, mag 4.39, RA 19.6683h, Dec 18.0139deg) [no display name]
- Sham / シャム (HIP 96837, mag 4.39, RA 19.6683h, Dec 18.0139deg)
- Delta Sagittae / デルタ・や (HIP 97365, mag 3.82, RA 19.7898h, Dec 18.5343deg)
- Gamma Sagittae / ガンマ・や (HIP 98337, mag 3.51, RA 19.9825h, Dec 19.4921deg)

## SGR -- Sagittarius / いて座

Counts: stars 8, edges 11, polylines 1, branch points 4, stars without display names 2

### Polylines

1. Kaus Australis -> Alnasl -> Kaus Media -> Kaus Australis -> Kaus Media -> Kaus Borealis -> HIP 92041 -> Kaus Media -> HIP 92041 -> Nunki -> HIP 93864 -> Ascella -> HIP 92041 -> Ascella -> Kaus Australis

### Edges

- Alnasl -- Kaus Media  |  アルナスル -- カウス・メディア
- Alnasl -- Kaus Australis  |  アルナスル -- カウス・アウストラリス
- Kaus Media -- Kaus Australis  |  カウス・メディア -- カウス・アウストラリス
- Kaus Media -- Kaus Borealis  |  カウス・メディア -- カウス・ボレアリス
- Kaus Media -- HIP 92041  |  カウス・メディア -- HIP 92041
- Kaus Australis -- Ascella  |  カウス・アウストラリス -- アスケラ
- Kaus Borealis -- HIP 92041  |  カウス・ボレアリス -- HIP 92041
- HIP 92041 -- Nunki  |  HIP 92041 -- ヌンキ
- HIP 92041 -- Ascella  |  HIP 92041 -- アスケラ
- Nunki -- HIP 93864  |  ヌンキ -- HIP 93864
- Ascella -- HIP 93864  |  アスケラ -- HIP 93864

### Branch Points

- Kaus Media / カウス・メディア (HIP 89931): degree 4
- Kaus Australis / カウス・アウストラリス (HIP 90185): degree 3
- HIP 92041 / HIP 92041 (HIP 92041): degree 4
- Ascella / アスケラ (HIP 93506): degree 3

### Stars

- Alnasl / アルナスル (HIP 88635, mag 2.98, RA 18.0968h, Dec -30.4241deg)
- Kaus Media / カウス・メディア (HIP 89931, mag 2.72, RA 18.3499h, Dec -29.8281deg)
- Kaus Australis / カウス・アウストラリス (HIP 90185, mag 1.79, RA 18.4029h, Dec -34.3846deg)
- Kaus Borealis / カウス・ボレアリス (HIP 90496, mag 2.82, RA 18.4662h, Dec -25.4217deg)
- HIP 92041 / HIP 92041 (HIP 92041, mag 3.17, RA 18.7609h, Dec -26.9908deg) [no display name]
- Nunki / ヌンキ (HIP 92855, mag 2.05, RA 18.9211h, Dec -26.2967deg)
- Ascella / アスケラ (HIP 93506, mag 2.60, RA 19.0435h, Dec -29.8801deg)
- HIP 93864 / HIP 93864 (HIP 93864, mag 3.32, RA 19.1157h, Dec -27.6704deg) [no display name]

## SCO -- Scorpius / さそり座

Counts: stars 16, edges 15, polylines 1, branch points 1, stars without display names 9

### Polylines

1. Acrab -> Dschubba -> HIP 78265 -> Dschubba -> Alniyat -> Antares -> HIP 81266 -> HIP 82396 -> HIP 82514 -> HIP 82729 -> HIP 84143 -> Sargas -> HIP 87073 -> HIP 86670 -> Lesath -> Shaula -> HIP 87261

### Edges

- HIP 78265 -- Dschubba  |  HIP 78265 -- ジュバ
- Dschubba -- Acrab  |  ジュバ -- アクラブ
- Dschubba -- Alniyat  |  ジュバ -- アルニヤト
- Alniyat -- Antares  |  アルニヤト -- アンタレス
- Antares -- HIP 81266  |  アンタレス -- HIP 81266
- HIP 81266 -- HIP 82396  |  HIP 81266 -- HIP 82396
- HIP 82396 -- HIP 82514  |  HIP 82396 -- HIP 82514
- HIP 82514 -- HIP 82729  |  HIP 82514 -- HIP 82729
- HIP 82729 -- HIP 84143  |  HIP 82729 -- HIP 84143
- HIP 84143 -- Sargas  |  HIP 84143 -- サルガス
- Lesath -- Shaula  |  レサト -- シャウラ
- Lesath -- HIP 86670  |  レサト -- HIP 86670
- Shaula -- HIP 87261  |  シャウラ -- HIP 87261
- Sargas -- HIP 87073  |  サルガス -- HIP 87073
- HIP 86670 -- HIP 87073  |  HIP 86670 -- HIP 87073

### Branch Points

- Dschubba / ジュバ (HIP 78401): degree 3

### Stars

- HIP 78265 / HIP 78265 (HIP 78265, mag 2.89, RA 15.9809h, Dec -26.1141deg) [no display name]
- Dschubba / ジュバ (HIP 78401, mag 2.32, RA 16.0056h, Dec -22.6217deg)
- Acrab / アクラブ (HIP 78820, mag 2.56, RA 16.0906h, Dec -19.8055deg)
- Alniyat / アルニヤト (HIP 80112, mag 2.89, RA 16.3532h, Dec -25.5928deg)
- Antares / アンタレス (HIP 80763, mag 1.06, RA 16.4901h, Dec -26.4319deg)
- HIP 81266 / HIP 81266 (HIP 81266, mag 2.82, RA 16.5980h, Dec -28.2160deg) [no display name]
- HIP 82396 / HIP 82396 (HIP 82396, mag 2.29, RA 16.8361h, Dec -34.2932deg) [no display name]
- HIP 82514 / HIP 82514 (HIP 82514, mag 3.00, RA 16.8645h, Dec -38.0474deg) [no display name]
- HIP 82729 / HIP 82729 (HIP 82729, mag 3.62, RA 16.9097h, Dec -42.3613deg) [no display name]
- HIP 84143 / HIP 84143 (HIP 84143, mag 3.32, RA 17.2026h, Dec -43.2392deg) [no display name]
- Lesath / レサト (HIP 85696, mag 2.70, RA 17.5127h, Dec -37.2958deg)
- Shaula / シャウラ (HIP 85927, mag 1.62, RA 17.5601h, Dec -37.1038deg)
- Sargas / サルガス (HIP 86228, mag 1.86, RA 17.6220h, Dec -42.9978deg)
- HIP 86670 / HIP 86670 (HIP 86670, mag 2.39, RA 17.7081h, Dec -39.0300deg) [no display name]
- HIP 87073 / HIP 87073 (HIP 87073, mag 2.99, RA 17.7931h, Dec -40.1270deg) [no display name]
- HIP 87261 / HIP 87261 (HIP 87261, mag 3.19, RA 17.8310h, Dec -37.0433deg) [no display name]

## SCL -- Sculptor / ちょうこくしつ座

Counts: stars 4, edges 3, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Alpha Sculptoris -> Delta Sculptoris -> Gamma Sculptoris -> Beta Sculptoris

### Edges

- Alpha Sculptoris -- Delta Sculptoris  |  アルファ・ちょうこくしつ -- デルタ・ちょうこくしつ
- Delta Sculptoris -- Gamma Sculptoris  |  デルタ・ちょうこくしつ -- ガンマ・ちょうこくしつ
- Gamma Sculptoris -- Beta Sculptoris  |  ガンマ・ちょうこくしつ -- ベータ・ちょうこくしつ

### Stars

- Alpha Sculptoris / アルファ・ちょうこくしつ (HIP 4577, mag 4.30, RA 0.9768h, Dec -29.3575deg)
- Gamma Sculptoris / ガンマ・ちょうこくしつ (HIP 115102, mag 4.41, RA 23.3137h, Dec -32.5320deg)
- Beta Sculptoris / ベータ・ちょうこくしつ (HIP 116231, mag 4.38, RA 23.5495h, Dec -37.8183deg)
- Delta Sculptoris / デルタ・ちょうこくしつ (HIP 117452, mag 4.57, RA 23.8154h, Dec -28.1303deg)

## SCT -- Scutum / たて座

Counts: stars 4, edges 4, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Beta Scuti -> Alpha Scuti -> Gamma Scuti -> Delta Scuti -> Beta Scuti

### Edges

- Gamma Scuti -- Alpha Scuti  |  ガンマ・たて -- アルファ・たて
- Gamma Scuti -- Delta Scuti  |  ガンマ・たて -- デルタ・たて
- Alpha Scuti -- Beta Scuti  |  アルファ・たて -- ベータ・たて
- Delta Scuti -- Beta Scuti  |  デルタ・たて -- ベータ・たて

### Stars

- Gamma Scuti / ガンマ・たて (HIP 90595, mag 4.67, RA 18.4866h, Dec -14.5658deg)
- Alpha Scuti / アルファ・たて (HIP 91117, mag 3.85, RA 18.5868h, Dec -8.2441deg)
- Delta Scuti / デルタ・たて (HIP 91726, mag 4.72, RA 18.7046h, Dec -9.0526deg)
- Beta Scuti / ベータ・たて (HIP 92175, mag 4.22, RA 18.7862h, Dec -4.7478deg)

## SER -- Serpens / へび座

Counts: stars 14, edges 13, polylines 2, branch points 1, stars without display names 5

### Polylines

1. Beta Serpentis -> Gamma Serpentis -> HIP 77450 -> HIP 76852 -> Beta Serpentis -> Delta Serpentis -> Unukalhai -> Epsilon Serpentis -> HIP 77516 -> Yed Prior
2. Sabik -> Xi Serpentis -> HIP 88048 -> Eta Serpentis -> HIP 92946

### Edges

- Delta Serpentis -- Unukalhai  |  デルタ・へび -- ウヌカルハイ
- Delta Serpentis -- Beta Serpentis  |  デルタ・へび -- ベータ・へび
- HIP 76852 -- Beta Serpentis  |  HIP 76852 -- ベータ・へび
- HIP 76852 -- HIP 77450  |  HIP 76852 -- HIP 77450
- Unukalhai -- Epsilon Serpentis  |  ウヌカルハイ -- イプシロン・へび
- Beta Serpentis -- Gamma Serpentis  |  ベータ・へび -- ガンマ・へび
- HIP 77450 -- Gamma Serpentis  |  HIP 77450 -- ガンマ・へび
- HIP 77516 -- Epsilon Serpentis  |  HIP 77516 -- イプシロン・へび
- HIP 77516 -- Yed Prior  |  HIP 77516 -- イェド・プリオル
- Sabik -- Xi Serpentis  |  サビク -- クシー・へび
- Xi Serpentis -- HIP 88048  |  クシー・へび -- HIP 88048
- HIP 88048 -- Eta Serpentis  |  HIP 88048 -- イータ・へび
- Eta Serpentis -- HIP 92946  |  イータ・へび -- HIP 92946

### Branch Points

- Beta Serpentis / ベータ・へび (HIP 77233): degree 3

### Stars

- Delta Serpentis / デルタ・へび (HIP 76276, mag 3.80, RA 15.5800h, Dec 10.5389deg)
- HIP 76852 / HIP 76852 (HIP 76852, mag 4.51, RA 15.6925h, Dec 19.6704deg) [no display name]
- Unukalhai / ウヌカルハイ (HIP 77070, mag 2.63, RA 15.7378h, Dec 6.4256deg)
- Beta Serpentis / ベータ・へび (HIP 77233, mag 3.65, RA 15.7698h, Dec 15.4218deg)
- HIP 77450 / HIP 77450 (HIP 77450, mag 4.09, RA 15.8123h, Dec 18.1416deg) [no display name]
- HIP 77516 / HIP 77516 (HIP 77516, mag 3.54, RA 15.8270h, Dec -3.4302deg) [no display name]
- Epsilon Serpentis / イプシロン・へび (HIP 77622, mag 3.71, RA 15.8469h, Dec 4.4777deg)
- Gamma Serpentis / ガンマ・へび (HIP 78072, mag 3.85, RA 15.9409h, Dec 15.6616deg)
- Yed Prior / イェド・プリオル (HIP 79593, mag 2.73, RA 16.2391h, Dec -3.6943deg)
- Sabik / サビク (HIP 84012, mag 2.43, RA 17.1729h, Dec -15.7249deg)
- Xi Serpentis / クシー・へび (HIP 86263, mag 3.54, RA 17.6264h, Dec -15.3986deg)
- HIP 88048 / HIP 88048 (HIP 88048, mag 3.32, RA 17.9838h, Dec -9.7736deg) [no display name]
- Eta Serpentis / イータ・へび (HIP 89962, mag 3.23, RA 18.3552h, Dec -2.8988deg)
- HIP 92946 / HIP 92946 (HIP 92946, mag 4.62, RA 18.9370h, Dec 4.2036deg) [no display name]

## SEX -- Sextans / ろくぶんぎ座

Counts: stars 3, edges 2, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Beta Sextantis -> Alpha Sextantis -> Gamma Sextantis

### Edges

- Beta Sextantis -- Alpha Sextantis  |  ベータ・ろくぶんぎ -- アルファ・ろくぶんぎ
- Alpha Sextantis -- Gamma Sextantis  |  アルファ・ろくぶんぎ -- ガンマ・ろくぶんぎ

### Stars

- Gamma Sextantis / ガンマ・ろくぶんぎ (HIP 48437, mag 5.05, RA 9.8751h, Dec -8.1049deg)
- Alpha Sextantis / アルファ・ろくぶんぎ (HIP 49641, mag 4.49, RA 10.1323h, Dec -0.3716deg)
- Beta Sextantis / ベータ・ろくぶんぎ (HIP 51437, mag 5.08, RA 10.5049h, Dec -0.6369deg)

## TAU -- Taurus / おうし座

Counts: stars 9, edges 8, polylines 2, branch points 1, stars without display names 5

### Polylines

1. HIP 26451 -> Aldebaran -> HIP 20894 -> HIP 20205 -> Delta1 Tauri -> Hyadum I -> Elnath
2. HIP 20205 -> HIP 18724 -> HIP 16083

### Edges

- HIP 16083 -- HIP 18724  |  HIP 16083 -- HIP 18724
- HIP 18724 -- HIP 20205  |  HIP 18724 -- HIP 20205
- HIP 20205 -- Delta1 Tauri  |  HIP 20205 -- デルタ1・おうし
- HIP 20205 -- HIP 20894  |  HIP 20205 -- HIP 20894
- Delta1 Tauri -- Hyadum I  |  デルタ1・おうし -- ヒアドゥムI
- Hyadum I -- Elnath  |  ヒアドゥムI -- エルナト
- HIP 20894 -- Aldebaran  |  HIP 20894 -- アルデバラン
- Aldebaran -- HIP 26451  |  アルデバラン -- HIP 26451

### Branch Points

- HIP 20205 / HIP 20205 (HIP 20205): degree 3

### Stars

- HIP 16083 / HIP 16083 (HIP 16083, mag 3.73, RA 3.4528h, Dec 9.7327deg) [no display name]
- HIP 18724 / HIP 18724 (HIP 18724, mag 3.41, RA 4.0113h, Dec 12.4903deg) [no display name]
- HIP 20205 / HIP 20205 (HIP 20205, mag 3.65, RA 4.3299h, Dec 15.6276deg) [no display name]
- Delta1 Tauri / デルタ1・おうし (HIP 20455, mag 3.76, RA 4.3823h, Dec 17.5425deg)
- Hyadum I / ヒアドゥムI (HIP 20889, mag 3.40, RA 4.3823h, Dec 17.5425deg)
- HIP 20894 / HIP 20894 (HIP 20894, mag 3.40, RA 4.4777h, Dec 15.8709deg) [no display name]
- Aldebaran / アルデバラン (HIP 21421, mag 0.85, RA 4.5987h, Dec 16.5093deg)
- Elnath / エルナト (HIP 25428, mag 1.65, RA 5.4382h, Dec 28.6075deg)
- HIP 26451 / HIP 26451 (HIP 26451, mag 2.97, RA 5.6274h, Dec 21.1425deg) [no display name]

## TEL -- Telescopium / ぼうえんきょう座

Counts: stars 3, edges 2, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Epsilon Telescopii -> Alpha Telescopii -> Zeta Telescopii

### Edges

- Epsilon Telescopii -- Alpha Telescopii  |  イプシロン・ぼうえんきょう -- アルファ・ぼうえんきょう
- Alpha Telescopii -- Zeta Telescopii  |  アルファ・ぼうえんきょう -- ゼータ・ぼうえんきょう

### Stars

- Epsilon Telescopii / イプシロン・ぼうえんきょう (HIP 89112, mag 4.52, RA 18.1872h, Dec -45.9544deg)
- Alpha Telescopii / アルファ・ぼうえんきょう (HIP 90422, mag 3.49, RA 18.4496h, Dec -45.9685deg)
- Zeta Telescopii / ゼータ・ぼうえんきょう (HIP 90568, mag 4.13, RA 18.4805h, Dec -49.0706deg)

## TRI -- Triangulum / さんかく座

Counts: stars 3, edges 3, polylines 1, branch points 0, stars without display names 0

### Polylines

1. Beta Trianguli -> Gamma Trianguli -> Mothallah -> Beta Trianguli

### Edges

- Beta Trianguli -- Gamma Trianguli  |  ベータ・さんかく -- ガンマ・さんかく
- Gamma Trianguli -- Mothallah  |  ガンマ・さんかく -- モサラー
- Mothallah -- Beta Trianguli  |  モサラー -- ベータ・さんかく

### Stars

- Mothallah / モサラー (HIP 8796, mag 3.42, RA 1.8847h, Dec 29.5788deg)
- Beta Trianguli / ベータ・さんかく (HIP 10064, mag 3.00, RA 2.1591h, Dec 34.9873deg)
- Gamma Trianguli / ガンマ・さんかく (HIP 10670, mag 4.03, RA 2.2886h, Dec 33.8472deg)

## TRA -- Triangulum Australe / みなみのさんかく座

Counts: stars 4, edges 4, polylines 1, branch points 0, stars without display names 1

### Polylines

1. Alpha Trianguli Australis -> Gamma Trianguli Australis -> HIP 76440 -> Beta Trianguli Australis -> Alpha Trianguli Australis

### Edges

- Alpha Trianguli Australis -- Gamma Trianguli Australis  |  アルファ・みなみのさんかく -- ガンマ・みなみのさんかく
- Gamma Trianguli Australis -- HIP 76440  |  ガンマ・みなみのさんかく -- HIP 76440
- HIP 76440 -- Beta Trianguli Australis  |  HIP 76440 -- ベータ・みなみのさんかく
- Beta Trianguli Australis -- Alpha Trianguli Australis  |  ベータ・みなみのさんかく -- アルファ・みなみのさんかく

### Stars

- Gamma Trianguli Australis / ガンマ・みなみのさんかく (HIP 74946, mag 2.87, RA 15.3152h, Dec -68.6795deg)
- HIP 76440 / HIP 76440 (HIP 76440, mag 4.11, RA 15.6120h, Dec -66.3170deg) [no display name]
- Beta Trianguli Australis / ベータ・みなみのさんかく (HIP 77952, mag 2.85, RA 15.9191h, Dec -63.4307deg)
- Alpha Trianguli Australis / アルファ・みなみのさんかく (HIP 82273, mag 1.91, RA 16.8111h, Dec -69.0277deg)

## TUC -- Tucana / きょしちょう座

Counts: stars 6, edges 6, polylines 1, branch points 1, stars without display names 2

### Polylines

1. HIP 110838 -> Alpha Tucanae -> Gamma Tucanae -> HIP 118322 -> Zeta Tucanae -> Beta1 Tucanae -> Gamma Tucanae

### Edges

- HIP 110838 -- Alpha Tucanae  |  HIP 110838 -- アルファ・きょしちょう
- Alpha Tucanae -- Gamma Tucanae  |  アルファ・きょしちょう -- ガンマ・きょしちょう
- Gamma Tucanae -- HIP 118322  |  ガンマ・きょしちょう -- HIP 118322
- HIP 118322 -- Zeta Tucanae  |  HIP 118322 -- ゼータ・きょしちょう
- Zeta Tucanae -- Beta1 Tucanae  |  ゼータ・きょしちょう -- ベータ1・きょしちょう
- Beta1 Tucanae -- Gamma Tucanae  |  ベータ1・きょしちょう -- ガンマ・きょしちょう

### Branch Points

- Gamma Tucanae / ガンマ・きょしちょう (HIP 114996): degree 3

### Stars

- Zeta Tucanae / ゼータ・きょしちょう (HIP 1599, mag 4.23, RA 0.3345h, Dec -64.8748deg)
- Beta1 Tucanae / ベータ1・きょしちょう (HIP 2484, mag 4.36, RA 0.5258h, Dec -62.9581deg)
- Alpha Tucanae / アルファ・きょしちょう (HIP 110130, mag 2.86, RA 22.3084h, Dec -60.2596deg)
- HIP 110838 / HIP 110838 (HIP 110838, mag 4.51, RA 22.4555h, Dec -64.9664deg) [no display name]
- Gamma Tucanae / ガンマ・きょしちょう (HIP 114996, mag 3.99, RA 23.2905h, Dec -58.2359deg)
- HIP 118322 / HIP 118322 (HIP 118322, mag 4.49, RA 23.9986h, Dec -65.5771deg) [no display name]

## UMA -- Ursa Major / おおぐま座

Counts: stars 19, edges 20, polylines 1, branch points 6, stars without display names 12

### Polylines

1. Alkaid -> Mizar -> Alioth -> Megrez -> Phecda -> HIP 57399 -> HIP 55219 -> HIP 55203 -> HIP 55219 -> HIP 57399 -> HIP 54539 -> HIP 50801 -> HIP 50372 -> HIP 50801 -> HIP 54539 -> HIP 57399 -> Phecda -> Merak -> Dubhe -> Megrez -> Dubhe -> HIP 46733 -> HIP 41704 -> HIP 48319 -> Merak -> HIP 48319 -> HIP 46853 -> HIP 44471 -> HIP 44127

### Edges

- Alkaid -- Mizar  |  アルカイド -- ミザール
- Mizar -- Alioth  |  ミザール -- アリオト
- Alioth -- Megrez  |  アリオト -- メグレズ
- Megrez -- Phecda  |  メグレズ -- フェクダ
- Phecda -- HIP 57399  |  フェクダ -- HIP 57399
- HIP 57399 -- HIP 55219  |  HIP 57399 -- HIP 55219
- HIP 55219 -- HIP 55203  |  HIP 55219 -- HIP 55203
- HIP 57399 -- HIP 54539  |  HIP 57399 -- HIP 54539
- HIP 54539 -- HIP 50801  |  HIP 54539 -- HIP 50801
- HIP 50801 -- HIP 50372  |  HIP 50801 -- HIP 50372
- Phecda -- Merak  |  フェクダ -- メラク
- Merak -- Dubhe  |  メラク -- ドゥーベ
- Dubhe -- Megrez  |  ドゥーベ -- メグレズ
- Dubhe -- HIP 46733  |  ドゥーベ -- HIP 46733
- HIP 46733 -- HIP 41704  |  HIP 46733 -- HIP 41704
- HIP 41704 -- HIP 48319  |  HIP 41704 -- HIP 48319
- HIP 48319 -- Merak  |  HIP 48319 -- メラク
- HIP 48319 -- HIP 46853  |  HIP 48319 -- HIP 46853
- HIP 46853 -- HIP 44471  |  HIP 46853 -- HIP 44471
- HIP 44471 -- HIP 44127  |  HIP 44471 -- HIP 44127

### Branch Points

- HIP 48319 / HIP 48319 (HIP 48319): degree 3
- Merak / メラク (HIP 53910): degree 3
- Dubhe / ドゥーベ (HIP 54061): degree 3
- HIP 57399 / HIP 57399 (HIP 57399): degree 3
- Phecda / フェクダ (HIP 58001): degree 3
- Megrez / メグレズ (HIP 59774): degree 3

### Stars

- HIP 41704 / HIP 41704 (HIP 41704, mag 3.35, RA 8.5044h, Dec 60.7182deg) [no display name]
- HIP 44127 / HIP 44127 (HIP 44127, mag 3.12, RA 8.9868h, Dec 48.0418deg) [no display name]
- HIP 44471 / HIP 44471 (HIP 44471, mag 3.57, RA 9.0604h, Dec 47.1565deg) [no display name]
- HIP 46733 / HIP 46733 (HIP 46733, mag 3.65, RA 9.5255h, Dec 63.0619deg) [no display name]
- HIP 46853 / HIP 46853 (HIP 46853, mag 3.17, RA 9.5477h, Dec 51.6773deg) [no display name]
- HIP 48319 / HIP 48319 (HIP 48319, mag 3.78, RA 9.8499h, Dec 59.0387deg) [no display name]
- HIP 50372 / HIP 50372 (HIP 50372, mag 3.45, RA 10.2850h, Dec 42.9144deg) [no display name]
- HIP 50801 / HIP 50801 (HIP 50801, mag 3.06, RA 10.3722h, Dec 41.4995deg) [no display name]
- Merak / メラク (HIP 53910, mag 2.37, RA 11.0307h, Dec 56.3824deg)
- Dubhe / ドゥーベ (HIP 54061, mag 1.79, RA 11.0621h, Dec 61.7510deg)
- HIP 54539 / HIP 54539 (HIP 54539, mag 3.00, RA 11.1611h, Dec 44.4985deg) [no display name]
- HIP 55203 / HIP 55203 (HIP 55203, mag 4.33, RA 11.3031h, Dec 31.5288deg) [no display name]
- HIP 55219 / HIP 55219 (HIP 55219, mag 3.49, RA 11.3080h, Dec 33.0943deg) [no display name]
- HIP 57399 / HIP 57399 (HIP 57399, mag 3.69, RA 11.7675h, Dec 47.7794deg) [no display name]
- Phecda / フェクダ (HIP 58001, mag 2.44, RA 11.8972h, Dec 53.6948deg)
- Megrez / メグレズ (HIP 59774, mag 3.31, RA 12.2569h, Dec 57.0326deg)
- Alioth / アリオト (HIP 62956, mag 1.76, RA 12.9005h, Dec 55.9598deg)
- Mizar / ミザール (HIP 65378, mag 2.23, RA 13.3987h, Dec 54.9254deg)
- Alkaid / アルカイド (HIP 67301, mag 1.86, RA 13.7923h, Dec 49.3133deg)

## UMI -- Ursa Minor / こぐま座

Counts: stars 7, edges 7, polylines 1, branch points 1, stars without display names 0

### Polylines

1. Polaris -> Yildun -> Epsilon Ursae Minoris -> Zeta Ursae Minoris -> Kochab -> Pherkad -> Eta Ursae Minoris -> Zeta Ursae Minoris

### Edges

- Polaris -- Yildun  |  ポラリス -- イルドゥン
- Yildun -- Epsilon Ursae Minoris  |  イルドゥン -- イプシロン・こぐま
- Epsilon Ursae Minoris -- Zeta Ursae Minoris  |  イプシロン・こぐま -- ゼータ・こぐま
- Zeta Ursae Minoris -- Kochab  |  ゼータ・こぐま -- コカブ
- Kochab -- Pherkad  |  コカブ -- フェルカド
- Pherkad -- Eta Ursae Minoris  |  フェルカド -- イータ・こぐま
- Eta Ursae Minoris -- Zeta Ursae Minoris  |  イータ・こぐま -- ゼータ・こぐま

### Branch Points

- Zeta Ursae Minoris / ゼータ・こぐま (HIP 77055): degree 3

### Stars

- Polaris / ポラリス (HIP 11767, mag 1.98, RA 2.5303h, Dec 89.2641deg)
- Kochab / コカブ (HIP 72607, mag 2.08, RA 14.8451h, Dec 74.1555deg)
- Pherkad / フェルカド (HIP 75097, mag 3.05, RA 15.3455h, Dec 71.8340deg)
- Zeta Ursae Minoris / ゼータ・こぐま (HIP 77055, mag 4.32, RA 15.7343h, Dec 77.7945deg)
- Eta Ursae Minoris / イータ・こぐま (HIP 79822, mag 4.95, RA 16.2918h, Dec 75.7547deg)
- Epsilon Ursae Minoris / イプシロン・こぐま (HIP 82080, mag 4.23, RA 16.7662h, Dec 82.0373deg)
- Yildun / イルドゥン (HIP 85822, mag 4.36, RA 17.5369h, Dec 86.5863deg)

## VEL -- Vela / ほ座

Counts: stars 11, edges 11, polylines 1, branch points 0, stars without display names 7

### Polylines

1. Regor -> Markeb Velae -> Alsephina -> HIP 48774 -> HIP 52727 -> HIP 51986 -> HIP 50191 -> HIP 46651 -> Suhail -> HIP 42884 -> HIP 42312 -> Regor

### Edges

- Regor -- Markeb Velae  |  レゴール -- マルケブ・ほ
- Markeb Velae -- Alsephina  |  マルケブ・ほ -- アルセフィナ
- Alsephina -- HIP 48774  |  アルセフィナ -- HIP 48774
- HIP 48774 -- HIP 52727  |  HIP 48774 -- HIP 52727
- HIP 52727 -- HIP 51986  |  HIP 52727 -- HIP 51986
- HIP 51986 -- HIP 50191  |  HIP 51986 -- HIP 50191
- HIP 50191 -- HIP 46651  |  HIP 50191 -- HIP 46651
- HIP 46651 -- Suhail  |  HIP 46651 -- スハイル
- Suhail -- HIP 42884  |  スハイル -- HIP 42884
- HIP 42884 -- HIP 42312  |  HIP 42884 -- HIP 42312
- HIP 42312 -- Regor  |  HIP 42312 -- レゴール

### Stars

- Regor / レゴール (HIP 39953, mag 1.75, RA 8.1589h, Dec -47.3366deg)
- HIP 42312 / HIP 42312 (HIP 42312, mag 4.11, RA 8.6274h, Dec -42.9891deg) [no display name]
- HIP 42884 / HIP 42884 (HIP 42884, mag 4.05, RA 8.7400h, Dec -42.6493deg) [no display name]
- Markeb Velae / マルケブ・ほ (HIP 42913, mag 2.47, RA 8.7451h, Dec -54.7088deg)
- Suhail / スハイル (HIP 44816, mag 2.21, RA 9.1333h, Dec -43.4326deg)
- Alsephina / アルセフィナ (HIP 45941, mag 1.96, RA 9.3686h, Dec -55.0107deg)
- HIP 46651 / HIP 46651 (HIP 46651, mag 3.60, RA 9.5117h, Dec -40.4668deg) [no display name]
- HIP 48774 / HIP 48774 (HIP 48774, mag 3.52, RA 9.9477h, Dec -54.5678deg) [no display name]
- HIP 50191 / HIP 50191 (HIP 50191, mag 3.85, RA 10.2456h, Dec -42.1219deg) [no display name]
- HIP 51986 / HIP 51986 (HIP 51986, mag 3.84, RA 10.6217h, Dec -48.2256deg) [no display name]
- HIP 52727 / HIP 52727 (HIP 52727, mag 2.69, RA 10.7795h, Dec -49.4203deg) [no display name]

## VIR -- Virgo / おとめ座

Counts: stars 14, edges 14, polylines 1, branch points 3, stars without display names 9

### Polylines

1. HIP 60129 -> HIP 58948 -> HIP 57380 -> Zavijava -> HIP 60129 -> Porrima -> HIP 63090 -> Vindemiatrix -> HIP 63090 -> Porrima -> HIP 64238 -> Spica -> HIP 64238 -> Porrima -> Heze -> HIP 68520 -> HIP 72220 -> HIP 68520 -> Heze -> HIP 69701 -> HIP 71957

### Edges

- HIP 57380 -- Zavijava  |  HIP 57380 -- ザヴィヤヴァ
- HIP 57380 -- HIP 58948  |  HIP 57380 -- HIP 58948
- Zavijava -- HIP 60129  |  ザヴィヤヴァ -- HIP 60129
- HIP 58948 -- HIP 60129  |  HIP 58948 -- HIP 60129
- HIP 60129 -- Porrima  |  HIP 60129 -- ポリマ
- Porrima -- HIP 63090  |  ポリマ -- HIP 63090
- Porrima -- HIP 64238  |  ポリマ -- HIP 64238
- Porrima -- Heze  |  ポリマ -- ヘゼ
- HIP 63090 -- Vindemiatrix  |  HIP 63090 -- ヴィンデミアトリックス
- HIP 64238 -- Spica  |  HIP 64238 -- スピカ
- Heze -- HIP 68520  |  ヘゼ -- HIP 68520
- Heze -- HIP 69701  |  ヘゼ -- HIP 69701
- HIP 68520 -- HIP 72220  |  HIP 68520 -- HIP 72220
- HIP 69701 -- HIP 71957  |  HIP 69701 -- HIP 71957

### Branch Points

- HIP 60129 / HIP 60129 (HIP 60129): degree 3
- Porrima / ポリマ (HIP 61941): degree 4
- Heze / ヘゼ (HIP 66249): degree 3

### Stars

- HIP 57380 / HIP 57380 (HIP 57380, mag 4.04, RA 11.7643h, Dec 6.5294deg) [no display name]
- Zavijava / ザヴィヤヴァ (HIP 57757, mag 3.59, RA 11.8449h, Dec 1.7647deg)
- HIP 58948 / HIP 58948 (HIP 58948, mag 4.12, RA 12.0868h, Dec 8.7330deg) [no display name]
- HIP 60129 / HIP 60129 (HIP 60129, mag 3.89, RA 12.3318h, Dec -0.6668deg) [no display name]
- Porrima / ポリマ (HIP 61941, mag 2.74, RA 12.6943h, Dec -1.4494deg)
- HIP 63090 / HIP 63090 (HIP 63090, mag 3.39, RA 12.9267h, Dec 3.3975deg) [no display name]
- Vindemiatrix / ヴィンデミアトリックス (HIP 63608, mag 2.85, RA 13.0363h, Dec 10.9591deg)
- HIP 64238 / HIP 64238 (HIP 64238, mag 4.38, RA 13.1658h, Dec -5.5390deg) [no display name]
- Spica / スピカ (HIP 65474, mag 0.98, RA 13.4199h, Dec -11.1613deg)
- Heze / ヘゼ (HIP 66249, mag 3.38, RA 13.5782h, Dec -0.5958deg)
- HIP 68520 / HIP 68520 (HIP 68520, mag 4.23, RA 14.0274h, Dec 1.5445deg) [no display name]
- HIP 69701 / HIP 69701 (HIP 69701, mag 4.07, RA 14.2669h, Dec -6.0005deg) [no display name]
- HIP 71957 / HIP 71957 (HIP 71957, mag 3.87, RA 14.7177h, Dec -5.6582deg) [no display name]
- HIP 72220 / HIP 72220 (HIP 72220, mag 3.73, RA 14.7708h, Dec 1.8929deg) [no display name]

## VOL -- Volans / とびうお座

Counts: stars 5, edges 6, polylines 1, branch points 1, stars without display names 1

### Polylines

1. Alpha Volantis -> Beta Volantis -> HIP 39794 -> Delta Volantis -> Gamma2 Volantis -> HIP 39794 -> Alpha Volantis

### Edges

- Gamma2 Volantis -- Delta Volantis  |  ガンマ2・とびうお -- デルタ・とびうお
- Gamma2 Volantis -- HIP 39794  |  ガンマ2・とびうお -- HIP 39794
- Delta Volantis -- HIP 39794  |  デルタ・とびうお -- HIP 39794
- HIP 39794 -- Beta Volantis  |  HIP 39794 -- ベータ・とびうお
- HIP 39794 -- Alpha Volantis  |  HIP 39794 -- アルファ・とびうお
- Beta Volantis -- Alpha Volantis  |  ベータ・とびうお -- アルファ・とびうお

### Branch Points

- HIP 39794 / HIP 39794 (HIP 39794): degree 4

### Stars

- Gamma2 Volantis / ガンマ2・とびうお (HIP 34481, mag 3.78, RA 7.1458h, Dec -70.4989deg)
- Delta Volantis / デルタ・とびうお (HIP 35228, mag 3.98, RA 7.2805h, Dec -67.9572deg)
- HIP 39794 / HIP 39794 (HIP 39794, mag 4.35, RA 8.1322h, Dec -68.6171deg) [no display name]
- Beta Volantis / ベータ・とびうお (HIP 41312, mag 3.75, RA 8.4289h, Dec -66.1369deg)
- Alpha Volantis / アルファ・とびうお (HIP 44382, mag 4.00, RA 9.0408h, Dec -66.3958deg)

## VUL -- Vulpecula / こぎつね座

Counts: stars 2, edges 1, polylines 1, branch points 0, stars without display names 1

### Polylines

1. Anser -> HIP 97886

### Edges

- Anser -- HIP 97886  |  アンサー -- HIP 97886

### Stars

- Anser / アンサー (HIP 95771, mag 4.44, RA 19.4784h, Dec 24.6649deg)
- HIP 97886 / HIP 97886 (HIP 97886, mag 4.57, RA 19.8910h, Dec 24.0796deg) [no display name]

