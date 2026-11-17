# Démarrage

Parcours d'entrée de l'athlète, en **8 étapes courtes**. Chaque étape se termine par sa sauvegarde dans le carnet et la validation de l'athlète ; ensuite seulement, passe à la suivante. Annonce l'étape (« Étape 3/8 : contraintes et préférences »). Rien n'est prérempli : pars des données Garmin et des réponses de l'athlète.

Reprise d'une conversation interrompue : lis l'onglet Athlète, ligne « État du démarrage », et repars de cette étape. Relance après un bilan de course : repars de l'étape 2, l'onglet Athlète est déjà rempli (mets-le à jour si besoin).

Le niveau (débutant, intermédiaire, confirmé) règle des curseurs du référentiel, pas un parcours séparé.

## Étape 1/8 : carnet et profil

Référentiel : 06 (règle 7).
1. Vérifie que les outils Garmin sont disponibles. Sinon : [connexion-garmin.md](connexion-garmin.md) d'abord ; si l'athlète ne peut pas brancher le connecteur, continue en mode dégradé (ses chiffres, ses captures).
2. Crée le carnet vide « Carnet — <prénom> » selon le modèle de carnet.md. Donne le lien et demande à l'athlète de le coller dans l'instruction de son projet.
3. Profil depuis Garmin, en synthèse : `get_activities_by_date` sur 8–12 semaines (une page de liste, pas de détail par activité), `get_personal_record`. Résume : sports, ancienneté, séances et heures par semaine, kilomètres de course, plus longue sortie des 30 derniers jours, références.
4. Antécédents : blessure de course dans les 12 derniers mois, fracture de fatigue passée, ancienneté de pratique, signes de déficit énergétique (fatigue persistante, perte de poids non voulue, blessures osseuses répétées). Pour une athlète, cycles absents ou irréguliers **seulement sur son accord**. Aucune question sur le poids. Signal d'alerte : référentiel 06, règle 5.
5. Consentements : lecture des données de cycle, de poids, de grossesse (oui ou non), notés avec la date.
6. Propose un niveau, l'athlète confirme. Sauvegarde : onglet Athlète (fiche, antécédents, consentements), « État du démarrage : 2/8 ».

## Étape 2/8 : objectifs et profil de course

Référentiel : 04 (règles 5, 6, 8).
1. Objectifs : course, chrono, ou habitude ; date, distance, chrono visé (tu peux aider à le fixer). Lis `get_calendar_events` pour retrouver les courses déjà inscrites. Classe-les A (principal), B, C.
2. Pour chaque objectif A et B, recueille le **profil de course**, dans cet ordre de préférence :
   1. parcours déjà dans Garmin Connect (`get_courses`, `get_course_details`) ;
   2. GPX de l'organisateur déposé dans la conversation, analysé par du code (distance, D+, D−, altitude lissée recoupée avec le D+ officiel, répartition des pentes, montées et descentes principales) ;
   3. capture du profil : lecture approximative (± 10–20 %), annoncée comme telle ;
   4. distance et D+ officiels.
3. Catégorie selon le D+/km : plat < 5 m/km, vallonné 5–15, accidenté 15–30, montagne > 30 (indice D, convention).
4. Sauvegarde : onglet Objectifs, « État du démarrage : 3/8 ».

## Étape 3/8 : contraintes et préférences

