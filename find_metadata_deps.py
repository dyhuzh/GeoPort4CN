"""
扫描当前 Python 环境中所有已安装包，找出在任意 __init__.py 中
调用 importlib.metadata.version() 的包。
PyInstaller 打包时需要对这些包加 --copy-metadata <name>。

用法：
  conda activate geoport4cn
  python find_metadata_deps.py
"""
import importlib.metadata
import re
import pathlib

pattern = re.compile(
    r'importlib[._]metadata.*?version\s*\('
    r'|from\s+importlib[._]metadata\s+import.*?version'
)

needs_copy = []

for dist in importlib.metadata.distributions():
    name = dist.name
    if not dist.files:
        continue
    for f in dist.files:
        if f.name != '__init__.py':
            continue
        try:
            # Use absolute path to read — avoids PackagePath.read_text() compat issues
            abs_path = pathlib.Path(str(f))
            if not abs_path.is_absolute():
                # Resolve relative to the dist's location
                abs_path = dist.locate_file(f)
            text = abs_path.read_text(encoding='utf-8', errors='ignore')
            if pattern.search(text):
                needs_copy.append(name)
                break
        except Exception:
            pass

print("# Add these to your PyInstaller command:")
for pkg in sorted(set(needs_copy)):
    print(f"    --copy-metadata {pkg} \\")
