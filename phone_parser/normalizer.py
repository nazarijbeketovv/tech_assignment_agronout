import re
from typing import Optional

class PhoneNormalizer:
    """
    Утилиты для нормализации телефонных строк в формат +7(YYY)XXX-XX-XX.
    """
    _DIGITS_RE = re.compile(r"\D+")

    @classmethod
    def normalize(cls, raw: str) -> Optional[str]:
        # Оставляем только цифры
        digits = cls._DIGITS_RE.sub("", raw)

        # Приводим к 11 цифрам: заменяем 8→7 или добавляем 7
        if len(digits) == 11 and digits.startswith("8"):
            digits = "7" + digits[1:]
        elif len(digits) == 10:
            digits = "7" + digits

        if not (len(digits) == 11 and digits.startswith("7")):
            return None

        c, area, part1, part2, part3 = (
            digits[0], digits[1:4], digits[4:7], digits[7:9], digits[9:11]
        )
        return f"+{c}({area}){part1}-{part2}-{part3}"