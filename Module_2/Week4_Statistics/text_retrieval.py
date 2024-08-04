import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Question 10:
vi_data_df = pd.read_csv('Module_2/Week4_Statistics/data/vi_text_retrieval.csv')
context = vi_data_df['text']
context = [doc.lower() for doc in context]

tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)

vector_8 = context_embedded.toarray()[7][0]
print(f"Vector của tài liệu thứ 8, từ đầu tiên: {vector_8}")

# Question 11:


def tfidf_search(question, tfidf_vectorizer, top_d=5):
    # Chuyển câu hỏi thành vector TF-IDF
    query_embedded = tfidf_vectorizer.transform([question.lower()])

    # Tính toán cosine similarity giữa vector của câu hỏi và ma trận TF-IDF của tài liệu
    cosine_scores = cosine_similarity(
        query_embedded, tfidf_vectorizer.transform(context)).flatten()

    # Lấy top k cosine scores và chỉ số của chúng
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc_score)

    return results


# Ví dụ sử dụng
question = vi_data_df.iloc[0]['question']
print(question)
results = tfidf_search(question, tfidf_vectorizer, top_d=5)
print(results[1]['cosine_score'])
