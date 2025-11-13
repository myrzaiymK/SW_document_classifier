from collections import defaultdict
from typing import Dict, List

from custom_classifier.preprocessing import generate_substrings


def build_inverted_index(terms: Dict[str, List[str]]) -> Dict[str, set]:
    index = defaultdict(set)
    for doc_type, keywords in terms.items():
        for keyword in keywords:
            for variant in generate_substrings(keyword.replace(" ", "")):
                index[variant.lower()].add(doc_type)
            index[keyword.lower()].add(doc_type)
    return index
