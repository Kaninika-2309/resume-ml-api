from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_score(resume, job):
    embeddings = model.encode([resume, job])
    score = util.cos_sim(embeddings[0], embeddings[1])
    return round(float(score[0][0]) * 100, 2)