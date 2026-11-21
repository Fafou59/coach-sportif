# 01 — Répartition des intensités

Ce fichier fixe comment le coach répartit le temps d'entraînement entre facile, modéré et dur, combien de séances dures il programme et comment il les espace. Il utilise le modèle en 3 intensités de Seiler, nommées comme les bandes FC (CONTEXT) pour ne pas les confondre avec les zones Z1–Z5 de Garmin : **Facile** (sous le 1er seuil, SV1/LT1), **Seuil** (entre les seuils), **Au-dessus** (au-dessus du 2e seuil, SV2/LT2/vitesse critique) (décision du 17/11/2026). Les correspondances avec les zones détaillées sont dans le fichier 02.

## Règles

**1. Majorité du volume en bande Facile**
- **Règle** : programmer la grande majorité du temps d'entraînement en endurance facile (bande Facile), quel que soit le modèle choisi.
- **Valeur par défaut** (révisée le 16/11/2026) : la répartition est un **indicateur suivi au bilan, pas une règle bloquante**. Repère : ≈ 80/20 (temps en bande Facile / hors bande Facile) au-dessus de 5 h/semaine, jusqu'à 70/30 en dessous. Le temps en bande Facile se lit dans Garmin comme le temps en Z1 + Z2 (Friel en course, Coggan à vélo), pas dans la seule Z1 (17/11/2026). Alerte seulement si le temps Au-dessus dépasse 30 % plusieurs semaines de suite. Sous ≈ 7 séances/semaine, compter en **temps**, pas en pourcentage de séances. Les contraintes réelles sont le budget de séances dures (règle 3), l'écart entre séances dures (règle 4) et la progression (fichier 03).
- **Indice** : B (principe, chez l'élite) — règle ; C (repères 80/20 et 70/30, alerte Au-dessus > 30 %) — indicateur.
- **Niveau de preuve** : Moyen chez l'élite (études descriptives convergentes, ≈ 75–90 % du temps en bande Facile). **Non démontré chez l'amateur** : chez des récréatifs, 77 % contre 40–46 % du temps en bande Facile donnent des gains similaires à court terme (Muñoz 2014, Festa 2020), sans données sur les blessures ni sur une saison. Voir `recherches/seance-complementaire-et-tests.md`.
- **Sources** : Seiler & Kjerland, 2006, *Scand J Med Sci Sports*, doi:10.1111/j.1600-0838.2004.00418.x ; Seiler, 2010, *IJSPP*, doi:10.1123/ijspp.5.3.276 ; Casado et al., 2022, *IJSPP*, doi:10.1123/ijspp.2021-0435.

**2. Modèle par défaut : pyramidal ; polarisé en option**
- **Règle** : utiliser une répartition pyramidale (Facile > Seuil > Au-dessus) en phase de base et pour les amateurs. Passer éventuellement à une répartition plus polarisée (peu de Seuil, Au-dessus un peu plus présent) dans les 6–8 semaines avant l'objectif, chez les athlètes confirmés.
- **Valeur par défaut** : pas de répartition cible en trois bandes ; la répartition se suit en indicateur (règle 1). À titre descriptif seulement, les études décrivent le pyramidal autour de 80 / 15 / 5 % du temps (Facile / Seuil / Au-dessus) et le polarisé autour de 80 / 5 / 15 % (retiré comme cible le 17/11/2026).
- **Indice** : A (équivalence des deux modèles, Rosenblat 2025) — règle ; C (polarisé en phase spécifique, Filipas) — valeur de départ.
- **Niveau de preuve** : Moyen.
  - Stöggl & Sperlich (2014) et Rosenblat (2019) trouvent un avantage au polarisé face au « seuil » ou au « haut volume ».
  - La méta-analyse de Silva Oliveira (2024) ne trouve un avantage qu'en VO2max, surtout pour les interventions < 12 semaines et les athlètes très entraînés, et aucun sur la performance en contre-la-montre.
  - La méta-analyse sur données individuelles de Rosenblat (2025) ne trouve aucune différence globale entre polarisé et pyramidal. Dans une analyse en sous-groupe, le pyramidal semble plus favorable aux récréatifs.
  - Filipas (2022) observe que l'enchaînement pyramidal puis polarisé donne les meilleurs résultats.
- **Sources** :
  - Stöggl & Sperlich, 2014, *Front Physiol*, doi:10.3389/fphys.2014.00033
  - Rosenblat et al., 2019, *J Strength Cond Res*, doi:10.1519/JSC.0000000000002618
  - Silva Oliveira, Boppre & Fonseca, 2024, *Sports Med* 54:2071–2095, doi:10.1007/s40279-024-02034-z
  - Rosenblat et al., 2025, *Sports Med* 55:655–673, doi:10.1007/s40279-024-02149-3
  - Filipas et al., 2022, *Scand J Med Sci Sports* 32:498–511, doi:10.1111/sms.14101
  - Casado et al., 2022 (voir règle 1)
- **Adaptation par niveau** :
  - Débutant : quasi 100 % en bande Facile, avec des éléments de vitesse courts (lignes droites).
  - Intermédiaire : pyramidal.
  - Confirmé : pyramidal en base, puis polarisé possible en phase spécifique.

**3. Nombre de séances dures par semaine**
- **Règle** : limiter le nombre de séances « dures » par semaine, en comptant ensemble course et vélo. Une séance est dure si son objectif principal est dans le haut de la bande Seuil ou Au-dessus (seuil, VMA, PMA, répétitions en côte de plus de 15 s, fractionné). Les sprints en côte de 15 s au plus, avec récupération complète, restent hors budget comme les lignes droites (règle 8 ; décision du 17/11/2026).
- **Valeur par défaut** : 2 séances dures par semaine. Jamais plus de 3, sortie longue incluse si elle contient de l'allure spécifique.
- **Indice** : C — valeur de départ (budget 0–1 / 1–2 / 2) ; garde-fou de prudence, non prouvé (plafond de 3 ; débutant sans séance dure les 4–8 premières semaines).
- **Niveau de preuve** : Faible (abaissé le 17/11/2026 : le fichier disait Moyen). La pratique observée chez l'élite comme chez les sous-élites est d'environ 2 séances intenses par semaine. Le plafond chez l'amateur est extrapolé.
- **Sources** : Seiler, 2010 (voir règle 1) ; Casado et al., 2022 (voir règle 1), qui recommande l'alternance jour dur / jour facile.
- **Adaptation par niveau** :
  - Débutant : 0 séance dure pendant les 4–8 premières semaines, puis 1.
  - Intermédiaire : 1–2.
  - Confirmé : 2, et 3 de façon ponctuelle (bloc court, puis allègement).

**4. Espacement des séances dures**
- **Règle** (révisée le 17/11/2026) : espacer deux séances dures (course ou vélo) de 48 h par défaut, avec une journée facile ou de repos entre elles.
- **Valeur par défaut** :
  - 48 h entre deux séances dures.
  - Tolérance : 24 h pour un confirmé, si la 2e séance est au Seuil et qu'aucune métrique de récupération ne dérive (fichier 08).
  - Pas de renforcement lourd des membres inférieurs dans les 24 h **avant** une séance dure ; placement le lendemain ou le même jour après la séance dure, selon le fichier 07 (règle 6).
- **Indice** : C (écart de 48 h) — valeur de départ ; B (pas de renfo lourd dans les 24 h avant, Doma) — règle.
- **Niveau de preuve** : Faible pour le délai de 48 h (abaissé le 17/11/2026 : le fichier disait Moyen) : il repose sur la cinétique de la VFC, pas sur un critère de blessure ou de performance. Faible pour le placement du renforcement, qui relève surtout de la pratique.
  - Après une séance au-dessus de SV1, la récupération de la VFC est plus lente qu'après une séance facile.
  - La réactivation parasympathique peut prendre 24–48 h après une séance de haute intensité.
- **Sources** : Seiler, Haugen & Kuffel, 2007, *Med Sci Sports Exerc* 39:1366–1373, doi:10.1249/mss.0b013e318060f17d ; Stanley et al., 2013, *Sports Med*, doi:10.1007/s40279-013-0083-4.

**5. Comment compter l'intensité : objectif de séance d'abord, temps en zone ensuite**
- **Règle** : planifier et contrôler la répartition à l'échelle de la séance (méthode « session goal »). Utiliser le temps passé en zone (FC, allure, puissance) seulement comme contrôle secondaire.
- **Valeur par défaut** :
  - Classer chaque séance comme Facile, Seuil ou Au-dessus selon son objectif principal.
  - Pas de cible en pourcentage de séances (la cible « 75–80 % des séances en Z1 » est retirée le 17/11/2026 : la répartition se lit en temps, règle 1).
  - Pour lire du temps en zone de FC, appliquer un facteur ≈ ×3 sur la part Seuil + Au-dessus pour retrouver la logique « séance ».
- **Indice** : B (comptage par objectif de séance, Sylta 2014) — règle ; C (facteur ≈ × 3) — valeur de départ.
- **Niveau de preuve** : Moyen. Sylta et al. (2014) montrent que le temps en zone de FC sous-estime d'environ 3 fois la part d'intensité haute par rapport à l'objectif de séance. La FC est en retard pendant les fractions, et l'échauffement et le retour au calme sont comptés en bande Facile.
- **Sources** : Sylta, Tønnessen & Seiler, 2014, *IJSPP* 9:100–107, doi:10.1123/ijspp.2013-0298.

**6. Multi-sport (course + vélo)**
- **Règle** : faire un seul budget de séances dures pour tous les sports, et tenir des seuils et des zones séparés par sport.
- **Valeur par défaut** :
  - Les séances dures de vélo comptent dans le maximum hebdomadaire de la règle 3.
  - Le vélo sert en priorité à ajouter du volume facile sans charge d'impact.
  - Les zones de FC de course ne doivent jamais être appliquées telles quelles au vélo.
- **Indice** : B (zones séparées par sport, Millet) — règle ; D (budget commun course + vélo) — garde-fou de prudence, non prouvé ; C (vélo = volume facile sans impact) — valeur de départ.
- **Niveau de preuve** : Moyen pour la spécificité des seuils et le transfert. Faible pour le budget commun, qui est déduit logiquement.
  - La VO2max et les seuils sont spécifiques à chaque activité.
  - La FC diffère entre course et vélo, aux intensités maximales comme sous-maximales. En pratique elle est souvent plus basse à vélo, mais la direction et l'ampleur n'ont pas été vérifiées dans le texte intégral.
  - Le transfert d'entraînement est plus important de la course vers le vélo que l'inverse.
- **Sources** : Millet, Vleck & Bentley, 2009, *Sports Med* 39:179–206, doi:10.2165/00007256-200939030-00002.

**7. Amateurs à faible volume**
- **Règle** : quand le volume total est faible (< 5 h/semaine), garder le budget de séances dures du niveau (règle 3, jusqu'à 2) et ne pas réduire l'intensité sous prétexte de polarisation. La séance dure représente alors une part plus élevée du temps total, et c'est acceptable.
- **Valeur par défaut** : sous 5 h/semaine, jusqu'à ≈ 30 % du temps hors bande Facile (repère 70/30 de la règle 1 ; harmonisé le 17/11/2026, le fichier disait « < 4 h : 25–30 % »).
- **Indice** : C — valeur de départ.
- **Niveau de preuve** : Faible. Les études chez les récréatifs (Muñoz, 2014 ; Festa, 2020) sont petites. Le résultat en sous-groupe de Rosenblat (2025) va dans le sens du pyramidal.
- **Sources** : Muñoz et al., 2014, *IJSPP* 9:265–272, doi:10.1123/ijspp.2012-0350 ; Festa et al., 2020, *Front Sports Act Living*, doi:10.3389/fspor.2019.00070 ; Rosenblat et al., 2025 (voir règle 2).

**8. Séance principale et séance à la carte**
- **Règle** (validée le 16/11/2026) : quand un athlète a droit à 2 séances dures, la semaine en contient une **principale**, prioritaire, et une **à la carte**.
  - Principale : porte la qualité du bloc, placée après un jour facile, protégée en premier quand la semaine se complique. Déplaçable dans la semaine. (Le « verrouillage » et l'obligation d'en parler au coach avant de la supprimer, sans fondement, sont retirés le 17/11/2026.)
  - À la carte : menu de 4 options, toutes dans les garde-fous, **décrites par leur contenu** (décision du 17/11/2026 ; les anciens % de charge, sans source, sont retirés). Repères pour un intermédiaire, adaptés par le coach au niveau et à la qualité de la principale :

    | Option | Contenu de départ | Séance dure ? |
    |---|---|---|
    | Aucune | EF classique | Non |
    | Légère | EF + 6 × 15 s de lignes droites | Non |
    | Moyenne | 10–15 min cumulés au Seuil (ex. 3 × 4 min) | Oui |
    | Soutenue | 20–25 min cumulés au Seuil, ou 8–10 min au Seuil haut ou à la VMA (ex. 8 × 1 min) | Oui |

    La Soutenue reste moins chargée que la principale.
  - **Deux qualités différentes** (décision Q129 du 21/11/2026) : la principale porte la qualité principale du bloc ; une à la carte Moyenne ou Soutenue travaille une autre qualité (ex. VMA en principale, seuil ou côtes en à la carte ; principale au seuil, à la carte en côtes ou VMA). Exception : l'affûtage, où les deux séances restent courtes, à l'allure de course. L'athlète peut demander autrement. Indice D (habitude de coach, non prouvée) : mélanger les qualités dans la semaine équivaut à les séquencer (Sylta 2016). Hors option Légère, elle compte dans le budget de séances dures et dans les 48 h. Jamais d'endurance de vitesse (dont les sprints de 30 s) en à la carte, quel que soit le niveau ; pour un confirmé qui prépare un 5–10 km, elle reste possible en séance principale (décision du 17/11/2026).
  - Le coach recommande une option selon l'état de la semaine ; si une métrique de récupération dérive, il ne propose que Aucune ou Légère. Seule l'option validée (« GO ») est créée dans Garmin ; pour en changer, l'athlète le demande au coach.
  - Accès : intermédiaire ou confirmé, ≈ 3 h 30/semaine et au moins 4 séances, après au moins 4 semaines avec une séance dure bien tolérée. Débutant : non. Si la sortie longue contient de l'allure spécifique, l'à la carte de l'intermédiaire est limitée à Aucune ou Légère.
- **Lignes droites et sprints courts** (≤ 15 s, à plat ou en côte, récupération complète, ≥ 2 min pour les sprints courts ; CONTEXT) : ajoutés à la fin d'une séance d'EF, hors budget, hors règle des 48 h. Les répétitions en côte de plus de 15 s font une séance dure (règle 3 ; décision du 17/11/2026).
- **Indice** : C (principe principale + à la carte, indirect ; principale prioritaire, protégée en premier) — valeur de départ ; D (contenus et durées des options) — valeur de départ ; C (lignes droites et sprints courts hors budget) — valeur de départ ; D (pas d'endurance de vitesse ni de sprints de 30 s en à la carte, tous niveaux) — garde-fou de prudence, non prouvé.
- **Niveau de preuve** : Faible pour les seuils chiffrés (conventions). Moyen pour le principe : l'intensité choisie améliore le ressenti (Andrade 2024, revue de 29 études) ; l'ajustement à l'état du jour ne coûte pas en performance et réduit les non-répondeurs (Düking 2021) ; mélanger les qualités dans la semaine équivaut à les séquencer (Sylta 2016). Aucune étude ne compare directement « 1 principale + 1 plus légère » à « 2 séances aussi dures ».

## Ce qui ne fait pas consensus

- **Polarisé ou pyramidal** : les méta-analyses divergent selon la façon de mesurer la répartition (temps en zone ou séance) et selon le critère étudié (VO2max ou performance). Aucune ne montre de supériorité nette sur la performance chez l'amateur.
- **Définition des zones** : les études utilisent des seuils différents (ventilatoires, lactate, %FCmax). La même semaine peut donc apparaître « polarisée » ou « pyramidale » selon la méthode.
- **Plafond de séances dures chez l'amateur** : ce n'est pas un résultat d'essai contrôlé, c'est une extrapolation de la pratique élite.
- **Classement de la sortie longue** : elle est facile physiologiquement, mais coûteuse en fatigue mécanique. Son classement comme « séance clé » est une convention de coaching.
- **Interférence course/vélo/renforcement chez l'amateur** : il y a peu de données directes.

## Décisions validées (14, 16 et 17/11/2026)

| Paramètre | Recommandation |
|---|---|
| Modèle par défaut | Pyramidal ; polarisé optionnel pour les confirmés en phase spécifique ; pas de répartition cible en trois bandes (17/11) |
| Nommage des 3 intensités de Seiler | Bandes Facile / Seuil / Au-dessus, jamais Z1/Z2/Z3 (réservés aux zones Garmin) (17/11) |
| Répartition des intensités | Indicateur, pas règle : ≈ 80/20 en temps en bande Facile (Garmin : Z1 + Z2 de Friel ou Coggan) au-dessus de 5 h/sem., jusqu'à 70/30 en dessous ; alerte si Au-dessus > 30 % plusieurs semaines (17/11) |
| Séances dures/semaine (débutant / intermédiaire / confirmé) | 0–1 / 1–2 / 2 (3 au maximum) |
| Écart entre deux séances dures | 48 h par défaut ; 24 h tolérées pour un confirmé si la 2e séance est au Seuil et qu'aucune métrique ne dérive (17/11) |
| Méthode de comptage | Objectif de séance (principale), temps en zone (contrôle) ; pas de cible en % de séances (17/11) |
| Sortie longue comptée comme séance dure | Oui si elle contient de l'allure spécifique, quelle que soit sa durée, sinon non (elle reste une séance clé dans tous les cas) (17/11) |
| Côtes | Répétitions en côte de plus de 15 s = séance dure ; sprints en côte ≤ 15 s avec récupération complète = hors budget, comme les lignes droites (17/11) |
| Budget commun course + vélo | Oui |
| Séance principale / à la carte | Règle 8 : principale prioritaire, protégée en premier, plus « verrouillée » (17/11) ; pas d'endurance de vitesse en à la carte, tous niveaux ; possible en principale pour un confirmé qui prépare un 5–10 km (17/11) |
