import os
import re

directory = r"E:\python PRUEBAS D EVOZ\Lib\site-packages\fairseq"

# Buscar:  variable: Tipo = Tipo()
pattern = re.compile(r'^(\s+)(\w+):\s*([A-Za-z_]\w*)\s*=\s*\3\(\)', re.MULTILINE)

count = 0
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".py"):
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                # Solo modificar si el archivo usa dataclasses
                if 'dataclass' in content and pattern.search(content):
                    new_content = pattern.sub(r'\1\2: \3 = field(default_factory=\3)', content)
                    
                    # Asegurar la importación de field
                    if 'from dataclasses import' not in new_content and 'import field' not in new_content:
                        new_content = "from dataclasses import field\n" + new_content
                    
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Patched: {filepath}")
                    count += 1
            except Exception as e:
                print(f"Error procesando {filepath}: {e}")

print(f"--- TOTAL DE ARCHIVOS FAIRSEQ PARCHEADOS: {count} ---")
