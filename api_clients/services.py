import re
import requests
import json
from config import DIFY_API_KEY, WORKFLOW_URL


def dify_classify(text: str) -> dict:
    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": {
            "text": text
        },
        "response_mode": "blocking",
        "user": "python-backend"
    }

    try:
        response = requests.post(
            WORKFLOW_URL,
            headers=headers,
            data=json.dumps(payload),
            timeout=60
        )
        if response.status_code != 200:
            return {"error": f"Dify error {response.status_code}", "details": response.text}

        data = response.json()
        outputs = data.get("data", {}).get("outputs", {})
        if "text" in outputs and isinstance(outputs["text"], str):
            text = outputs["text"]
            # убираем ```json ... ``` обертку
            text = re.sub(r"```json|```", "", text).strip()
            try:
                parsed = json.loads(text)
                outputs = parsed  # подменяем outputs настоящим словарём
            except json.JSONDecodeError:
                pass

        result = {
            "source": "local",
            "type": outputs.get("type", "Unknown"),
            "confidence": outputs.get("confidence", 0.0),
            "elapsed_time": data.get("data", {}).get("elapsed_time", 0.0)}
        return result

    except Exception as e:
        return {
                "source": "dify",
                "error": "Workflow request failed",
                "details": str(e),
            }

