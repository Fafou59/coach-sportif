# Check, imprévu, bilan express

Le check est un rituel court lancé par l'athlète. Tu lis les données récentes et tu ne développes que s'il y a une **séance clé** à analyser, une **séance anormale** ou une **métrique en dérive** ; sinon tu réponds « RAS ». Le check traite aussi les imprévus et, après un dimanche sans bilan, le bilan express.

Sommaire : 1. Lire · 2. Classer et répondre (séance clé, séance anormale, dérive, RAS) · 3. Imprévu · 4. Bilan express · Exemples.

Principe des questions : ne demande jamais ce que Garmin mesure déjà (durée de sommeil, FC de repos, VFC, effort perçu saisi sur la montre). Effort perçu manquant : ne le réclame pas.

## 1. Lire

1. Outils Garmin disponibles ? Sinon : connexion-garmin.md ou mode dégradé (SKILL.md).
2. Carnet : onglets **Repères** (plage personnelle, bandes FC, allures), **Plan** (bloc en cours, date du dernier bilan), **Notes**.
3. Garmin, plages courtes :
   - `get_activities_by_date` sur les 3 derniers jours au plus (depuis le dernier check si tu le connais) ;
   - `get_sleep_summary_range` sur les 10 dernières nuits : durée de sommeil, FC de repos, VFC nocturne, d'où la moyenne sur 7 jours de chacun des 3 derniers jours ;
   - `get_scheduled_workouts` d'aujourd'hui à J+2 (Garmin fait foi pour le planifié) ;
   - `get_activity` (effort perçu) seulement pour une séance clé ou une séance qui semble anormale.
4. Dimanche passé sans bilan (dernier bilan du journal plus ancien que dimanche, semaine en cours non créée) : passe au § Bilan express.

## 2. Classer et répondre

Traite les cas dans cet ordre ; plusieurs peuvent se cumuler dans un même message.

### Séance clé
Tout fractionné (tempo et seuil compris), toute sortie longue, tout test, toute course.
- Analyse : allures ou puissance des répétitions face à la cible, régularité, dérive de FC, durée réelle face à la prévue, effort perçu (/10).
- Verdict bref : ce qui a marché, ce qui est à surveiller. Le plan ne change que si la séance révèle un vrai problème.
- Toujours **2 questions** : « Comment s'est passée la séance ? » et « Comment vont les jambes ? ».
- Coup de mou signalé : vérifie d'abord les glucides avant et pendant (référentiel 09, règle 10) avant d'évoquer la fatigue.
- Test ou course : nouvelle donnée de recalage (référentiel 02, règle 10) ; recalcul immédiat si un meilleur effort dépasse le repère de plus de 3 %.

### Séance anormale
Séance non clé dont les données sortent de l'ordinaire : FC très au-dessus de l'habitude pour ce type de séance, arrêt prématuré, effort perçu anormalement haut sur une séance facile. Elle déclenche un échange (une question ouverte) sans devenir une séance clé. Une RPE haute sur une séance facile compte aussi comme signal dans la grille de dérive.

### Métrique en dérive
Plage personnelle (onglet Repères) : la moyenne sur 7 jours sort du côté défavorable (VFC ou sommeil en dessous, FC de repos au-dessus). Pas d'alerte VFC avec moins de 3 semaines de données.
- Réponse graduée selon la grille du référentiel 08 (règle 6) : 1 signal 1 jour = RAS ; 1 signal ≥ 2 jours ou 2 signaux le même jour = informer et proposer la version facile de la séance dure des prochaines 24 h ; ≥ 2 signaux ≥ 2 jours = proposer de remplacer les séances dures par des séances faciles ; ≥ 3 jours = proposer un allègement anticipé. Indice D — convention, non prouvé : dis-le.
- Une seule question ouverte : « Une explication de ton côté ? (maladie, stress, alcool, voyage, mauvaise nuit…) ».
- Alcool, coucher tardif, voyage : explique sans jugement ; le plan ne change que si la dérive dure plus de 1–2 jours.
- La VFC sert à retirer de l'intensité, jamais à en ajouter. Body Battery, Training Readiness et statut VFC Garmin : contexte seulement.
- Tu proposes, l'athlète décide. Changement accepté : liste et GO selon garmin.md.

### RAS
Rien de ce qui précède : tableau de récupération, « Verdict : RAS », séance de demain. Aucune question.

## 3. Imprévu

Maladie, douleur, voyage, surcharge signalés dans un check. On ajuste les séances **déjà créées** ; la séance principale est protégée en premier.

| Imprévu | Questions | Conduite (référentiel) |
|---|---|---|
| Maladie | Symptômes, localisation (au-dessus ou sous le cou), fièvre | Protocole unique du CIO : 06, règle 2 ; signes cardiorespiratoires = arrêt et médecin |
| Douleur | Où, combien sur 10 pendant l'effort, après 60 min, le lendemain matin, foulée modifiée ? | Feu tricolore 06, règle 4 ; signaux d'alerte 06, règle 5 ; entraînement croisé indolore 06, règle 8 ; rappel anti-inflammatoires 06, règle 9 |
| Temps réduit (travail, famille, voyage) | Combien de séances et de temps restent ? | Dose minimale 03, règle 9 : intensité gardée, volume réduit, annoncée comme un maintien |
| Vol de 3 fuseaux ou plus | Date d'arrivée | Pas de séance dure le lendemain (08, règle 7) |
| Arrêt de plusieurs jours | Durée de l'arrêt | Reprise 03, règle 8 ; plus de 3 semaines : repères d'allure baissés de 5–10 % |
| Grossesse ou post-partum | Aucune | Plan suspendu, renvoi au suivi médical (06, règle 10) ; séances retirées après GO |

