import os

# Define the root folder for your papers
root_dir = "Hydrogen_Journals"
output_file = "index.html"

# HTML structure for the beginning of the page
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Journal Papers</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1, h2 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 5px 0; }
    </style>
</head>
<body>
    <h1>Journal Papers</h1>
    <p>Click on the links below to access the papers.</p>
"""

# Loop through all directories and files under root_dir
html_content += "<ul>"
for foldername, subfolders, filenames in os.walk(root_dir):
    folder_name = os.path.basename(foldername)  # Extract folder name
    if filenames:
        html_content += f"<li><strong>{folder_name}</strong><ul>"
        for filename in filenames:
            # Only include PDF files
            if filename.endswith('.pdf'):
                file_path = os.path.join(foldername, filename)
                html_content += f'<li><a href="{file_path.replace("\\", "/")}">{filename}</a></li>'
        html_content += "</ul></li>"
html_content += "</ul>"

# HTML structure for the end of the page
html_content += """
</body>
</html>
"""

# Write the HTML content to a file
with open(output_file, "w") as f:
    f.write(html_content)

print(f"index.html has been generated successfully.")
