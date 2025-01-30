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
        .folder-spacing { margin-bottom: 20px; }
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
        
        # Sort the filenames alphabetically
        filenames.sort()
        
        # Add serial number to files and display them
        serial_number = 1
        for filename in filenames:
            # Only include PDF files
            if filename.endswith('.pdf'):
                file_path = os.path.join(foldername, filename)
                html_content += f'<li>{serial_number}. <a href="{file_path.replace("\\", "/")}">{filename}</a></li>'
                serial_number += 1
        
        html_content += "</ul></li>"
        # Add one line spacing between folders
        html_content += "<li class='folder-spacing'></li>"
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

