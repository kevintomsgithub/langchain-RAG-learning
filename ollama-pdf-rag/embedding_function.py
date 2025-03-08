from langchain_ollama import OllamaEmbeddings

# from langchain_community.embeddings.ollama import OllamaEmbeddings


def get_embedding_function():
    embed = OllamaEmbeddings(model="deepseek-r1")
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embed
