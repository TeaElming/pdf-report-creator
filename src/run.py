import json
from services.pdf_service import generate_pdf


def main():
  # Load fake data
  fake_data_file = 'src/static/fake_data/fake_data.json'
  with open(fake_data_file, "r") as f:
    fake_data = json.load(f)

    # Specify the output PDF file name
    output_pdf = "test_report"
    # Generate the PDF using the standard structure
    try:
      pdf_path = generate_pdf(output_pdf, fake_data, structure="standard")
      print(f"PDF generated successfully: {pdf_path}")
    except Exception as e:
      print(f"An error occurred while generating the PDF: {e}")


if __name__ == "__main__":
  main()
