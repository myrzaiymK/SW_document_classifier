import json
import os

def load_document_terms(file_path: str = None):
    """
    Загружает словарь терминов из JSON файла.
    По умолчанию ищет в app/data/document_terms.json
    """
    if not file_path:
        base_dir = os.path.dirname(os.path.dirname(__file__))  # /app
        file_path = os.path.join(base_dir, "data", "document_terms.json")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Не найден файл с терминами: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
