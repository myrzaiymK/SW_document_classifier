from collections import Counter
from custom_classifier.indexing import build_inverted_index
from custom_classifier.utils import load_document_terms


def local_document_classifier(text: str) -> dict:
    document_terms = load_document_terms()  # 🔹 загружаем из файла
    inverted_index = build_inverted_index(document_terms)

    counts = Counter()
    for term, types in inverted_index.items():
        if term in text:
            for t in types:
                counts[t] += 1

    total_matches = sum(counts.values())
    if not total_matches:
        return {"use_llm": True, "top_type": "Other", "confidence": 0.0, "candidates": []}

    top_type, top_count = counts.most_common(1)[0]
    confidence = top_count / total_matches

    return {
        "use_llm": confidence < 0.7,
        "top_type": top_type,
        "confidence": round(confidence, 3),
        "candidates": [doc for doc, _ in counts.most_common(10)]
    }
