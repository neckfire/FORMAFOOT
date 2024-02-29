import json
from typing import List
from fpdf import FPDF

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

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        # Set default font
        self.set_font('Arial', '', 12)
        # Set background color
        self.set_fill_color(240, 248, 255)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def header(self):
        # Set font
        self.set_font('Arial', 'B', 15)
        # Set fill color for title
        self.set_text_color(255, 255, 255)
        # Set background color for title
        self.set_fill_color(30, 144, 255)
        # Title
        self.cell(0, 10, 'Détails de la formation', border=1, ln=1, fill=True, align='C')
        # Set fill color for rest of the page
        self.set_fill_color(240, 248, 255)
        # Line break
        self.ln(20)

    def add_logo(self, logo_path, x, y, w, h):
        # Add logo
        self.image(logo_path, x=x, y=y, w=w, h=h)

    def add_text_block(self, text, x, y, w, h, border=0, align='L',size=12):
        self.set_xy(x, y)
        self.set_font('Arial', '', size)
        self.set_text_color(255, 255, 255)
        self.multi_cell(w, h, txt=text, border=border, align=align, fill=False)
        self.ln(h)
        self.set_fill_color(5, 75, 189)
        self.add_font("Graebenbach", "", "ressources/fonts/Graebenbach-Medium.otf", uni=True)
        self.set_font("Graebenbach")

def extract_details(formation_instance):
    #pdf.add_text_block(f"ID: {formation_instance.id}", x=5, y=5, w=0, h=6)
    #pdf.add_text_block(f"Prix: {formation_instance.prix}", x=10, y=160, w=0, h=6)
    #pdf.add_text_block(f"Créateur: {formation_instance.createur.nom} {formation_instance.createur.prenom}", x=10, y=160, w=0, h=6)
    #pdf.add_text_block(f"Catégorie: {formation_instance.categorie}", x=10, y=160, w=0, h=6)
    pdf.add_text_block(f"{formation_instance.description}", x=10, y=200, w=0, h=6, align='C', size=23)
    #pdf.add_text_block(f"Référence: {formation_instance.ref}", x=175, y=257, w=0, h=6)


def add_chapitre(pdf, chapitre, chapitreindex):
    pdf.add_page()
    pdf.add_logo(imageindex[i], x=0, y=0, w=210, h=297)
    pdf.chapter_title(chapitre.chapitre_titre)
    for subchapitre in chapitre.subchapitre:
        pdf.chapter_title(subchapitre.subchapitre_titre)
        for doc in subchapitre.documents:
            pdf.chapter_body(f"Document ID: {doc.id}\nType: {doc.type}\nDescription: {doc.description}\n")

pdf = PDF()
i=0
imageindex=("ressources/back/1.png","ressources/back/3.png","ressources/back/2.png","ressources/back/3.png")
pdf.add_page()
pdf.add_logo(imageindex[i], x=0, y=0, w=210, h=297)
pdf.add_text_block(formation_instance.titre, x=10, y=150, w=0, h=20, border=1, align='C', size=40)
extract_details(formation_instance)

#pdf.image('ressources/images/bandeau_white.png', x=10, y=100, w=200, h=60)
#for structure in formation_instance.structure:
#    for chapitre in structure.chapitres:
#        add_chapitre(pdf, chapitre, i)

i+=1
pdf.add_page()
pdf.add_logo(imageindex[i], x=0, y=0, w=210, h=297)
pdf.add_text_block("Finançable: " + str(formation_instance.financeable),x=15,y=40, w=80,h=20, border=0, align='C',size=20)
pdf.add_text_block("Prix: " + str(formation_instance.prix),x=115,y=80, w=80,h=20, border=0, align='C',size=20)
pdf.add_text_block("Durée totale: " + str(16),x=7,y=130, w=80,h=20, border=0, align='C',size=20)
pdf.add_text_block("Pré-requis: \n " + str(formation_instance.prerequis),x=118,y=168, w=76,h=14, border=1, align='C',size=15)




pdf_output_path = 'formation_details.pdf'
pdf.output(pdf_output_path)
print(f"PDF generated successfully: {pdf_output_path}")