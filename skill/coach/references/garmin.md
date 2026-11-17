# Séances Garmin : conventions et déroulé

Connecteur : missingmcp, qui fait tourner garmin_mcp sans modification (commit `a2ca5fc`, validé le 17/11/2026). Si un outil cité ici manque ou a changé de nom, dis-le et passe en mode dégradé (séances en texte). Repères de l'athlète (allures, FTP, bandes FC) : onglet Repères du carnet. Bornes des bandes FC et zones Coggan : référentiel 02 (règle 7, tableau B).

Sommaire : Déroulé de création · Modifier, déplacer, supprimer · Nom des séances · Cibles · Gabarits `upload_workout` · Lectures utiles · Parcours et PacePro · Zones FC du compte · Exemples.

## Déroulé de création

1. **Tableau de la semaine** en format B (jour, nom de séance) ; séance principale marquée ★.
2. **« GO »** explicite de l'athlète sur ce tableau.
3. **Créer** chaque séance avec `upload_workout` (renfo simple : `create_strength_workout`).
4. **Planifier** à sa date : `schedule_workout(workout_id, date)`, ou `schedule_week([{date, workout_id}])` qui renvoie aussi les ID d'entrées de calendrier.
5. **Relire** chaque séance avec `get_workout_by_id(id, raw=true)` : nom, sport, nombre de répétitions, cibles ; surtout l'unité `percent` des % FTP et l'ordre des bornes d'allure.
6. **Confirmer** à l'athlète : tableau de ce qui est créé, et toute anomalie corrigée ou restante.

N'utilise pas `push_workout_to_device` : le calendrier se synchronise seul, et chaque appel ajoute une copie sur la montre.

## Modifier, déplacer, supprimer

