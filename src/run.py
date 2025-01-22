import json
from services.pdf_service import generate_pdf


def main():
  fake_data_file = 'src/static/fake_data/fake_data.json'
  template_json_path = 'src/static/fake_data/fake_template.json'

  with open(fake_data_file, "r") as f:
    fake_data = json.load(f)

  output_pdf = "test_report"
  try:
    pdf_path = generate_pdf(
        filename=output_pdf,
        raw_json=fake_data,
        structure="standard",
        template_name="corporate",
        json_path=template_json_path
    )
    print(f"PDF generated successfully: {pdf_path}")
  except Exception as e:
    print(f"An error occurred while generating the PDF: {e}")


if __name__ == "__main__":
  main()
