import json

notebook_path = '/Users/alessandropausilli/Downloads/NYT/big data final.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell.get('outputs'):
        has_image = any('image/png' in output.get('data', {}) for output in cell['outputs'])
        has_html = any('text/html' in output.get('data', {}) for output in cell['outputs'])
        
        if has_image or has_html:
            source = ''.join(cell['source'])[:100].replace('\n', ' ')
            print(f"Cell {i} [Img:{has_image} HTML:{has_html}]: {source}")
