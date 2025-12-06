import json
import base64
import os

notebook_path = '/Users/alessandropausilli/Downloads/NYT/big data final.ipynb'
output_dir_images = '/Users/alessandropausilli/Downloads/NYT/images'
output_dir_graphs = '/Users/alessandropausilli/Downloads/NYT/graphs'

os.makedirs(output_dir_images, exist_ok=True)
os.makedirs(output_dir_graphs, exist_ok=True)

with open(notebook_path, 'r') as f:
    nb = json.load(f)

print(f"Processing {len(nb['cells'])} cells...")

image_count = 0
html_count = 0

for i, cell in enumerate(nb['cells']):
    if cell.get('outputs'):
        for output in cell['outputs']:
            # Extract Images (PNG)
            if 'data' in output and 'image/png' in output['data']:
                image_data = output['data']['image/png']
                image_bytes = base64.b64decode(image_data)
                image_filename = f"plot_cell_{i}_{image_count}.png"
                image_path = os.path.join(output_dir_images, image_filename)
                with open(image_path, 'wb') as img_f:
                    img_f.write(image_bytes)
                print(f"Saved image: {image_filename}")
                image_count += 1
            
            # Extract Interactive Graphs (HTML)
            if 'data' in output and 'text/html' in output['data']:
                html_content = output['data']['text/html']
                # Sometimes html content is a list of strings
                if isinstance(html_content, list):
                    html_content = ''.join(html_content)
                
                # Check if it looks like a plotly graph or significant HTML
                if 'plotly' in html_content or '<div' in html_content:
                     html_filename = f"graph_cell_{i}_{html_count}.html"
                     html_path = os.path.join(output_dir_graphs, html_filename)
                     with open(html_path, 'w') as html_f:
                         html_f.write(html_content)
                     print(f"Saved HTML: {html_filename}")
                     html_count += 1

print(f"Extraction complete. {image_count} images and {html_count} HTML files saved.")
