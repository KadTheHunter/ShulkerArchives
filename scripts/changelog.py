import csv

changelog = []
with open('changelog.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name = row[0]
        author = row[1]
        category = row[4]
        entryType = row[5]
        entry = f'- _{name}_ by _{author}_ in _{category}_'
        changelog.append((entryType, entry, category))

entryTypes = {}
for entryType, entry, category in changelog:
    if entryType not in entryTypes:
        entryTypes[entryType] = []
    entryTypes[entryType].append((entry, category))

for entryType, entries in entryTypes.items():
    print(entryType)
    for entry, category in entries:
        if category != "Collections":
            print(entry)

collections_entries = [(entry, category) for entryType, entries in entryTypes.items() for entry, category in entries if category == "Collections"]
print("Collections")
for entry, category in collections_entries:
    print(entry)
