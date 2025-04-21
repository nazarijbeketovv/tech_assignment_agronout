import re
from typing import List, Pattern
from .normalizer import PhoneNormalizer

class PhoneExtractor:
    """
    Ищет и извлекает уникальные телефонные номера из текста.
    """
    def __init__(self) -> None:
        self._seen: set[str] = set()
        # Шаблон: старт цифрой или '+', далее цифры и разделители
        self._pattern: Pattern[str] = re.compile(r"[\+\d][\d\-\.\(\)\s]{6,}\d")

    def extract(self, text: str) -> List[str]:
        results: List[str] = []
        for m in self._pattern.finditer(text):
            norm = PhoneNormalizer.normalize(m.group(0))
            if norm and norm not in self._seen:
                self._seen.add(norm)
                results.append(norm)
        return results