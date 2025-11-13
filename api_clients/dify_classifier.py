from custom_classifier.classifier import local_document_classifier
from .services import dify_classify

class DocumentClassifier:
    def classify_text(self, text: str) -> dict:
        """Комбинированная классификация: сначала по K/W, потом Dify при необходимости."""
        local_result = local_document_classifier(text)

        if not local_result["use_llm"]:
            # локальная классификация достаточно уверенная
            return {
                "source": "local",
                "type": local_result["top_type"],
                "confidence": round(local_result["confidence"], 2),
                "elapsed_time": 0.0,
            }

        # иначе — отправляем запрос в Dify
        dify_result = dify_classify(text)
        return dify_result



