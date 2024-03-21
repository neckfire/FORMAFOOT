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


class Module:
    def __init__(self, module_data: dict):
        self.info_sup: dict = module_data.get('info_sup')  # Informations supplémentaires sur le module
        self.chapitres: List[Chapitre] = [Chapitre(chapitre_data) for chapitre_data in module_data.get('chapitres', [])]  # Liste des chapitres du module
        self.description: str = module_data.get('description')  # Description du module
        self.module_titre: str = module_data.get('module_titre')  # Titre du module

class Formation:
<<<<<<< Updated upstream
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

def print_document_counts(formation_instance):
    nombres_doc = 0
    for structure in formation_instance.structure:
        for chapitre in structure.chapitres:
            print("Chapter:", chapitre.chapitre_titre)
            for subchapitre in chapitre.subchapitre:
                print("Subchapter:", subchapitre.subchapitre_titre)
                print("Number of documents:", len(subchapitre.documents))
                nombres_doc += len(subchapitre.documents)
                print("-----------------------------")
    return nombres_doc

file_path = 'ressources/api object/api.json'
json_data = load_json(file_path)

formation_instance = Formation(json_data)
formation_instance.nb_doc = print_document_counts(formation_instance)
=======
    def __init__(self, formation_data: dict):
        self.prix: Optional[float] = formation_data.get('prix')  # Prix de la formation (optionnel)
        self.titre: str = formation_data.get('titre')  # Titre de la formation
        self.apports: str = formation_data.get('apports')  # Apports de la formation
        self.createur: Createur = Createur(formation_data.get('createur', {}))  # Créateur de la formation
        self.info_sup: dict = formation_data.get('info_sup')  # Informations supplémentaires sur la formation
        self.categorie: str = formation_data.get('categorie')  # Catégorie de la formation
        self.prerequis: str = formation_data.get('prerequis')  # Prérequis de la formation
        self.structure: List[Structure] = [Structure(structure_data) for structure_data in formation_data.get('structure', [])]  # Structure de la formation (liste de structures)
        self.type_forma: str = formation_data.get('type_forma')  # Type de la formation
        self.description: str = formation_data.get('description')  # Description de la formation
        self.financeable: Optional[bool] = formation_data.get('financeable')  # Indicateur de possibilité de financement (optionnel)
        self.texte_financeable: str = formation_data.get('texte_financeable')  # Texte sur la possibilité de financement
        self.duree = self.get_duration()  # Durée totale de la formation
        self.nb_doc: int = self.print_document_counts()
        self.modules: List[Module] = [Module(module_data) for module_data in formation_data.get('structure', [])]  # Liste des modules de la formation



    def get_duration(self):
        total_seconds = 0
        for structure in self.structure: 
            for chapitre in structure.chapitres:
                print("Chapter:", chapitre.chapitre_titre)
                for subchapitre in chapitre.subchapitre:
                    print("Subchapter:", subchapitre.subchapitre_titre)
                    for document in subchapitre.documents:
                        # Analyse de la durée de la chaîne en secondes
                        duration_str = document.duree
                        hours, minutes, seconds = map(int, duration_str.split(':'))
                        doc_seconds = hours * 3600 + minutes * 60 + seconds
                        total_seconds += doc_seconds
                        print("Document Duration:", doc_seconds,"seconds")
                    print("-----------------------------")

        total_hours, remaining_seconds = divmod(total_seconds, 3600)
        total_minutes, total_seconds = divmod(remaining_seconds, 60)
        print("Total duration of the formation:")
        print(f"{int(total_hours)}H, {int(total_minutes)}, {int(total_seconds)} seconds")
        total_duration = f"{int(total_hours)} H {int(total_minutes)}"
        return total_duration
    
    def print_document_counts(self):
        nombres_doc = 0
        for structure in self.structure:
            for chapitre in structure.chapitres:
                print("Chapter:", chapitre.chapitre_titre)
                for subchapitre in chapitre.subchapitre:
                    print("Subchapter:", subchapitre.subchapitre_titre)
                    print("Number of documents:", len(subchapitre.documents))
                    nombres_doc += len(subchapitre.documents)
                    print("-----------------------------")
        return nombres_doc
>>>>>>> Stashed changes
