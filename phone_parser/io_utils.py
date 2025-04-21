import asyncio
from pathlib import Path
from typing import List
from loguru import logger
from .extractor import PhoneExtractor

async def read_file(path: Path) -> str:
    logger.debug(f"Чтение файла {path}")
    return await asyncio.to_thread(path.read_text, encoding="utf-8", errors="ignore")

async def process_file(path: Path) -> List[str]:
    text = await read_file(path)
    extractor = PhoneExtractor()
    return extractor.extract(text)