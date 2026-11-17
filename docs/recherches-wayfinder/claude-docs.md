# Que peut faire un skill avec Claude Docs sur claude.ai Free ?

Recherche du 17/11/2026 pour l'issue #4 (carte : #1). Elle vérifie l'hypothèse de l'[ADR 0002](../adr/0002-carnet-claude-doc-et-garmin-pour-le-realise.md) : le **carnet** de chaque athlète est un Claude Doc.

**Confiance** : **Élevé** = écrit noir sur blanc dans une source officielle ; **Moyen** = déduit d'une source officielle, des schémas d'outils Claude Docs ou du test du 14/11/2026 ; **Faible** = non documenté, ou sources contradictoires.

## Réponse courte

Sur Free, un skill peut faire **créer** le carnet comme Claude Doc depuis une conversation, puis le **relire** et le **modifier par morceaux** dans d'autres conversations. Les **tableaux** et les **onglets** sont pris en charge. L'athlète peut le **lire et le modifier sur mobile**. Claude Docs n'est **pas un connecteur personnalisé**, donc le connecteur Garmin reste possible. En revanche, quatre points ne sont pas documentés et doivent être testés : rouvrir le Doc à partir d'un lien placé dans l'instruction de projet, la limite de taille, la restauration d'une version, et le risque que Claude cherche le carnet dans Drive.

## Constats

