import os
documents = []
folder = "Semantic_Search/documents"

files = os.listdir(folder)

for file in files:
    path = os.path.join(folder,file)

    with open(path,"r") as f:
        content = f.read()

        documents.append(content)
        print(documents)

print(len(documents))        