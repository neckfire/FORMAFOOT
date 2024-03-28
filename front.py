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
        self.cell(0, 10, 'Détails de la formation', border=0, ln=1, fill=True, align='C')
        # Set fill color for rest of the page
        self.set_fill_color(240, 248, 255)
        # Line break
        self.ln(20)

    def add_logo(self, logo_path, x, y, w, h):
        self.image(logo_path, x=x, y=y, w=w, h=h)

    def add_text_block(self, text, x, y, w, h, border=0, align='L', size=12):
        self.set_xy(x, y)
        self.set_font('Arial', '', size)
        self.set_text_color(255, 255, 255)
        self.multi_cell(w, h, txt=text, border=border, align=align, fill=False)
        self.ln(h)
        self.set_fill_color(5, 75, 189)

    def create_pdf(self):
        for i in range(3):
            self.add_page()
            self.add_logo(self.imageindex[i], x=0, y=0, w=210, h=297)
            if i == 0:
                self.add_text_block(self.formation_instance.titre, x=10, y=150, w=0, h=20, border=0, align='C', size=40)
                self.extract_details()
            elif i == 1:
                self.add_page_details()
            else:
                self.add_page_3()

    def extract_details(self):
        self.add_text_block(f"{self.formation_instance.description}", x=10, y=200, w=0, h=6, align='C', size=23)

    def add_page_details(self):
        self.add_text_block("Finançable: " + str(self.formation_instance.financeable), x=15, y=40, w=80, h=20, border=0,
                            align='C', size=20)
        self.add_text_block("Prix: " + str(self.formation_instance.prix), x=115, y=80, w=80, h=20, border=0,
                            align='C', size=20)
        self.add_text_block("Durée totale:\n" + str(self.formation_instance.duree), x=7, y=120, w=80, h=20, border=0,
                            align='C', size=20)
        self.set_fill_color(4, 74, 189)
        self.rect(x=118, y=168, w=76, h=ceil((self.get_string_width(str(self.formation_instance.prerequis)) / 76)) * 15,
                style='F')
        self.add_text_block("Pré-requis: \n " + str(self.formation_instance.prerequis), x=118, y=168, w=76, h=14,
                            border=0, align='C', size=15)
        self.add_text_block("Nombre de documents: \n " + str(self.formation_instance.nb_doc), x=7, y=225, w=80, h=10,
                            border=0, align='C', size=15)
        self.add_page_nb(2)

    def add_page_nb(self, nbpage: int):
        self.add_logo(self.imageindex[4], x=85, y=262, w=30, h=30)
        self.add_text_block(str(nbpage), x=90, y=275, w=20, h=2, border=0, align='C', size=7)

    def add_page_3(self):
        i=3
        current_height = self.get_y()
        print(current_height)
        max_height = self.h - 100

        for module in self.formation_instance.modules:
            print(module.module_titre)
            module_lines = 2  # Titre du module et sa description
            self.add_text_block(module.module_titre, x=10, y=current_height, w=0, h=10, border=0, align='L', size=14)
            current_height += 10
            self.add_text_block(module.description, x=10, y=current_height, w=0, h=6, align='L', size=12)
            module_lines += module.description.count('\n') + 1
            current_height += 24

            for chapitre in module.chapitres:
                print(chapitre.chapitre_titre)
                chapitre_lines = 2  # Titre du chapitre et sa description
                self.add_text_block(chapitre.chapitre_titre, x=20, y=current_height, w=0, h=10, border=0, align='L', size=14)
                current_height += 10
                self.add_text_block(chapitre.description, x=20, y=current_height, w=0, h=6, align='L', size=12)
                chapitre_lines += chapitre.description.count('\n') + 1
                current_height += 24

                for subchapitre in chapitre.subchapitres:
                    print(subchapitre.subchapitre_titre)
                    subchapitre_lines = 2  # Titre du sous-chapitre et sa description
                    self.add_text_block(subchapitre.subchapitre_titre, x=30, y=current_height, w=0, h=10, border=0, align='L', size=14)
                    current_height += 10
                    self.add_text_block(subchapitre.description, x=30, y=current_height, w=0, h=6, align='L', size=12)
                    subchapitre_lines += subchapitre.description.count('\n') + 1
                    current_height += 12

                    for document in subchapitre.documents:
                        self.add_text_block("Nombre de documents : " + str(self.formation_instance.nb_doc), x=40, y=current_height, w=0, h=6, align='L', size=12)
                        doc_lines = str(self.formation_instance.nb_doc).count('\n') + 1
                        current_height += doc_lines * 12  # Height per line multiplied by number of lines

                        if current_height > max_height:
                            self.add_page_nb(i)
                            i+=1
                            self.add_page()
                            self.add_logo(self.imageindex[2], x=0, y=0, w=210, h=297)
                            current_height = self.get_y()

                    current_height += subchapitre_lines  # Height per line multiplied by number of lines

                current_height += chapitre_lines  # Height per line multiplied by number of lines

            current_height += module_lines  # Height per line multiplied by number of lines
            self.add_page_nb(i)
