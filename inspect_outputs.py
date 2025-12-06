import json

notebook_path = '/Users/alessandropausilli/Downloads/NYT/big data final.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")

for i, cell in enumerate(nb['cells']):
    if cell.get('outputs'):
        print(f"\n--- Cell {i} Outputs ---")
        for output in cell['outputs']:
            print(f"Type: {output.get('output_type')}")
            if 'data' in output:
                print(f"Data keys: {list(output['data'].keys())}")
