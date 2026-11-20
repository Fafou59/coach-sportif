# Bilan du dimanche, fin de bloc, course

Le bilan du dimanche est un rendez-vous en **deux temps** : d'abord la synthèse chiffrée et les questions, **sans adaptation** ; puis, après les réponses, l'adaptation et la création de la semaine suivante dans Garmin. L'athlète doit pouvoir donner son ressenti avant que tu ne conclues.

Sommaire : Temps 1 · Temps 2 · Fin de bloc · Course A ou B à J-7 · Bilan de course · Exemples.

## Temps 1 : synthèse et questions

1. Outils Garmin disponibles ? Sinon : connexion-garmin.md ou mode dégradé.
2. Carnet : tous les onglets sauf Archives. **Imprévus ouverts** (onglet Plan) d'abord : ils s'affichent dans les points saillants et ont leur question de suivi.
3. Garmin, semaine du lundi au dimanche :
   - `get_scheduled_workouts` (prévu) et `get_activities_by_date` (fait) ;
   - `get_activity` pour chaque activité : effort perçu (/10) → charge = RPE × durée en minutes, tous sports ;
   - `get_activities_by_date` sur 30 jours, course seulement : plus longue sortie, séance entière (référence du plafond 1,10 × de la semaine suivante) ;
   - temps en bande Facile (Z1 + Z2 de `get_activity_hr_in_timezones`) pour les séances de course et de vélo, plafond lu dans l'onglet Repères ; si c'est trop coûteux, omets-le.
   Séance clé déjà commentée (avant la « Dernière séance analysée » du Plan) : une ligne de rappel, sans nouvelle question.
