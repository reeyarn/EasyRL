from easyrl import parse_label_linkbase, Roles

# Get documentation
filename = "us-gaap-doc-2020-01-31.xml"
path = "/tmp/us-gaap-2020-01-31/elts/"
docs = parse_label_linkbase(path + filename)

for i, (concept, doc) in enumerate(docs.items()):
    print(f"{i}: {concept}: {doc}")
    if i > 32:
        break


# Get display labels
labels = parse_label_linkbase(path + 'us-gaap-lab-2020-01-31.xml', role=Roles.LABEL)


for i, (concept, label) in enumerate(labels.items()):
    print(f"{i}: {concept}: {label}")
    if i > 32:
        break