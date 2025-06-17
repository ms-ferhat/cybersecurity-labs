import os

def generate_index(base_path='.'):
    platforms = ['TryHackMe', 'HackTheBox', 'BlueTeamLabs', 'CyberDefenders', 'Other']
    index_lines = ["# 🗂️ Lab Index\n"]

    for platform in platforms:
        platform_path = os.path.join(base_path, platform)
        if not os.path.isdir(platform_path):
            continue

        index_lines.append(f"\n## 📚 {platform}\n")

        for lab in sorted(os.listdir(platform_path)):
            lab_path = os.path.join(platform_path, lab)
            readme_path = os.path.join(platform_path, lab, 'README.md')
            if os.path.isdir(lab_path) and os.path.exists(readme_path):
                rel_path = os.path.relpath(readme_path, base_path).replace("\\", "/")
                index_lines.append(f"- [{lab}]({rel_path})")

    with open(os.path.join(base_path, "_index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines))

    print("✅ _index.md generated successfully.")

if __name__ == "__main__":
    generate_index()
