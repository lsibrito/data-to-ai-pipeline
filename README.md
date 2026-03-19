<div align="center">
  <img src="logo.png" alt="Leonardo Brito Logo" width="120"/>
  <h1>🤖 Data to AI Pipeline (RAG Simples)</h1>
</div>

---

# Pipeline de Dados e IA com Python e Scikit-Learn

## 🎯 O Objetivo
Criei este projeto para entender e simular o funcionamento interno de um sistema **RAG (Retrieval-Augmented Generation)** construído "do zero". A ideia foi criar um fluxo de dados completo para IA sem depender de bibliotecas de alto nível (como LangChain), passando pela ingestão de documentos, vetorização matemática e um sistema de busca por similaridade.

Meu foco aqui foi entender a engenharia por trás da pergunta: *"Como a IA encontra o contexto exato em uma base de dados local para responder a uma pergunta de forma precisa?"*.

## 🛠 O que eu usei (Tech Stack)
Para focar nos fundamentos do Processamento de Linguagem Natural (NLP) e matemática de vetores dentro do ecossistema Python:
* [cite_start]**Python 3.x:** Linguagem base para orquestração[cite: 2].
* [cite_start]**Scikit-Learn:** Utilizado para transformar textos em vetores (`TfidfVectorizer`) e calcular a similaridade de cossenos (`cosine_similarity`)[cite: 1].
* **PyCharm:** IDE utilizada para desenvolvimento, refatoração e gestão do ambiente virtual.

## 🚀 Como o projeto funciona
O pipeline é modular e o script `main.py` integra as seguintes etapas:

1.  [cite_start]**Ingestão (`ingest.py`):** Carrega a base de conhecimento a partir do arquivo `documents.txt`[cite: 5].
2.  [cite_start]**Embeddings (`embeddings.py`):** Transforma os textos em representações numéricas (vetores)[cite: 3].
3.  **Busca (`search.py`):** Compara a pergunta do usuário com a base de dados para encontrar o trecho mais relevante.
4.  **Geração (`rag.py`):** Estrutura a resposta final baseada no contexto recuperado.

## 📂 Estrutura do Projeto (PyCharm)
```text
data-to-ai-pipeline/
├── src/
│   ├── ingest.py
│   ├── embeddings.py
│   ├── search.py
│   └── rag.py
├── data/
│   └── documents.txt
├── main.py
└── requirements.txt