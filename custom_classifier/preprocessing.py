import re
import unicodedata
from typing import List


def normalize_text(text: str) -> str:
    """
    Аккуратно нормализует OCR-текст:
    - сохраняет пробелы между словами,
    - исправляет типичные OCR-подмены,
    - убирает шум и невидимые символы,
    - не разрушает структуру документа.
    """
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"[\u200b\u200e\u200f\u2060]+", "", text)
    replacements = {
        "0": "o",
        "1": "i",
        "3": "e",
        "4": "a",
        "5": "s",
        "6": "g",
        "8": "b",
        "9": "g",
        "@": "a",
        "$": "s",
        "€": "e",
        "|": "i",
    }
    for wrong, right in replacements.items():
        text = text.replace(wrong, right)

    text = re.sub(r"[^\w\s.,:/\-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip().lower()

    return text
def generate_substrings(word: str, max_gap: int = 2) -> List[str]:
    """
    Разбивает слово на подстроки (для случая 'invoi ce', 'com mercial').
    Пример: 'invoice' -> ['invoice', 'invo ice', 'inv oice']
    """
    substrings = [word]
    for i in range(1, len(word)):
        if i <= max_gap:
            substrings.append(word[:i] + " " + word[i:])
    return substrings
