import json
import re

notebook_path = '/Users/alessandropausilli/Downloads/NYT/big data final.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if 'plotly' in source.lower() or 'plt.' in source.lower() or 'sns.' in source.lower():
            print(f"\n--- Cell {i} ---")
            print(source[:500]) # Print first 500 chars
            if 'plotly' in source.lower():
                print("[PLOTLY DETECTED]")
