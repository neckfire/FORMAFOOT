from front import PDF
from back import Formation
import json


def load_json(file_path: str) -> dict:
    with open(file_path, 'r', encoding="UTF8") as file:
        return json.load(file)

file_path: str = 'ressources/api object/api.json'
json_data: dict = load_json(file_path)

formation_instance: Formation = Formation(json_data)
pdf = PDF(formation_instance)
pdf.create_pdf()
pdf_output_path = 'formation_details.pdf'
pdf.output(pdf_output_path)
print(f"PDF generated successfully: {pdf_output_path}")