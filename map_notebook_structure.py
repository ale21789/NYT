import json
import os

notebook_path = '/Users/alessandropausilli/Downloads/NYT/big data final.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

image_count = 0
html_count = 0

current_markdown = []

print("--- NOTEBOOK STRUCTURE MAPPING ---")

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        source = ''.join(cell['source']).strip()
        if source:
            current_markdown.append(source)
    
    elif cell['cell_type'] == 'code':
        has_output = False
        files_generated = []
        
        if cell.get('outputs'):
            for output in cell['outputs']:
                # Check for Images
                if 'data' in output and 'image/png' in output['data']:
                    filename = f"images/plot_cell_{i}_{image_count}.png"
                    files_generated.append(filename)
                    image_count += 1
                    has_output = True
                
                # Check for HTML
                if 'data' in output and 'text/html' in output['data']:
                    html_content = output['data']['text/html']
                    if isinstance(html_content, list):
                        html_content = ''.join(html_content)
                    
                    if 'plotly' in html_content or '<div' in html_content:
                        filename = f"graphs/graph_cell_{i}_{html_count}.html"
                        files_generated.append(filename)
                        html_count += 1
                        has_output = True
        
        if has_output:
            print(f"\n[CELL {i}]")
            if current_markdown:
                print("DESCRIPTION:")
                print('\n'.join(current_markdown))
                current_markdown = [] # Reset after consuming for a visual
            else:
                print("DESCRIPTION: (No preceding markdown)")
            
            print("VISUALS:")
            for f in files_generated:
                print(f"- {f}")
