> Instantané de recherche du 17/11/2026 (ticket #3). Sources officielles d'Anthropic en priorité ; les sources secondaires sont marquées **[secondaire]**. Confiance : **Élevé** (source officielle explicite), **Moyen** (officiel indirect, sources en conflit ou secondaire solide), **Faible** (déduction ou témoignage isolé).

# Recherche — Comment des skills se partagent-ils des fichiers sur claude.ai ?

## 1. Réponse courte

1. **Officiellement, chaque skill est autonome.** Ses fichiers annexes vivent dans son propre dossier et sont appelés en chemin relatif depuis `SKILL.md`. Le centre d'aide le dit en toutes lettres : un skill ne peut pas référencer explicitement un autre skill, mais Claude peut en combiner plusieurs automatiquement. Aucun dossier partagé entre skills n'est documenté. Confiance **Élevé**.
2. **Techniquement, rien ne les isole.** Sur claude.ai, le dossier entier de chaque skill est copié dans le bac à sable d'exécution de code, sous `/mnt/skills/user/<nom>/` pour les skills importés. Claude pourrait donc lister et lire les fichiers d'un autre skill avec bash. Mais ce chemin n'est pas documenté par Anthropic, il a déjà été cassé (montage absent en février 2026) et rien ne garantit qu'il reste stable. Confiance **Faible** pour s'appuyer dessus.
3. **Conséquence.** La seule manière supportée de n'avoir le référentiel qu'en un seul exemplaire, c'est de le mettre dans **un seul** skill. Avec plusieurs skills, la source unique peut rester dans le dépôt, mais il faut copier le référentiel dans chaque ZIP au moment de la construction.

## 2. Faits établis

### 2.1 Isolement et partage de fichiers

| Fait | Source | Confiance |
|---|---|---|
| Un skill référence ses fichiers annexes (`references/`, `assets/`, `scripts/`) en **chemin relatif depuis la racine du skill**, à **un seul niveau** de profondeur depuis `SKILL.md`. | [Spécification Agent Skills](https://agentskills.io/specification) ; [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) | Élevé |
| Le centre d'aide dit qu'un skill ne peut pas référencer explicitement un autre skill, mais que Claude peut utiliser plusieurs skills ensemble automatiquement. | [Creating custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) | Élevé |
| « In chat on claude.ai, the skill's whole folder, scripts included, is copied into the code execution sandbox. » | [Create custom skills (claude.com/docs)](https://claude.com/docs/skills/how-to) | Élevé |
| L'isolement documenté du bac à sable sépare **les utilisateurs** (« no sandbox environments are ever shared between users »), pas les skills entre eux. Aucun isolement par skill n'est documenté. | [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude) | Élevé (le texte) / Faible (la déduction) |
| Sur claude.ai, les skills sont montés sous `/mnt/skills/public/` (Anthropic), `/mnt/skills/examples/`, `/mnt/skills/organization/` et `/mnt/skills/user/<nom>/SKILL.md` (skills importés). Ces chemins figurent dans le bloc `<available_skills>` du prompt système. | **[secondaire]** [anthropics/claude-code#26254](https://github.com/anthropics/claude-code/issues/26254) (16/02/2026, `ls` dans le conteneur) ; [simonw/claude-skills](https://github.com/simonw/claude-skills) (archive de `/mnt/skills`, 10/2025) | Moyen |
| Ce même ticket montre un montage raté : `/mnt/skills/user/` était absent alors que les skills étaient déclarés. Le ticket est toujours ouvert. | **[secondaire]** même ticket | Moyen |
| Via l'API, les skills sont copiés dans `/skills/{nom}/` d'un même conteneur (jusqu'à 20 skills par requête). | [Using Agent Skills with the API](https://platform.claude.com/docs/en/build-with-claude/skills-guide) | Élevé (API seulement) |
| Plugins : un plugin regroupe plusieurs skills, mais chacun garde son dossier `skills/<nom>/` avec ses propres fichiers. Aucun dossier commun lisible par les skills n'est documenté pour le chat. | [Plugin structure and testing](https://claude.com/docs/plugins/build.md) | Moyen (silence de la doc) |

**Point non établi** : on ne sait pas si un skill peut lire de façon fiable les fichiers d'un autre skill sur claude.ai (compte Free, mobile). Le test T3 (§ 5) suffit à trancher, mais même un succès resterait un comportement **non supporté**.

### 2.2 Limites

| Élément | Valeur | Source | Confiance |
|---|---|---|---|
| `name` | 64 caractères au plus ; minuscules, chiffres et tirets ; ni « anthropic » ni « claude » ; doit être identique au nom du dossier | [Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) ; [spec](https://agentskills.io/specification) ; [how-to](https://claude.com/docs/skills/how-to) | Élevé |
| `description` | **1 024** caractères selon la spec et la doc claude.com ; **200** selon le centre d'aide claude.ai | [how-to](https://claude.com/docs/skills/how-to) contre [12512198](https://support.claude.com/en/articles/12512198-creating-custom-skills) | Moyen (sources en conflit) : **viser ≤ 200** par prudence |
| Corps de `SKILL.md` | moins de 500 lignes, moins de 5 000 tokens environ (recommandation) | [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) ; [spec](https://agentskills.io/specification) | Élevé |
| Fichiers de référence | un seul niveau depuis `SKILL.md` ; table des matières au-delà de 100 lignes, sinon Claude peut ne lire qu'un aperçu (`head -100`) | [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) | Élevé |
| Taille d'un ZIP de skill sur claude.ai | **non chiffrée** (le message d'erreur parle seulement d'un ZIP qui « dépasse les limites de taille ») ; repères : 30 Mo non compressé via l'API, 30 Mo par fichier envoyé dans le chat | [12512180](https://support.claude.com/en/articles/12512180-using-skills-in-claude) ; [skills-guide](https://platform.claude.com/docs/en/build-with-claude/skills-guide) ; [12111783](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude) | Moyen |
| Nombre de fichiers par skill | non documenté (plugin : 5 000 fichiers, 200 Mo) | [Platform support](https://claude.com/docs/plugins/platform-support.md) | Faible pour un skill seul |
| Nombre de skills par compte | non documenté ; chaque skill actif coûte environ 100 tokens de métadonnées ; la doc évoque « 100+ » skills disponibles | [Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) ; [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) | Moyen |
| Structure du ZIP | le dossier du skill doit être la racine de l'archive (`mon-skill/SKILL.md`), pas les fichiers en vrac | [how-to](https://claude.com/docs/skills/how-to) | Élevé |

Pour comparer : le référentiel actuel (`docs/referentiel/00` à `09`) fait 1 562 lignes et 167 Ko, soit **de l'ordre de 40 à 50 k tokens** s'il était lu en entier (estimation) ; un fichier pèse en moyenne 4 à 6 k tokens. Il doit donc rester en fichiers de référence lus à la demande, jamais dans `SKILL.md`.

### 2.3 Forfait Free et applications

| Fait | Source | Confiance |
|---|---|---|
| Le centre d'aide inclut le forfait **Free** (skills soumis à l'activation de l'exécution de code). | [12512180](https://support.claude.com/en/articles/12512180-using-skills-in-claude) ; [12512176](https://support.claude.com/en/articles/12512176-what-are-skills) ; [tutoriel Academy](https://academy.claude.com/tutorials/teach-claude-your-way-of-working-using-skills) | Élevé (le texte) |
| **Conflit** : la doc claude.com et la doc plateforme écrivent « Pro, Max, Ultra, Team, and Enterprise » pour les skills personnalisés, sans Free. | [Skills overview](https://claude.com/docs/skills/overview.md) ; [Overview plateforme](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | Élevé (le conflit existe) |
| Le test T2 du 14/11/2026 (compte Free, app mobile) confirme qu'un skill importé se déclenche et lit ses fichiers annexes. | [ADR 0003](../adr/0003-methode-en-skills-instruction-projet-minimale.md) | Élevé (constat local) |
| L'exécution de code et la création de fichiers sont disponibles pour tous les forfaits, sur le web, Claude Desktop et les apps mobiles (iOS, Android). | [12111783](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude) | Élevé |

**Risque** : la disponibilité sur Free fonctionne aujourd'hui, mais la documentation se contredit. Il faut la revérifier avant d'ouvrir le coach à d'autres proches.

### 2.4 Déclenchement et combinaison

| Fait | Source | Confiance |
|---|---|---|
| Seuls le nom et la description de chaque skill actif sont dans le prompt système. Claude lit `SKILL.md` quand la demande correspond à la description ; la description est **la seule** partie lue avant cette décision. | [Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) ; [Skills overview](https://claude.com/docs/skills/overview.md) | Élevé |
| Déclenchement explicite possible : citer le skill par son nom (« Use my … skill ») ou taper `/` dans la zone de message et le choisir (documenté pour claude.ai et l'app desktop ; pas pour le mobile). | [12512180](https://support.claude.com/en/articles/12512180-using-skills-in-claude) ; [Skills overview](https://claude.com/docs/skills/overview.md) | Élevé (web, desktop) / Faible (`/` sur mobile) |
| Plusieurs skills peuvent servir dans une même conversation : « Claude can use more than one in a conversation ». La doc recommande plusieurs skills ciblés plutôt qu'un gros skill. | [how-to](https://claude.com/docs/skills/how-to) ; [12512198](https://support.claude.com/en/articles/12512198-creating-custom-skills) | Élevé |
| Écrire la description à la troisième personne, en disant ce que fait le skill **et quand** l'utiliser. | [Best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) | Élevé |

### 2.5 Mise à jour

| Fait | Source | Confiance |
|---|---|---|
| Pas de versionnage des skills personnels sur claude.ai ; l'API a des versions (`latest`, instantané complet à chaque version). | [12512180](https://support.claude.com/en/articles/12512180-using-skills-in-claude) (silence) ; [skills-guide](https://platform.claude.com/docs/en/build-with-claude/skills-guide) | Moyen |
| Réimporter un ZIP qui porte le nom d'un skill existant ouvre une boîte « Replace '<nom>' skill? » (Annuler / Importer et remplacer). Avec plusieurs ZIP à la fois, seul le premier est remplacé : il faut donc les importer **un par un**. | **[secondaire]** [anthropics/claude-code#82044](https://github.com/anthropics/claude-code/issues/82044) (28/07/2026) | Moyen |
| Le centre d'aide ne décrit pas de mise à jour sur place, sinon « Edit with Claude » sur les fichiers d'un skill ouvert dans le chat. Repli documenté : supprimer puis réimporter. | [12512198](https://support.claude.com/en/articles/12512198-creating-custom-skills) ; [12512180](https://support.claude.com/en/articles/12512180-using-skills-in-claude) | Moyen |
| Piste : un **plugin** ajouté depuis une « marketplace » GitHub se met à jour depuis sa source (« Check for updates », « Sync automatically »). La disponibilité de l'import de plugins sur **Free** n'est pas documentée. | [Plugins](https://claude.com/docs/plugins/overview.md) ; [Platform support](https://claude.com/docs/plugins/platform-support.md) | Faible pour Free |

### 2.6 Projets et contexte

| Fait | Source | Confiance |
|---|---|---|
| Les skills fonctionnent partout, y compris dans les projets. | [Tutoriel Academy](https://academy.claude.com/tutorials/teach-claude-your-way-of-working-using-skills) ; [Skills explained](https://claude.com/blog/skills-explained) (« any conversation, any project ») | Élevé |
| Les connaissances d'un projet sont **toujours chargées** ; un skill n'est chargé **qu'à la demande**. | [Skills overview](https://claude.com/docs/skills/overview.md) ; [Skills explained](https://claude.com/blog/skills-explained) | Élevé |
| Coût en contexte d'un skill : environ 100 tokens toujours présents (nom et description), puis le corps de `SKILL.md` quand il se déclenche, puis chaque fichier annexe **seulement s'il est lu**. Un script ne coûte que sa sortie. | [Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | Élevé |

## 3. Implications pour le choix d'architecture

### Option A — 1 skill : procédures et référentiel dans `references/`

- **Pour** : le référentiel n'existe qu'en un exemplaire, de façon supportée (chemins relatifs) ; un seul ZIP à réimporter ; aucun risque de versions divergentes entre skills ; un seul point d'entrée, ce qui colle à la règle « le skill socle lit le carnet ».
- **Contre** : une seule description (≤ 200 caractères par prudence) doit couvrir démarrage, check, bilans et Garmin, d'où un déclenchement moins fin (contournable en citant « coach » ou via `/`). C'est aussi contraire à la recommandation officielle de skills ciblés. Enfin, la règle de profondeur s'applique : une procédure (`references/check.md`) qui renvoie vers une règle (`references/referentiel/03-…`) fait **deux niveaux**, avec un risque de lecture partielle. Parade : `SKILL.md` sert d'index et lie directement **chaque** fichier, procédures comme référentiel, et chaque fichier long commence par une table des matières.
- `SKILL.md` doit rester sous 500 lignes : aiguillage, règles transverses (ton, « GO » avant Garmin, carnet = Claude Doc) et index des fichiers.

### Option B — 5 skills qui partagent un référentiel

- **Partage direct** (le skill `coach` contient le référentiel, les autres le lisent via `/mnt/skills/user/coach/…`) : **non supporté**. Le chemin n'est pas documenté, il dépend du nom du skill et du montage, et une panne de ce type a déjà été signalée. À éviter comme fondation.
- **Duplication à la construction** : chaque ZIP embarque la partie du référentiel dont il a besoin, copiée depuis `docs/referentiel/` par un script du dépôt. La source reste unique (le dépôt), la solution est supportée, et le déclenchement est fin. En contrepartie : jusqu'à 5 ZIP à réimporter **un par un** à chaque modification d'une règle, avec un risque de skills désynchronisés si l'un est oublié. La version dans la description (cadrage, Q18) permet de le repérer.

### Lecture pour le ticket #5

- Si la priorité est « une règle modifiée = une seule réimportation », l'option A, ou une option à 2–3 skills dont un seul porte le référentiel, est la seule qui tienne sans comportement non documenté.
- Si la priorité est un déclenchement fin par parcours, il faut l'option B **avec duplication par script**, jamais avec lecture croisée.
- Le cadrage actuel (Q22 : `coach`, `coach-demarrage`, `coach-check`, `coach-bilan`, `coach-garmin` et « le référentiel en fichiers annexes ») suppose implicitement un partage qui n'est pas supporté. Il faut préciser **dans quel(s) skill(s)** vivent les annexes.

## 4. Questions ouvertes

- Lecture croisée réelle sur Free et mobile (test T3 ci-dessous).
- Taille maximale d'un ZIP et nombre de fichiers sur claude.ai : non publiés.
- Forfait Free : conflit entre le centre d'aide (inclus) et la doc claude.com (exclu).
- Import de plugins depuis une marketplace GitHub sur Free : disponibilité non documentée. Si c'est possible, cela réglerait la corvée des mises à jour (synchronisation depuis le dépôt public).

## 5. Test proposé (T3, environ 10 minutes, compte Free)

1. Importer deux skills : `test-b` avec `references/secret.md`, et `test-a` dont les instructions disent : « Exécute `ls /mnt/skills/user/`, puis lis `/mnt/skills/user/test-b/references/secret.md` et donne le mot. »
2. Depuis l'app mobile, dans un projet, déclencher seulement `test-a`. Noter si le dossier de `test-b` est présent et lisible.
3. Réimporter `test-a` modifié (v2) et vérifier la boîte « Replace » puis le contenu chargé.
4. Facultatif : tenter **Customize > Plugins > Add > Add marketplace** avec le dépôt public, pour savoir si l'option existe sur Free.

## Sources

Officielles : [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) · [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) · [Using Agent Skills with the API](https://platform.claude.com/docs/en/build-with-claude/skills-guide) · [Skills overview (claude.com)](https://claude.com/docs/skills/overview.md) · [Create custom skills (claude.com)](https://claude.com/docs/skills/how-to) · [Plugins](https://claude.com/docs/plugins/overview.md) · [Plugin structure](https://claude.com/docs/plugins/build.md) · [Plugin platform support](https://claude.com/docs/plugins/platform-support.md) · [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude) · [Creating custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) · [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills) · [Create and edit files](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude) · [Tutoriel Academy](https://academy.claude.com/tutorials/teach-claude-your-way-of-working-using-skills) · [Skills explained](https://claude.com/blog/skills-explained) · [Equipping agents… (engineering)](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) · [Spécification Agent Skills](https://agentskills.io/specification) · [anthropics/skills](https://github.com/anthropics/skills)

Secondaires : [anthropics/claude-code#26254](https://github.com/anthropics/claude-code/issues/26254) (chemins `/mnt/skills/…`, montage absent) · [anthropics/claude-code#82044](https://github.com/anthropics/claude-code/issues/82044) (remplacement à la réimportation) · [simonw/claude-skills](https://github.com/simonw/claude-skills) (archive de `/mnt/skills`)
