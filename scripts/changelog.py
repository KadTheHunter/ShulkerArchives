import csv


def generate_changelog(version):  # noqa F402

    changelog = []  # noqa F402
    archivist_picks = []
    with open('changelog.csv', 'r', encoding='utf-8') as f:  # noqa F402
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            name = row[0]
            author = row[1]
            notes = row[3]
            category = row[4]
            entry_type = row[5]
            entry = f'- _{name}_ by _{author}_ in _{category}_'
            changelog.append((entry_type, entry, category))

            if notes and "Archivist Pick" in notes:
                archivist_picks.append(entry)

    entry_types = {}
    for entry_type, entry, category in changelog:
        if entry_type not in entry_types:
            entry_types[entry_type] = []
        entry_types[entry_type].append((entry, category))

    output = [
        "---\n",
        "layout: single\n",
        f"title: \"v{version} Release\"\n",
        "toc: true\n",
        "toc_sticky: true\n",
        "toc_label: Table of Contents\n",
        "toc_icon: scroll\n",
        "---\n",
        "*Looking for file downloads? [Jump to the bottom!](#download)*\n",
        "{: .notice--primary}\n\n",
        "# Summary / Notes\n",
        "In total there are now X Entries and X Collections.\n\n",
    ]

    ordered_sections = ["Kit", "Item", "Book"]

    for section in ordered_sections:
        if section in entry_types:
            section_entries = [e for e, cat in entry_types[section] if cat != "Collections"]
            count = len(section_entries)
            output.extend([
                f"# {section}s\n",
                f"{count} {section.lower()}{'s' if count != 1 else ''} were added.\n\n",
                "## Added\n"
            ])
            for entry in section_entries:
                output.append(f"{entry}\n")
            output.append("\n")
            output.append("***\n\n")

    collections_entries = [
        (entry, category)
        for entry_type in entry_types.values()
        for entry, category in entry_type
        if category == "Collections"
    ]

    if collections_entries:
        collection_count = len(collections_entries)
        entry_count = sum(1 for _ in entry_types.get("Item", []) if _[1] == "Collections")
        output.extend([
            "# Collections\n",
            f"{collection_count} collection{'s' if collection_count != 1 else ''} were added, with {entry_count} entr{'ies' if entry_count != 1 else 'y'}.\n\n",  # noqa: E501
            "## Added\n"
        ])
        for entry, _ in collections_entries:
            output.append(f"{entry}\n")
        output.append("\n")
        output.append("***\n\n")

    if archivist_picks:
        output.extend([
            "# Archivist Picks\n",
            f"{len(archivist_picks)} entries were flagged as Archivist Picks, and copied to the AP racks.\n\n"
        ])

        archivist_picks_by_type = {}
        for entry_type in ["Kit", "Item", "Book"]:
            if entry_type in entry_types:
                archivist_picks_by_type[entry_type] = [
                    entry for entry, _ in entry_types[entry_type]
                    if entry in archivist_picks
                ]

        for entry_type, picks in archivist_picks_by_type.items():
            if picks:
                output.append(f"### {entry_type}s\n")
                for pick in picks:
                    output.append(f"{pick}\n")
                output.append("\n")

        output.append("\n")
        output.append("***\n\n")

    output.extend([
        "# Build Changes\n\n",
        "# Organization/Display Changes\n\n",
        "# Download\n",
        f'[v{version}]({{{{ site.baseurl }}}}/releases/v{version}/TheShulkerArchives_v{version}.zip){{: .align-center .btn .btn--success .btn--x-large style="width: 70%;"}}\n',  # noqa: E501
        f'[Mirror (GitHub)](https://github.com/KadTheHunter/ShulkerArchives/releases/tag/v{version}){{: .align-center .btn .btn--success .btn--x-large style="width: 70%;"}}\n'  # noqa: E501
    ])

    flat_output = []
    for item in output:
        if isinstance(item, list):
            flat_output.extend(item)
        else:
            flat_output.append(item)

    return "".join(flat_output)


if __name__ == "__main__":
    version = input("Enter the version number (e.g. 1.0.0): ").strip()
    changelog = generate_changelog(version)
    print("\n" + "=" * 50 + "\n")
    print(changelog)
    save = input("\nWould you like to save this to CHANGELOG.md? (y/n): ").strip().lower()
    if save == 'y':
        with open('CHANGELOG.md', 'w', encoding='utf-8') as f:
            f.write(changelog)
        print("Changelog saved to CHANGELOG.md")