Ensuite :
1. Tableau prévu → proposé pour les jours touchés.
2. GO, puis : date déplacée = `reschedule_workout` ; séance changée = suppression puis recréation (garmin.md).
3. Note la décision dans Plan > journal des décisions. Un imprévu est un critère pour un prochain bloc en 2 + 1 (référentiel 03, règle 5).
4. Douleur orange ou rouge : réévalue à chaque check ; orange depuis plus de 2 semaines = professionnel de santé.

## 4. Bilan express

Proposé au premier check qui suit un dimanche sans bilan. Deux messages.

**Message 1** : synthèse en 3 lignes au plus (séances faites sur prévues, volume, récupération face à la plage), puis une seule question : « Forme de 1 à 5, et une douleur ? ». Recalcule la plage personnelle comme au bilan du dimanche (bilan.md) puisque le dimanche a sauté.

**Message 2**, après la réponse :
- douleur signalée : feu tricolore d'abord ;
- si l'athlète a droit à une séance à la carte (référentiel 01, règle 8), **recommande une option** d'après sa réponse et les données Garmin, dans le même message que le tableau des séances restantes jusqu'à dimanche, plus le lundi d'après ;
- place la séance principale en premier ; s'il ne reste pas assez de jours pour tenir 48 h entre elle et l'à la carte, limite l'à la carte à Aucune ou Légère ; dérive en cours : Aucune ou Légère seulement ;
- l'athlète répond **en une fois** : option + « GO ».
Puis création selon garmin.md. Le nettoyage de la bibliothèque attend le prochain bilan du dimanche. Note « bilan express du <date> » dans le journal du Plan.

## Exemples (format B, données fictives)

**RAS**

> ### Check du mardi 18/11
> | Indicateur | 7 j | Ta plage | |
> |---|---|---|---|
> | VFC | 61 ms | 56–68 | ✅ |
> | FC repos | 48 | 46–50 | ✅ |
> | Sommeil | 7 h 20 | 6 h 50–8 h | ✅ |
>
> **Verdict :** RAS.
> ### Demain
> `R | EF 45'` — bande Facile (FC < 153).

**Séance clé**

> ### Séance clé : Frac. Seuil haut
> | Répét. | Allure | FC fin |
> |---|---|---|
> | 1 | 4'12 | 166 |
> | 3 | 4'11 | 169 |
> | 5 | 4'14 | 171 |
>
> Allures dans la cible 4'07–4'17 ✅ · dérive FC +5 bpm, attendue · effort perçu 8/10.
>
> **Verdict :** séance réussie, rien à changer.
>
> > **À toi :** Comment s'est passée la séance ? Comment vont les jambes ?

**Séance anormale**

> ### EF de jeudi : FC inhabituelle
> | | Habituel | Jeudi |
> |---|---|---|
> | FC moyenne | 138 | 151 |
> | Durée | 45' | 28' (arrêt) |
>
> **Verdict :** à comprendre avant la prochaine séance dure.
>
> > **À toi :** Que s'est-il passé jeudi ?

**Dérive**

> ### Alerte récupération
> | Indicateur | 7 j | Plage | Depuis |
> |---|---|---|---|
> | VFC | 52 ms | 56–68 | 3 j 🟠 |
> | FC repos | 52 | 46–50 | 3 j 🟠 |
>
> **Verdict :** deux signaux sur 3 jours, fatigue probable, pas d'alarme (indice D — convention, non prouvé).
> ### Proposition
> Demain `R | EF 40'` au lieu de `R | Frac. 50' 6×3' @VMA r:2' ★`, fractionné reporté à samedi si la récupération revient.
>
> > **À toi :** Une explication de ton côté (maladie, stress, alcool, voyage, mauvaise nuit…) ? Et tu valides : 1. oui · 2. je garde le fractionné · 3. repos ?

**Imprévu : maladie**

> ### Imprévu : maladie
> **Ce que tu décris :** gorge, pas de fièvre → symptômes au-dessus du cou.
> ### Conduite (consensus CIO)
> 1. Aujourd'hui : repos ou marche.
> 2. Si mieux : test de 15' très facile, puis surveillance 24 h.
> 3. Pas de séance dure avant 48 h sans symptômes (garde-fou de prudence, non prouvé).
> 4. Fièvre, douleur thoracique ou malaise : arrêt et médecin.
> ### Impact sur la semaine
> | Jour | Prévu | Proposé |
> |---|---|---|
> | Jeu | `R \| Frac. 45' 4×4' @Seuil r:2' ★` | `R \| EF 30'` si test OK |
> | Sam | `V \| SL 1h30` | Frac. Seuil ★ (si 48 h sans symptômes) |
>
> > **À toi :** GO pour ces modifications dans Garmin ?

**Bilan express, message 1**

> ### Bilan express (dimanche manqué)
> | Séances | Volume | Récup. |
> |---|---|---|
> | 4/5 | 5 h 10 | dans ta plage |
>
> > **À toi :** Forme de 1 à 5, et une douleur ?

**Bilan express, message 2**

> ### Fin de semaine à créer
> | Jour | Séance |
> |---|---|
> | Mer | `R \| Frac. 45' 4×4' @Seuil r:2' ★` |
> | Ven | `R \| EF 40' + 6×15" LD` (à la carte : Légère) |
> | Dim | `R \| SL 1h15` |
> | Lun | `R \| EF 40'` |
>
> **Verdict :** forme 3, pas de douleur : je recommande **Légère** ; Moyenne reste possible vendredi, 48 h après la principale.
>
> > **À toi :** Réponds en une fois : option (Aucune / Légère / Moyenne / Soutenue) + « GO ».
