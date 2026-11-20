# Check, imprévu, bilan express

Le check est un rituel court lancé par l'athlète. Tu lis les données récentes et tu ne développes que s'il y a une **séance clé** à analyser, une **séance anormale** ou une **métrique en dérive** ; sinon tu réponds « RAS ». Le check traite aussi les imprévus et, après un dimanche sans bilan, le bilan express.

Sommaire : 1. Lire · 2. Classer et répondre (séance clé, séance anormale, dérive, RAS) · 3. Imprévu · 4. Bilan express · Exemples.

Principe des questions : ne demande jamais ce que Garmin mesure déjà (durée de sommeil, FC de repos, VFC, effort perçu saisi sur la montre). Effort perçu manquant : ne le réclame pas.

## 1. Lire

1. Outils Garmin disponibles ? Sinon : connexion-garmin.md ou mode dégradé (SKILL.md).
2. Carnet : onglets **Repères** (plage personnelle, bandes FC, allures), **Plan** (imprévus ouverts, dernière séance analysée, bloc en cours, date du dernier bilan), **Notes**.
3. **Imprévus ouverts** : relis-les avant tout le reste. Leur conduite s'applique à la séance de demain et à tout ce que tu proposes ; rappelle-les dans le message (une ligne chacun) et pose la question de suivi utile (douleur : combien sur 10 aujourd'hui ; maladie : symptômes, test de reprise fait ?).
4. Garmin, plages courtes :
   - `get_activities_by_date` depuis le lendemain de la **dernière séance analysée** (onglet Plan), 3 derniers jours au plus ;
   - `get_sleep_summary_range` sur les 10 dernières nuits : durée de sommeil, FC de repos, VFC nocturne, d'où la moyenne sur 7 jours de chacun des 3 derniers jours ;
   - `get_scheduled_workouts` d'aujourd'hui à J+2 (Garmin fait foi pour le planifié) ;
   - `get_activity` (effort perçu) seulement pour une séance clé ou une séance qui semble anormale.
5. Dimanche passé sans bilan (dernier bilan du journal plus ancien que dimanche, semaine en cours non créée) : passe au § Bilan express.

## 2. Classer et répondre

Traite les cas dans cet ordre ; plusieurs peuvent se cumuler dans un même message. Après le message, mets à jour « Dernière séance analysée » (onglet Plan) avec la date de la plus récente séance lue.

