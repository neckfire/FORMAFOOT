import json
from typing import List

class Document:
    def __init__(self, document_data):
        self.id = document_data.get('id')
        self.file = document_data.get('file')
        self.type = document_data.get('type')
        self.duree = document_data.get('duree')
        self.creation = document_data.get('creation')
        self.info_sup = document_data.get('info_sup')
        self.description = document_data.get('description')
        self.telechargeable = document_data.get('telechargeable')

class SubChapitre:
    def __init__(self, subchapitre_data):
        self.id = subchapitre_data.get('id')
        self.ordre = subchapitre_data.get('ordre')
        self.creation = subchapitre_data.get('creation')
        self.info_sup = subchapitre_data.get('info_sup')
        self.documents = [Document(doc_data) for doc_data in subchapitre_data.get('documents', [])]
        self.description = subchapitre_data.get('description')
        self.subchapitre_titre = subchapitre_data.get('subchapitre_titre')

class Chapitre:
    def __init__(self, chapitre_data):
        self.id = chapitre_data.get('id')
        self.ordre = chapitre_data.get('ordre')
        self.creation = chapitre_data.get('creation')
        self.info_sup = chapitre_data.get('info_sup')
        self.chapitre_titre = chapitre_data.get('chapitre_titre')
        self.chapitre_is_completed = chapitre_data.get('chapitre_is_completed')
        self.subchapitre = [SubChapitre(sub_data) for sub_data in chapitre_data.get('subchapitre', [])]

class Structure:
    def __init__(self, structure_data):
        self.id = structure_data.get('id')
        self.ordre = structure_data.get('ordre')
        self.creation = structure_data.get('creation')
        self.info_sup = structure_data.get('info_sup')
        self.chapitres = [Chapitre(chap_data) for chap_data in structure_data.get('chapitres', [])]

class Createur:
    def __init__(self, createur_data):
        self.nom = createur_data.get('nom')
        self.prenom = createur_data.get('prenom')

class Formation:
    def __init__(self, formation_data):
        self.id = formation_data.get('id')
        self.ref = formation_data.get('ref')
        self.avis = formation_data.get('avis', [])
        self.prix = formation_data.get('prix')
        self.tags = formation_data.get('tags', [])
        self.photo = formation_data.get('photo')
        self.titre = formation_data.get('titre')
        self.apports = formation_data.get('apports')
        self.createur = Createur(formation_data.get('createur', {}))
        self.creation = formation_data.get('creation')
        self.info_sup = formation_data.get('info_sup')
        self.categorie = formation_data.get('categorie')
        self.is_active = formation_data.get('is_active')
        self.prerequis = formation_data.get('prerequis')
        self.structure = [Structure(structure_data) for structure_data in formation_data.get('structure', [])]
        self.type_forma = formation_data.get('type_forma')
        self.description = formation_data.get('description')
        self.financeable = formation_data.get('financeable')
        self.is_completed = formation_data.get('is_completed')
        self.caroussel_accueil = formation_data.get('caroussel_accueil')
        self.texte_financeable = formation_data.get('texte_financeable')
        self.formation_percentage_completed = formation_data.get('formation_percentage_completed')

class Module:
    def __init__(self, module_data):
        self.id = module_data.get('id')
        self.ordre = module_data.get('ordre')
        self.creation = module_data.get('creation')
        self.info_sup = module_data.get('info_sup')
        self.chapitres = [Chapitre(chapitre_data) for chapitre_data in module_data.get('chapitres', [])]
        self.description = module_data.get('description')
        self.module_titre = module_data.get('module_titre')
        self.module_is_completed = module_data.get('module_is_completed')
        self.module_percentage_completed = module_data.get('module_percentage_completed')

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

file_path = 'ressources/api object/api.json'
json_data = load_json(file_path)

formation_instance = Formation(json_data)
