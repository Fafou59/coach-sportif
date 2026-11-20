# Carnet : modèle et usage

Le carnet est un **Claude Doc** propre à l'athlète, en 6 onglets. Il fait foi pour tout ce qui est décidé ; Garmin fait foi pour le planifié et le réalisé.

Sommaire : Ouvrir et modifier · Onglets à lire par situation · Qui écrit quoi · Création · Modèle des onglets · Sauvegarde.

## Ouvrir et modifier

- Ouvre le carnet avec l'outil Claude Docs à partir du lien claude.ai de l'instruction de projet ; il ne se trouve jamais dans Google Drive.
- Pas de lien, ou seulement un texte d'attente (« pas encore créé », texte entre chevrons) : pas encore de carnet ; au démarrage, crée-le (§ Création), sinon demande le lien. Lien valide : c'est **le** carnet, un seul par athlète, jamais de second ni de copie.
- Liste d'abord les onglets, puis lis seulement ceux de la situation (tableau ci-dessous).
- Modifie l'onglet ou le bloc concerné (une ligne de tableau, une section), jamais le Doc entier.
- Le carnet s'écrit **sans GO ni autorisation**, y compris en MODE RÉPÉTITION (qui ne bloque que Garmin). Après chaque modification, dis en une ligne ce qui a changé et dans quel onglet.
- Écris au moment de la décision, dans le message où elle est prise : un imprévu en particulier (SKILL.md, Imprévus ouverts) ne reste jamais seulement dans la conversation.
- Tu ne supprimes rien : un bloc terminé se **déplace** vers Archives.
- Aucun identifiant Garmin (ID de séance, ID d'activité) dans le carnet : relis-les dans Garmin au besoin.

## Onglets à lire par situation

| Situation | Onglets lus |
|---|---|
| Démarrage | Tous, au fur et à mesure des étapes |
| Check, imprévu, bilan express | Repères, Plan, Notes (+ Athlète si douleur ou antécédent utile) |
| Bilan du dimanche, fin de bloc | Tous sauf Archives |
| Course à J-7, bilan de course | Objectifs, Repères, Plan |
| Question libre | Plan (imprévus ouverts) si la réponse touche ses séances, plus selon le sujet ; aucun si la question est générale |

Dans Plan, lis toujours en premier « Imprévus ouverts » et « Dernière séance analysée ».

Archives ne se relit que sur demande de l'athlète ou pour comparer avec un bloc passé précis.

## Qui écrit quoi

| Onglet | Contenu | Écrit par |
|---|---|---|
| Athlète | Fiche, niveaux de preuve, antécédents, consentements, contraintes et préférences, état du démarrage | Coach ; l'athlète peut modifier contraintes, préférences et consentements |
| Objectifs | Objectifs A/B/C, chronos (ou « sans chrono »), verdicts, profil de course de chaque A et B | Coach |
| Repères | Allures, puissances, bandes FC, plage personnelle de récupération | Coach |
| Plan | Imprévus ouverts, dernière séance analysée, plan macro, bloc en cours, suivi hebdomadaire, journal des décisions | Coach |
| Notes | Notes libres | Athlète seulement (le coach lit, n'écrit pas) |
| Archives | Blocs terminés (détail et journal) | Coach, par déplacement |

## Création (démarrage, étape 1)

Seulement quand il n'y a pas encore de carnet (aucun lien claude.ai, ou texte d'attente). Crée le Doc « Carnet — <prénom> » avec les 6 onglets ci-dessous, tableaux vides. Donne le lien à l'athlète et demande-lui de remplacer, dans l'instruction de son projet, la ligne « Mon carnet : pas encore créé… » par ce lien. Rien n'est prérempli, ni depuis la mémoire de Claude ni depuis une autre conversation : chaque onglet se remplit à son étape.

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

## Niveaux de preuve (expliqués au démarrage)
Chaque conseil s'appuie sur une règle plus ou moins prouvée, dite en mots : « solide (plusieurs études) » (A), « assez solide (une étude) » (B), « peu étudié » (C), « habitude de coach, non prouvée » (D).
« Choix de prudence » : appliqué par sécurité, même sans preuve forte (garde-fou de prudence, S).
Demande « pourquoi ? » pour avoir l'étude derrière un conseil.

## Antécédents (demandés une fois)
| Question | Réponse |
|---|---|
| Blessure de course < 12 mois | |
| Fracture de fatigue passée | |
| Fatigue persistante | |
| Perte de poids non voulue | |
| Blessures osseuses répétées | |

## Consentements (bloc 🔒 ; « OK » = accord pour toutes les données listées ; sans réponse, rien n'est lu)
| Donnée | Accord | Date | Retrait le |
|---|---|---|---|
| Cycle menstruel | oui / non / sans objet | | |
| Grossesse | oui / non / sans objet | | |
| Poids | oui / non | | |

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
| Priorité | Objectif | Date | Chrono visé (ou « sans chrono ») | Verdict |
|---|---|---|---|---|
| A | | | | |

Verdict du calendrier entier : …

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
| Sport | LTHR | Facile | Seuil | Au-dessus | Source de la LTHR | Confiance |
|---|---|---|---|---|---|---|
| Course | | | | | | |
| Vélo | | | | | | |

Source : précise et jamais vide (course et date, test et date, séances au seuil et leurs dates, efforts de la vitesse critique et leurs dates, « estimation Garmin »). Valeur remplacée : ancienne → nouvelle et raison au journal des décisions du Plan.

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
## Imprévus ouverts (relus avant toute séance proposée)
| Depuis | Imprévu | Feu ou symptômes | Conduite en cours | Clôture quand |
|---|---|---|---|---|
| | | | | |

Dernière séance analysée : <date> (check, bilan ou bilan de course ; le check suivant n'analyse que les séances clés postérieures)

## Plan macro
| Bloc | Semaines | Phase | Qualité principale | Volume/sem. |
|---|---|---|---|---|

Calcul de la sortie longue : départ <durée> (sortie du <date>) · <n> hausses, <m> semaines allégées · pic <durée> (borne : 1,10 × / plafond 05.3 / contrainte). Le bloc détaillé et les bilans suivent ce calcul ; un changement passe par une correction validée.

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

Y figurent aussi : les imprévus ouverts et clos (avec leur date de clôture), chaque « choix de l'athlète contre l'avis du coach » (le choix, le coût redit, la raison de l'athlète), chaque correction d'une valeur validée (ancienne → nouvelle, raison) et chaque « question sur le référentiel » (règle, problème, à transmettre à qui tient le référentiel).
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
