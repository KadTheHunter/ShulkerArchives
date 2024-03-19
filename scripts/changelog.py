import csv

changelog = []
with open('changelog.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        author = row[1]
        category = row[4]
        entryType = row[5]
        entry = f'- _{name}_ by _{author}_ in _{category}_'
        changelog.append((entryType, entry))

entryTypes = {}
for entryType, entry in changelog:
    if entryType not in entryTypes:
        entryTypes[entryType] = []
    entryTypes[entryType].append(entry)

for entryType, entries in entryTypes.items():
    print(entryType)
    for entry in entries:
        print(entry)
