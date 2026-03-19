from src.ingest import load_documents
from src.embeddings import create_embeddings
from src.search import search
from src.rag import generate_answer

docs = load_documents("data/documents.txt")
vectors, vectorizer = create_embeddings(docs)

question = input("Digite sua pergunta: ")
context = search(question, vectors, vectorizer, docs)
answer = generate_answer(context)

print("\n", answer)
