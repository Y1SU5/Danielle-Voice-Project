import re

filepath = r"E:\python PRUEBAS D EVOZ\Lib\site-packages\fairseq\dataclass\configs.py"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace assignments of the form `name: Type = Type()` with `name: Type = field(default_factory=Type)`
# This fixes the ValueError: mutable default <class '...'> for field ... is not allowed
pattern = re.compile(r'^(\s+)(\w+):\s*([A-Z]\w*)\s*=\s*\3\(\)', re.MULTILINE)
new_content = pattern.sub(r'\1\2: \3 = field(default_factory=\3)', content)

# Check if 'field' is imported. If not, we might have issues, but it usually is in fairseq configs.py
if 'from dataclasses import' not in new_content and 'import field' not in new_content:
    new_content = "from dataclasses import field\n" + new_content

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("fairseq configs.py parched successfully!")
