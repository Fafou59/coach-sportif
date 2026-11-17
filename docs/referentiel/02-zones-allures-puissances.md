# 02 — Zones, allures et puissances

Ce fichier fixe comment le coach définit les zones d'intensité de chaque athlète en course (VMA, vitesse critique, seuil), à vélo (FTP, puissance critique) et en fréquence cardiaque. Il précise comment estimer ces zones à partir de l'historique Garmin ou d'un test, et quand les recalibrer. Toutes les zones détaillées se rattachent aux 3 bandes Facile / Seuil / Au-dessus du fichier 01 (modèle de Seiler).

## Règles

**1. Ancrer les zones sur des seuils individuels, pas sur des % de maximum**
- **Règle** : calculer les zones à partir d'un repère de seuil (vitesse critique ou allure seuil, FTP ou puissance critique, FC au seuil) plutôt qu'à partir de %FCmax ou %VO2max.
- **Valeur par défaut** : repère principal = allure seuil ou vitesse critique en course, FTP à vélo.
- **Indice** : B (Iannetta : seuil lactique entre 60 et 90 % de la FCmax) — règle.
- **Niveau de preuve** : Élevé.
  - Iannetta et al. (2020, n = 100) : le seuil lactique se situe entre 60 et 90 % de la FCmax selon les individus, et le MLSS entre 75 et 97 %.
  - Des pourcentages fixes ne placent donc pas les athlètes dans le même domaine métabolique.
- **Sources** : Iannetta et al., 2020, *Med Sci Sports Exerc* 52:466–473, doi:10.1249/MSS.0000000000002147 ; Jamnick et al., 2020, *Sports Med*, doi:10.1007/s40279-020-01322-8 ; Jones et al., 2019, *Physiol Rep*, doi:10.14814/phy2.14098.

**2. Course : allures calculées depuis la vitesse critique (ou une course), % VMA en simple conversion**
- **Règle** (révisée le 17/11/2026) : calculer les allures depuis la vitesse critique (CS) ou depuis une course récente (règle 9). Le % VMA n'est qu'une conversion affichée, parce que c'est l'usage habituel en France, avec des fourchettes larges ; il ne sert pas à fixer une allure.
- **Valeur par défaut** : voir les tableaux A et A bis plus bas (colonne % CS = référence ; colonne % VMA = conversion indicative).
- **Indice** : D (fourchettes en % VMA) — valeur de départ.
- **Niveau de preuve** : Faible (abaissé le 17/11/2026 : le fichier disait Faible à Moyen).
  - Le concept de vitesse critique est solide.
  - Les pourcentages de VMA sont des conventions de coaching, issues de sources secondaires : manuels de Billat et de Cazorla, tables VDOT de Daniels. Le seuil varie entre environ 75 et 92 % de la VMA selon le niveau de l'athlète.
  - Le rapport CS/VMA n'est pas établi : il dépend du niveau et du protocole du test VMA (estimation de la note de recherche : CS ≈ 85–90 % de la VMA chez l'amateur, confiance faible).
- **Sources** :
  - Jones & Vanhatalo, 2017, *Sports Med* 47(S1):65–78, doi:10.1007/s40279-017-0688-0
  - Daniels, *Daniels' Running Formula*, Human Kinetics (livre, **source secondaire**)
  - Pourcentages de VMA : **sources secondaires** (manuels et sites de coaching francophones). Aucune publication de référence unique n'a été vérifiée.

**3. Vitesse critique estimée depuis Garmin**
- **Règle** : estimer la vitesse critique (CS) à partir des meilleurs efforts récents enregistrés par la montre, sur au moins 3 efforts quasi maximaux.
- **Valeur par défaut** :
  - Données : au moins 3 efforts quasi maximaux de **3 à 20 min** (domaine de validité du modèle), sur les **6 à 16 dernières semaines** (fenêtre de Smyth & Muniz-Pumares). Si les efforts n'étaient pas maximaux, la CS obtenue est un plancher.
  - Calcul : CS = pente de la droite distance–temps.
  - Allure marathon visée : environ 80 % de CS pour un marathon en 5–6 h, environ 93 % pour 2 h 30. Au-delà de 94 % de CS sur le premier semi, le risque de forte baisse d'allure en seconde moitié augmente.
