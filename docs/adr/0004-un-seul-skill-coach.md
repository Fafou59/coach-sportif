# Un seul skill `coach`, procédures et référentiel en fichiers annexes

Q22 prévoyait cinq skills (`coach`, `coach-demarrage`, `coach-check`, `coach-bilan`, `coach-garmin`). La recherche du 17/11/2026 (ticket #3) a montré qu'aucun partage de fichiers entre skills n'est documenté sur claude.ai : avec cinq skills, le référentiel devrait être copié dans chaque ZIP et chaque proche réimporterait jusqu'à cinq ZIP à chaque modification. Le kit est donc **un seul skill nommé `coach`** : `SKILL.md` porte l'aiguillage, les règles transverses et un index qui pointe directement vers chaque procédure (démarrage, check, bilan, Garmin) et vers les fichiers du référentiel à lire pour chacune (règle des références à un seul niveau). Mettre la méthode dans les instructions de projet reste écarté (ADR 0003) : elles sont relues à chaque message, alors qu'un skill ne charge ses annexes qu'à la demande.

## Conséquences
- Une mise à jour de la méthode = un seul ZIP à réimporter.
- La description du skill (≤ 200 caractères) doit couvrir démarrage, check, bilan et Garmin ; l'instruction de projet cite le skill pour fiabiliser le déclenchement.
- Importer le nouveau `coach` remplace l'ancien skill du même nom : les anciens `coach`, `coach-objectifs` et `coach-suivi` sont désactivés pendant la répétition à blanc (leurs sources restent archivées), puis supprimés aux démarrages réels.

## Options écartées
- Cinq skills avec copie du référentiel par script : mises à jour lourdes et risque de skills désynchronisés.
- Lecture croisée entre skills (`/mnt/skills/user/…`) : comportement non documenté, déjà cassé une fois.
- Tout dans les instructions de projet : relu à chaque message (référentiel ≈ 40–50 k tokens), coût de quota prohibitif en Free.
