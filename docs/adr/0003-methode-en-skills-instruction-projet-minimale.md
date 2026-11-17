# La méthode vit dans des skills ; le projet ne porte qu'une instruction minimale

En Free, les instructions et fichiers d'un projet sont relus à chaque message, alors qu'un skill n'est chargé que lorsqu'il sert. Le test T2 (14/11/2026, compte Free) a montré qu'un skill importé se déclenche depuis l'app mobile, lit ses fichiers annexes, et cohabite avec le connecteur Garmin et Claude Docs. La méthode et le référentiel de règles sont donc livrés en skills communs à tous les athlètes ; le projet de chaque athlète ne contient qu'une instruction courte pointant vers son carnet.

## Conséquences
- Mettre à jour la méthode = réimporter les ZIP des skills, sans toucher aux carnets.
- Quand Google Drive est aussi connecté, Claude a tendance à y chercher le carnet : l'instruction de projet et le skill socle doivent dire explicitement que le carnet est un **Claude Doc** (lien fourni) et qu'il ne faut pas chercher dans Drive.

## Option écartée
- Méthode dans les instructions de projet : installation plus simple, mais relue à chaque message (quota) et non modulaire.