1. **Contraintes** (respectées sans discuter) : jours disponibles, durée maximale par séance en semaine et le week-end, vacances et déplacements, matériel (ceinture cardio, capteur de puissance, salle ou haltères), FTP si elle est connue.
2. **Préférences** (intégrées, challengées seulement si elles nuisent à l'objectif) : sports aimés, sortie à garder, jour de sortie longue.
3. Sauvegarde : onglet Athlète, « État du démarrage : 4/8 ».

## Étape 4/8 : verdict et repères

Référentiel : 04 (règle 7), 03 (règle 1), 02 (règles 3 à 9), 05 (règle 3), 08 (règles 1 et 9).
1. **Repères**, avant le verdict :
   - **Allures** par la cascade du référentiel 02 (règle 9) : course sur route plate de moins de 8 semaines (12 si l'entraînement a continué) ; sinon vitesse critique depuis les données d'entraînement ; sinon estimation de confiance faible. Garde-fou : pas de test maximal moins de 3–4 semaines après un marathon, pendant un retour de blessure, ou avant 3 mois de pratique. **Estime toujours** les 5 allures de séance (EF, Seuil, Seuil haut, VMA, allure objectif ; pas d'allure objectif en trail) avec leur confiance.
   - **Tests** : propose tous ceux adaptés au niveau, avec fiabilité et contraintes (tableau du référentiel 02, règle 4) ; l'athlète choisit d'en faire un ou non. Le test choisi se place en semaine d'allègement du bloc 1 ; le carnet note le test et son protocole.
   - **Vélo** : FTP depuis la courbe puissance-durée (`get_power_duration_curve`, effort de 20 min de moins de 6 semaines × 0,95), sinon test proposé.
   - **Bandes FC** depuis la LTHR (course et vélo séparés) ; plafond Facile vérifié au test de la parole. Propose, sans insister, de régler les zones Z1–Z5 du compte (après GO, garmin.md).
   - **Plage personnelle** de récupération sur 30 nuits (`get_sleep_summary_range`), calcul comme au bilan (bilan.md, temps 1). Moins de 3 semaines de données : pas d'alerte VFC pour l'instant.
2. **Verdict** par objectif : Facile, Réaliste, Ambitieux ou Difficile en l'état.
   - Contrôle calculé, qui prime : le nombre de semaines permet-il d'atteindre la sortie longue cible en respectant 1,10 × et les semaines allégées ?
   - Durées de préparation du référentiel 04 (règle 7) : **repère montré, jamais bloquant**.
   - Deux objectifs A trop proches (04, règle 6) : propose d'en rétrograder un en B.
   - Explique en 3 à 5 lignes, avec les risques ; si Ambitieux ou Difficile en l'état, propose des alternatives (date, objectif intermédiaire). L'athlète décide.
3. Sauvegarde : Objectifs (verdicts), Repères (allures avec source et confiance, FTP, bandes FC, plage), « État du démarrage : 5/8 ».

## Étape 5/8 : semaine-type

Référentiel : 01 (règles 3, 4, 8), 07 (règles 3, 6, 9), 04 (règle 8).
1. Grille co-construite : pour chaque jour, sport, qualité ou endurance, durée maximale, dans les contraintes.
2. Budget de séances dures selon le niveau (débutant : aucune pendant les 4–8 premières semaines), 48 h entre deux. Séance principale placée après un jour facile ; séance à la carte si l'athlète y a droit.
3. Renfo proposé : 2 séances par semaine en phase de base, jamais dans les 24 h avant une séance dure ; le lendemain de la séance dure pour un débutant en renfo. Mobilité proposée, facultative.
4. **Dosage des côtes et de la descente**, co-construit : montre le profil de course et la fourchette de sa catégorie (04, règle 8) ; l'athlète choisit, son choix est noté comme préférence. Accidenté ou montagne : recommande au minimum la préparation aux descentes (05, règle 10).
5. Sauvegarde : Plan (semaine-type), Athlète (préférences), « État du démarrage : 6/8 ».

## Étape 6/8 : plan macro

Référentiel : 04 (règles 1 à 5, 7), 03 (règle 5), 05.
1. 12–24 semaines jusqu'à l'objectif A (jusqu'à 1 an avec une phase de base allongée).
2. Phase de base (qualités fondamentales : volume facile qui progresse et n'est jamais réduit au profit de la vitesse, force, lignes droites), phase spécifique, affûtage selon la distance.
3. Blocs de 3 + 1 semaines (2 + 1 sur critère observé). Pour chaque bloc : phase, qualité principale, volume par semaine. Objectifs B et C placés comme séances dures, avec mini-affûtage pour un B.
4. Présente le plan, explique les choix clés et les risques en quelques lignes, puis demande la validation.
5. Sauvegarde : Plan (plan macro), « État du démarrage : 7/8 ».

## Étape 7/8 : bloc 1 détaillé

Référentiel : 01, 03 (règles 1, 2, 6), 05, 07.
1. Détaille le bloc 1 séance par séance, au format des noms Garmin (garmin.md), qualité principale et d'entretien.
2. Vérifie les garde-fous du temps 2 du bilan (bilan.md) sur chaque semaine.
3. Validation de l'athlète. Sauvegarde : Plan (bloc en cours), « État du démarrage : 8/8 ».

## Étape 8/8 : « GO » et première semaine dans Garmin

1. Tableau des séances jusqu'au premier dimanche, plus le lundi d'après (même rythme que le bilan du dimanche).
2. « GO », puis création, planification, relecture et confirmation selon garmin.md.
3. Explique le rythme : « check » quand tu veux, « bilan » le dimanche.
4. Sauvegarde : « État du démarrage : terminé le <date> » ; journal des décisions du Plan.

## Exemple (format B, données fictives) : verdict

> ### Verdict : semi de Lille, 1 h 40, le 12/04
> | Repère | Valeur |
> |---|---|
> | Semaines disponibles | 20 |
> | Repère de préparation (intermédiaire) | 10–12 sem. |
> | Sortie longue actuelle → cible | 1 h 05 → 1 h 50 |
> | Allure @21K estimée | 4'50 (confiance moyenne, 10 km de septembre) |
>
> **Verdict : Ambitieux.** Le temps suffit pour la sortie longue en respectant 1,10 ×, mais 1 h 40 demande 10 s/km de mieux que ton estimation. Alternative : viser 1 h 43 et recaler après le bloc 2.
>
> > **À toi :** Tu gardes 1 h 40, ou tu préfères 1 h 43 ?
