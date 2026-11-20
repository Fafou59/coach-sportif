# Démarrage

Parcours d'entrée de l'athlète, en **8 étapes courtes**. Chaque étape se termine par sa sauvegarde dans le carnet et la validation de l'athlète ; ensuite seulement, passe à la suivante. Annonce l'étape (« Étape 3/8 : contraintes et préférences »).

**Page blanche** : rien n'est prérempli. Le profil vient de Garmin et des réponses données dans cette conversation ; ce que la mémoire de Claude ou une autre conversation dit de l'athlète ne s'affiche pas et ne se demande pas à confirmer.

Reprise d'une conversation interrompue : lis l'onglet Athlète, ligne « État du démarrage », et repars de cette étape. Relance après un bilan de course : repars de l'étape 2, l'onglet Athlète est déjà rempli (mets-le à jour si besoin). Dans les deux cas, relis d'abord la section « Imprévus ouverts » de l'onglet Plan : un imprévu ouvert s'applique au plan que tu construis.

Le niveau (débutant, intermédiaire, confirmé) règle des curseurs du référentiel et la quantité de détail montrée (SKILL.md, Rôle et ton), pas un parcours séparé.

## Étape 1/8 : carnet et profil

Référentiel : 06 (règle 7), 00 (doctrine).
1. Vérifie que les outils Garmin sont disponibles. Sinon : [connexion-garmin.md](connexion-garmin.md) d'abord ; si l'athlète ne peut pas brancher le connecteur, continue en mode dégradé (ses chiffres, ses captures).
2. **Carnet** : si l'instruction du projet ne contient aucun lien claude.ai, ou seulement un texte d'attente (« pas encore créé », texte entre chevrons), crée le carnet vide « Carnet — <prénom> » selon le modèle de carnet.md. Donne le lien et demande à l'athlète de remplacer, dans l'instruction de son projet, la ligne « Mon carnet : pas encore créé… » par ce lien. Lien valide présent : ouvre ce carnet, sans en créer d'autre.
3. **Niveaux de preuve** : explique-les une fois, en 3 lignes, et recopie-les dans l'onglet Athlète :
   > Chaque conseil s'appuie sur une règle plus ou moins prouvée. Je te le dis en mots : « solide (plusieurs études) », « assez solide (une étude) », « peu étudié », « habitude de coach, non prouvée ».
   > « Choix de prudence » : je l'applique par sécurité, même sans preuve forte.
   > Demande « pourquoi ? » quand tu veux l'étude derrière un conseil.
4. Profil depuis Garmin, en synthèse : `get_activities_by_date` sur 8–12 semaines (une page de liste, pas de détail par activité), `get_personal_record`. Résume : sports, ancienneté, séances et heures par semaine, kilomètres de course, plus longue sortie des 30 derniers jours, références.
5. **Antécédents**, une seule fois, en une liste ❓ oui/non (« réponds non à tout si rien ») : blessure de course dans les 12 derniers mois, fracture de fatigue passée, fatigue persistante, perte de poids non voulue, blessures osseuses répétées. Pour une athlète, cycles absents ou irréguliers **seulement sur son accord**. Aucune question sur le poids. Réponse partielle : **une** relance précise sur le point manquant, puis tu notes ce que tu as ; ces questions ne reviennent plus dans les messages suivants. Signal d'alerte : référentiel 06, règle 5.
6. **Consentements** : bloc 🔒 en fin de message, une ligne par donnée, « si elle te concerne » : cycle menstruel, grossesse, poids. « OK » vaut accord pour toutes ; « non » pour une donnée la refuse ; retrait possible à tout moment. Note chaque réponse avec la date ; sans réponse, rien n'est lu.
7. Propose un niveau, l'athlète confirme. Sauvegarde : onglet Athlète (fiche, niveaux de preuve, antécédents, consentements), « État du démarrage : 2/8 ».

## Étape 2/8 : objectifs et profil de course

