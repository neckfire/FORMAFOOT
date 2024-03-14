import json
from typing import List, Optional

class Document:
    def __init__(self, document_data: dict):
        self.file: str = document_data.get('file')
        self.type: str = document_data.get('type')
        self.duree: str = document_data.get('duree')
class SubChapitre:
    def __init__(self, subchapitre_data: dict):
        self.info_sup: dict = subchapitre_data.get('info_sup')
        self.documents: List[Document] = [Document(doc_data) for doc_data in subchapitre_data.get('documents', [])]
        self.description: str = subchapitre_data.get('description')
        self.subchapitre_titre: str = subchapitre_data.get('subchapitre_titre')
class Chapitre:
    def __init__(self, chapitre_data: dict):
        self.info_sup: dict = chapitre_data.get('info_sup')
        self.chapitre_titre: str = chapitre_data.get('chapitre_titre')
        self.subchapitre: List[SubChapitre] = [SubChapitre(sub_data) for sub_data in chapitre_data.get('subchapitre', [])]
class Structure:
    def __init__(self, structure_data: dict):
        self.info_sup: dict = structure_data.get('info_sup')
        self.chapitres: List[Chapitre] = [Chapitre(chap_data) for chap_data in structure_data.get('chapitres', [])]

class Createur:
    def __init__(self, createur_data: dict):
        self.nom: str = createur_data.get('nom')
        self.prenom: str = createur_data.get('prenom')

class Formation:
    def __init__(self, formation_data: dict):
        self.prix: Optional[float] = formation_data.get('prix')
        self.titre: str = formation_data.get('titre')
        self.apports: str = formation_data.get('apports')
        self.createur: Createur = Createur(formation_data.get('createur', {}))
        self.info_sup: dict = formation_data.get('info_sup')
        self.categorie: str = formation_data.get('categorie')
        self.prerequis: str = formation_data.get('prerequis')
        self.structure: List[Structure] = [Structure(structure_data) for structure_data in formation_data.get('structure', [])]
        self.type_forma: str = formation_data.get('type_forma')
        self.description: str = formation_data.get('description')
        self.financeable: Optional[bool] = formation_data.get('financeable')
        self.texte_financeable: str = formation_data.get('texte_financeable')
        self.duree = self.get_duration()
    
    def get_duration(self):
        total_seconds = 0
        for structure in self.structure: 
            for chapitre in structure.chapitres:
                print("Chapter:", chapitre.chapitre_titre)
                for subchapitre in chapitre.subchapitre:
                    print("Subchapter:", subchapitre.subchapitre_titre)
                    for document in subchapitre.documents:
                        # Parse duration string into seconds
                        duration_str = document.duree
                        hours, minutes, seconds = map(int, duration_str.split(':'))
                        doc_seconds = hours * 3600 + minutes * 60 + seconds
                        total_seconds += doc_seconds
                        print("Document Duration:", doc_seconds, "seconds")
                    print("-----------------------------")

        total_hours, remaining_seconds = divmod(total_seconds, 3600)
        total_minutes, total_seconds = divmod(remaining_seconds, 60)
        print("Total duration of the formation:")
        print(f"{int(total_hours)}H, {int(total_minutes)}, {int(total_seconds)} seconds")
        total_duration = f"{int(total_hours)} H {int(total_minutes)}"
        return total_duration


class Module:
    def __init__(self, module_data: dict):
        self.info_sup: dict = module_data.get('info_sup')
        self.chapitres: List[Chapitre] = [Chapitre(chapitre_data) for chapitre_data in module_data.get('chapitres', [])]
        self.description: str = module_data.get('description')
        self.module_titre: str = module_data.get('module_titre')

def load_json(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)

def print_document_counts(formation_instance: Formation) -> int:
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

file_path: str = 'ressources/api object/api.json'
json_data: dict = load_json(file_path)

formation_instance: Formation = Formation(json_data)
formation_instance.nb_doc: int = print_document_counts(formation_instance)
