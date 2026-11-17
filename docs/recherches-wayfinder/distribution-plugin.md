> Instantané de recherche du 17/11/2026 (ticket #12). Sources officielles d'Anthropic en priorité ; les sources secondaires sont marquées **[secondaire]**. Confiance : **Élevé** (source officielle explicite), **Moyen** (officiel indirect, sources en conflit ou secondaire solide), **Faible** (déduction ou témoignage isolé).

# Recherche — Peut-on distribuer le coach comme plugin sur Claude Free ?

## 1. Réponse courte

1. **Officiellement, non : les plugins sont réservés aux forfaits payants.** Le centre d'aide ouvre l'article sur les plugins par cette phrase : « Plugins are available to all paid plans (Pro, Max, Ultra, Team, Enterprise). » Free n'y figure pas, alors que l'article voisin sur les skills cite bien Free. Confiance **Élevé** pour ce que dit la doc.
2. **Mais ce n'est pas encore vérifié sur un vrai compte Free.** Depuis le 9/11/2026, Free a reçu la nouvelle page unique « Plugins » (ex-« Customize »), et la doc d'Anthropic s'est déjà trompée une fois sur Free : elle réserve les skills aux forfaits payants, alors que notre test T2 a prouvé le contraire. Seul un test de 10 minutes sur un compte Free dira si le bouton **Add > Add marketplace** existe. Confiance **Moyen** sur le blocage réel.
3. **Si l'option existe, le mécanisme convient parfaitement.** On ajoute une fois `Fafou59/coach-sportif`, on installe le plugin, et les mises à jour arrivent ensuite **sans action du proche** (« Sync automatically » pour un dépôt github.com) ou d'un clic (« Check for updates »). Les skills du plugin servent dans le chat web, desktop et mobile. Confiance **Élevé** sur les forfaits payants.
4. **Recommandation :** garder le **ZIP de skill** comme voie de distribution de référence pour les proches en Free (ADR 0004), et faire le test T4 (§ 6) avant de préparer la structure de plugin. Ne bâtir la distribution en plugin que si T4 réussit sur Free, mobile compris.

## 2. Faits établis

### 2.1 Forfaits

| Fait | Source | Confiance |
|---|---|---|
| « Plugins are available to all paid plans (Pro, Max, Ultra, Team, Enterprise). » Free n'est cité nulle part dans l'article. | [Use plugins in Claude (13837440)](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) | Élevé |
| À l'inverse, « Skills are available for users on Free, Pro, Max, Ultra, Team, and Enterprise plans » (exécution de code requise). | [Using skills in Claude (12512180)](https://support.claude.com/en/articles/12512180-using-skills-in-claude) | Élevé |
| La doc claude.com réserve **aussi** les skills aux forfaits payants (« Pro, Max, Ultra, Team, and Enterprise »), ce que le test T2 (compte Free, 14/11/2026) contredit. La liste des forfaits dans la doc claude.com n'est donc pas une preuve suffisante. | [Skills overview](https://claude.com/docs/skills/overview.md) ; [ADR 0003](../adr/0003-methode-en-skills-instruction-projet-minimale.md) | Élevé (le conflit) |
| La page unique « Plugins » remplace les onglets Skills, Connectors et Plugins. Déploiement progressif pour Free, Pro, Max, Ultra et Team dès le 29/10, disponible pour tous le 9/11/2026. L'article ne dit pas ce qu'un compte Free peut y faire (ajouter une marketplace, téléverser un plugin). | [Manage plugins, skills, and connectors from one Plugins page (17740565)](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page) | Élevé (le texte) / Faible (ce qu'il implique pour Free) |
| L'onglet **Discover** (annuaire d'Anthropic) n'apparaît que sur Pro, Max, Ultra, Team et Enterprise. La doc ne restreint pas explicitement **Add marketplace** ni **Upload plugin**. | [Plugins](https://claude.com/docs/plugins/overview.md) ; [Platform support](https://claude.com/docs/plugins/platform-support.md) | Élevé (le texte) / Faible (la déduction pour Free) |
| La page tarifs ne cite les plugins dans aucun forfait ; les skills y sont cochés pour Free ; Free a jusqu'à 5 projets. | [Pricing](https://claude.com/pricing) | Moyen |
| Des guides tiers disent les plugins payants ; un ticket signale même un compte Pro sans bouton « + » pour ajouter une marketplace (bug, clos). | **[secondaire]** [fast.io](https://fast.io/resources/claude-plugins-guide/) ; [claudeissues.com #50394](https://claudeissues.com/issue/50394-bug-cowork-customize-panel-has-no-button-to-add-marketplace-or-create-plugin-on) | Faible |

### 2.2 Ajout depuis GitHub et mises à jour (forfaits payants)

| Fait | Source | Confiance |
|---|---|---|
| Parcours : **Customize (désormais « Plugins ») > Plugins > Add > Add marketplace**, puis l'URL du dépôt ou le raccourci `owner/repo`. Les dépôts GitHub publics fonctionnent ; un dépôt privé demande de connecter GitHub. | [Plugins](https://claude.com/docs/plugins/overview.md) ; [13837440](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) | Élevé |
| Ajout et gestion depuis claude.ai ou l'app desktop. Aucun parcours d'ajout n'est documenté dans les apps mobiles. | [Platform support](https://claude.com/docs/plugins/platform-support.md) | Élevé (web, desktop) / Faible (mobile) |
| Mises à jour : un plugin issu d'une marketplace se met à jour depuis sa source ; une fois synchronisée, la nouvelle version arrive sur le compte **automatiquement, sans rien accepter**. **Check for updates** force la récupération ; pour une marketplace ajoutée soi-même depuis github.com, on peut activer **Sync automatically**. | [Plugins — Manage installed plugins](https://claude.com/docs/plugins/overview.md#manage-installed-plugins) | Élevé |
| La doc ne dit pas à quelle fréquence tourne « Sync automatically », ni si claude.ai détecte une nouvelle version par le champ `version` ou par le commit. Côté Claude Code : nouvelle copie seulement si la version calculée change (`version` de `plugin.json`, sinon commit) ; un `version` figé bloque les mises à jour. | [Host and maintain a marketplace](https://code.claude.com/docs/en/plugins/host-marketplace.md#release-a-new-version) | Moyen (transposé à claude.ai) |
| Limites : 25 marketplaces ajoutées soi-même par compte ; 5 000 fichiers et 200 Mo par plugin. | [Platform support](https://claude.com/docs/plugins/platform-support.md) | Élevé |
| Un dépôt ajouté en marketplace ou un plugin téléversé n'est **pas** revu par Anthropic. | [Plugins](https://claude.com/docs/plugins/overview.md) | Élevé |

### 2.3 Supports, projets et usage

| Fait | Source | Confiance |
|---|---|---|
| Une fois installé, le plugin est rattaché au compte : « Chat on the web, desktop, and mobile: its skills, commands, and connectors are available in your conversations. » | [Plugins — Find the plugin in each app](https://claude.com/docs/plugins/overview.md) ; [Connectors, skills, and plugins](https://claude.com/docs/extend/overview.md) | Élevé (doc claude.com) |
| Le centre d'aide, lui, ne cite que « Chat on the web » et l'onglet Chat de Claude Desktop, sans mentionner le mobile. | [13837440](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) | Moyen (silence, pas contradiction) |
| Dans le chat, seuls les skills, les commandes (chargées comme skills) et les connecteurs distants servent ; agents, hooks et serveurs MCP locaux sont ignorés. Un dossier `bin/` à la racine du plugin fait **refuser** l'installation sur claude.ai. | [Platform support](https://claude.com/docs/plugins/platform-support.md) | Élevé |
| Les skills d'un plugin apparaissent dans **Customize > Skills** avec le nom du plugin ; ils s'activent et se désactivent avec le plugin. Dans le menu `/`, on les trouve sous la forme `plugin:skill`. | [Skills overview](https://claude.com/docs/skills/overview.md) ; [Plugins](https://claude.com/docs/plugins/overview.md) | Élevé |
| Projets : aucune page ne parle des skills **de plugin** dans un projet. Les skills en général fonctionnent dans les projets, et un skill de plugin est listé comme les autres : il devrait donc fonctionner aussi dans un projet. | [Tutoriel Academy](https://academy.claude.com/tutorials/teach-claude-your-way-of-working-using-skills) ; [Skills overview](https://claude.com/docs/skills/overview.md) | Moyen (déduction) |
| Dans le chat claude.ai, le dossier entier du skill est copié dans le bac à sable ; les fichiers `references/` restent lus à la demande, comme pour un skill importé en ZIP. | [Create custom skills](https://claude.com/docs/skills/how-to.md) | Élevé |

### 2.4 Structure de dépôt exigée

Une marketplace est un dépôt qui contient `.claude-plugin/marketplace.json` à sa racine. Chaque plugin a son manifeste `.claude-plugin/plugin.json` et ses skills dans `skills/<nom>/SKILL.md`. Sources : [Plugin structure and testing](https://claude.com/docs/plugins/build.md), [Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace.md), [Marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference.md). Confiance **Élevé**.

Structure proposée pour ce dépôt (le plugin dans un sous-dossier, pour ne pas embarquer `docs/` ni `tests/`) :

```text
coach-sportif/                         # racine du dépôt = racine de la marketplace
├── .claude-plugin/
│   └── marketplace.json
└── plugins/
    └── coach/
        ├── .claude-plugin/
        │   └── plugin.json
        └── skills/
            └── coach/
                ├── SKILL.md           # même contenu que le skill du ZIP (ADR 0004)
                └── references/…
```

```json
// .claude-plugin/marketplace.json
{
  "name": "coach-sportif",
  "owner": { "name": "Fafou59" },
  "description": "Coach sportif pour les proches",
  "plugins": [
    { "name": "coach", "source": "./plugins/coach", "description": "Coach course, vélo, renfo, yoga" }
  ]
}
```

```json
// plugins/coach/.claude-plugin/plugin.json
{ "name": "coach", "version": "1.0.0", "description": "…" }
```

Règles utiles :

- **Champs obligatoires** : `name`, `owner.name` et `plugins` dans `marketplace.json` ; `name` et `source` pour chaque entrée. Le `source` relatif commence par `./` et se lit depuis la racine du dépôt, jamais avec `..`.
- **Noms** : l'entrée et `plugin.json` portent le même `name`. Le nom de marketplace ne doit pas imiter un nom officiel (ni `claude-…` réservé, ni caractères non ASCII). Le nom du skill ne doit contenir ni « claude » ni « anthropic ».
- **Version** : la monter à chaque publication, ou l'omettre partout pour suivre les commits. Ne pas la mettre à la fois dans `plugin.json` et dans l'entrée de la marketplace.
- **Interdit sur claude.ai** : un dossier `bin/` à la racine du plugin.
- **Le même dossier `skills/coach/` peut servir à produire le ZIP du skill** : les deux voies de distribution peuvent coexister sans dupliquer la source.
- **Dépôt public** : tout ce qui est sous `plugins/coach/` est lisible et installable par n'importe qui. Aucune donnée personnelle d'un athlète ne doit s'y trouver.

## 3. Comparaison pour un proche non technicien

| Critère | ZIP de skill (voie actuelle) | Plugin depuis la marketplace GitHub |
|---|---|---|
| Disponible sur Free | **Oui**, documenté et vérifié (T2) | **Non selon la doc** ; à vérifier (T4) |
| Installation initiale | Télécharger le ZIP, Customize > Skills > + > Importer | Plugins > Add > Add marketplace, coller `Fafou59/coach-sportif`, installer `coach`, activer « Sync automatically » |
| Possible depuis le téléphone seul | Import non documenté sur mobile | Ajout non documenté sur mobile |
| À chaque mise à jour | Retélécharger, réimporter, confirmer « Replace » ; risque d'oubli ou de mauvais fichier | **Rien** (sync auto) ou un clic sur « Check for updates » |
| Savoir quelle version tourne | Version écrite dans la description (Q18) | Version du plugin affichée dans Plugins |
| Usage web, desktop, mobile | Oui (T2 sur mobile) | Oui selon la doc claude.com |
| Usage dans un projet | Oui | Probable (non documenté) |
| Risque | Désynchronisation entre proches | Une erreur poussée sur `main` part chez tout le monde, sans relecture d'Anthropic |

Pour quelqu'un qui n'est pas à l'aise avec les fichiers, le plugin est nettement meilleur : une seule manipulation au départ, puis plus rien. Mais ce gain ne vaut que si l'option existe sur son compte Free.

## 4. Recommandation

1. **Ne rien changer à l'ADR 0004 pour l'instant** : le ZIP d'un seul skill `coach` reste la distribution de référence, seule voie documentée sur Free.
2. **Faire le test T4 (§ 6) sur un compte Free avant d'écrire le moindre fichier de plugin.** Il coûte 10 minutes et tranche la question.
3. **Si T4 réussit** (marketplace ajoutable, skill déclenché sur mobile, mise à jour reçue) : ajouter la structure du § 2.4, publier depuis la branche par défaut, et proposer le plugin aux proches. Garder le ZIP en secours. Écrire alors un ADR qui remplace la conséquence « un seul ZIP à réimporter ».
4. **Si T4 échoue** : clore la piste. Elle redeviendra intéressante si un proche passe à un forfait payant ou si Anthropic ouvre les plugins à Free (page des plugins à surveiller).
5. Dans les deux cas, désactiver le skill importé en ZIP avant d'installer le plugin : deux skills `coach` actifs en même temps risquent de se concurrencer au déclenchement (non documenté, confiance **Faible**).

## 5. Questions ouvertes

- Le bouton **Add > Add marketplace** (et **Upload plugin**) existe-t-il sur Free depuis la page unique « Plugins » du 9/11/2026 ?
- Délai réel de « Sync automatically » et critère de détection d'une nouvelle version sur claude.ai (`version` ou commit).
- Usage confirmé d'un skill de plugin dans un **projet**, depuis l'**app mobile**.
- Comportement si un skill personnel et un skill de plugin portent le même nom `coach`.

## 6. Test proposé (T4, environ 10 minutes, compte Free)

1. Sur claude.ai (web), compte Free : ouvrir **Plugins** (ex-Customize). Noter si **Add > Add marketplace** et **Add > Upload plugin** existent, ou si une invitation à passer à un forfait payant apparaît (capture d'écran).
2. Si l'option existe : sur une branche de test, créer la structure du § 2.4 avec un skill `test-plugin` qui renvoie un mot secret tiré de `references/secret.md`. Ajouter la marketplace (`Fafou59/coach-sportif#<branche>` ou un dépôt de test), installer le plugin, vérifier que le skill apparaît dans **Skills** avec le nom du plugin.
3. Dans l'app mobile, dans un projet : déclencher le skill et vérifier qu'il lit le mot secret.
4. Changer le mot secret et monter `version` à `1.0.1`, pousser. Sur le web, vérifier que **Sync automatically** est proposé et l'activer ; noter le délai avant que le mobile renvoie le nouveau mot. Sinon, cliquer **Check for updates**.
5. Supprimer ensuite la marketplace et le plugin de test.

## Sources

Officielles : [Use plugins in Claude (13837440)](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) · [Manage plugins, skills, and connectors from one Plugins page (17740565)](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page) · [Manage plugins for your organization (13837433)](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization) · [Using skills in Claude (12512180)](https://support.claude.com/en/articles/12512180-using-skills-in-claude) · [Plugins](https://claude.com/docs/plugins/overview.md) · [Plugin feature support across platforms](https://claude.com/docs/plugins/platform-support.md) · [Plugin structure and testing](https://claude.com/docs/plugins/build.md) · [Connectors, skills, and plugins](https://claude.com/docs/extend/overview.md) · [Skills overview](https://claude.com/docs/skills/overview.md) · [Create custom skills](https://claude.com/docs/skills/how-to.md) · [Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace.md) · [Host and maintain a marketplace](https://code.claude.com/docs/en/plugins/host-marketplace.md) · [Marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference.md) · [Pricing](https://claude.com/pricing) · [Tutoriel Academy](https://academy.claude.com/tutorials/teach-claude-your-way-of-working-using-skills)

Secondaires : [fast.io — Claude plugins guide](https://fast.io/resources/claude-plugins-guide/) (plugins payants) · [claudeissues.com #50394](https://claudeissues.com/issue/50394-bug-cowork-customize-panel-has-no-button-to-add-marketplace-or-create-plugin-on) (bouton absent sur Pro, bug clos)

Liens internes : [partage-skills.md § 2.5](https://github.com/Fafou59/coach-sportif/blob/research/partage-skills/docs/recherches-wayfinder/partage-skills.md) · ADR 0004 « Un seul skill `coach` » (dépôt local, pas encore poussé).