Référentiel : 04 (règles 5, 6, 8).
1. Objectifs : course, chrono, ou habitude ; date, distance. Lis `get_calendar_events` pour retrouver les courses déjà inscrites.
2. **Chrono** : pour **chaque** objectif A et B, demande le chrono visé ou « sans chrono » (finir, plaisir). Tu peux aider à le fixer. Le verdict de l'étape 4 attend cette réponse.
3. **Classement** A (principal), B, C, proposé par toi avec ta raison : **un seul A** recommandé par période de préparation (12–24 semaines ; habitude de coach, non prouvée). Plusieurs A : vérifie l'écart minimal entre chaque paire (04, règle 6) ; écart trop court, ou classement contraire à ta recommandation : challenge une fois (SKILL.md), l'athlète tranche, et le choix maintenu va au journal.
4. Pour chaque objectif A et B, recueille le **profil de course**, dans cet ordre de préférence :
   1. parcours déjà dans Garmin Connect (`get_courses`, `get_course_details`) ;
   2. GPX de l'organisateur déposé dans la conversation, analysé par du code (distance, D+, D−, altitude lissée recoupée avec le D+ officiel, répartition des pentes, montées et descentes principales) ;
   3. capture du profil : lecture approximative (± 10–20 %), annoncée comme telle ;
   4. distance et D+ officiels.
5. Catégorie selon le D+/km : plat < 5 m/km, vallonné 5–15, accidenté 15–30, montagne > 30 (habitude de coach, non prouvée).
6. Sauvegarde : onglet Objectifs (chrono ou « sans chrono » pour chaque A et B), « État du démarrage : 3/8 ».

## Étape 3/8 : contraintes et préférences