| # | Constat | Confiance | Source |
|---|---|---|---|
| 1 | Claude Docs est disponible sur Free (comme sur tous les forfaits) et activé par défaut. | Élevé | [S1], [S2], [S3] |
| 2 | **Prérequis** : les artefacts, donc Claude Docs, exigent que l'option « Exécution de code et création de fichiers » (*Create and edit files*) soit activée dans **Paramètres > Capacités**. C'est une étape à prévoir à l'installation chez un proche. | Élevé | [S2] |
| 3 | On crée un Doc **depuis n'importe quelle conversation** en le demandant, avec `/docs`, ou par « Output » > « Docs ». Pour rédiger, Claude peut s'appuyer sur les fichiers, la mémoire, les **projets**, les **skills** et les applis connectées. Un skill peut donc piloter la création du carnet. | Élevé | [S1] |
| 4 | Sur iOS et Android, on peut demander un Doc (« revenir plus tard » pour le résultat), l'ouvrir en plein écran depuis l'onglet **Artefacts** et **le modifier**. Le mobile ne permet pas de changer le partage. | Élevé | [S1], [S2], [S4] |
| 5 | Chaque Doc est enregistré dans l'onglet **Artefacts** et « peut être retrouvé depuis n'importe quelle conversation ». La doc vise l'utilisateur qui le rouvre, pas Claude qui le relit depuis une nouvelle conversation. | Élevé | [S1], [S2] |
| 6 | Claude peut **rouvrir et relire** un Doc à partir de son lien dans une nouvelle conversation. Ce n'est pas écrit dans l'aide. C'est déduit du test sur compte Free du 14/11/2026 (réussi) et du schéma de l'outil `read` : un lien `claude.ai/artifact/<id>` se lit en passant l'`id` comme référence du Doc, ce qui liste ses onglets puis leur contenu. | Moyen | Test du 14/11 (ADR 0002), [T] |
| 7 | **Modifier une section sans tout réécrire.** Ce qui est documenté : on demande la modification dans la conversation (« ajoute une section risques ») et Claude signale ce qu'il a changé ; on surligne un passage et on clique « Edit with Claude », et la modification porte sur ce passage ; on peut aussi écrire « @Claude » dans un commentaire. Côté outils, `update` vise un **nœud** (un bloc) ou un onglet, et `batch` applique plusieurs opérations de façon atomique, ce qui va dans le sens d'une modification par bloc. | Élevé (fonction), Moyen (granularité réelle) | [S1], [S2], [T] |
| 8 | **Tableaux** : un Doc peut contenir titres, **tableaux** et mise en forme, et il existe des raccourcis clavier pour les tableaux. La façon dont Claude modifie une seule cellule ou ligne n'est pas documentée. | Élevé (présence), Moyen (modification par Claude) | [S1] |
| 9 | **Onglets** : un Doc peut avoir plusieurs onglets, « comme les sections d'un carnet ». Un Doc garde toujours au moins un onglet. | Élevé | [S1], [T] (`delete`) |
| 10 | **Taille** : aucune limite de taille n'est documentée pour un Doc. Seules limites trouvées : (a) Claude Docs consomme le quota du forfait, et un long Doc tiré de plusieurs sources en consomme davantage ; (b) les 100 Mo et 25 000 enregistrements par artefact concernent le stockage de données des artefacts-applis, pas le texte d'un Doc ; (c) l'export accepte jusqu'à environ 11 Mo (`maxBytes` de l'outil `export`). En pratique, la limite est la fenêtre de contexte et le quota Free à chaque relecture. | Faible | [S1], [S2], [T] |
| 11 | **Historique des versions** : il existe (cité dans les limites connues : en panneau étroit, il s'affiche par-dessus le texte). Toute modification est attribuée à son auteur, personne ou Claude. La restauration d'une version n'est pas décrite. Une source secondaire (référence de l'API Compliance, vue via une recherche) indique que la liste des versions d'un Doc est vide côté API. | Moyen (existence, attribution), Faible (restauration) | [S1], [S5] (secondaire) |
| 12 | **Suppression** : supprimer un Doc depuis l'appli est définitif (pas de corbeille) et le rend indisponible pour tous. L'outil `delete` se dit au contraire « restaurable, contrairement au Delete de l'appli ». Seul le propriétaire peut renommer ou supprimer. | Élevé (appli), Moyen (outil) | [S1], [T] |
| 13 | **Partage sur Free** : les sources se contredisent. L'article Claude Docs dit que Free peut partager « avec quiconque a le lien », mais le tableau de l'article sur le partage ne coche pas Free pour cette option. Ce qui est sûr : Free ne peut pas inviter par e-mail ; via un lien, un Doc ne s'ouvre qu'à une personne connectée à Claude, et **en lecture seule** ; Claude agit avec les droits de la personne qui le sollicite. | Élevé (pas d'invitation, lecture seule par lien), Faible (lien sur Free) | [S1], [S4] |
| 14 | **Projets sur Free** : disponibles (5 projets au maximum), avec instructions de projet. Que Claude retrouve le carnet grâce à un lien écrit dans l'instruction de projet n'est **pas documenté**. C'est plausible au vu de [6] (un lien suffit à `read`), mais à vérifier. | Élevé (projets), Moyen (lien en instruction) | [S6], [T], test du 14/11 |
| 15 | **Claude Docs ne compte pas comme connecteur personnalisé** : c'est un modèle d'artefact, activé par défaut et piloté par Paramètres > Capacités, alors qu'un connecteur personnalisé s'ajoute par URL dans Personnaliser > Connecteurs. La limite Free est d'**un connecteur personnalisé** (ici Garmin/missingmcp). Google Drive est un connecteur de l'annuaire, pas un connecteur personnalisé. Aucune page ne dit explicitement « Docs ne compte pas », d'où un niveau Moyen pour cette conclusion. | Élevé (limite Free, nature de Drive), Moyen (Docs hors quota) | [S1], [S2], [S7], [S8] |
| 16 | **Google Drive** : une fois connecté, Drive peut être **activé ou désactivé par conversation** (+ > Connecteurs) ; Claude peut alors chercher dans Drive « de lui-même ». Aucune source officielle ne décrit une confusion entre carnet et Drive, ni la formulation qui l'éviterait. Claude Docs exporte aussi vers Google Docs, ce qui crée une copie de plus à ne pas confondre. | Élevé (activation par conversation), Faible (formulation anti-Drive) | [S8], [S1] |

## Implications pour le carnet

1. **L'ADR 0002 tient** : création, relecture et modification par morceaux sont documentées ou observées sur Free, et le Doc n'occupe pas le seul connecteur personnalisé.
2. **Guide d'installation** : ajouter « Paramètres > Capacités > Exécution de code et création de fichiers : activé » (constat 2). Faire créer le carnet **dans le compte de l'athlète** : il en est propriétaire, car un lien ne donne qu'une lecture seule et Free ne peut pas inviter.
3. **Instruction de projet** (ADR 0003) : y mettre le lien complet `https://claude.ai/artifact/…` et le désigner sans ambiguïté. Formulation proposée, à valider en test : « Le carnet est un **Claude Doc** (artefact claude.ai), à ouvrir avec l'outil Claude Docs à partir de ce lien. Ce n'est pas un fichier Google Drive : ne le cherche jamais dans Drive et n'en crée pas de copie. » Si Drive est connecté, conseiller de le **désactiver dans les conversations du coach**.
4. **Structure** : utiliser des **onglets** (fiche, objectifs et profils de course, plan et bloc, journal des décisions, notes de l'athlète) et des **tableaux** pour les allures et les blocs. Le skill relit seulement l'onglet utile et modifie un bloc précis, jamais le Doc entier, ce qui économise le quota.
5. **Taille** : en l'absence de limite documentée, garder le carnet compact (archiver le journal des décisions par bloc dans un onglet séparé) et mesurer pendant la répétition.
6. **Sécurité des données** : la restauration de versions n'est pas garantie et la suppression depuis l'appli est définitive. Le skill ne supprime jamais rien. Proposer un **export Markdown** du carnet à chaque fin de bloc.

## À tester pendant la répétition à blanc

- [ ] Compte Free neuf : l'option Capacités est-elle active par défaut ? La création du carnet fonctionne-t-elle depuis le skill `coach-demarrage`, sur le web puis sur mobile ?
- [ ] Le lien dans l'**instruction de projet** suffit-il pour qu'une nouvelle conversation ouvre le carnet sans qu'on le recolle ?
- [ ] Modification d'**une section**, puis d'**une ligne de tableau** : le reste du Doc est-il intact (comparer dans l'historique) ?
- [ ] Avec **Google Drive connecté et activé** : Claude cherche-t-il le carnet dans Drive ? La formulation proposée l'en empêche-t-elle ?
- [ ] Édition par l'athlète sur **mobile** (onglet notes), puis relecture par Claude dans la conversation suivante.
- [ ] **Historique des versions** : peut-on voir et restaurer une version antérieure sur Free ?
- [ ] **Taille** : remplir le carnet comme après 3 blocs. Mesurer la consommation de quota d'une relecture et repérer toute troncature.
- [ ] Coexistence : Garmin (connecteur personnalisé) et Claude Docs utilisés dans la même conversation.

## Sources

- [S1] Anthropic, *Get started with Claude Docs* : <https://support.claude.com/en/articles/16923645-get-started-with-claude-docs> (consulté le 17/11/2026)
- [S2] Anthropic, *What are artifacts and how do I use them?* : <https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them>
- [S3] Anthropic, *Release notes* (16/09/2026, « Create designs, decks, and docs in any conversation ») : <https://support.claude.com/en/articles/12138966-release-notes>
- [S4] Anthropic, *Share artifacts* : <https://support.claude.com/en/articles/9547008-publish-and-share-artifacts>
- [S5] **Secondaire** : extrait de la référence de l'API Compliance (Claude Docs, liste de versions vide), vu dans un résumé de recherche web, page d'origine non ouverte.
- [S6] Anthropic, *What are projects?* : <https://support.claude.com/en/articles/9517075-what-are-projects>
- [S7] Anthropic, *Get started with custom connectors using remote MCP* : <https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp>, et *Use connectors to extend Claude's capabilities* : <https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities>
- [S8] Anthropic, *Google Drive* (connecteur) : <https://claude.com/docs/connectors/google/drive>
- [T] Schémas des outils Claude Docs exposés dans une session Claude Code (`create`, `read`, `update`, `batch`, `query`, `export`, `delete`, `guide`), **inspectés sans les appeler** le 17/11/2026. Les outils de claude.ai Free sont probablement les mêmes, sans garantie, d'où au mieux un niveau Moyen.
