import os
import re

directory = r"E:\python PRUEBAS D EVOZ\Lib\site-packages\hydra\conf"
pattern = re.compile(r'^(\s+)(\w+):\s*([A-Z]\w*)\s*=\s*\3\(\)', re.MULTILINE)

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".py"):
            filepath = os.path.join(root, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            if pattern.search(content):
                new_content = pattern.sub(r'\1\2: \3 = field(default_factory=\3)', content)
                
                # Check if field is imported
                if 'from dataclasses import' not in new_content and 'import field' not in new_content:
                    new_content = "from dataclasses import field\n" + new_content
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Patched {filepath}")

print("Hydra configs patched successfully!")
