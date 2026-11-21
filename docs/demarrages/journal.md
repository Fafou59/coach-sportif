# Journal des démarrages réels

Carte : [démarrages réels et premier bilan du dimanche](https://github.com/Fafou59/coach-sportif/issues/30). Le dépôt est public : ce journal ne contient que des défauts anonymisés (« athlète 1 », « athlète 2 »), **aucune donnée de santé**, aucun lien vers un carnet (Q115). Les notes brutes restent hors de git.

## Critères (Q110)

| Critère | Ce qui est vérifié |
|---|---|
| C1 Garmin | Aucune écriture sans GO ; calendrier et carnet concordent après chaque écriture |
| C2 Garde-fous | Règles du référentiel appliquées (charge, sortie longue, reprise, séances dures) |
| C3 Messages | Format B ; questions conformes ; aucun détail interne affiché |
| C4 Carnet | Créé à l'étape 1, à jour, sans valeur périmée |
| C5 Fidélité | Chiffres et règles retrouvés dans le référentiel ; mêmes données, mêmes chiffres |
| C6 Quota | Mesuré sur le compte Free de l'athlète 2 |
| C7 Guide | L'athlète 2 installe seule ; chaque intervention est un défaut |

## Athlète 1 : démarrage du 20–21/11/2026 (skill v0.4)

Démarrage complet en 8 étapes, sur un forfait payant (une compaction automatique). Audit du 21/11 sur la conversation, le carnet et le calendrier Garmin (lecture seule).

| Critère | Résultat |
|---|---|
| C1 | ✗ séances créées sur GO, mais carnet et calendrier ne concordent plus (défaut D5) |
| C2 | ✗ bloc de base hors référentiel (D2), trois hausses fortes la même semaine (D4) ; reprise, cumul des 30 %, 1,10 × et affûtage conformes |
| C3 | ✗ phrase interne affichée, un message sans verdict (D7) ; 8 étapes dans l'ordre, format B respecté ailleurs |
| C4 | ✗ valeurs périmées (D6) |
| C5 | ✗ allures fausses au premier calcul (D1), chiffres instables d'un message à l'autre (D3) |

Les trois erreurs de fond (D1, D2, D3) ont été repérées par l'athlète, pas par le coach. Décision : correctif v0.4.1 avant le premier bilan du 29/11 et avant la suite du démarrage de l'athlète 2 (Q125), puis démarrage complet refait par l'athlète 1 (Q128).

### Défauts

- **D1 Allures** (C5, C2) : le garde-fou « pas de test maximal après un marathon » (02, règle 9) a été appliqué comme une baisse de 5–10 % des allures alors que des données récentes existaient ; le Seuil tombait sur l'allure marathon. Vitesse critique aussi calculée avec deux courses de 2023 et 2025, hors de la fenêtre de 8 semaines. Le sens de « Seuil » et « Seuil haut » n'a pas été relié aux noms d'allures de l'athlète.
- **D2 Qualités du bloc** (C2, C5) : bloc de base proposé à 100 % au seuil (principale et à la carte), contraire au contenu de base d'un confirmé (04, règle 1 : VMA, vitesse courte, force). Le choix était caché dans le tableau du plan macro au lieu d'être une question. Après correction, il reste une principale au seuil le 22/12.
- **D3 Chiffres instables** (C5) : dans la même conversation, retour de l'intensité 29/11 puis 02/12 ; pic de sortie longue 3 h 53, 3 h 52 puis 3 h 45 ; série 1 h 49 / 2 h 00 puis 1 h 48 / 1 h 58 ; semaine allégée 32 puis 31 km. Des paramètres sans règle (sorties longues et EF de reprise) changent d'une session à l'autre.
- **D4 Trois hausses fortes** (C2) : semaine du 30/11 : retour de l'intensité, sortie longue de 1 h à 1 h 30 (+50 %) et volume +15 % (03, règle 6 ; 05, règle 1).
- **D5 Carnet et calendrier désynchronisés** (C1, C4) : deux séances créées sur GO absentes du carnet ; le carnet dit qu'une ancienne séance reste au calendrier alors qu'elle a été retirée ; une séance d'un ancien plan le jour même n'a pas été vue, la lecture du calendrier commençant au lendemain.
- **D6 Valeurs périmées au carnet** (C4) : ancien calcul de sortie longue (3 h 53) resté dans l'onglet Objectifs alors que le Plan dit 3 h 45 ; texte d'attente « Verdict du calendrier entier : … ».
- **D7 Format** (C3) : une phrase de travail interne, en anglais, affichée à l'athlète ; message des allures corrigées sans verdict.
- **D8 Mineurs** (C5) : VMA notée sans le test qui l'a donnée (02, règle 4) ; consentements notés « oui » pour des données qui ne concernent pas l'athlète, au lieu de « sans objet ».
- **D9 Référentiel ambigu** : 02, règle 9 (quand baisser les repères de 5–10 %) ; 01, règle 8 (les 4 semaines avec une séance dure avant d'ouvrir l'à la carte comptent-elles depuis une reprise ?).

## Athlète 2 : démarrage en cours (skill v0.4, compte Free)

- **C6 Quota** : limite atteinte après 3 ou 4 étapes du démarrage ; pause, puis reprise après la réinitialisation du quota. À qualifier : reprise sans perte depuis le carnet ?
- **Retour** : sans chrono en tête, l'athlète a dû demander une estimation ; elle aurait aimé que le coach la propose spontanément, puis l'ajuste en fin de bloc selon les fractionnés et la RPE.
