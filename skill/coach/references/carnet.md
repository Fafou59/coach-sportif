# Carnet : modèle et usage

Le carnet est un **Claude Doc** propre à l'athlète, en 6 onglets. Il fait foi pour tout ce qui est décidé ; Garmin fait foi pour le planifié et le réalisé.

Sommaire : Ouvrir et modifier · Onglets à lire par situation · Qui écrit quoi · Création · Modèle des onglets · Sauvegarde.

## Ouvrir et modifier

- Ouvre le carnet avec l'outil Claude Docs à partir du lien de l'instruction de projet. Jamais de recherche dans Google Drive, jamais de copie. Lien absent : demande-le.
- Liste d'abord les onglets, puis lis seulement ceux de la situation (tableau ci-dessous).
- Modifie l'onglet ou le bloc concerné (une ligne de tableau, une section), jamais le Doc entier.
- Tu ne supprimes rien : un bloc terminé se **déplace** vers Archives.
- Aucun identifiant Garmin (ID de séance, ID d'activité) dans le carnet : relis-les dans Garmin au besoin.
- Après chaque modification, dis en une ligne ce qui a changé et dans quel onglet.

## Onglets à lire par situation

| Situation | Onglets lus |
|---|---|
| Démarrage | Tous, au fur et à mesure des étapes |
| Check, imprévu, bilan express | Repères, Plan, Notes (+ Athlète si douleur ou antécédent utile) |
| Bilan du dimanche, fin de bloc | Tous sauf Archives |
| Course à J-7, bilan de course | Objectifs, Repères, Plan |
| Question libre | Selon le sujet ; aucun si la question est générale |

Archives ne se relit que sur demande de l'athlète ou pour comparer avec un bloc passé précis.

## Qui écrit quoi

| Onglet | Contenu | Écrit par |
|---|---|---|
| Athlète | Fiche, antécédents, consentements, contraintes et préférences, état du démarrage | Coach ; l'athlète peut modifier contraintes et préférences |
| Objectifs | Objectifs A/B/C, verdicts, profil de course de chaque A et B | Coach |
| Repères | Allures, puissances, bandes FC, plage personnelle de récupération | Coach |
| Plan | Plan macro, bloc en cours, journal des décisions du bloc | Coach |
| Notes | Notes libres | Athlète seulement (le coach lit, n'écrit pas) |
| Archives | Blocs terminés (détail et journal) | Coach, par déplacement |

## Création (démarrage, étape 1)

Crée le Doc « Carnet — <prénom> » avec les 6 onglets ci-dessous, tableaux vides. Donne le lien à l'athlète et demande-lui de le coller dans l'instruction de son projet (modèle : `kit/instruction-projet.md` du dépôt). Rien n'est prérempli : chaque onglet se remplit à son étape.

## Modèle des onglets

### Onglet « Athlète »

```
## Fiche
| Champ | Valeur |
|---|---|
| Prénom | |
| Sports | |
| Niveau | débutant / intermédiaire / confirmé |
| Ancienneté de pratique | |
| Volume habituel (8–12 sem.) | h/sem., séances/sem., km course |
| Plus longue sortie (30 j) | |
| Références (courses, records) | |
| Matériel | ceinture cardio, capteur de puissance, salle ou haltères |

## Antécédents
| Question | Réponse |
|---|---|
| Blessure de course < 12 mois | |
| Fracture de fatigue passée | |
| Signes de déficit énergétique | |

## Consentements
| Donnée | Accord | Date |
|---|---|---|
| Cycle menstruel | oui / non | |
| Poids | oui / non | |
| Grossesse | oui / non | |

## Contraintes
| Contrainte | Détail |
|---|---|
| Jours disponibles | |
| Durée max par séance (semaine / week-end) | |
| Vacances, déplacements | |

## Préférences
| Préférence | Détail | Revue le |
|---|---|---|
| Dosage côtes et descente | | |

## État du démarrage
Étape : 1/8 — <date>
```

### Onglet « Objectifs »

```
## Objectifs
| Priorité | Objectif | Date | Chrono visé | Verdict |
|---|---|---|---|---|
| A | | | | |

## Profil de course — <objectif>
| Champ | Valeur |
|---|---|
| Distance | |
| D+ / D− | |
| D+/km et catégorie | plat / vallonné / accidenté / montagne |
| Montées principales | longueur, pente, durée estimée |
| Descentes principales | |
| Source et précision | Garmin Connect / GPX / capture / officiel |
```

### Onglet « Repères »

```
## Allures (course)
| Allure | Valeur | Source | Confiance | Mise à jour |
|---|---|---|---|---|
| EF | | | | |
| Seuil | | | | |
| Seuil haut | | | | |
| VMA | | | | |
| Allure objectif (@21K…) | | | | |

Test qui a donné la valeur : <test, protocole, date>

## Puissances (vélo)
| Repère | Valeur | Source | Confiance | Mise à jour |
|---|---|---|---|---|
| FTP | | | | |

## Bandes FC
| Sport | LTHR | Facile | Seuil | Au-dessus |
|---|---|---|---|---|
| Course | | | | |
| Vélo | | | | |

## Plage personnelle de récupération (recalculée le dimanche)
| Métrique | Ligne de base 28–30 j | Plage | Calculée le |
|---|---|---|---|
| VFC nocturne | | | |
| FC de repos | | | |
| Durée de sommeil | | | |

Autres : sudation (L/h), tolérance digestive.
```

### Onglet « Plan »

```
## Plan macro
| Bloc | Semaines | Phase | Qualité principale | Volume/sem. |
|---|---|---|---|---|

## Semaine-type
| Jour | Séance (sport, qualité ou endurance, durée max) |
|---|---|

## Bloc en cours : bloc <n> (<3+1 ou 2+1>), du <date> au <date>
Qualité principale : … · Qualité d'entretien : …
| Semaine | Jour | Séance (nomenclature Garmin) | Statut |
|---|---|---|---|

## Suivi hebdomadaire (rempli au bilan du dimanche)
| Semaine | Course (km, h) | Total (h) | Charge RPE | Bande Facile | Plus longue sortie |
|---|---|---|---|---|---|

## Journal des décisions du bloc
| Date | Décision | Raison |
|---|---|---|
```

### Onglet « Notes »

```
Notes libres de l'athlète.
```

### Onglet « Archives »

```
## Bloc <n> — du <date> au <date>
(détail du bloc et journal des décisions, déplacés depuis Plan à la fin du bloc)
```

## Sauvegarde

À chaque fin de bloc, propose un **export Markdown** du carnet : l'historique des versions des Claude Docs n'est pas garanti et une suppression depuis l'appli est définitive.
