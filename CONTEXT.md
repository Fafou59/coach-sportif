# Coach Sportif

Coach d'entraînement IA pour un cercle privé d'athlètes d'endurance : il fixe les objectifs, construit un plan sur mesure et en suit l'exécution à partir des données de la montre.

## Langage

### Athlète et objectifs

**Athlète** :
Personne coachée, du débutant au confirmé amateur. Chaque athlète a son propre compte et ses propres données.
_À éviter_ : utilisateur, client, coureur (trop restrictif)

**Sport couvert** :
Discipline pour laquelle le coach prescrit des séances : course (route et trail), vélo, renfo, mobilité. Natation et triathlon sont hors périmètre pour l'instant.

**Objectif** :
Échéance que l'athlète se fixe (course, chrono, habitude), classée A (principal), B ou C (étapes de préparation).
_À éviter_ : but, cible

**Profil de course** :
Description du parcours d'un objectif A ou B, recueillie au démarrage et stockée dans le carnet : distance, D+ et D−, D+/km, catégorie (plat, vallonné, accidenté, montagne) et montées et descentes principales. Elle oriente le travail spécifique et le plan de course.
_À éviter_ : parcours, tracé, profil altimétrique (seulement une partie)

**Verdict** :
Avis franc du coach sur la faisabilité d'un objectif : Facile, Réaliste, Ambitieux ou Difficile en l'état. L'athlète décide toujours.
_À éviter_ : évaluation, faisabilité

**Contrainte** :
Limite non négociable de l'athlète (jours disponibles, durée max, vacances, matériel), que le coach respecte sans discuter.
_À éviter_ : disponibilité, impératif

**Préférence** :
Souhait de l'athlète (ex. garder une sortie vélo d'entretien) que le coach intègre mais peut challenger, en explicitant le conflit, s'il nuit à l'objectif.
_À éviter_ : envie, contrainte souple

**Mobilité** :
Séance d'assouplissement et d'amplitude articulaire, sans prescription d'intensité.
_À éviter_ : yoga, stretching

### Plan

**Carnet** :
Document vivant propre à chaque athlète, organisé en six onglets (Athlète, Objectifs, Repères, Plan, Notes, Archives), source de vérité de ce qui est décidé. Le réalisé et le planifié, eux, se lisent dans la montre.
_À éviter_ : journal, fiche athlète (la fiche est une partie du carnet)

**Démarrage** :
Parcours d'entrée d'un athlète, en étapes courtes sauvegardées dans le carnet : profil (antécédents compris), objectifs (avec leur profil de course), contraintes et préférences, verdict, semaine-type, plan macro, premier bloc, création de la première semaine.
_À éviter_ : onboarding, questionnaire

**Plan macro** :
Vue d'ensemble de la saison jusqu'à l'objectif principal : succession des blocs, qualité travaillée et volume par semaine.
_À éviter_ : plan global, programme

**Phase de base** :
Première partie du plan macro, consacrée aux qualités fondamentales : volume en endurance qui progresse (jamais réduit au profit de la vitesse), force (renfo) et vitesse courte (lignes droites). Suivie de la phase spécifique puis de l'affûtage.
_À éviter_ : foncier, phase générale

**Bloc** :
Unité de planification : 2 à 3 semaines de charge suivies d'une semaine d'allègement. Un bloc est détaillé séance par séance et validé à son démarrage.
_À éviter_ : cycle, mésocycle

**Semaine-type** :
Grille co-construite qui fixe, par jour de la semaine, le type de séance (sport, qualité ou endurance, durée maximale).
_À éviter_ : semaine modèle, routine

**Séance clé** :
Séance qui appelle une analyse et un échange avec l'athlète : tout fractionné (y compris tempo et seuil), toute sortie longue, tout test (FTP, VMA), toute course.
_À éviter_ : entraînement important, séance qualité

**Séance dure** :
Séance qui consomme le budget hebdomadaire d'intensité (course et vélo confondus) : fractionné (dont les répétitions en côte de plus de 15 s), tempo, seuil, test, course, et sortie longue contenant de l'allure spécifique. Toute séance dure est une séance clé ; l'inverse est faux (une sortie longue en endurance est clé sans être dure).
_À éviter_ : séance intense, séance de qualité

**Allure nommée** :
Allure de référence en course, désignée par son nom plutôt que par une valeur, recalée à chaque fin de bloc ou après une course. Les allures nommées forment une table de correspondance avec les autres méthodes ; seul un sous-ensemble sert dans les séances : EF, Seuil, Seuil haut, VMA et allure objectif.

**Allure objectif** :
Allure de la course visée sur route, notée @42K, @21K, @10K ou @5K, recalée sur les résultats réels de l'athlète. En trail, il n'y a pas d'allure objectif : on pilote à l'effort.
_À éviter_ : allure spécifique (quand on parle de la valeur), allure cible

**Seuil haut** :
Allure proche de la vitesse critique, tenable environ 20 à 40 minutes, au-dessus du seuil.
_À éviter_ : Seuil 30

