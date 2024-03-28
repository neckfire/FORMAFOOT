# Automatisation PDF - FORMAFOOT

Bienvenue dans le projet d'automatisation PDF FORMAFOOT !

![Bandeau FORMAFOOT](ressources\images\bandeau_dakr.png)

## Objectif

L'objectif est d'automatiser la construction de brochures PDF pour présenter les programmes de formation de FORMAFOOT.

## Contenu

- **Ressources Images**
- **Exemples de Design**
- **api.json**
- **Dossier de Polices**
- **main.py** (Fichier essentiel à l'exécution du code)

## Fonctionnalités

- Page 1 : Titre et Description du Programme de Formation
- Page 2 : Informations Générales
- Pages 3 et suivantes : Détails du Programme de Formation avec Modules, Chapitres, Sous-chapitres et Documents

## Détails Techniques

- **Langage** : Python 3.10
- **Bibliothèque** : fpdf2==2.7.7, defusedxml==0.7.1, fonttools==4.49.0, fpdf2==2.7.7, pillow==10.2.0
- **Approche** : Programmation Orientée Objet

## Contact
- Marc GARNIER DE BOISGROLLIER  - marc.garnier-de-boisgrollier.edu@groupe-gema.com
- Housni MZE ALI - housni.mze-ali.edu@groupe-gema.com
- Bradley DOMINGOS - bradley.domingos.edu@groupe-gema.com
---
- Remi BAREILLE - remi.bareille.int@groupe-gema.com
- Bastien ANGELOZ - bastien.angeloz.int@groupe-gema.com

Le PDF généré, `formation_details.pdf`, présentera les détails du programme de formation FORMAFOOT de manière structurée.

*Automatisez la création de brochures PDF avec style !*

À partir de ce readme, et de ce code :

```python
from back import Formation
from fpdf import FPDF
from math import ceil

class PDF(FPDF):
    def __init__(self, formation: Formation):
        super().__init__()
        self.documents_count = 0
        self.formation_instance = formation
        self.imageindex = ("ressources/back/1.png", "ressources/back/3.png", "ressources/back/2.png", "ressources/back/3.png",
                           "ressources/images/sticker_round.png")

        # Définir la police par défaut
        self.set_font('Arial', '', 12)
        # Définir la couleur de fond
        self.set_fill_color(240, 248, 255)

    # Autres méthodes telles que définies dans votre code fourni...
```

Et cette image :
`ressources\images\bandeau_dakr.png`

Voici un readme de haute qualité avec des blocs de code présentant certaines fonctionnalités :

### Code pour la Génération de PDF :

```python
from back import Formation
from fpdf import FPDF
from math import ceil

class PDF(FPDF):
    # Votre définition de classe PDF telle que fournie...
```

### Exemples de Définitions de Classes :

```python
from typing import List, Optional
from datetime import timedelta

class Document:
    # Définition de classe Document...

class SubChapitre:
    # Définition de classe SubChapitre...

class Chapitre:
    # Définition de classe Chapitre...

class Module:
    # Définition de classe Module...

class Createur:
    # Définition de classe Createur...

class Formation:
    # Définition de classe Formation...
```

Cette structure améliore la lisibilité et facilite la compréhension de l'objectif et de la fonctionnalité de votre projet.