- **Indice** : B en groupe, C pour un individu (CS depuis l'historique ; allure marathon en % CS, Smyth) — règle ; C (domaine 3–20 min, fenêtre de 6–16 semaines) — valeur de départ.
- **Niveau de preuve** : Moyen en groupe, Faible pour un individu. Étude sur plus de 25 000 coureurs récréatifs, avec une erreur de prédiction d'environ 8 % (Smyth & Muniz-Pumares, 2020) ; accord individuel modeste avec des contre-la-montre (r = 0,67, Hunter et al. 2023, voir `recherches/construction-tableau-allures.md`).
- **Sources** : Smyth & Muniz-Pumares, 2020, *Med Sci Sports Exerc* 52:2637–2645, doi:10.1249/MSS.0000000000002412, PMC7664951.

**4. Tests de terrain proposés (course)**
- **Règle** (validée le 16/11/2026) : le coach propose les tests adaptés au niveau de l'athlète, avec leur fiabilité et leurs contraintes ; l'athlète choisit. Une VMA ne vaut qu'avec son protocole : le carnet note toujours quel test a donné la valeur. Aucun test maximal pendant le garde-fou de la règle 9.
- **Valeur par défaut** : 5 tests proposés.
- **Indice** : B (tests au choix, protocole noté, Kuipers) — règle ; D (accès du débutant aux tests maximaux après 3 mois de pratique) — garde-fou de prudence, non prouvé.

| Test | Donne | Fiabilité | Pour qui | Contraintes |
|---|---|---|---|---|
| 5 km / parkrun | Allure 5 km ; CS avec une 2e course | Moyen (CV ≈ 1–2 %, Hurst & Board 2016, Laursen 2007) | Tous (débutant après 3 mois) | Gratuit, chronométré ; le peloton aide à gérer l'allure |
| Demi-Cooper (6 min) | VMA | Faible à Moyen (r = 0,94 avec le tapis pour un test de **5 min**, Berthon 1997 ; le format de 6 min n'est pas celui validé) | Débutant après 3 mois de pratique (garde-fou de la règle 9), intermédiaire, confirmé | Piste, gestion d'allure |
| Chrono 30 min | Allure seuil + FC au seuil | Moyen (± 0,21 m/s, ± 8 bpm, McGehee 2005) | Intermédiaire, confirmé | Plat, ceinture cardio, effort long |
| 3 chronos 1 200 / 2 400 / 3 600 m | Vitesse critique | Moyen (CV 0,4 %, Galbraith 2014) | Confirmé | Piste, 30 min entre chaque effort |
| Test de la parole | Borne haute de l'EF | Moyen (Persinger 2004) | Tous | Aucun |

- **Non proposés** (voir `recherches/seance-complementaire-et-tests.md`) : UMTT (valide mais logistique lourde, retiré par l'utilisateur), VAMEVAL (pas de validation primaire), 45-15 (VMA ≈ 13 % au-dessus du tapis, % non transposables), 3 min à fond (l'amateur gère mal le départ), navette 20 m (sous-estime la VMA du coureur), chrono 1 500 m (validé chez l'élite seulement, n'apporte rien de plus que le demi-Cooper).
- **Sources** : Berthon et al., 1997, *Eur J Appl Physiol* 75:233–238, doi:10.1007/s004210050153 ; autres références dans la note de recherche.

**5. Vélo : zones de Coggan en % FTP**
- **Règle** : calculer les zones de puissance à partir de la FTP selon le modèle de Coggan (tableau B plus bas).
- **Valeur par défaut** : FTP ≈ 95 % de la puissance moyenne d'un test de 20 min à fond, échauffement inclus.
- **Indice** : C (Borszcz, Lillo-Bevia) — valeur de départ.
- **Niveau de preuve** : Moyen.
  - Borszcz et al. (2019) : la FTP sur 20 min est proche du MLSS (biais +1,4 %, r = 0,91), mais l'erreur individuelle est plus grande chez les cyclistes moins entraînés.
  - Lillo-Bevia et al. (2022) : le facteur 0,95 surestime le MLSS d'environ 12 W.
  - Les zones elles-mêmes sont une convention (**source secondaire**).
- **Sources** :
  - Allen & Coggan, *Training and Racing with a Power Meter*, VeloPress (livre, **source secondaire**)
  - Borszcz, Tramontin & Costa, 2019, *IJSPP* 14:1029–1035, doi:10.1123/ijspp.2018-0572
  - Lillo-Bevia et al., 2022, *J Strength Cond Res* 36:167–173, doi:10.1519/JSC.0000000000003403, PMID 31714462

**6. Estimer la FTP sans test**
- **Règle** : estimer la FTP à partir de la courbe puissance-durée Garmin si elle contient un effort maximal de 20 min datant de moins de 6 semaines. Sinon, proposer un test de 20 min ou un test rampe.
- **Valeur par défaut** :
  - Depuis l'historique : meilleure puissance 20 min × 0,95.
  - Test rampe : 75 % de la meilleure minute.
  - Si plusieurs efforts maximaux de 3 à 12 min sont disponibles, préférer un calcul de puissance critique.
- **Indice** : D (test rampe à 75 % de la meilleure minute) — valeur de départ.
- **Niveau de preuve** :
  - Faible pour le test rampe : le facteur 0,75 vient des plateformes d'entraînement (**source secondaire**) et n'a pas été vérifié dans une étude publiée.
  - Moyen pour la puissance critique.
- **Sources** : Jones & Vanhatalo, 2017 (voir règle 2).

**7. Zones de fréquence cardiaque**
- **Règle** :
  - Baser les zones FC sur la FC au seuil (LTHR), et non sur la FCmax théorique.
  - Utiliser la FC comme contrôle des séances longues et faciles, pas pour piloter les fractions courtes.
  - Tenir des zones FC séparées pour la course et pour le vélo.
- **Valeur par défaut** :
  - **LTHR course** : FC moyenne des 20 dernières minutes d'un effort solo de 30 min à fond, ou d'une course de 10 km à fond.
  - **Deux systèmes, deux vocabulaires** (décision du 17/11/2026) :
    - **Prescription : 3 bandes**, calées sur le modèle en 3 intensités de Seiler (fichier 01), nommées par des mots pour éviter toute confusion avec Z1–Z5 : **Facile** / **Seuil** / **Au-dessus**. Course (regroupement Friel) : Facile < 90 % LTHR ; Seuil 90–99 % ; Au-dessus ≥ 100 %. Vélo (regroupement Coggan) : Facile < 84 % LTHR ; Seuil 84–105 % ; Au-dessus > 105 %. Ce sont les cibles des séances dans Garmin. Le plafond de la bande Facile est individualisé au test de la parole (il peut être sous 90 % LTHR). Raison : une bande de 5 % de LTHR (≈ 8 bpm) est de l'ordre de l'erreur de mesure (McGehee) et de la dérive cardiaque au cours d'une sortie longue.
    - **Analyse : 5 zones Z1–Z5** de Friel (course) et de Coggan (vélo), réglées dans les zones FC du compte Garmin **après « GO »** de l'athlète (modification d'un réglage du compte). Elles servent au temps passé par zone et à la comparaison avec Garmin et les autres applis, jamais aux cibles de séance. Friel Z1 < 85 % LTHR ; Z2 85–89 % ; Z3 90–94 % ; Z4 95–99 % ; Z5 ≥ 100 %. Coggan Z1 < 68 % ; Z2 69–83 % ; Z3 84–94 % ; Z4 95–105 % ; Z5 > 105 %.
  - **FCmax** : en dernier recours seulement, 208 − 0,7 × âge, avec un écart-type d'environ ±10 bpm. Préférer la FC maximale observée en course.
- **Indice** : B (FC sur la LTHR, McGehee ; limites de la FCmax théorique, Tanaka) — règle ; D (bornes en % LTHR) — valeur de départ.
- **Niveau de preuve** :
  - Moyen pour les limites de la FCmax théorique (Tanaka, 2001 ; Iannetta, 2020).
  - Faible pour les pourcentages de LTHR, qui viennent de sources secondaires.
  - Moyen pour l'écart entre sports : la FC diffère entre course et vélo.
- **Sources** :
  - Tanaka, Monahan & Seals, 2001, *J Am Coll Cardiol* 37:153–156, doi:10.1016/S0735-1097(00)01054-8
  - Friel, *The Triathlete's Training Bible* (livre, **source secondaire**)
  - Millet et al., 2009, *Sports Med*, doi:10.2165/00007256-200939030-00002

**8. Estimations automatiques Garmin**
- **Règle** : traiter la VO2max, le seuil lactique et la FTP estimés par Garmin comme des indicateurs de tendance, jamais comme une valeur de référence quand une course ou un test récent est disponible.
- **Valeur par défaut** : ordre de priorité des sources :
  1. Course récente ou test
  2. Meilleurs efforts de l'historique (CS ou 20 min)
  3. Estimation Garmin
  4. Formule théorique
- **Indice** : B (Heiber, Lu) — règle.
- **Niveau de preuve** : Moyen (pour la non-fiabilité). Deux études indépendantes trouvent l'allure au seuil Garmin fausse dans les deux sens selon le modèle (−12 % sur Fenix 7, +2,2 km/h sur Forerunner 265) ; le prédicteur de course n'est validé que par une thèse (semi ≈ 5,5 % trop rapide). Voir `recherches/construction-tableau-allures.md`.

**9. Construction du tableau d'allures au démarrage (cascade)**
- **Règle** (validée le 16/11/2026) : suivre la cascade ci-dessous. **Quel que soit le résultat, le coach estime toujours les allures**, en indiquant son degré de confiance (élevé, moyen, faible), et **propose tous les tests adaptés** à l'athlète pour affiner, avec leur fiabilité et leur accessibilité (tableau des tests de la règle 4). L'athlète choisit de faire un test ou non.
- **Valeur par défaut** :
  - **Garde-fou** : pas de test maximal moins de 3–4 semaines après un marathon, pendant un retour de blessure, ou chez un débutant de moins de 3 mois de pratique ; partir alors des repères précédents baissés de 5–10 %.
  1. Course sur route plate de moins de 8 semaines (12 si l'entraînement a continué normalement). Avec 2 courses ou plus, exposant de Riegel propre à l'athlète et CS. Riegel prédit un marathon trop rapide d'au moins 10 min pour la moitié des coureurs : ne pas extrapoler le marathon depuis une course courte sans correction.
  2. Sinon, CS depuis les données d'entraînement (règle 3).
  3. Sinon, estimation de faible confiance (historique, test de la parole, estimation Garmin en dernier recours) et test terrain proposé, placé en semaine d'allègement.
  - Limite haute de l'EF : vérifiée au test de la parole, quel que soit le niveau.
- **Indice** : B (cascade course > CS > estimation ; pas de Riegel brut au marathon, Vickers) — règle ; D (récence de 8 ou 12 semaines) — valeur de départ ; D (pas de test maximal après un marathon, une blessure ou avant 3 mois de pratique) — garde-fou de prudence, non prouvé.
- **Niveau de preuve** : Moyen pour la hiérarchie des sources (voir `recherches/construction-tableau-allures.md`) ; Faible pour les fenêtres de 8 et 12 semaines (convention).

**10. Recalibrage**
- **Règle** (révisée le 17/11/2026) : à la fin de **chaque** bloc et après chaque course, réestimer les allures **sans plafond**, à partir de la meilleure donnée disponible, et annoncer le niveau de confiance (élevé, moyen, faible). Recalculer plus tôt si de nouvelles données le justifient.
- **Valeur par défaut** :
  - Ordre des données, de la meilleure à la moins bonne :
    1. une course dans le bloc ;
    2. un test (règle 4) ;
    3. une CS recalculée sur au moins 3 efforts quasi maximaux de 3 à 20 min (règle 3) ;
    4. les séances au seuil (RPE, dérive de FC).
  - Aucun plafond de variation par bloc. L'ancien ajustement de ±1–2 % plafonné à ±3 % est retiré : c'était une convention proposée par une note de recherche, sans source, sous le bruit de mesure (erreur individuelle de la CS ≈ 8 %), et il gelait un débutant qui progresse vite.
  - Après 2–3 blocs sans course ni test, proposer un test.
  - Recalcul immédiat si :
    - un nouveau meilleur effort dépasse le repère actuel de plus de 3 % ;
    - les séances au seuil deviennent anormalement faciles ou difficiles, sur au moins 2 séances avec un écart de RPE d'au moins 2 points ;
    - l'athlète reprend après plus de 3 semaines d'arrêt (rabaisser les repères de 5–10 % en attendant des données).
- **Indice** : D — valeur de départ (rythme et ordre des données de recalage).
- **Niveau de preuve** : Faible. C'est une règle de pratique, sans étude dédiée.

**11. Séance sur tapis : pente de 1 % (option sur demande)**
- **Règle** : si l'athlète demande à courir une séance sur tapis, la séance précise une pente de 1 %, pour que les allures correspondent à celles du plat en extérieur.
- **Indice** : C (Jones & Doust, un seul essai, non testé aux allures lentes) — valeur de départ (abaissé le 17/11/2026 : le fichier disait B).
- **Niveau de preuve** : Moyen. Un essai de référence entre ≈ 10,5 et 18 km/h (Jones & Doust 1996) ; non testé à des vitesses plus lentes.
- **Sources** : Jones & Doust, 1996, *J Sports Sci*, doi:10.1080/02640419608727717.

## Tableau A — Course (valeurs par défaut)

Révisé le 17/11/2026. La référence est la colonne seuil / CS ; le % VMA n'est qu'une conversion indicative (**Faible**). Le rapport CS/VMA n'est pas établi : les fourchettes % VMA réunissent la convention de terrain et la conversion depuis la CS avec CS ≈ 85–90 % VMA (note `recherches/week-end-choc-et-allures.md`), d'où leur largeur.

| Bande (Seiler) | Zone détaillée | Repère seuil / CS (référence) | % VMA (conversion, Faible) | Repère pratique |
|---|---|---|---|---|
| Facile | Récupération | — | < 65 % | Très facile |
| Facile | Endurance fondamentale | < SV1, < ~80 % CS | ≈ 65–75 % | Conversation aisée |
| Facile–Seuil | Endurance active / allure marathon | ~80–90 % CS | ≈ 68–83 % | Allure marathon (amateur) |
| Seuil | Seuil / tempo | ≈ 93–97 % CS (≈ MLSS) | ≈ 79–90 % | Allure tenable ≈ 60 min |
| Seuil–Au-dessus | Seuil haut | ≈ 100 % CS | ≈ 85–93 % | Allure tenable ≈ 20–40 min |
| Au-dessus | VMA longue | > CS | ≈ 90–100 % | Allure 3–5 km |
| Au-dessus | VMA courte / vitesse | ≫ CS | 100–110 % | Fractions 30 s à 2 min |

### Tableau A bis — Les 12 allures nommées : table de correspondance

Validé le 16/11/2026 (voir `recherches/week-end-choc-et-allures.md`), fourchettes % VMA élargies le 17/11/2026. Les 12 allures servent **uniquement de langage commun** avec les autres méthodes et applis ; elles ne sont pas toutes utilisées dans les séances. Les allures se calculent depuis la CS ou une course (règle 2) ; % CS : estimations (Faible) ; % VMA : conversion indicative (**Faible**), fourchettes larges qui réunissent la convention de terrain (**sources secondaires**) et la conversion avec CS ≈ 85–90 % VMA, rapport non établi (voir tableau A). Les allures de course se recalent en priorité sur les performances réelles de l'athlète.

| Allure | % VMA (conversion, Faible) | ≈ % CS | Daniels | Bande (Seiler) | Note |
|---|---|---|---|---|---|
| EF | ≈ 65–75 | < 80 | E | Facile | Utilisée en séance |
| Active | ≈ 68–80 | 80–88 | E haut / M | Facile | Redondante avec EF haut et Marathon |
| Marathon | ≈ 68–84 | 80–93 | M | Facile–Seuil | Allure objectif si marathon |
| Sweet Spot | ≈ 75–87 | 88–93 | entre M et T | Seuil | Notion cycliste sans preuve en course ; redondante avec Semi |
| Semi | ≈ 77–88 | 90–97 | T bas | Seuil | Allure objectif si semi |
| Seuil | ≈ 79–90 | 93–97 (≈ MLSS) | T | Seuil | Utilisée en séance |
| Seuil 60 | ≈ 79–90 | 93–97 | T | Seuil | = Seuil (tenable ≈ 55 min, Baron 2008) |
| 10 km | ≈ 82–93 | 97–103 | T haut / I bas | Seuil–Au-dessus | ≈ Seuil haut (coureur 40–50 min) ou Seuil (coureur 60 min) |
| Seuil 30 | ≈ 85–93 | ≈ 100 (= CS) | T haut | Seuil / Au-dessus | = Seuil haut |
| 5 km | ≈ 88–97 | 103–108 | I bas | Au-dessus | Allure objectif si 5 km |
| VMA | 100 | ≈ 110–118 | I | Au-dessus | Utilisée en séance |
| VMA 30/30 | 100–105 | ≈ 112–122 | I/R | Au-dessus | Format de séance VMA, pas une allure |

### Allures utilisées dans les séances (5)

1. **EF** (sous le premier seuil).
2. **Seuil** (= Seuil 60, ≈ seuil lactique / MLSS).
3. **Seuil haut** (= Seuil 30, ≈ vitesse critique).
4. **VMA** (le 30/30 est un format de séance VMA).
5. **Allure objectif** : Marathon, Semi, 10 km ou 5 km selon la course visée, recalée sur les résultats réels.

Chacune correspond à une frontière physiologique distincte ou à la course visée.

En trail, piloter à la FC ou au RPE plutôt qu'à l'allure : la pente rend l'allure inutilisable.

## Tableau B — Vélo (Coggan, % FTP)

| Bande (Seiler) | Zone Coggan | % FTP |
|---|---|---|
| Facile | Z1 Récupération active | < 55 % |
| Facile | Z2 Endurance | 56–75 % |
| Seuil | Z3 Tempo | 76–90 % |
| Seuil–Au-dessus | Z4 Seuil | 91–105 % |
| Au-dessus | Z5 VO2max | 106–120 % |
| Au-dessus | Z6 Capacité anaérobie | 121–150 % |
| — | Z7 Neuromusculaire | Sprints maximaux |

## Ce qui ne fait pas consensus

- **FTP et MLSS** : on ne sait pas si FTP, MLSS et puissance critique désignent le même seuil. La puissance critique est en général un peu au-dessus du MLSS.
- **Facteur 0,95** : il est contesté au niveau individuel.
- **Correspondance %VMA ↔ seuil** : elle dépend fortement du niveau de l'athlète. Le seuil est plus haut en % VMA chez les coureurs entraînés.
- **VMA selon le protocole** : la valeur obtenue diffère selon le test (paliers, durée, piste ou tapis).
- **Bornes de zones en FC** : il n'y a pas de consensus. Les modèles de Friel, de Coggan et des montres divergent.
- **Valeurs Garmin** : leur fiabilité n'a pas été évaluée dans ce référentiel.

## Décisions validées (14/11/2026, révisées le 17/11/2026)

| Paramètre | Recommandation |
|---|---|
| Repère principal en course | Allures calculées depuis la vitesse critique (CS) ou une course ; % VMA en simple conversion affichée, fourchettes larges (17/11) |
| Bornes du tableau A | Valeurs de départ, ajustées après une course de référence ; rapport CS/VMA non établi (17/11) |
| Allures nommées | 12 en table de correspondance ; 5 utilisées en séance (EF, Seuil, Seuil haut, VMA, Allure objectif) |
| Tests proposés | 5 km/parkrun, demi-Cooper, chrono 30 min, 3 chronos (confirmé), test de la parole |
| Test FTP proposé | 20 min × 0,95 ; test rampe si l'athlète est novice à vélo |
| Zones FC | LTHR ; 3 bandes Facile / Seuil / Au-dessus pour les cibles, 5 zones Z1–Z5 (Friel, Coggan) réglées dans Garmin après « GO » pour l'analyse (17/11) ; FCmax théorique en dernier recours |
| Fréquence de recalibrage | Fin de chaque bloc et après chaque course + déclencheurs automatiques ; sans plafond, meilleure donnée disponible (course > test > CS recalculée > séances au seuil), confiance annoncée (17/11) |
| Utilisation des estimations Garmin | Tendance uniquement |
| Séance sur tapis | Sur demande : pente de 1 % précisée (C, valeur de départ) (17/11) |
| Nom des 3 intensités dans les tableaux | Bandes Facile / Seuil / Au-dessus (modèle de Seiler), plus Z1/Z2/Z3 (17/11) |