**Lignes droites** :
Accélérations progressives de 8 à 15 secondes, sans aller à fond, avec récupération complète. Ce n'est pas une séance dure.
_À éviter_ : sprints (réservé aux sprints courts, à fond), accélérations

**Sprints courts** :
Efforts à fond de 15 secondes au plus, avec récupération complète (au moins 2 min), à plat ou en côte, ajoutés à une séance d'EF. Hors budget de séances dures, comme les lignes droites.
_À éviter_ : sprint pour un effort de plus de 15 s (endurance de vitesse ou répétitions en côte), lignes droites (qui ne vont pas à fond)

**Endurance de vitesse** :
Répétitions à fond ou presque, d'environ 20 secondes à 1 min 30. Toujours une séance dure, jamais en séance à la carte ; possible en séance principale pour un confirmé qui prépare un 5–10 km.
_À éviter_ : endurance de force (sens Campus Coach), résistance

**Endurance de force** :
Travail musculaire prolongé contre une résistance : côtes (répétitions de plus de 15 s, donc séance dure), bondissements, vélo à basse cadence.
_À éviter_ : force-endurance, renfo spécifique

**Séance principale** :
Séance dure prioritaire de la semaine : elle porte la qualité du bloc et c'est elle qu'on protège en premier quand la semaine se complique.
_À éviter_ : séance clé (sens plus large), fractionné principal, séance verrouillée

**Séance à la carte** :
Seconde séance dure facultative, choisie par l'athlète dans un menu (Aucune, Légère, Moyenne, Soutenue) dont toutes les options respectent les garde-fous ; seule l'option validée est créée dans la montre.
_À éviter_ : séance complémentaire, fractionné bonus

**Bande FC** :
Une des trois cibles de fréquence cardiaque des séances : Facile, Seuil ou Au-dessus. À distinguer des zones Z1–Z5 de Garmin, qui servent seulement à l'analyse. Les trois bandes nomment aussi les 3 intensités du modèle de Seiler : Facile (sous le 1er seuil), Seuil (entre les seuils), Au-dessus (au-dessus du 2e seuil). La répartition 80/20 se lit en temps en bande Facile (Z1 + Z2 de Friel en course, de Coggan à vélo).
_À éviter_ : zone (réservé à Z1–Z5), zone cible, Z1/Z2/Z3 pour le modèle de Seiler

**Séance anormale** :
Séance qui n'est pas une séance clé mais dont les données sortent de l'ordinaire (FC très haute, arrêt prématuré). Elle déclenche un échange sans devenir une séance clé.

### Suivi

**Check** :
Rituel court lancé par l'athlète : le coach lit les données récentes et ne développe que s'il y a une séance clé à analyser, une séance anormale ou une métrique en dérive ; sinon il répond « RAS ». « check » est le seul mot que l'athlète retient : selon le jour et le carnet, le coach en fait un check, le bilan du dimanche ou un bilan express (Q105).
_À éviter_ : suivi quotidien, point du jour

**Bilan du dimanche** :
Rendez-vous hebdomadaire en deux temps : synthèse chiffrée et questions sans adaptation, puis adaptation et création de la semaine suivante dans la montre.
_À éviter_ : revue hebdo, check-in

**Bilan express** :
Version courte du bilan du dimanche, proposée au premier check qui suit un dimanche sans bilan : synthèse en 3 lignes, une question de forme, création des séances restantes.

**Plage personnelle** :
Fourchette propre à l'athlète pour une métrique de récupération (VFC, FC de repos, durée de sommeil) : ligne de base sur 28–30 jours ± le plus petit changement significatif. Une métrique dérive quand sa moyenne sur 7 jours en sort du côté défavorable (VFC ou sommeil en dessous, FC de repos au-dessus).
_À éviter_ : bande personnelle, bande (réservé aux bandes FC)

**Imprévu** :
Événement qui écarte l'athlète du plan (maladie, douleur, voyage, surcharge). Il est signalé dans un check et traité par ajustement des séances déjà créées.
_À éviter_ : incident, aléa

**Bilan de course** :
Retour après une course objectif : ressenti, ce qui a marché, reprise, puis relance du démarrage à l'étape des objectifs.
_À éviter_ : bilan de fin d'objectif, débrief

### Méthode

**Référentiel de règles** :
Ensemble des règles d'entraînement appliquées par le coach. Chaque règle a une source, un niveau de preuve (élevé, moyen, faible), un indice (A, B, C, D, S) avec son statut, et une valeur par défaut validée par l'utilisateur. Statuts (doctrine du 17/11/2026, `docs/referentiel/00-doctrine.md`) : règle (A–B), garde-fou de prudence non prouvé (C–D à enjeu de sécurité), valeur de départ ou indicateur (autres C–D, jamais bloquants), choix de sécurité ou de conception (S).
_À éviter_ : règles du coach, garde-fous (un garde-fou est une catégorie de règle)