1. **Contraintes** (respectées sans discuter) : jours disponibles, durée maximale par séance en semaine et le week-end, vacances et déplacements, matériel (ceinture cardio, capteur de puissance, salle ou haltères), FTP si elle est connue.
2. **Préférences** : sports aimés, sortie à garder, jour de sortie longue. Sans impact sur l'objectif : intégrées telles quelles. Contre une règle solide (ex. « pas de renfo », alors que le renfo réduit les blessures, solide, et compte d'autant plus pour un débutant) : challenge une fois avec une option courte (ex. 15' au poids du corps, 2 fois par semaine), l'athlète tranche.
3. Sauvegarde : onglet Athlète, « État du démarrage : 4/8 ».

## Étape 4/8 : verdict et repères

Référentiel : 04 (règles 6, 7), 03 (règles 1, 8, 10), 02 (règles 3 à 9), 05 (règle 3), 08 (règles 1 et 9).
1. **Repères**, avant le verdict. Tous vont au carnet ; le message montre ceux qui servent au niveau de l'athlète (débutant : allure facile au test de la parole et durée des séances).
   - **Allures** par la cascade du référentiel 02 (règle 9) : course sur route plate de moins de 8 semaines (12 si l'entraînement a continué) ; sinon vitesse critique depuis les données d'entraînement ; sinon estimation de confiance faible. Garde-fou : pas de test maximal moins de 3–4 semaines après un marathon, pendant un retour de blessure, ou avant 3 mois de pratique. **Estime toujours** les 5 allures de séance (EF, Seuil, Seuil haut, VMA, allure objectif ; pas d'allure objectif en trail) avec leur confiance.
   - **Source de chaque repère**, dans le message et au carnet (SKILL.md, Repères et calculs) : la marche de la cascade retenue et la donnée exacte (« 10 km du <date> en <chrono> », « VC sur 3 efforts : <durée> le <date>, … », « séances au seuil du <date> et du <date> », « estimation Garmin du seuil »). Onglet Repères déjà rempli (relance après un bilan de course, nouveau démarrage) : pars de ses valeurs et explique chaque écart (ancienne → nouvelle, donnée nouvelle) ; mêmes données, mêmes repères.
   - **Tests** : propose tous ceux adaptés au niveau, avec fiabilité et contraintes (tableau du référentiel 02, règle 4) ; l'athlète choisit d'en faire un ou non. Le test choisi se place en semaine d'allègement du bloc 1 ; le carnet note le test et son protocole.
   - **Vélo** : FTP depuis la courbe puissance-durée (`get_power_duration_curve`, effort de 20 min de moins de 6 semaines × 0,95), sinon test proposé.
   - **Bandes FC** depuis la LTHR (course et vélo séparés), source citée comme pour les allures ; plafond Facile vérifié au test de la parole. **Une seule cible pour l'EF** : la bande Facile avec son plafond individualisé. Une plage plus étroite observée dans les données (ex. 130–142 en EF) se présente comme une observation, pas comme une cible. Propose, sans insister, de régler les zones Z1–Z5 du compte (après GO, garmin.md).
   - **Plage personnelle** de récupération sur 30 nuits (`get_sleep_summary_range`), calcul comme au bilan (bilan.md, temps 1). Moins de 28 nuits, ou montre sans ces mesures : dis que le suivi de récupération reposera sur le ressenti (check.md, Métrique en dérive).
2. **Verdict** par objectif, puis sur le **calendrier entier** : Facile, Réaliste, Ambitieux ou Difficile en l'état.
   - Contrôle calculé, qui prime : le nombre de semaines permet-il d'atteindre la sortie longue cible ? Fais le § Calcul de la sortie longue et montre-le dans le message.
   - Course A ou B plus longue que 1,10 × la plus longue sortie préparée avant elle : § Calcul de la sortie longue, point 5.
   - Durées de préparation du référentiel 04 (règle 7) : **repère montré, jamais bloquant**.
   - Calendrier : objectifs A trop proches (04, règle 6), spécificités opposées (ex. 5 km et trail long), objectif A sans bloc de développement : nomme le coût et propose d'en rétrograder un en B.
   - Explique en 3 à 5 lignes, avec les risques ; si Ambitieux ou Difficile en l'état, propose des alternatives (date, objectif intermédiaire, chrono). L'athlète décide ; un choix contre ton avis suit SKILL.md § Challenger une fois.
3. Sauvegarde : Objectifs (verdicts, ligne du calcul de sortie longue), Repères (allures, FTP, bandes FC, chacune avec source et confiance ; plage), « État du démarrage : 5/8 ».

## Étape 5/8 : semaine-type

Référentiel : 01 (règles 3, 4, 8), 07 (règles 3, 6, 9), 04 (règle 8), 03 (règle 10).
1. Grille co-construite : pour chaque jour, sport, qualité ou endurance, durée maximale, dans les contraintes. Débutant en course : 3 séances de course-marche par semaine par défaut ; 2 acceptées, avec une progression annoncée plus lente.
2. Budget de séances dures selon le niveau (débutant : aucune pendant les 4–8 premières semaines), 48 h entre deux. Séance principale placée après un jour facile. Séance à la carte seulement si l'athlète y a droit (01, règle 8) ; sinon, dis « pas encore disponible » et à quelle condition elle le deviendra. Dès qu'elle peut s'ouvrir un jour (intermédiaire ou confirmé), réserve son créneau dans la grille et compte-le comme **jour dur** : les options Moyenne et Soutenue sont des séances dures.
3. Renfo proposé : 2 séances par semaine en phase de base. Renfo jambes (lourd ou pliométrie) placé **le lendemain d'un jour dur, ou le même jour après lui** (07, règle 6) ; débutant en renfo : le lendemain. Jour dur = séance principale, créneau à la carte (même pas encore ouvert), course B ou C. Haut du corps et gainage : n'importe quel jour. Mobilité proposée, facultative.
4. **Contrôle du renfo**, avant de présenter la grille : pour chaque renfo jambes, regarde la séance des 24 h suivantes. Jour dur le lendemain : déplace le renfo. Le message montre ce contrôle jour par jour (ex. « Renfo jambes mar → mer EF ✅ · Renfo jambes ven → sam EF ✅ »), jamais un « conforme » sans lui.
5. **Dosage des côtes et de la descente**, co-construit : montre le profil de course et la fourchette de sa catégorie (04, règle 8) ; l'athlète choisit, son choix est noté comme préférence. Accidenté ou montagne : recommande au minimum la préparation aux descentes (05, règle 10).
6. Sauvegarde : Plan (semaine-type, créneau à la carte compris), Athlète (préférences), « État du démarrage : 6/8 ».

## Étape 6/8 : plan macro

Référentiel : 04 (règles 1 à 5, 7), 03 (règles 5, 8, 10), 05.
1. 12–24 semaines jusqu'à l'objectif A (jusqu'à 1 an avec une phase de base allongée).
2. Phase de base (qualités fondamentales : volume facile qui progresse et n'est jamais réduit au profit de la vitesse, force, lignes droites), phase spécifique, affûtage selon la distance.
3. Blocs de 3 + 1 semaines (2 + 1 sur critère observé). Pour chaque bloc : phase, qualité principale, volume par semaine. Objectifs B et C placés comme séances dures, avec mini-affûtage pour un B.
4. **Après une course récente** : reprise selon 06 (règle 1), puis premier bloc à **70–80 % du volume habituel d'avant la course** (03, règle 8 ; habitude de coach, non prouvée — choix de prudence) ; ensuite, garde-fou des 30 % cumulés sur 2 semaines.
5. **Débutant** : progression en course-marche (03, règle 10) : séance de 20–30 min au départ (ex. 5' marche, 3 × (6' course / 2' marche), 5' marche), durée totale + 5 min par semaine jusqu'à 30 min, puis 1,10 × sur la séance entière, marche comprise ; temps couru + 10–15 % par semaine. Sous 30 min de séance, pas de plafond 1,10 ×.
6. **Sortie longue** : refais le § Calcul de la sortie longue avec les blocs réels du plan (hausses semaine par semaine, semaines allégées) et montre-le. Même départ et mêmes règles qu'à l'étape 4 : le pic tombe au même chiffre ; s'il change (blocs différents, contrainte nouvelle), c'est une correction (SKILL.md, Repères et calculs). Courses A ou B au-delà de 1,10 × : point 5 du calcul.
7. Présente le plan, explique les choix clés et les risques en quelques lignes, puis demande la validation.
8. Sauvegarde : Plan (plan macro, ligne du calcul de sortie longue), « État du démarrage : 7/8 ».

## Étape 7/8 : bloc 1 détaillé

Référentiel : 01, 03 (règles 1, 2, 6, 8, 10), 05, 07.
1. Détaille le bloc 1 séance par séance, au format des noms Garmin (garmin.md), qualité principale et d'entretien.
2. Vérifie les garde-fous du temps 2 du bilan (bilan.md, tableau et contrôle jour par jour) sur chaque semaine, **en partant de la semaine réellement précédente** (dernière semaine faite, reprise comprise) : hausse et cumul sur 2 semaines se calculent depuis elle, pas depuis la semaine 1 du bloc ; cumul des 30 % : semaine N ≤ 1,30 × semaine N-2 ; une semaine allégée, d'affûtage ou de récupération **prévue au plan** (y compris la récupération après une course B ou C) ne sert jamais de référence : on la remplace par la dernière semaine pleine d'avant elle (Q100, Q102 ; habitude de coach, non prouvée). Une semaine réduite par un imprévu, ou la reprise après une course A, relève de la règle 8 (03, règle 2). 1,10 × se cite juste : chaque sortie face à la plus longue des 30 derniers jours, jamais face à la sortie de la semaine d'avant.
3. Sorties longues du bloc = celles du calcul écrit au Plan macro à l'étape 6. Un écart avec ce calcul est une correction : ❓ avec la raison, avant d'écrire.
4. Validation de l'athlète. Sauvegarde : Plan (bloc en cours), « État du démarrage : 8/8 ».

## Étape 8/8 : « GO » et première semaine dans Garmin

1. Relis « Imprévus ouverts » (onglet Plan), puis tableau des séances jusqu'au premier dimanche, plus le lundi d'après (même rythme que le bilan du dimanche).
2. Bloc ✅ GO requis, puis création, planification, relecture et confirmation selon garmin.md.
3. Explique le rythme en une ligne : un seul mot, « check », quand tu veux (surtout après une séance importante, et le dimanche) ; le coach choisit lui-même entre check, bilan du dimanche et bilan express.
4. Sauvegarde : « État du démarrage : terminé le <date> » ; journal des décisions du Plan.

## Calcul de la sortie longue (étapes 4, 6 et 7)

Une seule méthode, refaite à l'identique à chaque étape, montrée dans le message et écrite au carnet :
1. **Départ** : plus longue sortie de course des 30 derniers jours, séance entière, lue dans Garmin (date, durée, distance). C'est la référence de 1,10 × (03, règle 1). Après une course récente : reprise (06, règle 1), puis premier bloc à 70–80 % du volume d'avant la course (03, règle 8).
2. **Hausses** : nombre de semaines où la sortie longue monte, chacune ≤ 1,10 × la plus longue des 30 derniers jours, jamais la semaine d'une autre hausse forte (03, règle 6 ; 05, règle 1).
3. **Semaines allégées** : sortie longue maintenue ou −20 à −30 % (05, règle 1), sans hausse.
4. **Pic** = départ × 1,10 puissance le nombre de hausses, borné par le plafond de durée (05, règle 3) et la durée maximale du week-end (contraintes). En une ligne, ex. « départ 1 h 05 (sortie du 12/10) · 6 hausses sur 9 semaines de charge, 3 allégées · 1 h 05 × 1,10⁶ = 1 h 55 → plafond 05.3 : 1 h 50 ».
5. **Course plus longue que le pic** (décision Q101) : une course qui dépassera 1,10 × la plus longue sortie préparée avant elle est un **pic au-delà de la règle 03.1** (risque de blessure accru, assez solide, une étude).
   - **Objectif A** (marathon, trail long) : c'est le cas normal, puisque la sortie longue est plafonnée. Explique-le **une seule fois**, au verdict et au plan macro, comme une caractéristique de l'objectif ; n'y reviens plus ensuite.
   - **Course B ou C** : signale-le à chaque fois et mets-le dans le choix de l'athlète : `❓ **Qn – Pic de course** : la garder en connaissance de cause, ou <alternative : format plus court, autre date>` avec ta recommandation.

## Exemple (format B, données fictives) : verdict

Chiffres inventés pour montrer la forme ; les vrais viennent du carnet et de Garmin.

> ### Verdict : semi de Lille, 1 h 40, le 12/04
> | Repère | Valeur |
> |---|---|
> | Semaines disponibles | 20 |
> | Repère de préparation (intermédiaire) | 10–12 sem. |
> | Sortie longue : départ → pic | 1 h 05 (12/10) → 1 h 50 |
> | Calcul | 6 hausses ≤ 1,10 ×, 3 sem. allégées ; 1 h 55 bornée à 1 h 50 (plafond semi) |
> | Allure @21K estimée | 4'50 (confiance moyenne, 10 km du 21/09 en 46'10) |
>
> **Verdict : Ambitieux.** Le temps suffit pour la sortie longue en respectant 1,10 × (assez solide, une étude), mais 1 h 40 demande 10 s/km de mieux que ton estimation.
>
> ❓ **Q1 – Chrono** : tu gardes 1 h 40 ?
> ➡️ Viser 1 h 43 et recaler après le bloc 2. Réponds « OK » pour 1 h 43, ou garde 1 h 40.

## Exemple (format B, données fictives) : antécédents et consentements

> ### Étape 1/8 : ta santé
> Ton profil Garmin est noté dans le carnet. Quelques questions, une seule fois.
>
> ❓ **Q1 – Antécédents** (oui ou non pour chacun ; réponds « non à tout » si rien) : blessure de course depuis 12 mois · fracture de fatigue passée · fatigue qui dure · perte de poids non voulue · blessures osseuses répétées.
>
> ---
> 🔒 **Consentement** — données sensibles, si elles te concernent : cycle menstruel · grossesse · poids. « OK » = j'accepte que tu lises ces données ; réponds « non » pour celles que tu refuses. Tu peux retirer ton accord à tout moment.
