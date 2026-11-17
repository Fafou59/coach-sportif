# Outils Garmin exposés par missingmcp

Recherche du 17/11/2026, ticket [#2](https://github.com/Fafou59/coach-sportif/issues/2). Elle répond à la question : quels outils Garmin le connecteur missingmcp expose-t-il réellement, et avec quelles limites pour le coach (cadrage § 2 et § 3, ADR 0001 à 0003) ?

Méthode : lecture du code source au commit figé. Aucun outil Garmin n'a été appelé (le compte branché est un compte réel).

Niveaux de confiance :
- **Élevé** : lu dans le code ou la docstring du commit figé, ou confirmé par un test en conditions réelles publié par le mainteneur.
- **Moyen** : documenté par le dépôt mais pas vérifié en conditions réelles, ou déduit du code sans test.
- **Faible** : inférence de notre part.

## Sources

| Réf. | Source primaire |
|---|---|
| S1 | missingmcp, `Dockerfile` (branche `main`) : `ARG GARMIN_MCP_REF=a2ca5fcac34524b83814fe2fcf3d479f8a75983f`, avec le commentaire de revue du 28/10/2026 — https://github.com/VelkyVenik/missingmcp/blob/main/Dockerfile |
| S2 | missingmcp, page `/garmin` (`src/missingmcp/templates/garmin.html`) : « All 157 tools », générée depuis le commit `a2ca5fc` ; garmin_mcp tourne « unmodified » — https://missingmcp.com/garmin |
| S3 | Taxuspt/garmin_mcp au commit `a2ca5fc` (20/10/2026), `src/garmin_mcp/*.py` — https://github.com/Taxuspt/garmin_mcp/tree/a2ca5fcac34524b83814fe2fcf3d479f8a75983f |
| S4 | Même commit, `workout_templates.py` (ressource `workout://reference/structure`) |
| S5 | Ticket amont [#245](https://github.com/Taxuspt/garmin_mcp/issues/245) : l'ID 6 `power.between` est enregistré comme `pace.zone` et s'affiche en km/h sur la montre (test sur Instinct 2X Solar) |
| S6 | Tickets amont [#369](https://github.com/Taxuspt/garmin_mcp/issues/369) (plage % FTP) et [#367](https://github.com/Taxuspt/garmin_mcp/issues/367) (unité relue par `get_workout_by_id`) |
| S7 | PR amont ouvertes au 17/11/2026 : [#194](https://github.com/Taxuspt/garmin_mcp/pull/194) (watts), [#485](https://github.com/Taxuspt/garmin_mcp/pull/485) (GPX en base64), [#507](https://github.com/Taxuspt/garmin_mcp/pull/507) (ID d'entrée de calendrier), [#516](https://github.com/Taxuspt/garmin_mcp/pull/516) (échauffement à 0) ; ticket [#523](https://github.com/Taxuspt/garmin_mcp/issues/523) (pas de modification de séance) |
| S8 | Schémas des outils Garmin chargés dans cette session (ToolSearch, sans appel) |

## Réponse courte

- missingmcp fait tourner **garmin_mcp sans modification au commit `a2ca5fc`**, qui est aussi la **tête actuelle de `main`** chez Taxuspt (vérifié le 17/11/2026 : aucun commit après). Il n'y a donc **aucune différence** entre la version figée et `main`. Seules des PR encore ouvertes pourraient changer la donne (S7). **Élevé** (S1, S3).
- **157 outils** sont exposés, sans filtrage : `GARMIN_TOOL_PROFILE` n'est pas défini côté missingmcp. Les 157 noms de la session correspondent un à un aux 157 outils du code source, et les docstrings sont identiques. **Élevé** (S1, S2, S3, S8).
- **Couverture de nos besoins** : bonne pour les séances structurées, la planification, la suppression, les zones FC, l'effort perçu, la VFC, la FC de repos et le sommeil.
- **Trois limites fortes** :
  1. les **parcours ne peuvent pas être envoyés** depuis Claude ;
  2. une **séance ne peut pas être modifiée** : il faut la supprimer puis la recréer ;
  3. la docstring **recommande à tort l'ID 6 pour une cible en watts absolus**.

## 1. Séances course et vélo structurées

**Outil générique : `upload_workout(workout_data)`**, et `upload_workouts(workouts)` pour plusieurs séances. Il prend le JSON Garmin brut. **Élevé** (S3 `workouts.py`).

**Structure d'une séance**
- `ExecutableStepDTO` pour une étape simple, `RepeatGroupDTO` pour un bloc répété.
- Un bloc répété exige `endCondition {conditionTypeId: 7, "iterations"}` et `numberOfIterations`. Le serveur répare l'ID manquant.
- `stepOrder` est un compteur unique, en profondeur, sur toute la séance : il ne repart pas à 1 dans un bloc. **Élevé**.

**Types d'étape (`stepTypeId`)** : 1 échauffement, 2 retour au calme, 3 intervalle, 4 récupération active, 5 repos, 6 répétition. **Élevé** (S4).

**Conditions de fin (`conditionTypeId`)** : 1 bouton tour, 2 temps (s), 3 distance (m), 4 calories, 5 puissance, 6 FC, 7 itérations, 8 repos fixe, 9 répétition fixe, 10 répétitions (renfo), 11 TSS. Une paire ID/clé incohérente est **rejetée avant l'envoi**. **Élevé** (S3, constante `END_CONDITION_TYPE_IDS`).

**Sports (`sportTypeId` des séances, différents de ceux des activités)** : 1 course, 2 vélo, 5 renfo, 6 cardio, 12 marche (docstring). La référence S4 ajoute 3 autre, 4 natation, 7 yoga, 8 pilates, 9 HIIT, 11 mobilité, 13 rucking. **Élevé** pour 1, 2, 5, 6 et 12 ; **Moyen** pour 7 et 11 (documentés, sans test publié).

### Cibles

| Besoin | Encodage | Confiance |
|---|---|---|
| Sans cible | ID 1 `no.target` | Élevé |
| **FC en plage bpm** (bandes FC) | ID 4 `heart.rate.zone` + `targetValueOne`/`targetValueTwo` en bpm, **sans** `zoneNumber`. Garmin l'affiche comme une FC « Custom » | Élevé |
| FC en zone nommée | ID 4 + `zoneNumber` 1–5. Ne pas mélanger avec une plage : Garmin supprime la plage en silence | Élevé |
| **Allure** | ID 6 `pace.zone` + bornes en **m/s** (5:00/km = 3,333 m/s). Ordre des bornes à vérifier à la répétition à blanc | Élevé (encodage) / Moyen (ordre des bornes) |
| **Puissance en % FTP** | **ID 2 `power.zone`** + `targetValueOne`/`targetValueTwo` en pourcentages + `"targetValueUnit": {"unitKey": "percent"}`. Garmin Connect affiche « Custom Power 76–81% FTP » avec les watts correspondants. Sans l'unité, Garmin lit les bornes comme des watts | Élevé (S3, S6) |
| Puissance en zone 1–7 | ID 2 `power.zone` + `zoneNumber` | Élevé |
| Puissance en watts absolus | **Piège** : la docstring et la référence S4 recommandent l'ID 6 `power.between`. Or Garmin enregistre l'ID 6 comme `pace.zone` et la montre affiche « 864 km/h » (S5). Il faut l'**ID 2 `power.zone` avec les bornes en watts**. Le code figé accepte encore l'ID 6 ; la correction est dans la PR #194, toujours ouverte | Élevé (S5, test publié) |
| Cible secondaire | `secondaryTargetType` + `secondaryTargetValueOne/Two` (ex. cadence + puissance) | Moyen |

À la relecture, `get_workout_by_id` conserve l'unité (`target_value_unit`). Son option `raw=true` renvoie le JSON Garmin complet, ce qui permet de **vérifier un % FTP après la création**. **Élevé** (S6, correctif `fc3f11c` antérieur au pin).

**Constructeurs simplifiés** (course et marche uniquement, cible FC uniquement) :
- `create_run_workout` : séance continue, avec `hr_min`/`hr_max` en bpm ;
- `create_run_interval_workout` : répétitions + récupération, FC en bpm sur les répétitions et en option sur les récupérations ;
- `create_walk_run_workout` et `create_z2_walk_workout`.

Leurs limites : **pas de cible d'allure, pas de vélo, pas de description libre** (elle est générée automatiquement), et l'échauffement et le retour au calme de `create_run_workout` sont des étapes en marche. Pour nos séances avec allure nommée, ou à vélo, il faut donc passer par **`upload_workout`**. **Élevé** (S3 `workout_builders.py`).

`upload_workout` transmet les autres champs tels quels, dont `description`. Le nom fait **256 caractères au plus** : au-delà, Garmin le tronque sans prévenir (docstrings des constructeurs). **Moyen** pour la description, **Élevé** pour la longueur du nom.

## 2. Renfo et mobilité

**Renfo** : `create_strength_workout(name, exercises=[{name, sets, reps, rest_seconds, category?}])`. Chaque exercice devient une étape en répétitions, regroupée en bloc répété quand il y a plusieurs séries.
- `category` doit appartenir au catalogue Garmin ; `UNASSIGNED` et `OTHER` sont refusés (erreur 400).
- `exerciseName` n'est conservé que s'il correspond à une clé Garmin.
- **Pas de charge ni d'exercice chronométré** (gainage en secondes, par exemple) avec ce constructeur.

Pour ces cas, il faut passer par `upload_workout` en sport 5, avec `category`, `exerciseName`, `weightValue`/`weightUnit` et une condition de fin en temps ou en répétitions. **Élevé** (S3).

Le catalogue des exercices est référencé dans la docstring : https://connect.garmin.com/web-data/exercises/Exercises.json.

Après la séance, `get_activity_exercise_sets` lit les séries réalisées et `set_activity_exercise_sets` permet de les corriger. **Élevé**.

**Mobilité (séance simple)** : il n'existe **pas de constructeur dédié**. Il faut utiliser `upload_workout` avec des étapes en temps ou au bouton tour, sans cible, en sport 11 `mobility` ou 7 `yoga` (S4), ou à défaut 6 `cardio_training`. **Moyen** : les ID viennent de la référence du dépôt, sans test publié. **À valider lors de la répétition à blanc.**

## 3. Calendrier, suppression, lecture

| Besoin | Outil(s) | Points d'attention | Confiance |
|---|---|---|---|
| Planifier | `schedule_workout(workout_id, date)`, `schedule_workouts([...])` (accepte aussi `workout_data` pour créer et planifier en un appel), `schedule_week([{date, workout_id}])` | Idempotents : pas de doublon si la séance est déjà à cette date. `schedule_workout` **ne renvoie pas l'ID de l'entrée de calendrier** (PR #507 ouverte) ; `schedule_week` le renvoie quand Garmin le fournit | Élevé |
| Déplacer | `reschedule_workout(scheduled_workout_id, date)` | Déplace l'entrée sans créer de doublon. Prend l'**ID d'entrée de calendrier**, pas l'ID de séance | Élevé |
| Déplanifier | `unschedule_workout(id)`, `unschedule_workouts([ids])` | Même ID d'entrée de calendrier. La séance reste dans la bibliothèque. L'index de calendrier se met à jour avec un léger délai juste après une planification | Élevé |
| Lire le planifié | `get_scheduled_workouts(start, end)` | Renvoie `date`, `scheduled_workout_id`, `workout_id`, `name`, `sport` et `completed` | Élevé |
| Lire une séance | `get_workouts` (liste), `get_workout_by_id(id, raw?)` | — | Élevé |
| Supprimer | `delete_workout(id, confirm)`, `delete_workouts(ids, confirm)` | **Deux temps** : `confirm=false` (par défaut) renvoie un aperçu, `confirm=true` supprime définitivement. Ce mécanisme recoupe notre règle « rien sans GO » | Élevé |
| Modifier | **Aucun outil** | Il faut supprimer puis recréer (ticket amont #523 ouvert) | Élevé |
| Envoyer sur la montre | `push_workout_to_device(workout_id, device_id?)` | **Inutile pour une séance planifiée** : le calendrier se synchronise seul. Chaque appel ajoute une copie | Élevé |
| Courses de l'athlète | `get_calendar_events(start, end)` | Lecture seule ; aucun outil pour créer un événement | Élevé |

## 4. Zones FC du compte

- `get_heart_rate_zones(sport?)` lit les profils DEFAULT, RUNNING, CYCLING, etc.
- `set_heart_rate_zones(sport, max_hr?, resting_hr?, lactate_threshold_hr?, calculation_method?, zone_boundaries?)` écrit **un seul sport**, en relisant puis réécrivant la configuration et en renvoyant la version enregistrée par Garmin. **Élevé** (S3 `user_profile.py`).

Limites :
- les bornes manuelles exigent `calculation_method="custom_bpm"` et **5 planchers bpm strictement croissants** (Z1 à Z5, le plafond de Z5 étant la FC max) ;
- changer de méthode **ne recalcule pas** les planchers ;
- fournir `resting_hr` **désactive la mise à jour automatique** de la FC de repos par Garmin ;
- aucun effet rétroactif sur les activités passées.

Rappel de notre cadrage : les zones Z1–Z5 servent à l'analyse, les séances visent des bandes FC en bpm. Régler les zones du compte reste donc optionnel. **Élevé**.

## 5. Parcours

| Outil | Ce qu'il fait réellement | Confiance |
|---|---|---|
| `get_courses` | Liste : id, nom, distance, type, date | Élevé |
| `get_course_details(id)` | Distance, **D+ et D−**, points d'intérêt, nombre de points. Ne renvoie **pas** les points du tracé : le profil fin n'est donc pas lisible ici | Élevé |
| `download_course_gpx(id)` | Reconstruit le GPX et l'**écrit sur le disque du serveur** ; il renvoie seulement le chemin, pas le contenu. Via missingmcp, ce fichier est **inaccessible** à l'athlète comme à Claude | Élevé (code) |
| `upload_course(gpx_path, ...)` | Lit un fichier GPX **sur le disque du serveur**. Depuis Claude (connecteur distant), impossible d'y déposer un fichier : **inutilisable via missingmcp**. La PR #485 (paramètre `gpx_base64`) corrigerait ce point mais reste ouverte | Élevé (code, PR #485) |
| `delete_course(id, confirm)` | Suppression en deux temps | Élevé |
| Envoyer un parcours sur la montre | **Aucun outil** (`push_workout_to_device` ne concerne que les séances) | Élevé |

Conséquence pour le cadrage (04.10, 05.6 : « parcours envoyé à la montre après GO ») : le coach peut **lire** un parcours déjà présent dans Garmin Connect (distance, D+, D−) pour le profil de course. En revanche, l'import et l'envoi à la montre restent **à faire par l'athlète** dans l'application Garmin Connect. **Élevé**.

## 6. Effort perçu, récupération, sommeil

| Besoin | Outil(s) | Détail | Confiance |
|---|---|---|---|
| **Effort perçu (RPE)** | `get_activity(id)` → `workout_rpe`, `workout_feel` | Valeur **brute de Garmin sur 0–100** (RPE 7 = 70), à diviser par 10. **Absent des listes** (`get_activities_by_date`, `get_activities_fordate`) : il faut **un appel par activité**. Écriture possible avec `set_perceived_effort(id, rpe 0–10)` | Élevé |
| **VFC sur une plage** | `get_hrv_trend(start, end)` | **30 jours au plus** (7–21 recommandés) : moyenne de la nuit, moyenne sur 7 jours, statut, moyenne de la période. Couvre tout juste la ligne de base de 28–30 jours. Un appel Garmin par jour en interne | Élevé |
| VFC sur un jour | `get_hrv_data(date)` | Avec ligne de base Garmin (bornes « balanced ») ; série par tranches de 5 min en option, volumineuse | Élevé |
| **FC de repos** | `get_rhr_day(date)` pour un jour ; **aucun outil de plage dédié**. Sur une plage, `get_sleep_summary_range` donne `resting_heart_rate_bpm` par nuit | Le champ vient de l'enregistrement de sommeil ; comparer avec `get_rhr_day` sur quelques jours lors de la répétition à blanc | Élevé (outil) / Moyen (équivalence des valeurs) |
| **Sommeil sur une plage** | `get_sleep_summary_range(start, end)` | **90 nuits au plus** ; résumé compact par nuit : score, durée, phases, réveils, FC de repos, VFC nocturne si disponible. Une requête par nuit en interne ; une erreur interrompt la plage | Élevé |
| VFC battement par battement (DFA-α1, hors V1) | `get_activity_fit_data` | Calcule RMSSD, SDNN et pNN50 à partir des intervalles R-R du fichier FIT, et peut renvoyer les R-R bruts. DFA-α1 n'est pas calculé | Moyen |

## 7. Outils de synthèse économes en contexte

- **`get_sleep_summary_range`** : un seul appel suffit pour le sommeil, la FC de repos et la VFC nocturne sur 28–30 jours. C'est le meilleur candidat pour la ligne de base du dimanche.
- `get_hrv_trend` : VFC, 30 jours au plus.
- `get_activities_by_date` : liste allégée, paginée par 100 (sans RPE ni charge).
- `get_training_load_trend` : charge aiguë et chronique Garmin, 90 jours au plus. Il contient un ACWR, que **notre référentiel n'utilise pas** (fichier 03).
- `get_weekly_intensity_minutes`, `get_stats_range` (28 jours au plus), `get_progress_summary_between_dates` (cumul d'une métrique : distance, durée, D+…).
- `get_heart_rates_summary` (~500 octets au lieu de ~25 ko), `get_sleep_summary` (~350 octets au lieu de ~50 ko), `get_morning_training_readiness`, `get_training_status`.

**Coût caché** : 157 schémas d'outils sont chargés dans chaque conversation, et la docstring de `upload_workout` à elle seule fait plusieurs milliers de caractères. missingmcp n'active pas de profil réduit (`GARMIN_TOOL_PROFILE`), et l'athlète ne peut pas le régler. **Élevé** (S1). L'effet sur le quota de Claude Free reste **à mesurer** lors de la répétition à blanc (**Faible**, non mesuré).

## 8. Manques par rapport à nos besoins

1. **Envoi de parcours** : ni import GPX ni envoi à la montre depuis Claude. Le coach donne une consigne et l'athlète agit dans Garmin Connect.
2. **Pas de modification de séance** : un ajustement après un imprévu se fait par suppression (en deux temps) puis recréation et nouvelle planification. Il faut prévoir un GO couvrant les deux.
3. **Watts absolus mal documentés** : la docstring induit en erreur (ID 6). Le skill `coach-garmin` doit imposer l'**ID 2 `power.zone`**, en % FTP avec l'unité `percent` (notre cas nominal) ou en watts.
4. **Pas d'allure dans les constructeurs simplifiés** : toutes nos séances avec allure nommée passent par `upload_workout` en m/s. Le skill doit donner la conversion et un gabarit JSON.
5. **RPE coûteux à lire** : un `get_activity` par activité. Sur une semaine de 5 à 8 activités, ça reste acceptable ; à limiter aux séances clés pendant les checks.
6. **Pas d'ID d'entrée de calendrier** au retour de `schedule_workout` : relire `get_scheduled_workouts` avant de déplacer ou déplanifier (ou utiliser `schedule_week`).
7. **Mobilité** : le sport 11 `mobility` n'a pas été testé publiquement (repli : 6 `cardio_training`).
8. **Ressources MCP** (`workout://templates/*`) : nous ignorons si le client Claude.ai les expose au modèle. Il ne faut pas compter dessus ; les gabarits doivent vivre dans le skill (**Faible**).

## 9. Version figée et `main`

- Pin missingmcp : `a2ca5fcac34524b83814fe2fcf3d479f8a75983f` (20/10/2026), relu par l'opérateur le 28/10/2026. Il apporte 3 outils par rapport au pin précédent (`delete_activity`, `reschedule_workout`, `push_workout_to_device`) et le `confirm=true` obligatoire pour les suppressions (S1).
- `main` chez Taxuspt au 17/11/2026 : **même commit**, donc aucune différence.
- PR ouvertes qui changeraient nos limites si elles étaient fusionnées **puis** reprises par missingmcp (un changement de pin est une décision relue par l'opérateur, S1) :
  - #194 : watts en ID 2, ID 6 réservé à l'allure ;
  - #485 : GPX en base64, ce qui rendrait possible l'import de parcours ;
  - #507 : ID d'entrée de calendrier renvoyé à la planification ;
  - #515 et #516 : robustesse des constructeurs ;
  - ticket #523 : modification de séance.
- À surveiller : un changement de pin chez missingmcp peut renommer ou modifier des outils. Le skill `coach-garmin` devrait citer le commit sur lequel il a été validé.
