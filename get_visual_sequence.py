import json

notebook_path = '/Users/alessandropausilli/Downloads/NYT/big data final.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

visual_sequence = []

print("--- VISUAL SEQUENCE ---")

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and cell.get('outputs'):
        for output in cell['outputs']:
            if 'data' in output:
                print(f"Cell {i} data keys: {list(output['data'].keys())}")
                if 'image/png' in output['data']:
                    visual_sequence.append({'type': 'image', 'cell_index': i})
                elif 'text/html' in output['data']:
                    visual_sequence.append({'type': 'html', 'cell_index': i})

for i, item in enumerate(visual_sequence):
    print(f"{i}: {item['type']} (Cell {item['cell_index']})")
