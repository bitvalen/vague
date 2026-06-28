import json
import time
import sys

def run(ext_json, inst_path, theme_id, theme_name, action="install"):
    print(f"  [INFO] Reading {ext_json}")
    try:
        with open(ext_json, "r") as f:
            exts = json.load(f)
    except FileNotFoundError:
        exts = []
        
    print(f"  [INFO] Found {len(exts)} existing extension(s)")

    # Clean out any old/stale entries for this theme
    exts = [e for e in exts if e.get("identifier", {}).get("id") != theme_id]

    if action == "install":
        new_entry = {
            "identifier": {"id": theme_id},
            "version": "0.0.1",
            "location": {"$mid": 1, "path": inst_path, "scheme": "file"},
            "relativeLocation": theme_name,
            "metadata": {
                "installedTimestamp": int(time.time() * 1000),
                "source": "local",
                "isBuiltin": False,
                "isMachineScoped": False,
                "isApplicationScoped": False
            }
        }
        exts.append(new_entry)
        print(f"  [INFO] Appending new entry:")
        print(f"           id       : {theme_id}")
        print(f"           path     : {inst_path}")
        print(f"           timestamp: {new_entry['metadata']['installedTimestamp']}")
    elif action == "uninstall":
        print(f"  [OK] Removed entry for '{theme_id}'")

    with open(ext_json, "w") as f:
        json.dump(exts, f, indent=2)
        
    print(f"  [OK] extensions.json updated ({len(exts)} extension(s) remaining/total)")

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: script.py <ext_json> <inst_path> <theme_id> <theme_name> <install|uninstall>")
        sys.exit(1)
    run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])