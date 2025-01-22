| Column Name     | Data Type     | Description                                |
|-----------------|---------------|--------------------------------------------|
| template_id     | INTEGER (PK)  | Unique identifier for the template         |
| name            | TEXT          | Template name (e.g., "corporate")          |
| header_logo     | TEXT          | URL or base64-encoded image for logo       |
| header_naming   | TEXT          | Header title or naming convention          |
| header_colors   | JSON          | JSON object for header color scheme        |
| footer_data     | JSON          | JSON object for footer information         |
| font_family     | TEXT          | Font family for the template               |
| font_size       | INTEGER       | Default font size                          |
| text_colors     | JSON          | JSON object for title/text colors          |
