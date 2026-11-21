# Journal des versions du skill `coach`

## v0.4.1 (21/11/2026) — correctif après le premier démarrage réel

- #36 Allures : le garde-fou « pas de test maximal après un marathon » interdit le test, il ne baisse plus les allures quand des données récentes existent (référentiel 02, règle 9, Q126) ; contrôle de cohérence écrit sous le tableau des allures (EF, Seuil, Seuil haut, VMA face aux courses et séances réelles) ; courses hors fenêtre de récence seulement pour ce contrôle ; chaque allure reliée au nom que l'athlète emploie ; VMA déclarée notée « sans test ».
- #37 Qualités des blocs proposées en question à l'étape 6, selon le contenu de phase par niveau (04, règle 1) ; principale et à la carte travaillent deux qualités différentes, sauf en affûtage (01, règle 8, Q129) ; contrôle à l'étape 7 et en fin de bloc.
- #38 Mêmes données, mêmes chiffres : milieu de la fourchette par défaut ; toute autre valeur ou tout paramètre sans règle (sortie longue et EF de reprise) posé en question ; chiffre déjà au carnet recopié, jamais recalculé.
- #39 Une seule hausse forte par semaine, contrôlée semaine par semaine dans le message (étape 7, fin de bloc).
- #40 Calendrier Garmin lu depuis aujourd'hui avant toute création ; carnet mis à jour dans le même message, relu contre le calendrier.
- #41 Une seule valeur par donnée au carnet ; textes d'attente remplis ou retirés ; relecture du carnet en fin de démarrage.
- #42 Messages en français, sans note de travail ; un verdict dans chaque message, correction comprise.
- Q133 Tests de recalage : toute course compte, ainsi qu'un test intégré (dernière répétition quasi à fond) ; un refus n'est reproposé qu'à la fin de bloc suivante (02, règle 10).
- Q134 À la carte après une reprise de course : accès conservé si des séances dures étaient tolérées avant, seulement Aucune ou Légère pendant 2 semaines de retour de l'intensité (01, règle 8).
- Q131 Chrono : sans chrono en tête, le coach propose spontanément une fourchette estimée (étape 2) ; il la recalcule à chaque fin de bloc depuis les allures recalées, la cible ne change qu'avec l'accord de l'athlète.

## v0.4 (20/11/2026) — retours sur le guide d'installation

- Q103 Garmin : le coach propose lui-même le branchement quand les outils manquent ; les points de vigilance missingmcp sont dits **avant** toute saisie d'identifiants, avec ❓ « tu veux le brancher ? » ; refus ou branchement noté dans l'onglet Athlète (ligne « Garmin ») pour ne pas reproposer ; ajout impossible depuis l'appli mobile, dit à l'athlète. Le guide n'a plus d'étape « Brancher Garmin ».
- Q105 Un seul mot, « check » : `check.md` § 0 choisit le rendez-vous (imprévu, bilan du dimanche, check avec rappel si une séance du dimanche reste à faire, bilan express, bilan avancé à la demande, check) ; « bilan » et « point » valent « check ». Fin du démarrage : rythme expliqué avec ce seul mot.

## v0.3 (20/11/2026) — corrections de la répétition ciblée

- #27.1 Renfo : créneau à la carte compté comme jour dur dès la semaine-type ; renfo jambes le lendemain d'un jour dur ou le même jour après lui ; contrôle jour par jour écrit dans le message (démarrage étape 5, bilan temps 2 à l'ouverture de l'à la carte, bilan express) ; aucun garde-fou affiché comme respecté sans comparaison.
- #27.2 Sortie longue : § Calcul de la sortie longue (départ = plus longue sortie des 30 j, hausses, semaines allégées, plafond) refait à l'identique aux étapes 4, 6, 7 et écrit au Plan ; toute valeur validée modifiée passe par une correction ❓.
- #27.3 Repères : source précise et confiance pour chaque allure, puissance, FC, dans le message et l'onglet Repères (cascade 02.9) ; départ des valeurs déjà au carnet, changement expliqué.
- #27.4 Séance Garmin non créée par le coach ni notée au carnet : décrite, sans origine ni date de création supposées.
- #27.5 Exemples : avertissement « chiffres inventés » au-dessus des exemples ; plafonds FC des exemples (151, 152, 153 bpm) remplacés par l'onglet Repères.
- #28 Référentiel appliqué à la lettre : problème dit en une ligne, ❓ à l'athlète, question notée pour qui tient le référentiel ; Q99 (cumul des 30 % après une semaine allégée, d'affûtage ou de récupération mesuré depuis la dernière semaine pleine d'avant) ; course A ou B au-delà de 1,10 × signalée comme pic et mise au choix de l'athlète.

## v0.2 (19/11/2026) — corrections de la répétition à blanc

- #17 Carnet : « pas encore de carnet » = aucun lien ou texte d'attente → créé au démarrage, étape 1 ; jamais de second carnet quand un lien valide existe ; instructions du kit sans texte entre chevrons.
- #18 Consentements : bloc 🔒 qui liste chaque donnée « si elle te concerne » ; « OK » vaut accord pour toutes, « non » par donnée, retrait à tout moment ; sans réponse, rien n'est lu.
- #19 Progression : 1,10 × cité juste (plus longue sortie des 30 derniers jours, séance entière) ; hausse contrôlée depuis la semaine réellement précédente, reprise comprise ; premier bloc après une course à 70–80 % du volume d'avant (Q93).
- #20 Objectifs : chrono visé ou « sans chrono » pour chaque A et B ; tout en français ; une seule cible EF (bande Facile), plage étroite observée = observation.
- #21 Lisibilité : solidité des règles en mots (expliquée une fois au démarrage, notée au carnet) ; questions ❓ numérotées avec ➡️ et « OK » ; blocs ✅ GO requis et 🔒 Consentement isolés sous un trait.
- #22 Check : date de la dernière séance analysée dans Plan, séances clés postérieures seulement ; sans plage personnelle, suivi par le ressenti.
- #23 Bilan : échelles 5 = au mieux avec bornes (Q96), réponse en une ligne ; carnet écrit sans GO (même en MODE RÉPÉTITION) ; pas d'indicateurs Garmin propriétaires ; à la carte « pas encore disponible » ; ménage de la bibliothèque par ID, sans occurrence future, après la comparaison prévu / fait ; « cause inconnue » plutôt qu'une cause inventée.
- #24 Challenge : coût redit une fois, « Tu maintiens ? », choix noté au journal ; un seul A recommandé par période de préparation ; verdict sur le calendrier entier ; pas de re-challenge sans fait nouveau (Q97).
- #25 Démarrage : rien depuis la mémoire de Claude ; aucun détail d'outil dans les messages ; antécédents en une liste ❓ oui/non, une seule relance ; détail adapté au niveau ; préférence contre une règle solide challengée ; progression débutant en course-marche (03, règle 10, Q98).
- #26 Imprévus (critique) : 48 h après maladie = séances dures seulement, EF après test de reprise réussi ; imprévu écrit au carnet dans le message même (« Imprévus ouverts », bloc en cours, journal) et relu avant toute séance proposée.
- Garde-fou des 30 % : une semaine allégée prévue au plan n'est jamais la référence (Q100, Q102) ; imprévu ou reprise après une course A : règle 8.
- Course plus longue que la préparation (Q101) : pic expliqué une fois pour un objectif A ; signalé à chaque fois pour une course B ou C.
- Contrôle du renfo refait chaque fois que la semaine-type est montrée ou modifiée, question libre comprise (vérification courte du 20/11 : renfo du mercredi resté la veille de la séance à la carte du jeudi).
