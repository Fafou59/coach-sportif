# Brancher le connecteur Garmin

À dérouler quand les outils Garmin sont absents de la conversation, ou quand un appel Garmin échoue sur une erreur de connexion ou d'authentification. Regarde d'abord l'onglet Athlète : « Garmin : branché » → le connecteur existe déjà, va directement au § Si ça ne marche pas ; « Garmin : non branché, choix du… » → mode dégradé sans reproposer. Propose d'abord le branchement, risques compris (§ 1), puis guide l'athlète **une étape à la fois**, en mots simples, et attends qu'il confirme avant la suivante. N'invente aucune donnée Garmin en attendant : passe en mode dégradé (SKILL.md) si l'athlète veut avancer sans connecteur.

Le connecteur est **missingmcp**, un service tiers qui relie Garmin Connect à Claude (cadrage Q8). Les libellés de menus ci-dessous viennent de la page missingmcp (en anglais) et de l'aide Claude ; ceux marqués « à vérifier » n'ont pas été confirmés dans l'interface en français.

## 1. Proposer, risques d'abord

Avant toute étape, et donc avant que l'athlète tape le moindre identifiant, un message format B :
- une ligne : le connecteur Garmin n'est pas branché ; avec lui, le coach lit tes séances et ta récupération, et crée les séances dans ta montre (après ton « GO ») ;
- les **points de vigilance** ci-dessous, en 5 lignes courtes ;
- `❓ **Q1 – Garmin** : tu veux le brancher maintenant ?` avec `➡️ Oui, si les points ci-dessus te conviennent ; sinon le coach continue en mode dégradé.`

Réponse « non » : note-le dans l'onglet Athlète, dès que le carnet existe (« Garmin : non branché, choix du <date> ») et continue en mode dégradé (SKILL.md) ; ne repropose le branchement que si l'athlète en reparle. Réponse « oui » ou « OK » : § 2.

### Points de vigilance (à dire à l'athlète, honnêtement)
- **Service tiers non officiel** : missingmcp n'est ni affilié ni approuvé par Garmin. Il est opéré par **une seule personne**. Il passe par un accès non officiel à Garmin Connect, comme d'autres outils libres.
- **Identifiants** : le mot de passe Garmin sert une seule fois et n'est pas conservé ; le service garde des **jetons de session chiffrés** (AES-256-GCM) pour accéder aux données, qui transitent à la demande sans être stockées (selon la page missingmcp).
- **Conditions Garmin** : elles demandent de ne pas confier ses identifiants à un tiers ; la page missingmcp le reconnaît. C'est à l'athlète de décider.
- **Pérennité** : le service peut cesser de fonctionner si Garmin change son système de connexion ou bloque cet accès ; il faut aussi **se reconnecter** quand les jetons expirent (durée non publiée).
- **Révocation** : la connexion peut être retirée à tout moment en supprimant le connecteur dans Claude (la révocation côté missingmcp n'est pas détaillée par la page).
- **Quota** : le connecteur expose environ 157 outils, chargés dans chaque conversation ; l'effet sur le quota du forfait gratuit reste à mesurer.

## 2. Avant de commencer

- Un compte Claude (le forfait gratuit suffit) et un compte Garmin Connect.
- Dans Claude : **Paramètres > Capacités > « Exécution de code et création de fichiers »** activé. Sans cette option, ni le skill ni le carnet (Claude Doc) ne fonctionnent.
- Le forfait gratuit n'accepte **qu'un seul connecteur personnalisé** : Garmin l'occupe. Claude Docs n'en est pas un et reste disponible.
- L'ajout du connecteur se fait sur **claude.ai dans un navigateur ou dans l'appli de bureau**, pas depuis l'appli mobile ; il se synchronise ensuite avec le téléphone. Athlète sur téléphone : il fait les étapes 1 à 3 sur un ordinateur, puis revient ici ; en attendant, la procédure en cours continue en mode dégradé si elle le peut.

## 3. Étapes

1. **Ouvrir la page du service** : https://missingmcp.com/garmin. Elle donne l'adresse du connecteur : `https://missingmcp.com/garmin/mcp`.
2. **Ajouter le connecteur dans Claude** : menu **Personnaliser > Connecteurs**, bouton **+ Ajouter**, puis **Ajouter un connecteur personnalisé** (en anglais : Customize > Connectors > + Add > Add custom connector ; libellés français à vérifier, le menu peut aussi se trouver sous Paramètres > Connecteurs).
   - Nom : `Garmin`.
   - Adresse : `https://missingmcp.com/garmin/mcp`.
   - Client OAuth : choisir l'enregistrement automatique (« Register automatically » ; libellé à vérifier).
3. **Se connecter à Garmin** : Claude ouvre une page de connexion missingmcp. Saisir l'e-mail et le mot de passe Garmin Connect, puis le code de vérification si Garmin en demande un (double authentification prise en charge). Ces identifiants se saisissent sur cette page, jamais dans la conversation.
4. **Activer le connecteur dans la conversation du coach** : menu **+** de la zone de message > **Connecteurs** > Garmin activé (à vérifier). Si Google Drive est connecté, le désactiver dans les conversations du coach, pour que Claude ne cherche pas le carnet dans Drive.
5. **Vérifier** : l'athlète écrit « Quelle est ma dernière activité Garmin ? ». Tu lis `get_activities_by_date` sur les 7 derniers jours et réponds par une ligne : date, sport, durée. Si ça marche, le connecteur est branché : note « Garmin : branché le <date> » dans l'onglet Athlète (dès que le carnet existe) et reprends la procédure en cours.

## Si ça ne marche pas

| Symptôme | Piste |
|---|---|
| Aucun outil Garmin dans la conversation | Connecteur non activé dans cette conversation (étape 4) |
| Erreur d'authentification après des semaines sans souci | Session Garmin expirée : refaire l'étape 3 (se reconnecter depuis le connecteur, libellé à vérifier) |
| Échec persistant | Le service peut être en panne ou bloqué par Garmin : mode dégradé, réessayer plus tard |
