class DataExtractor:
  """
  A class to handle different data structures and extract relevant information.
  """

  @staticmethod
  def extract_standard(raw_json):
    """
    Extracts data for the standard report structure.
    """
    extracted_data = {
        "report_title": raw_json.get("report_title", "Default Report Title"),
        "report_description": raw_json.get("report_description", "Default Report Description"),
        "contents": [],
    }

    # Process sections in 'contents'
    raw_contents = raw_json.get("contents", {})
    for section_key, section in raw_contents.items():
      extracted_section = {
          "title": section.get("title", "Untitled Section"),
          "text": section.get("text", "No text provided."),
          "description": section.get("description", ""),
          "base64imgs": section.get("base64imgs", []),
      }
      extracted_data["contents"].append(extracted_section)

    return extracted_data

  @staticmethod
  def extract_alternative(raw_json):
    """
    Extracts data for an alternative report structure (example).
    """
    extracted_data = {
        "header": raw_json.get("header", "Default Header"),
        "footer": raw_json.get("footer", "Default Footer"),
        "sections": [],
    }

    # Process sections in 'sections'
    raw_sections = raw_json.get("sections", {})
    for section_key, section in raw_sections.items():
      extracted_section = {
          "heading": section.get("heading", "Default Heading"),
          "content": section.get("content", "Default Content"),
          "images": section.get("images", []),
      }
      extracted_data["sections"].append(extracted_section)

    return extracted_data
