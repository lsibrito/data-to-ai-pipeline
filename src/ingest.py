def load_documents(path):
    with open(path, "r", encoding="utf-8") as file:
        docs = file.readlines()
    return [doc.strip() for doc in docs]
