import os
import re

intro = """# Cybersecurity Lab

This repository contains solutions to various blue team and general cybersecurity labs from platforms like TryHackMe, Hack The Box, Blue Team Labs Online, and CyberDefenders.

## 🧠 Categories
- 🔵 Blue Team (SIEM, Threat Hunting, DFIR)
- 🛡️ Red Team (Exploitation, Enumeration)
- 🌐 Web Security (XSS, SQLi)
- 🔍 Forensics & Reverse Engineering
- 📚 Other (General Cybersecurity)"""
def generate_index(base_path='.'):
    platforms = ['TryHackMe', 'HackTheBox', 'BlueTeamLabs', 'CyberDefenders', 'Other']
    index_lines = [intro ]

    for platform in platforms:
        platform_path = os.path.join(base_path, platform)
        if not os.path.isdir(platform_path):
            continue

        index_lines.append(f"\n##  {platform}\n")

        for lab in sorted(os.listdir(platform_path)):
            lab_path = os.path.join(platform_path, lab)
            readme_path = os.path.join(platform_path, lab, 'README.md')
            if os.path.isdir(lab_path) and os.path.exists(readme_path):
                rel_path = os.path.relpath(readme_path, base_path).replace("\\", "/")
                index_lines.append(f"- [{lab}]({rel_path})")

    # Write to _index.md
    with open(os.path.join(base_path, "_index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines))

    print("✅ _index.md generated.")
    update_readme(base_path, index_lines)

def update_readme(base_path, index_lines):
    readme_path = os.path.join(base_path, "README.md")

    if not os.path.exists(readme_path):
        print("❌ README.md not found.")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- INDEX_START -->"
    end_marker = "<!-- INDEX_END -->"

    pattern = re.compile(
        f"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
        flags=re.DOTALL,
    )

    new_index_block = start_marker + "\n" + "\n".join(index_lines) + "\n" + end_marker
    if pattern.search(content):
        updated_content = pattern.sub(new_index_block, content)
    else:
        # If markers are not present, append to end
        updated_content = content.strip() + "\n\n" + new_index_block

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("✅ README.md updated with index.")

if __name__ == "__main__":
    generate_index()