### Séance clé
Tout fractionné (tempo et seuil compris), toute sortie longue, tout test, toute course, **postérieure à la dernière séance analysée**. Une séance déjà commentée (check, bilan, bilan de course) ne se réanalyse pas.
- Analyse : allures ou puissance des répétitions face à la cible (onglet Repères), régularité, dérive de FC, durée réelle face à la prévue, effort perçu (/10).
- Verdict bref : ce qui a marché, ce qui est à surveiller. Le plan ne change que si la séance révèle un vrai problème.
- Toujours **2 questions** : `❓ **Q1 – Séance**` (comment s'est-elle passée ?) et `❓ **Q2 – Jambes**` (1 = lourdes · 5 = fraîches).
- Coup de mou signalé : vérifie d'abord les glucides avant et pendant (référentiel 09, règle 10) avant d'évoquer la fatigue.
- Test ou course : nouvelle donnée de recalage (référentiel 02, règle 10) ; recalcul immédiat si un meilleur effort dépasse le repère de plus de 3 %.

### Séance anormale
Séance non clé dont les données sortent de l'ordinaire : FC très au-dessus de l'habitude pour ce type de séance, arrêt prématuré, effort perçu anormalement haut sur une séance facile. Elle déclenche un échange (une question ouverte) sans devenir une séance clé. Une RPE haute sur une séance facile compte aussi comme signal dans la grille de dérive.

### Métrique en dérive
Plage personnelle (onglet Repères) : la moyenne sur 7 jours sort du côté défavorable (VFC ou sommeil en dessous, FC de repos au-dessus). Pas d'alerte VFC avec moins de 3 semaines de données.
- Réponse graduée selon la grille du référentiel 08 (règle 6) : 1 signal 1 jour = RAS ; 1 signal ≥ 2 jours ou 2 signaux le même jour = informer et proposer la version facile de la séance dure des prochaines 24 h ; ≥ 2 signaux ≥ 2 jours = proposer de remplacer les séances dures par des séances faciles ; ≥ 3 jours = proposer un allègement anticipé. Dis que la grille est une habitude de coach, non prouvée.
- Une seule question ouverte : `❓ **Q1 – Une explication ?**` (maladie, stress, alcool, voyage, mauvaise nuit…).
- Alcool, coucher tardif, voyage : explique sans jugement ; le plan ne change que si la dérive dure plus de 1–2 jours.
- La VFC sert à retirer de l'intensité, jamais à en ajouter.
- Tu proposes, l'athlète décide. Changement accepté : liste et GO selon garmin.md.

**Sans plage personnelle** (moins de 28 jours de données, montre sans ces mesures, mode dégradé) : dis-le, puis appuie-toi sur le **ressenti**, assez solide pour suivre la récupération (référentiel 08, règle 13) : `❓ Forme (1 = vidé · 5 = au top)`, `❓ Fatigue (1 = épuisé · 5 = reposé)`, `❓ Courbatures (1 = fortes · 5 = aucune)`. Sans montre compatible, la plage ne se calculera jamais : précise que le suivi de récupération reposera sur ces questions.

### RAS
Rien de ce qui précède : tableau de récupération, « Verdict : RAS », séance de demain. Aucune question.

## 3. Imprévu

Maladie, douleur, voyage, surcharge signalés dans un check. On ajuste les séances **déjà créées** ; la séance principale est protégée en premier.

| Imprévu | Questions | Conduite (référentiel) |
|---|---|---|
| Maladie | Symptômes, localisation (au-dessus ou sous le cou), fièvre | 06, règle 2 (ci-dessous) ; signes cardiorespiratoires = arrêt et médecin |
| Douleur | Où, combien sur 10 pendant l'effort, après 60 min, le lendemain matin, foulée modifiée ? | Feu tricolore 06, règle 4 ; signaux d'alerte 06, règle 5 ; entraînement croisé indolore 06, règle 8 ; rappel anti-inflammatoires 06, règle 9 |
| Temps réduit (travail, famille, voyage) | Combien de séances et de temps restent ? | Dose minimale 03, règle 9 : intensité gardée, volume réduit, annoncée comme un maintien |
| Vol de 3 fuseaux ou plus | Date d'arrivée | Pas de séance dure le lendemain (08, règle 7) |
| Arrêt de plusieurs jours | Durée de l'arrêt | Reprise 03, règle 8 ; plus de 3 semaines : repères d'allure baissés de 5–10 % |
| Grossesse ou post-partum | Aucune | Plan suspendu, renvoi au suivi médical (06, règle 10) ; séances retirées après GO |

**Maladie, une seule conduite cohérente** (06, règle 2) :
- Fièvre, frissons, courbatures généralisées, symptômes sous le cou ou « pas assez bien » : pas d'entraînement ; avis médical si fièvre, plus de 7 jours ou aggravation.
- Symptômes légers au-dessus du cou seulement : EF courte possible, ou test de reprise (10–20 min très facile) puis surveillance 24 h.
- Test et 24 h normaux : **EF autorisée** pendant 2–3 jours.
- Les **48 h** sans symptômes ni fièvre portent sur les **séances dures** seulement (habitude de coach, non prouvée — choix de prudence) ; l'EF n'attend pas ces 48 h.
Relis ton message avant de l'envoyer : une même séance ne peut pas être à la fois interdite et autorisée.

Ensuite, dans le **même message** :
1. Tableau prévu → proposé pour les jours touchés.
2. **Carnet, sans attendre ni demander** (orange, rouge, maladie, signal d'alerte, séances suspendues) : ligne dans « Imprévus ouverts » (date, quoi, feu ou symptômes, conduite, condition de clôture), séances touchées marquées dans le bloc en cours, ligne au journal des décisions. Annonce-le en une ligne. Cela vaut même en attendant l'avis d'un professionnel de santé : c'est justement ce que la conversation suivante doit savoir.
3. Bloc ✅ GO requis pour Garmin ; après GO : date déplacée = `reschedule_workout` ; séance changée = suppression puis recréation (garmin.md).
4. Un imprévu est un critère pour un prochain bloc en 2 + 1 (référentiel 03, règle 5).

Suivi : douleur orange ou rouge réévaluée à chaque check ; orange depuis plus de 2 semaines = professionnel de santé. Clôture (douleur verte, retour des séances dures autorisé) : ligne déplacée vers le journal avec la date.

## 4. Bilan express

Proposé au premier check qui suit un dimanche sans bilan. Deux messages. Relis d'abord les imprévus ouverts : ils priment sur la semaine à créer.

**Message 1** : synthèse en 3 lignes au plus (séances faites sur prévues, volume, récupération face à la plage, imprévus ouverts), puis les questions : `❓ **Q1 – Forme** (1 = vidé · 5 = au top)` et `❓ **Q2 – Douleur** (non, ou où et combien sur 10)`, plus le suivi de chaque imprévu ouvert. Recalcule la plage personnelle comme au bilan du dimanche (bilan.md) puisque le dimanche a sauté.

**Message 2**, après la réponse :
- douleur signalée ou imprévu ouvert : feu tricolore et conduite de l'imprévu d'abord ;
- séance à la carte : si l'athlète y a droit (référentiel 01, règle 8), **recommande une option** d'après sa réponse et les données Garmin ; sinon, « pas encore disponible » en une ligne ;
- place la séance principale en premier ; s'il ne reste pas assez de jours pour tenir 48 h entre elle et l'à la carte, limite l'à la carte à Aucune ou Légère ; dérive en cours : Aucune ou Légère seulement ; Moyenne ou Soutenue : pas de renfo jambes la veille (contrôle jour par jour de bilan.md, temps 2) ;
- tableau des séances restantes jusqu'à dimanche, plus le lundi d'après ;
- l'athlète répond **en une fois** : option + « GO ».
Puis création selon garmin.md. Le ménage de la bibliothèque attend le prochain bilan du dimanche. Note « bilan express du <date> » dans le journal du Plan et mets à jour la dernière séance analysée.

## Exemples (format B, données fictives)

Chiffres inventés pour montrer la forme ; les plafonds, plages et cibles réels viennent de l'onglet Repères du carnet, les mesures de Garmin.

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
> `R | EF 45'` — bande Facile (FC sous ton plafond Facile de l'onglet Repères).

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
> ❓ **Q1 – Séance** : comment s'est-elle passée ?
> ❓ **Q2 – Jambes** (1 = lourdes · 5 = fraîches) : combien ?

**Séance anormale**

> ### EF de jeudi : FC inhabituelle
> | | Habituel | Jeudi |
> |---|---|---|
> | FC moyenne en EF | ta moyenne habituelle | +13 bpm |
> | Durée | 45' | 28' (arrêt) |
>
> **Verdict :** à comprendre avant la prochaine séance dure.
>
> ❓ **Q1 – Jeudi** : que s'est-il passé ?

**Dérive**

> ### Alerte récupération
> | Indicateur | 7 j | Plage | Depuis |
> |---|---|---|---|
> | VFC | 52 ms | 56–68 | 3 j 🟠 |
> | FC repos | 52 | 46–50 | 3 j 🟠 |
>
> **Verdict :** deux signaux sur 3 jours, fatigue probable, pas d'alarme (grille : habitude de coach, non prouvée).
>
> ❓ **Q1 – Une explication ?** (maladie, stress, alcool, voyage, mauvaise nuit…)
> ❓ **Q2 – Demain** : EF 40' au lieu du fractionné, reporté à samedi si la récupération revient ?
> ➡️ Oui, EF 40'. Réponds « OK », ou « je garde le fractionné », ou « repos ».
>
> ---
> ✅ **GO requis** — si OK : `R | Frac. 50' 6×3' @VMA r:2' ★` de mercredi déplacé à samedi, `R | EF 40'` créé mercredi — Réponds « GO » pour valider.

**Imprévu : maladie**

> ### Imprévu : maladie
> **Ce que tu décris :** gorge, pas de fièvre → symptômes au-dessus du cou.
> ### Conduite (consensus CIO, solide)
> 1. Aujourd'hui : repos, ou EF très courte si tu te sens bien.
> 2. Demain : test de 15' très facile, puis surveillance 24 h.
> 3. Test et 24 h normaux : EF autorisée.
> 4. Séance dure : seulement 48 h après la fin des symptômes (habitude de coach, non prouvée — choix de prudence).
> 5. Fièvre, douleur thoracique ou malaise : arrêt et médecin.
> ### Impact sur la semaine
> | Jour | Prévu | Proposé |
> |---|---|---|
> | Jeu | `R \| Frac. 45' 4×4' @Seuil r:2' ★` | `R \| EF 30'` si test OK |
> | Sam | `V \| SL 1h30` | Frac. Seuil ★ (si 48 h sans symptômes) |
>
> Carnet : imprévu « maladie, au-dessus du cou » ajouté aux imprévus ouverts, séances de jeudi et samedi marquées.
>
> ---
> ✅ **GO requis** — jeudi : fractionné remplacé par `R | EF 30'` ; samedi : SL remplacée par le fractionné Seuil — Réponds « GO » pour valider.

**Bilan express, message 1**

> ### Bilan express (dimanche manqué)
> | Séances | Volume | Récup. |
> |---|---|---|
> | 4/5 | 5 h 10 | dans ta plage |
>
> Imprévu ouvert : tibia gauche, rouge le 17/11, course suspendue.
>
> ❓ **Q1 – Forme** (1 = vidé · 5 = au top) : combien ?
> ❓ **Q2 – Tibia** : combien sur 10 aujourd'hui, au repos et en marchant ? Rendez-vous pris ?

**Bilan express, message 2**

> ### Fin de semaine à créer
> | Jour | Séance |
> |---|---|
> | Mer | `R \| Frac. 45' 4×4' @Seuil r:2' ★` |
> | Ven | `R \| EF 40' + 6×15" LD` (à la carte : Légère) |
> | Dim | `R \| SL 1h15` |
> | Lun | `R \| EF 40'` |
>
> **Verdict :** forme 3, pas de douleur, aucun imprévu ouvert.
>
> ❓ **Q1 – À la carte de vendredi** : Aucune, Légère, Moyenne ou Soutenue ?
> ➡️ Légère ; Moyenne reste possible vendredi, 48 h après la principale.
>
> ---
> ✅ **GO requis** — création des 4 séances ci-dessus — Réponds en une fois : option (ou « OK ») + « GO ».
