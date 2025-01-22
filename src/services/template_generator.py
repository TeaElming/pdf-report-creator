import json
import base64
import io
from PIL import Image as PILImage


class TemplateGenerator:
  def __init__(self, json_path):
    """
    Initialize the TemplateGenerator with the path to the JSON file.
    """
    self.json_path = json_path

  def fetch_template(self, template_name):
    """
    Fetch template data by template name from the JSON file.
    """
    with open(self.json_path, "r") as file:
      templates = json.load(file)

    template_data = templates.get(template_name)
    if template_data:
      return self._parse_template_data(template_data)
    else:
      raise ValueError(
          f"Template '{template_name}' not found in the JSON file.")

  def _parse_template_data(self, template_data):
    """
    Parse template data into a usable configuration dictionary.
    If the header_logo is base64-encoded, decode it.
    """
    header_logo = template_data.get("header_logo")
    if header_logo and header_logo.startswith("data:image"):
      # Extract the base64 string and decode it
      header_logo = self._decode_base64_image(header_logo)

    return {
        "name": template_data.get("name", "default"),
        "header": {
            "logo": header_logo,
            "naming": template_data.get("header_naming"),
            "colors": template_data.get("header_colors", {})
        },
        "footer": template_data.get("footer_data", {}),
        "styling": {
            "font_family": template_data.get("font_family", "Helvetica"),
            "font_size": template_data.get("font_size", 12),
            "text_colors": template_data.get("text_colors", {})
        }
    }

  def _decode_base64_image(self, base64_image):
    """
    Decodes a base64 image string and returns a PIL Image.
    """
    image_data = base64_image.split(
        ",")[1]  # Remove prefix (e.g., data:image/png;base64,)
    img_bytes = base64.b64decode(image_data)
    return PILImage.open(io.BytesIO(img_bytes))
