from fpdf import FPDF
from back import formation_instance
from math import ceil

<<<<<<< Updated upstream

class PDF(FPDF):
    def __init__(self):
        super().__init__()
=======
class PDF(FPDF):
    def __init__(self, formation: Formation):
        super().__init__()
        self.formation_instance = formation
        self.imageindex=("ressources/back/1.png","ressources/back/3.png","ressources/back/2.png","ressources/back/3.png","ressources/images/sticker_round.png")
        self.set_y=40
>>>>>>> Stashed changes
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
        self.image(logo_path, x=x, y=y, w=w, h=h)

    def add_text_block(self, text, x, y, w, h, border=0, align='L',size=12):
        self.add_font("mediasans","", "ressources/fonts/mediasans-regular.otf", uni=True)
        self.set_font('mediasans', '', size)
        self.set_text_color(255, 255, 255)
        self.multi_cell(w, h, txt=text, border=border, align=align, fill=False)
        self.ln(h)
        self.set_fill_color(5, 75, 189)
        #self.add_font("Graebenbach", "", "ressources/fonts/Graebenbach-Medium.otf", uni=True)
        #self.set_font("Graebenbach")

<<<<<<< Updated upstream
def extract_details(formation_instance):
    #pdf.add_text_block(f"ID: {formation_instance.id}", x=5, y=5, w=0, h=6)
    #pdf.add_text_block(f"Prix: {formation_instance.prix}", x=10, y=160, w=0, h=6)
    #pdf.add_text_block(f"Créateur: {formation_instance.createur.nom} {formation_instance.createur.prenom}", x=10, y=160, w=0, h=6)
    #pdf.add_text_block(f"Catégorie: {formation_instance.categorie}", x=10, y=160, w=0, h=6)
    pdf.add_text_block(f"{formation_instance.description}", x=10, y=200, w=0, h=6, align='C', size=23)
    #pdf.add_text_block(f"Référence: {formation_instance.ref}", x=175, y=257, w=0, h=6)
=======
    def create_pdf(self):
        i=0
        self.add_page()
        self.add_logo(self.imageindex[i], x=0, y=0, w=210, h=297)
        self.add_text_block(self.formation_instance.titre, x=10, y=150, w=0, h=20, border=1, align='C', size=40)
        self.extract_details()
        i+=1
        self.add_page()
        self.add_logo(self.imageindex[i], x=0, y=0, w=210, h=297)
        self.add_text_block("Finançable: " + str(self.formation_instance.financeable),x=15,y=40, w=80,h=20, border=0, align='C',size=20)
        self.add_text_block("Prix: " + str(self.formation_instance.prix),x=115,y=80, w=80,h=20, border=0, align='C',size=20)
        self.add_text_block("Durée totale:\n" + str(self.formation_instance.duree),x=7,y=120, w=80,h=20, border=0, align='C',size=20)
        self.set_fill_color(4, 74, 189)
        #Rect(float x, float y, float w, float h [, string style])
        self.rect(x=118,y=168, w=76,h=ceil((self.get_string_width(str(self.formation_instance.prerequis))/76))*15,style='F')
        self.add_text_block("Pré-requis: \n " + str(self.formation_instance.prerequis),x=118,y=168, w=76,h=14, border=0, align='C',size=15)
        self.add_text_block("Nombre de documents: \n " + str(self.formation_instance.nb_doc),x=7,y=225, w=80,h=10, border=0, align='C',size=15)
        self.add_page_nb(2)
        i+=1
        self.add_page()
        self.add_logo(self.imageindex[i], x=0, y=0, w=210, h=297)
        self.listeverything()

    def extract_details(self):
        #pdf.add_text_block(f"ID: {formation_instance.id}", x=5, y=5, w=0, h=6)
        #pdf.add_text_block(f"Prix: {formation_instance.prix}", x=10, y=160, w=0, h=6)
        #pdf.add_text_block(f"Créateur: {formation_instance.createur.nom} {formation_instance.createur.prenom}", x=10, y=160, w=0, h=6)
        #pdf.add_text_block(f"Catégorie: {formation_instance.categorie}", x=10, y=160, w=0, h=6)
        self.add_text_block(f"{self.formation_instance.description}", x=10, y=200, w=0, h=6, align='C', size=23)
        #pdf.add_text_block(f"Référence: {formation_instance.ref}", x=175, y=257, w=0, h=6)

    def add_page_nb(self, nbpage: int):
        self.add_logo(self.imageindex[4], x=85,y=262,w=30,h=30)
        self.add_text_block(str(nbpage), x=90,y=275,w=20,h=2, border=0, align='C',size=7)
