# 08 — Métriques de récupération

Ce fichier fixe comment le coach lit la VFC nocturne, la FC de repos et le sommeil, quelle confiance il accorde aux scores Garmin, et ce qu'une dérive déclenche. Le principe du check s'applique : le coach compare la moyenne des 7 derniers jours à la plage personnelle du carnet (règle 1) et ne parle que si une métrique dérive. L'athlète décide toujours ; le coach informe et propose.

## Règles

**1. Ligne de base et lecture en tendance**
- **Règle** : ne jamais réagir à une valeur isolée de VFC. Comparer la moyenne glissante sur 7 jours de la VFC nocturne (RMSSD) à la ligne de base personnelle, avec une plage personnelle égale à la moyenne ± le plus petit changement significatif (SWC). On dit « plage » et non « bande » pour ne pas confondre avec les bandes FC (CONTEXT ; 17/11/2026).
- **Valeur par défaut** :
  - Ligne de base recalculée au bilan du dimanche sur les 28–30 derniers jours (règle 9).
  - SWC = 0,5 × l'écart-type de la ligne de base.
  - Dérive VFC = moyenne sur 7 jours sous la borne basse.
  - Pas d'alerte VFC tant qu'il y a moins de 3 semaines de données.
  - Définition unique de la dérive VFC (17/11/2026) : celle-ci, sur la plage personnelle. Le statut VFC Garmin ne sert que de contexte (règle 5).
- **Indice** : B (moyenne sur 7 jours, Plews) — règle ; C (plage ± 0,5 SD, délai de 3 semaines) — valeur de départ.
- **Niveau de preuve** : Moyen. Plews (2013) montre que la moyenne sur 7 jours reflète mieux l'adaptation qu'une valeur isolée. La plage ± 0,5 SD est celle des essais de Vesterinen (2016) et de Javaloyes (2019). Garmin compare aussi une moyenne sur 7 jours à une plage établie sur environ 3 semaines.
- **Sources** :
  - Plews et al., 2013, *IJSPP* 8:688–691, doi:10.1123/ijspp.8.6.688
  - Plews et al., 2013, *Sports Med* 43:773–781, doi:10.1007/s40279-013-0071-8
  - Buchheit, 2014, *Front Physiol* 5:73, doi:10.3389/fphys.2014.00073

**2. Entraînement guidé par la VFC : un garde-fou, pas un moteur**
- **Règle** : utiliser la VFC pour *retirer* de l'intensité en cas de dérive, jamais pour en ajouter.
- **Valeur par défaut** : si la VFC est sous la plage personnelle, le coach propose de remplacer la séance dure par une séance facile ou par du repos ; l'athlète décide (règle 6).
- **Indice** : B (Düking : performance non significative, moins de non-répondeurs) — règle.
- **Niveau de preuve** : Moyen.
  - Les essais de Kiviniemi (2007), Vesterinen (2016) et Javaloyes (2019) donnent un résultat égal ou meilleur qu'un plan prédéfini, souvent avec moins de séances intenses.
  - Méta-analyse de Düking (2021, 8 études, 198 participants) : effet positif sur les paramètres sous-maximaux (g = 0,30), effet non significatif sur la performance et la VO2max, moins de non-répondeurs.
  - Granero-Gallegos (2020) : petit effet favorable sur la VO2max.
- **Sources** :
  - Kiviniemi et al., 2007, *Eur J Appl Physiol* 101:743–751, doi:10.1007/s00421-007-0552-2
  - Vesterinen et al., 2016, *Med Sci Sports Exerc* 48:1347–1354, doi:10.1249/MSS.0000000000000910
  - Javaloyes et al., 2019, *IJSPP* 14:23–32, doi:10.1123/ijspp.2018-0122
  - Düking et al., 2021, *J Sci Med Sport* 24:1180–1192, doi:10.1016/j.jsams.2021.04.012
  - Granero-Gallegos et al., 2020, *Int J Environ Res Public Health* 17:7999, doi:10.3390/ijerph17217999

