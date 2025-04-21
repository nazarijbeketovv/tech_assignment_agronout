import asyncio
import click
from pathlib import Path
from loguru import logger
from .io_utils import process_file

@click.command(name="phone-extractor")
@click.argument(
    "file", type=click.Path(exists=True, path_type=Path)
)
def main(file: Path) -> None:
    """
    CLI для извлечения номеров из текстового файла.
    """
    logger.info(f"Начало обработки: {file}")
    numbers = asyncio.run(process_file(file))
    for num in numbers:
        click.echo(num)