4. **Plage personnelle** : `get_sleep_summary_range` sur les 30 dernières nuits (un seul appel ; `get_hrv_trend` sur 30 jours si la VFC y manque). Pour la VFC, la FC de repos et la durée de sommeil : ligne de base = moyenne sur 28–30 j, SWC = 0,5 × écart-type, plage = ligne de base ± SWC. Compare la moyenne des 7 derniers jours. Mets à jour l'onglet Repères (référentiel 08, règles 1, 4 et 9). Moins de 28 nuits ou pas de mesures : dis-le ; les questions de ressenti portent la récupération.
5. Calcule les **indicateurs**, commentés mais jamais décisifs seuls : hausse du volume de course face à la **semaine réellement précédente**, reprise comprise (repères 10 / 15 / 20 % selon le niveau), cumul sur 2 semaines (garde-fou de 30 %, référence du tableau du temps 2), hausse de la charge RPE totale, part de la sortie longue, répartition en bande Facile (≈ 80/20, jusqu'à 70/30 sous 5 h/semaine). Compare avec le suivi hebdomadaire de l'onglet Plan.
6. Message format B : tableau prévu / fait, points saillants (séances clés, indicateurs, récupération, imprévus ouverts, notes de l'athlète), puis les questions. **Aucune adaptation à ce stade.** Écart entre prévu et fait sans explication dans les données (séance absente du calendrier, activité manquante) : « cause inconnue », et demande à l'athlète.

**Questions** (format ❓, toutes les échelles 5 = au mieux ; réponse possible en une ligne, dans l'ordre des numéros, puis texte libre facultatif) :
1. `❓ **Q1 – Forme** (1 = vidé · 5 = au top)`
2. `❓ **Q2 – Jambes** (1 = lourdes · 5 = fraîches)`
3. `❓ **Q3 – Stress hors sport** (1 = très stressé · 5 = serein)`
4. `❓ **Q4 – Motivation** (1 = aucune · 5 = à fond)`
5. `❓ **Q5 – Douleur** : non, ou où et combien sur 10` (plus le suivi de chaque imprévu ouvert)
6. `❓ **Q6 – Contraintes** de la semaine à venir`

Exemple de réponse : `4 · 3 · 2 · 5 · non · indispo mardi`.
Seulement sur signal (durée de sommeil hors plage, ou forme ≤ 2) : sommeil ressenti. Jamais : l'effort perçu manquant.

## Temps 2 : adaptation et semaine suivante

1. **Imprévus ouverts** et **douleur** : feu tricolore d'abord (référentiel 06, règle 4) ; un imprévu ouvert prime sur le bloc détaillé. **Dérive** : grille du référentiel 08 (règle 6). Forme, jambes, stress et motivation pèsent avec les données ; un indicateur seul ne déclenche rien.
2. Dis clairement si une adaptation est nécessaire ou non, et pourquoi.
3. **Séance à la carte** : si l'athlète y a droit (référentiel 01, règle 8 : intermédiaire ou confirmé, ≈ 3 h 30/semaine et au moins 4 séances, après 4 semaines avec une séance dure bien tolérée), **recommande une option d'après les réponses du temps 1**. Dérive en cours : Aucune ou Légère seulement. Intermédiaire dont la sortie longue contient de l'allure spécifique : Aucune ou Légère. Jamais d'endurance de vitesse en à la carte. L'athlète choisit avant le GO ; seule l'option retenue est créée. S'il n'y a pas droit : « pas encore disponible », sans recommander d'option.
   **Ouverture de l'à la carte** (premier bilan où l'athlète y a droit), et chaque fois que Moyenne ou Soutenue est retenue : c'est un jour dur. Relis la semaine-type (onglet Plan) : un renfo jambes la veille de ce jour se déplace au lendemain d'un jour dur ou au même jour après lui (07, règle 6), ou l'option se limite à Aucune ou Légère. Semaine-type changée : écris-la au carnet et annonce-le.
4. Construis la semaine à partir du bloc détaillé (onglet Plan) et des contraintes annoncées, puis vérifie chaque garde-fou **sur la semaine construite, jour par jour**. Le message liste chaque contrôle avec ce qui a été comparé (ex. « Renfo jambes mar → mer EF ✅ », « SL 1 h 20 ≤ 1,10 × 1 h 15 (sortie du 09/11) = 1 h 22 ✅ », « cumul 2 sem. : 38 km → 46 km = +21 % ✅ »). Un garde-fou que tu n'as pas comparé ne s'affiche pas comme respecté.

   | Garde-fou | Référentiel |
   |---|---|
   | Budget de séances dures (course + vélo) selon le niveau | 01, règle 3 |
   | 48 h entre deux séances dures (24 h tolérées : confirmé, 2e au Seuil, aucune dérive) | 01, règle 4 |
   | Pas de renfo lourd des jambes ni de pliométrie dans les 24 h avant une séance dure (principale, à la carte Moyenne ou Soutenue, course, test) | 07, règle 6 |
   | Chaque sortie de course ≤ 1,10 × la plus longue des 30 derniers jours, séance entière (jamais face à la sortie de la semaine d'avant) | 03, règle 1 |
   | Débutant : course-marche, 1,10 × sur la séance entière marche comprise, pas de plafond sous 30 min de séance, temps couru + 10–15 %/semaine | 03, règle 10 |
   | Cumul de hausse ≤ 30 % sur 2 semaines : semaine N ≤ 1,30 × semaine N-2 ; une semaine allégée, d'affûtage ou de récupération **prévue au plan** (y compris la récupération après une course B ou C) ne sert jamais de référence : on la remplace par la dernière semaine pleine d'avant elle (Q100, Q102 ; habitude de coach, non prouvée). Une semaine réduite par un imprévu, ou la reprise après une course A, relève de la règle 8 | 03, règles 2 et 8 |
   | Premier bloc après la reprise d'une course : 70–80 % du volume habituel d'avant la course | 03, règle 8 |
   | Une seule hausse forte par semaine | 03, règle 6 |
   | Plafond de durée de la sortie longue | 05, règle 3 |
   | Rappel glucides dans la description au-delà de 75 min | 09, règles 1 et 10 |

5. Message format B : adaptation, tableau de la semaine **jusqu'au lundi d'après** (séances déjà créées exclues), séance principale ★, option à la carte ; puis le tableau des séances à retirer de la bibliothèque (garmin.md, Ménage de la bibliothèque : séances sans occurrence future seulement). Un seul bloc ✅ GO requis pour les deux listes.
6. Après GO : création, planification, relecture, confirmation (garmin.md) ; ménage de la bibliothèque (`delete_workouts`, aperçu puis confirmation).
7. Carnet, sans demander de validation (annonce en une ligne ce qui est écrit) : onglet Plan (statut des séances, ligne du suivi hebdomadaire, journal des décisions, dernière séance analysée, imprévus ouverts mis à jour), onglet Repères (plage) déjà à jour. Le carnet s'écrit au temps 2 même sans GO Garmin, et aussi en MODE RÉPÉTITION.

## Fin de bloc

Au bilan qui clôt la semaine d'allègement, en plus du temps 2 :
1. **Recalage des allures, sans plafond** (référentiel 02, règle 10), sur la meilleure donnée du bloc : course > test > vitesse critique recalculée sur 3 efforts quasi maximaux de 3 à 20 min > séances au seuil. Pars des valeurs de l'onglet Repères ; pour chaque repère : avant → après, source précise (course et date, test et date, efforts de la VC et leurs dates, séances au seuil et leurs dates) et confiance (SKILL.md, Repères et calculs). Même chose pour la FTP et la LTHR (bandes FC) ; si la LTHR change, propose de mettre à jour les zones Z1–Z5 du compte (après GO, garmin.md).
2. Après 2–3 blocs sans course ni test : propose un test (référentiel 02, règle 4), placé en semaine d'allègement.
3. **Bloc suivant** : 3 + 1 par défaut, 2 + 1 sur critère observé (récupération lente, imprévu, débutant qui récupère lentement ; l'âge seul n'est pas un critère) ; une qualité principale et une d'entretien ; détaillé séance par séance et **validé** par l'athlète (référentiel 04, règle 3). Garde-fous vérifiés comme au temps 2 : cumul des 30 % : semaine N ≤ 1,30 × semaine N-2 ; une semaine allégée, d'affûtage ou de récupération **prévue au plan** (y compris la récupération après une course B ou C) ne sert jamais de référence : on la remplace par la dernière semaine pleine d'avant elle (Q100, Q102 ; habitude de coach, non prouvée). Une semaine réduite par un imprévu, ou la reprise après une course A, relève de la règle 8 (03, règle 2) ; 1,10 × face à la plus longue sortie des 30 derniers jours ; sorties longues selon le calcul du Plan macro (demarrage.md, Calcul de la sortie longue), tout écart présenté comme une correction. Revois la préférence de dosage des côtes (référentiel 04, règle 8).
4. **Archive** : déplace le détail du bloc terminé et son journal de Plan vers Archives ; les imprévus encore ouverts restent dans Plan.
5. Propose un **export Markdown** du carnet (sauvegarde).

## Course A ou B à J-7

Au bilan ou au check qui tombe à J-7, remets un **plan de course** (référentiel 04, règle 10) :
- segments tirés du profil de course (onglet Objectifs) : effort visé, ravitaillement, passages en marche ; en trail, effort plutôt qu'allure ;
- départ à l'allure objectif ou un peu en dessous ; par temps chaud, allure ajustée (04, règle 9) ;
- course avec GPX : réglages PacePro proposés, avec leur raisonnement, que l'athlète saisit lui-même, ou à défaut l'envoi du parcours sur la montre par l'athlète (option) ;
- nutrition en 4 points : charge si besoin, repas d'avant-course, ravitaillement par heure, hydratation et sodium (09, règle 10) ;
- course de plus de 90 min : « Évite ibuprofène, aspirine ou antidouleur pour tenir, avant comme pendant la course, sauf avis de ton médecin. » (06, règle 9) ;
- renfo : dernier lourd à J-7/J-10, activation légère jusqu'à J-4, rien après (07, règle 7).

## Bilan de course

Après une course objectif :
1. Lis l'activité (`get_activity`, découpage) et le profil de course.
2. Questions ❓ : ressenti, ce qui a marché, ce qui n'a pas marché, douleur.
3. **Reprise** : tableau du référentiel 06 (règle 1) selon la distance et le dénivelé ; haut des fourchettes pour un débutant ou sur critère observé. Fixe la date de retour de l'intensité. Séances de reprise créées après GO. Ensuite, le **premier bloc repart à 70–80 % du volume habituel d'avant la course** (03, règle 8), puis garde-fou des 30 % sur 2 semaines, contrôlé depuis la dernière semaine de reprise.
4. Le résultat devient la meilleure donnée de recalage (02, règle 10), appliquée au retour de l'intensité, pas avant.
5. Carnet : résultat dans Objectifs, bloc terminé vers Archives, « Dernière séance analysée » = date de la course (le check suivant ne la réanalyse pas).
6. Relance le démarrage **à l'étape 2** (objectifs) : demarrage.md.

## Exemples (format B, données fictives)

Chiffres inventés pour montrer la forme ; les vrais viennent du carnet (onglet Repères) et de Garmin.

**Temps 1**

> ### Bilan — semaine 3 du bloc 2 (charge)
> | | Prévu | Fait |
> |---|---|---|
> | Séances | 5 | 5 |
> | Course | 40 km | 42 km |
> | Total | 5 h 55 | 6 h 05 |
>
> **Points saillants :** séance clé Seuil haut réussie · bande Facile 81 % · récupération dans ta plage · volume course +6 % sur la semaine d'avant.
>
> **Verdict :** semaine conforme, pas d'adaptation pour l'instant.
>
> ❓ **Q1 – Forme** (1 = vidé · 5 = au top)
> ❓ **Q2 – Jambes** (1 = lourdes · 5 = fraîches)
> ❓ **Q3 – Stress hors sport** (1 = très stressé · 5 = serein)
> ❓ **Q4 – Motivation** (1 = aucune · 5 = à fond)
> ❓ **Q5 – Douleur** : non, ou où et combien sur 10
> ❓ **Q6 – Contraintes** de la semaine à venir
>
> Réponds en une ligne dans l'ordre, ex. `4 · 3 · 2 · 5 · non · indispo mardi`.

**Temps 2**

> ### Adaptation
> **Aucune nécessaire** : jambes 2/5 en fin de bloc de charge, attendu. Semaine 4 = allègement (−35 %).
> ### Semaine du 24/11
> | Jour | Séance |
> |---|---|
> | Mar | — (indispo) |
> | Mer | `R \| EF 40' + 6×15" LD` |
> | Jeu | `R \| Frac. 45' 4×4' @Seuil r:2' ★` |
> | Ven | `Renfo \| 30'` |
> | Dim | `R \| SL 1h10` |
> | Lun 1/12 | `R \| EF 40'` |
>
> Contrôles : renfo jambes ven → sam repos ✅ · SL 1 h 10 ≤ 1,10 × 1 h 20 (sortie du 16/11) ✅ · 1 séance dure ✅
>
> À la carte : je recommande **Aucune** (jambes 2/5, allègement).
> ### À retirer de la bibliothèque
> | Séance | Dernière date | Future ? |
> |---|---|---|
> | `R \| Frac. 50' 6×3' @VMA r:2' ★` | 20/11 | non |
> | `R \| SL 1h05` | 23/11 | non |
>
> `R | EF 40'` reste : il est planifié mercredi. Tes activités réalisées restent ; le détail de la semaine est dans le carnet.
>
> Carnet mis à jour : suivi hebdomadaire et journal (onglet Plan).
>
> ---
> ✅ **GO requis** — création des 5 séances de la semaine du 24/11 et suppression des 2 séances ci-dessus — Réponds « GO » pour valider.

**Fin de bloc**

> ### Fin du bloc 2 : recalage
> | Allure | Avant | Après | Source |
> |---|---|---|---|
> | Seuil | 4'38 | 4'32 | 10 km du 16/11 en 41'50 |
> | Seuil haut | 4'18 | 4'12 | 10 km du 16/11 en 41'50 |
>
> **Verdict :** progression nette, confiance élevée (course récente). Bloc 3 en 3 + 1, qualité principale : Seuil haut.
>
> ❓ **Q1 – Bloc 3** : tu valides le bloc tel que détaillé dans ton carnet ?
> ➡️ Oui. Réponds « OK ».

**Bilan de course**

> ### Semi de Lille : 1 h 39'52
> | Segment | Allure | Cible |
> |---|---|---|
> | 0–10 km | 4'42 | 4'45 |
> | 10–21 km | 4'45 | 4'45 |
>
> **Verdict :** course maîtrisée, départ bien tenu. Reprise : EF dès jeudi, intensité à partir du 2/12 ; premier bloc à 70–80 % de ton volume d'avant course.
>
> ❓ **Q1 – Ressenti** : comment l'as-tu vécue ?
> ❓ **Q2 – Ce qui a marché, ce qui a coincé** ?
> ❓ **Q3 – Douleur** : non, ou où et combien sur 10 ?
