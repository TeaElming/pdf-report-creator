from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import base64
import io
from PIL import Image as PILImage
from services.data_structures import DataExtractor


def generate_pdf(filename, raw_json, structure="standard"):
  """
  Generates a PDF using extracted data from raw JSON input.
  """
  # Dynamically select the extraction method, these names will have to be udpated later on to fit the existing ones
  if structure == "standard":
    extracted_data = DataExtractor.extract_standard(raw_json)
  elif structure == "alternative":
    extracted_data = DataExtractor.extract_alternative(raw_json)
  else:
    raise ValueError(f"Unsupported structure type: {structure}")

  file_path = f"{filename}.pdf"
  doc = SimpleDocTemplate(file_path, pagesize=A4)
  styles = getSampleStyleSheet()
  story = []  # Holds content for the PDF

  # Add Report Title and Description
  story.append(Paragraph(extracted_data["report_title"], styles["Title"]))
  story.append(Spacer(1, 12))
  story.append(
      Paragraph(extracted_data["report_description"], styles["BodyText"]))
  story.append(Spacer(1, 24))

  # Process Each Section in 'contents'
  for section in extracted_data["contents"]:
    # Add Section Title
    story.append(Paragraph(section["title"], styles["Heading2"]))
    story.append(Spacer(1, 12))

    # Add Section Text
    story.append(Paragraph(section["text"], styles["BodyText"]))
    story.append(Spacer(1, 12))

    # Add Section Description
    story.append(Paragraph(section["description"], styles["Italic"]))
    story.append(Spacer(1, 12))

    # Add Base64 Images
    for img_data in section["base64imgs"]:
      # Decode the base64 image
      img_bytes = base64.b64decode(img_data)
      img = PILImage.open(io.BytesIO(img_bytes))
      img_path = f"temp_{section['title'].replace(' ', '_')}.png"
      img.save(img_path)  # Save temporarily
      story.append(Image(img_path, width=400, height=300))
      story.append(Spacer(1, 24))

  # Build the PDF
  doc.build(story)
  return file_path