- **Déplacer** une séance de date : `reschedule_workout(scheduled_workout_id, date)`. L'ID d'entrée de calendrier se lit avec `get_scheduled_workouts` (champ `scheduled_workout_id`, différent de l'ID de séance). Pas de suppression.
- **Modifier** (contenu, durée, cible) : aucun outil ne modifie une séance. Supprime puis recrée, après une liste précise (séance retirée → séance qui la remplace) et un nouveau GO qui couvre les deux.
- **Supprimer** : `delete_workouts(ids)` d'abord avec `confirm=false` (aperçu), puis `confirm=true` après GO. C'est définitif.
- **Nettoyer la bibliothèque** (bilan du dimanche) : liste les séances de la semaine écoulée, GO, puis suppression. Les activités réalisées restent.

## Nom des séances

Format : `<sport> | <type> <durée> [contenu]` (256 caractères au plus, sinon Garmin tronque).

| Exemple | Sens |
|---|---|
| `R \| EF 45'` | Course, endurance fondamentale |
| `R \| EF 45' + 6×15" LD` | EF avec lignes droites |
| `R \| SL 1h30` · `V \| SL 2h` | Sortie longue course, vélo |
| `R \| Frac. 55' 5×5' @Seuil haut r:2'` | Fractionné : répétitions, allure nommée, récupération |
| `R \| Côtes 50' 8×1' r:descente` | Côtes |
| `R \| Test 30'` · `V \| Test FTP 1h` | Tests |
| `Renfo \| 30'` · `Mobilité \| 20'` | Renfo, mobilité |

- Allures : `@EF`, `@Seuil`, `@Seuil haut`, `@VMA`, allure objectif `@42K`, `@21K`, `@10K`, `@5K`. Jamais d'allure objectif en trail : on pilote à l'effort.
- `★` en fin de nom : séance principale. `(à la carte)` : l'option retenue.
- **Description** : objectif de la séance, consignes (effort, terrain, marche en côte), et au-delà de 75 min les glucides par heure (référentiel 09, règle 1).

## Cibles par type de séance

| Séance | Cible | Encodage |
|---|---|---|
| EF, sortie longue course | Bande FC Facile en bpm, plafond individualisé | ID 4 `heart.rate.zone`, `targetValueOne`/`Two` en bpm, **sans** `zoneNumber` |
| Fractionné sur le plat | Allure nommée ± 5 s/km (indice D, convention) | ID 6 `pace.zone`, bornes en **m/s** |
| Côtes, trail | Bande FC Seuil ou Au-dessus, ou pas de cible + effort perçu en description | ID 4 en bpm, ou ID 1 |
| Récupérations | Aucune | ID 1 `no.target` |
| Vélo avec capteur | % FTP (zones Coggan) | ID 2 `power.zone` + `targetValueUnit: {"unitKey": "percent"}` |
| Vélo sans capteur | Bande FC vélo en bpm | ID 4 en bpm |
| Renfo | Séries × répétitions | `create_strength_workout` ; `upload_workout` sport 5 pour charges et gainage en secondes |
| Mobilité | Aucune, étapes en temps | `upload_workout` sport 11 `mobility` (à tester à blanc ; repli : sport 6) |

Pièges :
- **Puissance : jamais l'ID 6.** La docstring de `upload_workout` le propose pour les watts, mais Garmin l'enregistre comme une allure. Toujours l'ID 2 `power.zone`.
- Sans l'unité `percent`, Garmin lit les bornes ID 2 comme des watts.
- FC : soit une plage en bpm, soit un `zoneNumber`, jamais les deux (Garmin efface la plage).
- Borne basse de la bande Facile : basse et large (≈ 60 % de la LTHR) ; seul le plafond compte.
- Allure : m/s = 1000 ÷ secondes par km (5'00/km = 300 s = 3,333 m/s). Mets la vitesse lente en `targetValueOne` et la rapide en `targetValueTwo`, puis vérifie l'ordre à la relecture (ordre à valider à la répétition à blanc).

**Échauffement et retour au calme** : pour les fractionnés et les tests, étapes au **bouton tour** (`conditionTypeId 1`, `lap.button`), durées indicatives en description (20' / 10'). Pas d'échauffement séparé pour une EF.

## Gabarits `upload_workout`

Codes : `stepTypeId` 1 échauffement, 2 retour au calme, 3 intervalle, 4 récupération, 5 repos, 6 répétition. `conditionTypeId` 1 bouton tour, 2 temps (s), 3 distance (m), 7 itérations, 10 répétitions (renfo). Sports : 1 course, 2 vélo, 5 renfo, 6 cardio, 11 mobilité. `stepOrder` est un compteur unique en profondeur : un bloc répété prend le numéro suivant et ses étapes continuent (bloc 2, enfants 3 et 4, retour au calme 5).

**EF course, bande Facile** (plafond 152 bpm, exemple) :

```json
{"workoutName": "R | EF 45'", "description": "Endurance fondamentale. Tu dois pouvoir parler.",
 "sportType": {"sportTypeId": 1, "sportTypeKey": "running"},
 "workoutSegments": [{"segmentOrder": 1, "sportType": {"sportTypeId": 1, "sportTypeKey": "running"},
  "workoutSteps": [{"type": "ExecutableStepDTO", "stepOrder": 1,
   "stepType": {"stepTypeId": 3, "stepTypeKey": "interval"},
   "endCondition": {"conditionTypeId": 2, "conditionTypeKey": "time"}, "endConditionValue": 2700,
   "targetType": {"workoutTargetTypeId": 4, "workoutTargetTypeKey": "heart.rate.zone"},
   "targetValueOne": 100, "targetValueTwo": 152}]}]}
```

**Fractionné à l'allure** (5 × 5' @Seuil haut 4'12 ± 5 s/km → 3,891–4,049 m/s, récupération 2') :

```json
{"workoutName": "R | Frac. 55' 5×5' @Seuil haut r:2' ★",
 "description": "Séance principale. Échauffement 20' au bouton tour, retour au calme 10'.",
 "sportType": {"sportTypeId": 1, "sportTypeKey": "running"},
 "workoutSegments": [{"segmentOrder": 1, "sportType": {"sportTypeId": 1, "sportTypeKey": "running"},
  "workoutSteps": [
   {"type": "ExecutableStepDTO", "stepOrder": 1, "stepType": {"stepTypeId": 1, "stepTypeKey": "warmup"},
    "endCondition": {"conditionTypeId": 1, "conditionTypeKey": "lap.button"},
    "targetType": {"workoutTargetTypeId": 1, "workoutTargetTypeKey": "no.target"}},
   {"type": "RepeatGroupDTO", "stepOrder": 2, "stepType": {"stepTypeId": 6, "stepTypeKey": "repeat"},
    "numberOfIterations": 5, "endCondition": {"conditionTypeId": 7, "conditionTypeKey": "iterations"},
    "workoutSteps": [
     {"type": "ExecutableStepDTO", "stepOrder": 3, "stepType": {"stepTypeId": 3, "stepTypeKey": "interval"},
      "endCondition": {"conditionTypeId": 2, "conditionTypeKey": "time"}, "endConditionValue": 300,
      "targetType": {"workoutTargetTypeId": 6, "workoutTargetTypeKey": "pace.zone"},
      "targetValueOne": 3.891, "targetValueTwo": 4.049},
     {"type": "ExecutableStepDTO", "stepOrder": 4, "stepType": {"stepTypeId": 4, "stepTypeKey": "recovery"},
      "endCondition": {"conditionTypeId": 2, "conditionTypeKey": "time"}, "endConditionValue": 120,
      "targetType": {"workoutTargetTypeId": 1, "workoutTargetTypeKey": "no.target"}}]},
   {"type": "ExecutableStepDTO", "stepOrder": 5, "stepType": {"stepTypeId": 2, "stepTypeKey": "cooldown"},
    "endCondition": {"conditionTypeId": 1, "conditionTypeKey": "lap.button"},
    "targetType": {"workoutTargetTypeId": 1, "workoutTargetTypeKey": "no.target"}}]}]}
```

**Vélo en % FTP** (étape de 20' à 76–90 % FTP, tempo) : comme ci-dessus avec `sportTypeId 2 cycling` et, sur l'étape :

```json
"targetType": {"workoutTargetTypeId": 2, "workoutTargetTypeKey": "power.zone"},
"targetValueOne": 76, "targetValueTwo": 90, "targetValueUnit": {"unitKey": "percent"}
```

**Mobilité** : `sportType {"sportTypeId": 11, "sportTypeKey": "mobility"}`, étapes en temps, `no.target`.

**Renfo** : `create_strength_workout(name, exercises=[{name, sets, reps, rest_seconds, category}])`. `category` appartient au catalogue Garmin (SQUAT, LUNGE, DEADLIFT, PLANK…) ; `UNASSIGNED` et `OTHER` sont refusés. Gainage en secondes ou charge : `upload_workout` sport 5 avec `category`, `exerciseName`, `weightValue`, `weightUnit` et une fin en temps ou en répétitions.

## Lectures utiles

| Besoin | Outil | Remarque |
|---|---|---|
| Activités d'une période | `get_activities_by_date(start, end)` | Plage courte ; sans effort perçu |
| Détail d'une activité, effort perçu | `get_activity(id)` | `workout_rpe` sur 0–100 : divise par 10 |
| Répétitions d'un fractionné | `get_activity_splits(id)` ou `get_activity_typed_splits(id)` | Séance clé seulement |
| Temps par zone FC | `get_activity_hr_in_timezones(id)` | Bande Facile = Z1 + Z2 |
| Séances planifiées | `get_scheduled_workouts(start, end)` | Fait foi pour le planifié |
| Sommeil, FC de repos, VFC nocturne | `get_sleep_summary_range(start, end)` | 90 nuits au plus ; un appel pour 28–30 j |
| VFC en tendance | `get_hrv_trend(start, end)` | 30 jours au plus |
| FC de repos d'un jour | `get_rhr_day(date)` | |
| Courses au calendrier | `get_calendar_events(start, end)` | Lecture seule |
| Parcours | `get_courses`, `get_course_details(id)` | Distance, D+, D−, points d'intérêt ; pas le tracé |
| Records | `get_personal_record` | Démarrage |
| Puissance-durée | `get_power_duration_curve` | Estimation de FTP |

Contexte seulement, jamais décisionnels : Body Battery, Training Readiness, statut VFC Garmin, VO2max et prédictions de course Garmin. `get_training_load_trend` contient un ratio aigu/chronique que le référentiel n'utilise pas (fichier 03, règle 3).

## Parcours et PacePro

Le connecteur lit un parcours de Garmin Connect mais ne peut ni l'importer, ni l'envoyer à la montre, ni créer ou lire une stratégie PacePro. Profil fin : GPX déposé dans la conversation, analysé par du code. À J-7, le coach propose des réglages PacePro que l'athlète saisit lui-même dans l'app Garmin Connect, ou à défaut l'envoi du parcours sur la montre par l'athlète, étapes à l'appui. C'est une option, jamais une obligation.

## Zones FC du compte (Z1–Z5, analyse)

Optionnel, après GO seulement, un sport à la fois : `set_heart_rate_zones(sport="running" ou "cycling", calculation_method="custom_bpm", max_hr=…, zone_boundaries=[Z1, Z2, Z3, Z4, Z5])`, 5 planchers en bpm strictement croissants.
- Course (Friel) : Z2 = 85 %, Z3 = 90 %, Z4 = 95 %, Z5 = 100 % de la LTHR course ; Z1 = plancher actuel conservé.
- Vélo (Coggan) : Z2 = 69 %, Z3 = 84 %, Z4 = 95 %, Z5 = 106 % de la LTHR vélo ; Z1 = plancher actuel conservé.
- **Ne passe jamais `resting_hr`** : cela coupe la mise à jour automatique de la FC de repos par Garmin.
- Lis d'abord `get_heart_rate_zones(sport)`, puis relis le résultat renvoyé. Aucun effet sur les activités passées.

## Exemples de messages (format B)

**Avant création :**

> ### Semaine du 24/11 à créer
> | Jour | Séance |
> |---|---|
> | Mer | `R \| EF 40' + 6×15" LD` |
> | Jeu | `R \| Frac. 45' 4×4' @Seuil r:2' ★` |
> | Ven | `Renfo \| 30'` |
> | Dim | `R \| SL 1h10` |
>
> **Verdict :** 4 séances, dans le budget (1 séance dure).
>
> > **À toi :** GO pour créer ces 4 séances dans Garmin ?

**Avant suppression :**

> ### Séances à supprimer de la bibliothèque
> | Date | Séance |
> |---|---|
> | 18/11 | `R \| EF 45'` |
> | 20/11 | `R \| Frac. 50' 6×3' @VMA r:2' ★` |
>
> **Verdict :** semaine écoulée ; tes activités réalisées restent.
>
> > **À toi :** GO pour supprimer ces 2 séances ?

**Après création :**

> ### Créé dans Garmin
> | Jour | Séance | Relue |
> |---|---|---|
> | Mer | `R \| EF 40' + 6×15" LD` | ✅ |
> | Jeu | `R \| Frac. 45' 4×4' @Seuil r:2' ★` | ✅ allure 4'25–4'35 |
>
> **Verdict :** tout est planifié ; ta montre se synchronise seule.
