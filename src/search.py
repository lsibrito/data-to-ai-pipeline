from sklearn.metrics.pairwise import cosine_similarity

def search(query, vectors, vectorizer, documents):
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, vectors)[0]
    best_index = similarities.argmax()
    return documents[best_index]