>>>>>>> Stashed changes


def add_chapitre(pdf, chapitre, chapitreindex):
    pdf.add_page()
    pdf.add_logo(imageindex[i], x=0, y=0, w=210, h=297)
    pdf.chapter_title(chapitre.chapitre_titre)
    for subchapitre in chapitre.subchapitre:
        pdf.chapter_title(subchapitre.subchapitre_titre)
        for doc in subchapitre.documents:
            pdf.chapter_body(f"Document ID: {doc.id}\nType: {doc.type}\nDescription: {doc.description}\n")

<<<<<<< Updated upstream

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
pdf.set_fill_color(4, 74, 189)
#Rect(float x, float y, float w, float h [, string style])
pdf.rect(x=118,y=168, w=76,h=ceil((pdf.get_string_width(str(formation_instance.prerequis))/76))*15,style='F')
pdf.add_text_block("Pré-requis: \n " + str(formation_instance.prerequis),x=118,y=168, w=76,h=14, border=0, align='C',size=15)
pdf.add_text_block("Nombre de documents: \n " + str(formation_instance.nb_doc),x=7,y=225, w=80,h=10, border=0, align='C',size=15)
=======
    def listeverything(self):
        print("test")
        if self.set_y>250:
           self.set_y=40
           self.add_page()
        for module in self.formation_instance.modules:
            print("test2")
            self.add_text_block("Module: \n " + str(module.module_titre), x = 10, y = self.set_y, w=80,h=30, border=0, align='C',size=15)
            self.set_y += 15
            if self.set_y>250:
               self.set_y = 40
               self.add_page()
            for chapitre in module.chapitres:
               self.add_text_block("Chapitre: \n " + str(chapitre.chapitre_titre), x = 40, y = self.set_y, w=85,h=20, border=0, align='C',size=15)
               self.set_y += 15
               if self.set_y>250:
                   self.set_y=40
                   self.add_page()
               for sub in chapitre.subchapitre:
                   self.add_text_block("Sous-chapitres: \n " + str(sub.subchapitre_titre), x = 70, y = self.set_y, w=90,h=14, border=0, align='C',size=15)
                   self.set_y += 15
                   if self.set_y>250:
                       self.set_y=40
                       self.add_page()
                   for document in sub:
                       self.add_text_block("Documents: \n " + str(len(sub.documents)), document, x = 100, y = self.set_y, w=100,h=12, border=0, align='C',size=15)
                       self.set_y += 15
                       if self.set_y>250:
                           self.set_y=40
                           self.add_page()
                
    # def listeverything(self, formation_instance):
    #     self.add_page()
    #     y = 20  # Starting y position
    #     for module in formation_instance.modules:
    #         self.set_font('Arial', 'B', 12)
    #         self.cell(0, 10, f'Module: {module.module_titre}', 0, 1, 'L')
    #         for chapitre in module.chapitres:
    #             self.set_font('Arial', 'B', 10)
    #             self.cell(0, 10, f'Chapitre: {chapitre.chapitre_titre}', 0, 1, 'L')
    #             for subchapitre in chapitre.subchapitre:
    #                 self.set_font('Arial', 'I', 10)
    #                 self.cell(0, 10, f'Sous-chapitre: {subchapitre.subchapitre_titre}', 0, 1, 'L')
    #                 for document in subchapitre.documents:
    #                     self.set_font('Arial', '', 10)
    #                     self.cell(0, 10, f'Document: {document.file}', 0, 1, 'L')
    #     self.output('formation_details.pdf')
>>>>>>> Stashed changes