**3. Coefficient de variation et VFC « trop haute »**
- **Règle** : suivre le coefficient de variation (CV) sur 7 jours à titre descriptif. Une VFC au-dessus de la plage personnelle en pleine surcharge, avec une RPE haute, n'est pas forcément un bon signe.
- **Valeur par défaut** : pas de décision automatique. Mention au bilan du dimanche si le CV monte nettement pendant que la moyenne baisse.
- **Indice** : C — indicateur.
- **Niveau de preuve** : Faible. Plews (2012) est une étude de cas. Le Meur (2013) observe une hyperactivité parasympathique en surmenage.
- **Sources** : Plews et al., 2012, *Eur J Appl Physiol* 112:3729–3741, doi:10.1007/s00421-012-2354-4 ; Le Meur et al., 2013, *Med Sci Sports Exerc* 45:2061–2071, doi:10.1249/MSS.0b013e3182980125.

**4. FC de repos et sommeil**
- **Règle** : lire la FC de repos et la *durée* de sommeil en tendance, avec la même méthode que la VFC (règle 1). Ne jamais interpréter les phases de sommeil ni le score de sommeil.
- **Valeur par défaut** (révisée le 17/11/2026) :
  - Dérive FC de repos : moyenne sur 7 jours au-dessus de la plage personnelle (ligne de base + SWC, SWC = 0,5 × l'écart-type, règle 1).
  - Dérive sommeil : moyenne sur 7 jours de la durée de sommeil sous la plage personnelle (ligne de base − SWC).
  - Les anciens seuils fixes (+5 bpm sur 2 nuits ; moins de 6 h sur 2 nuits) sont retirés.
  - Repère éducatif : 7–9 h.
  - Option, seulement si l'athlète le demande : la semaine de course, viser plus de 8 h au lit, surtout avant une nuit courte prévisible (départ matinal, voyage) ; essai croisé (n = 9) : 3 nuits allongées améliorent un contre-la-montre, 3 nuits écourtées le dégradent (Roberts 2019).
- **Indice** : C–D (plage personnelle, méthode de la VFC étendue à la FC de repos et au sommeil) — indicateur ; A (repère de 7–9 h de sommeil, Watson, Walsh) — règle ; C (sommeil allongé avant une course, Roberts) — valeur de départ, option sur demande.
- **Niveau de preuve** : Faible pour les seuils.
  - Les anciens seuils fixes étaient des conventions de pratique ; la plage personnelle est extrapolée de la VFC, sans validation propre pour la FC de repos et le sommeil. La FC de repos est moins sensible que la VFC (Buchheit, 2014), et la FC de repos nocturne Garmin n'a pas pu être validée par Dial (2025).
  - Sommeil : importance établie (au moins 7 h chez l'adulte ; consensus athlètes de Walsh, 2021).
  - Les montres Garmin surestiment le temps de sommeil, et leurs phases sont peu fiables (Chinoy, 2021).
- **Sources** :
  - Watson et al., 2015, *Sleep* 38:843–844, doi:10.5665/sleep.4716
  - Walsh et al., 2021, *Br J Sports Med* 55:356–368, doi:10.1136/bjsports-2020-102025
  - Chinoy et al., 2021, *Sleep* 44:zsaa291, doi:10.1093/sleep/zsaa291
  - Dial et al., 2025, *Physiol Rep* 13:e70527, doi:10.14814/phy2.70527
  - Roberts et al., 2019, *Med Sci Sports Exerc*, doi:10.1249/MSS.0000000000002071

**5. Scores Garmin : contexte, pas décision**
- **Règle** : préférer les métriques brutes aux scores composites. Body Battery et Training Readiness ne déclenchent jamais seuls une action.
- **Valeur par défaut** : le statut VFC Garmin (« Bas », « Faible »…) sert de contexte seulement ; la dérive VFC se définit sur la plage personnelle (règle 1, révisé le 17/11/2026). Body Battery et Training Readiness servent de contexte seulement.
- **Indice** : S (scores propriétaires non validés : métriques brutes préférées, scores en contexte) — choix de conception (17/11/2026 : le fichier disait B avec un niveau de preuve Faible).
- **Niveau de preuve** : Faible.
  - Dial (2025) : VFC nocturne de la Fenix 6 contre ECG, CCC 0,87, erreur moyenne d'environ 10,5 %, en dessous des bagues Oura.
  - Aucune validation indépendante publiée n'a été trouvée pour Body Battery ni Training Readiness. Les formules sont propriétaires.
  - Training Readiness intègre la « charge aiguë » (manuel Garmin), un critère que le fichier 03 (règle 3) exclut des décisions.
- **Sources** : Dial et al., 2025 (règle 4) ; Miller et al., 2022, *Sensors* 22:6317, doi:10.3390/s22166317, PMID 36016077 ; manuel Garmin « Training Readiness » (**source fabricant**).

**6. Grille de décision**
- **Règle** : graduer la réponse selon le nombre et la durée des signaux : dérive VFC, dérive FC de repos, dérive sommeil, RPE anormalement haute sur une séance facile, symptômes.
- **Valeur par défaut** :

| Situation | Réponse du coach |
|---|---|
| 1 signal, 1 jour | Rien (« RAS ») |
| 1 signal ≥ 2 jours, ou 2 signaux le même jour | Informer au check ; proposer la version facile de la séance dure des prochaines 24 h |
| ≥ 2 signaux pendant ≥ 2 jours | Proposer de remplacer les séances dures par des séances faciles jusqu'au retour dans la plage personnelle |
| Signaux ≥ 3 jours | Proposer un allègement anticipé (fichier 03, règle 5) |
| Fièvre ou symptômes généraux | Repos ; reprise selon le fichier 06, règle 2 |

  - Quand une métrique dérive, le coach **propose** l'adaptation et l'athlète décide (aligné sur la règle 2 le 17/11/2026).
- **Indice** : D — valeur de départ.
- **Niveau de preuve** : Faible à Moyen. La logique « sous la plage → facile » vient des essais de la règle 2. Les durées sont des conventions, alignées sur le fichier 03 (règle 5).

**7. Maladie, alcool, voyage**
- **Règle** :
  - Pas d'entraînement en cas de fièvre, de courbatures généralisées ou de symptômes « sous le cou ».
  - Une dérive explicable par l'alcool, un coucher tardif ou un voyage est expliquée sans jugement. Le plan n'est modifié que si elle persiste plus de 1–2 jours.
- **Valeur par défaut** :
  - Symptômes légers « au-dessus du cou » sans fièvre : séance facile et courte possible.
  - Après une fièvre : protocole unique du fichier 06, règle 2 (démarche du CIO : test de reprise, pas de séance dure dans les 48 h qui suivent la disparition des symptômes et de la fièvre). Le second protocole de ce fichier est retiré le 17/11/2026.
  - Douleur thoracique, palpitations : arrêt et avis médical.
  - Par défaut, pas de séance dure le lendemain d'un vol de 3 fuseaux horaires ou plus.
  - Option, seulement si l'athlète le demande : course à 3 fuseaux ou plus, arriver plusieurs jours avant et régler lumière et horaires de sommeil selon le consensus (Janse van Rensburg 2021, qui reconnaît le manque de preuves) ; le repère « un jour par fuseau » n'est pas vérifié.
- **Indice** : B (alcool, voyage expliqués, Pietilä) — règle ; D (vol ≥ 3 fuseaux) — valeur de départ ; C (décalage horaire, Janse van Rensburg) — valeur de départ, option sur demande ; après une fièvre : voir fichier 06, règle 2.
- **Niveau de preuve** :
  - Faible pour la règle du « cou » (usage clinique).
  - Moyen pour le lien entre charge et maladie (consensus du CIO).
  - Moyen pour l'effet de l'alcool : baisse de la récupération nocturne liée à la dose, dès ≤ 0,25 g/kg (Pietilä, 2018).
  - Une hausse de la FC de repos peut précéder les symptômes d'une infection (Radin, 2020 ; Mishra, 2020).
- **Sources** :
  - Schwellnus et al., 2016, *Br J Sports Med* 50:1043–1052, doi:10.1136/bjsports-2016-096572
  - Pietilä et al., 2018, *JMIR Ment Health* 5:e23, doi:10.2196/mental.9519
  - Radin et al., 2020, *Lancet Digit Health* 2:e85–e93, doi:10.1016/S2589-7500(19)30222-5
  - Mishra et al., 2020, *Nat Biomed Eng* 4:1208–1220, doi:10.1038/s41551-020-00640-6
  - Janse van Rensburg et al., 2021, *Sports Med* 51:2029–2050, doi:10.1007/s40279-021-01502-0

**8. Cycle menstruel (sur option uniquement)**
- **Règle** : ne lire les données de cycle qu'avec l'accord explicite de l'athlète. Pas de périodisation par phase par défaut. Avec l'option activée, la phase sert à *interpréter* les métriques, et les symptômes rapportés servent à *adapter*.
- **Valeur par défaut** : option activée, une baisse de VFC en phase lutéale ne déclenche pas d'alerte à elle seule. Sans option, le coach ne déduit rien et ne pose aucune question.
- **Indice** : S (lecture des données de cycle sur accord explicite) — choix de sécurité ; C (pas de périodisation par phase, McNulty : preuves de faible qualité) — valeur de départ (17/11/2026 : le fichier disait B).
- **Niveau de preuve** : Faible.
  - McNulty (2020) : baisse « triviale » de la performance en début de phase folliculaire, preuves de faible qualité ; les auteurs recommandent une approche individualisée.
  - Colenso-Semple (2023) : pas d'effet de la phase sur la force.
  - Schmalenberger (2019) : la VFC baisse de la phase folliculaire à la phase lutéale (d = −0,39).
- **Sources** :
  - McNulty et al., 2020, *Sports Med* 50:1813–1827, doi:10.1007/s40279-020-01319-3
  - Colenso-Semple et al., 2023, *Front Sports Act Living* 5:1054542, doi:10.3389/fspor.2023.1054542
  - Schmalenberger et al., 2019, *J Clin Med* 8:1946, doi:10.3390/jcm8111946

**9. Durée de la ligne de base**
- **Règle** : calculer la ligne de base sur 28–30 jours plutôt que sur 14.
- **Valeur par défaut** : 28–30 jours pour tous les athlètes.
- **Indice** : C — valeur de départ.
- **Niveau de preuve** : Faible. C'est un raisonnement : la fenêtre couvre un cycle menstruel complet sans avoir besoin des données de cycle (règle 8), et elle est proche de la plage Garmin (environ 3 semaines) et des lignes de base de 4 semaines des essais de la règle 2. Une fenêtre de 14 jours peut tomber entièrement dans une même phase du cycle.

**10. RED-S : signaux d'alerte, jamais de conseil de perte de poids**
- **Règle** : le coach ne donne jamais de conseil de perte de poids et ne commente ni le poids ni le corps. Il repère les signaux d'un déficit énergétique relatif (RED-S) et oriente vers un médecin, sans poser de diagnostic.
- **Valeur par défaut** :
  - Orienter vers un médecin dès 1 signal fort, ou dès 2 signaux secondaires présents depuis plusieurs semaines.
  - Signaux forts :
    - règles absentes depuis plus de 3 mois ou devenues irrégulières (seulement si l'option est activée ou si l'athlète en parle) ;
    - fracture de fatigue, surtout récidivante.
  - Signaux secondaires :
    - fatigue persistante ;
    - baisse de performance inexpliquée ;
    - infections répétées ;
    - perte de poids non voulue évoquée par l'athlète ;
    - baisse de libido ;
    - troubles digestifs ;
    - humeur dégradée.
- **Indice** : S (jamais de conseil de perte de poids) — choix de sécurité ; A (signaux RED-S → médecin, CIO) — règle ; D (seuil d'orientation : 1 signal fort ou 2 secondaires) — garde-fou de prudence, non prouvé.
- **Niveau de preuve** : Élevé pour l'existence et les signaux du RED-S (consensus du CIO). Faible pour le seuil d'orientation.
- **Sources** : Mountjoy et al., 2023, *Br J Sports Med* 57:1073–1097, doi:10.1136/bjsports-2023-106994.

**11. Fatigue inexpliquée : suggérer d'en parler au médecin (fer)**
- **Règle** : en cas de fatigue persistante ou de baisse de performance inexpliquée, ou chez un athlète à profil à risque (femme, surtout si les règles sont abondantes ; alimentation sans viande ; gros volume d'entraînement), le coach **suggère de discuter d'un dosage de ferritine avec un médecin**. Il ne prescrit jamais d'examen ni de complément en fer (fichier 09, règle 9).
- **Valeur par défaut** :
  - Formule type : « Une fatigue qui dure sans explication mérite d'en parler à ton médecin ; il pourra juger utile de doser ta ferritine. »
  - Question sur les règles seulement si l'option cycle est activée ou si l'athlète en parle (règle 8).
  - Signaux de RED-S associés : règle 10.
- **Indice** : B (traitement de la carence sans anémie : ferritine et VO2max améliorées, Burden) — règle ; C (profil à risque, mécanismes, Sim ; prévalence non vérifiée) — garde-fou de prudence, non prouvé ; S (ni examen ni complément prescrits par le coach) — choix de sécurité.
- **Niveau de preuve** : Moyen. Chez des athlètes d'endurance carencés sans anémie, le traitement améliore la ferritine (g = 1,09) et la VO2max (g = 0,61) (méta-analyse, Burden 2015). Mécanismes de la carence chez l'athlète : Sim (2019). Prévalence non vérifiée.
- **Sources** :
  - Burden et al., 2015, *Br J Sports Med*, doi:10.1136/bjsports-2014-093624
  - Sim et al., 2019, *Eur J Appl Physiol*, doi:10.1007/s00421-019-04157-y

**12. Massage et compression : confort seulement (option sur demande)**
- **Règle** : seulement si l'athlète en parle, présenter massage et compression comme des outils de **confort** (courbatures, fatigue perçue), sans effet sur la performance, et jamais prioritaires sur le sommeil et l'alimentation.
- **Indice** : A–B (Davis, Dupuy, Brown) — règle.
- **Niveau de preuve** : Moyen à Élevé. Massage sans effet sur la performance, petit effet sur les courbatures (méta-analyse de 29 études, Davis 2020) ; massage le plus efficace sur courbatures et fatigue perçue (Dupuy 2018) ; compression surtout utile après le renfo (Brown 2017).
- **Sources** :
  - Davis et al., 2020, *BMJ Open Sport Exerc Med*, doi:10.1136/bmjsem-2019-000614
  - Dupuy et al., 2018, *Front Physiol*, doi:10.3389/fphys.2018.00403
  - Brown et al., 2017, *Sports Med*, doi:10.1007/s40279-017-0728-9

## Ce qui ne fait pas consensus

- **Largeur de la plage** : 0,5 SD ou 1 SD, RMSSD brut ou logarithmique. Les essais diffèrent.
- **Durée de la ligne de base** : de 7 à 30 jours selon les études.
- **VFC haute** : signe de bonne forme ou de surmenage parasympathique ? Cela dépend du contexte.
- **Précision au poignet** : correcte en moyenne, mais erreur individuelle d'environ 10 %. Les phases de sommeil sont peu fiables.
- **Entraînement selon le cycle** : les preuves sont insuffisantes.
- **Règle du « cou »** : c'est un usage clinique, pas un résultat d'essai.

## Décisions validées (14/11/2026, révisées le 17/11/2026)

| Paramètre | Recommandation |
|---|---|
| Fenêtre de la ligne de base | 28–30 jours (au lieu de 14), recalculée le dimanche |
| Plage personnelle VFC | Moyenne 7 j vs ligne de base ± 0,5 SD ; seule définition de la dérive VFC, statut Garmin en contexte (17/11) |
| Seuils FC de repos / sommeil | Même méthode que la VFC : moyenne 7 j vs plage personnelle (17/11) |
| Grille de décision | 1 jour : rien ; 2 jours : informer et proposer la version facile ; ≥ 2 signaux sur 2 jours : proposer de remplacer ; ≥ 3 jours : proposer un allègement ; l'athlète décide (17/11) |
| Après une fièvre | Protocole unique du fichier 06, règle 2 (17/11) |
| Body Battery / Training Readiness | Contexte seulement (S, choix de conception, 17/11) |
| Phases et score de sommeil | Non interprétés |
| Cycle menstruel | Sur option (S) ; interprétation des métriques, pas de périodisation (C, valeur de départ) (17/11) |
| Lecture du poids (outils Garmin) | Jamais, sauf demande explicite de l'athlète |
| Orientation RED-S | 1 signal fort ou 2 signaux secondaires → médecin |
| Fer | Fatigue inexpliquée ou profil à risque → suggérer d'en parler au médecin (dosage de ferritine) ; ni examen ni complément prescrits (17/11) |
| Options sur demande | Sommeil allongé avant course (C) ; décalage horaire (C) ; massage et compression pour le confort (A–B) (17/11) |
