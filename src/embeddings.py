from sklearn.feature_extraction.text import TfidfVectorizer

def create_embeddings(documents):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)
    return vectors, vectorizer
