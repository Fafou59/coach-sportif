# Installer ton coach sportif

Ce guide t'installe un coach d'entraînement (course, trail, vélo, renfo, mobilité) qui fonctionne **gratuitement** dans Claude et lit les données de ta montre **Garmin**. Compte environ **20 minutes**, sur un **ordinateur** pour l'installation et le branchement de Garmin ; ensuite tout se fait aussi depuis ton téléphone.

> ⚠️ Les noms de menus marqués *(à vérifier)* peuvent légèrement différer dans ton interface : cherche l'équivalent le plus proche.

## Ce qu'il te faut

- Une montre Garmin et ton compte **Garmin Connect** (e-mail et mot de passe). Sans Garmin, le coach fonctionne aussi, mais tu lui donnes tes chiffres toi-même et tu saisis les séances dans ton appli.
- Une adresse e-mail pour créer ton compte Claude.
- Le fichier **`coach.zip`**, à télécharger sur la page des versions : https://github.com/Fafou59/coach-sportif/releases/latest (bloc « Assets »). Ne le décompresse pas.

## 1. Créer ton compte Claude

1. Va sur https://claude.ai et crée un compte (le forfait **gratuit** suffit).
2. Installe aussi l'appli **Claude** sur ton téléphone et connecte-toi avec le même compte.

## 2. Activer l'exécution de code

Sans cette option, ni le coach ni ton carnet ne fonctionnent.

1. Sur claude.ai : **Paramètres > Capacités** *(à vérifier)*.
2. Active **« Exécution de code et création de fichiers »**.

## 3. Importer le coach

1. Sur claude.ai : **Personnaliser > Skills** *(à vérifier)*, ou directement https://claude.ai/customize/skills.
2. Clique sur **+** (ou « Importer un skill ») et choisis le fichier **`coach.zip`**.
3. Vérifie que le skill **coach** apparaît et qu'il est **activé**.

## 4. Créer ton projet « Coach »

1. Sur claude.ai : **Projets > Nouveau projet**, nomme-le **« Coach »**.
2. Dans les **instructions du projet**, colle exactement ce texte :

```
Tu es mon coach d'entraînement. Utilise le skill `coach` pour chaque message.

Mon carnet : pas encore créé, le coach le créera au démarrage.
(Quand le coach t'a donné le lien du carnet, remplace la ligne ci-dessus par : « Mon carnet est le Claude Doc à ce lien : » suivi du lien.)

Ouvre le carnet avec l'outil Claude Docs à partir de son lien ; ce n'est pas un fichier Google Drive. Il n'existe qu'un carnet : dès que le lien est là, travaille toujours dans celui-ci.
```

## 5. Ton premier échange : le démarrage

1. Dans le projet **Coach**, ouvre une nouvelle conversation.
2. Si Google Drive est connecté à ton compte Claude, désactive-le dans cette conversation (menu **+** de la zone de message *(à vérifier)*) : sinon Claude risque de chercher ton carnet dans Drive.
3. Écris : **« Je veux commencer »**.
4. **Garmin** : le coach te propose de brancher ta montre. Il t'explique d'abord les risques de ce service non officiel (missingmcp), puis te guide pas à pas, **sur ordinateur**. Tu peux refuser : il continue alors avec les chiffres que tu lui donnes.
5. Le coach crée ton **carnet** (un document Claude où il note tout) et te donne son lien. **Colle ce lien dans les instructions du projet**, comme indiqué entre parenthèses.
6. Réponds à ses questions, étape par étape (8 étapes : profil, objectifs, contraintes, verdict, semaine-type, plan, premier bloc, première semaine). Ça peut s'étaler sur plusieurs conversations : tout est sauvegardé dans le carnet.

## 6. Au quotidien

Un seul mot à retenir : **« check »**.

| Tu écris | Quand | Ce que fait le coach |
|---|---|---|
| **« check »** | quand tu veux, surtout après une séance importante, et le **dimanche** | Il regarde ta montre et choisit lui-même : un point rapide (« RAS » s'il n'y a rien à dire), le **bilan de la semaine** le dimanche (quelques questions, puis la semaine suivante), ou un bilan court si tu as sauté le dimanche |
| ce qui t'arrive | dès que ça arrive | Douleur, maladie, voyage, semaine chargée : il adapte |

Quelques règles du jeu :

- **Le coach ne te contacte jamais de lui-même** : c'est toi qui écris « check ».
- **Rien ne change dans ta montre sans ton « GO »** : le coach te montre d'abord ce qu'il va créer, déplacer ou supprimer, puis attend que tu écrives **GO**.
- Ses questions sont numérotées (❓ Q1, Q2…). Quand il te donne une recommandation (➡️), répondre **« OK »** veut dire que tu la suis.
- Il te dit à quel point chaque conseil est prouvé (« solide », « peu étudié », « habitude de coach »…). Demande **« pourquoi ? »** pour avoir l'étude.
- Il propose, **tu décides**. Il peut te challenger une fois, puis il applique ton choix.

## 7. Mettre à jour le coach

Quand une nouvelle version sort, télécharge le nouveau **`coach.zip`** sur https://github.com/Fafou59/coach-sportif/releases/latest et réimporte-le comme à l'étape 3 : Claude propose de **remplacer** l'ancien. Ton carnet et tes séances ne bougent pas.

## Bon à savoir

- **Ce n'est pas un médecin.** En cas de douleur forte, de douleur qui augmente, de malaise ou de fièvre, le coach te dira de consulter : suis ce conseil.
- **Ton carnet t'appartient** : il est dans ton compte Claude. Le coach te proposera régulièrement de l'exporter pour en garder une copie. Ne le supprime pas.
- **Forfait gratuit** : le nombre de messages est limité sur quelques heures. Si tu atteins la limite, reprends plus tard : le carnet garde tout.

## En cas de souci

| Ce qui se passe | Que faire |
|---|---|
| Le coach dit que Garmin n'est pas branché | Vérifie que le connecteur Garmin est activé dans la conversation (menu **+**) ; sinon, le coach te guide pour le brancher |
| Erreur de connexion Garmin après quelques semaines | Ta connexion a expiré : le coach te guide pour te reconnecter |
| Le coach ne retrouve pas ton carnet | Vérifie que le lien du carnet est bien dans les instructions du projet, et que Google Drive est désactivé |
| Le coach ne semble pas « coach » | Vérifie que le skill **coach** est activé (étape 3) et que tu écris dans le projet **Coach** |
