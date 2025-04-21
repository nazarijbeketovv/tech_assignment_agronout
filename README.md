# 📞 Phone Parser

[![Python](https://img.shields.io/badge/python->=3.11-blue.svg)]

CLI-инструмент для **извлечения** и **нормализации** российских телефонных номеров из любых текстовых файлов.

---

## 🚀 Возможности

- 🔍 Поиск телефоноподобных фрагментов в многомегабайтных текстах
- 🔄 Нормализация в единый формат: `+7(YYY)XXX-XX-XX`
- 📜 Асинхронное чтение файлов для высокой производительности

---

## 📖 Содержание

1. [Требования](#-требования)
2. [Установка](#-установка)
3. [Быстрый старт](#-быстрый-старт)
4. [Использование](#-использование)
5. [Структура проекта](#-структура-проекта)


---

## 🛠️ Требования

- Python **>=3.11**
- Платформа: Linux/Mac/Windows

---

## ⚙️ Установка

```bash
# Клонируем репозиторий
git clone https://github.com/nazarijbeketovv/tech_assignment_agronout.git
cd tech_assignment_agronout

# Cоздаём виртуальное окружение
python3.11 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Устанавливаем зависимости
pip install -e .
```

---

## 🎬 Быстрый старт

1. Подготовьте файл с текстом (`input.txt`):
    ```txt
    Связаться можно по +7 912-345-67-89 или 8 (495) 123 45 67.
    WhatsApp: +7(903)4567890
    ```

2. Запустите CLI-команду:
    ```bash
    parse input.txt
    ```

3. Вывод:
    ```text
    +7(912)345-67-89
    +7(495)123-45-67
    +7(903)456-78-90
    ```

---

## 🧩 Использование как модуль

Если хотите использовать API внутри кода:

```python
from phone_parser.extractor import PhoneExtractor

text = open("test.txt", encoding="utf-8").read()
extractor = PhoneExtractor()
numbers = extractor.extract(text)
print(numbers)
# ['+7(912)345-67-89', '+7(495)123-45-67', ...]
```

---

## 📂 Структура проекта

```
phone_parser/           # Пакет
├── __init__.py            # Версия и экспорт
├── normalizer.py          # Логика нормализации
├── extractor.py           # Поиск и извлечение
├── io_utils.py            # Асинхронное I/O
└── cli.py                 # CLI-интерфейс

pyproject.toml             # Метаданные проекта
requirements.txt           # Список зависимостей
README.md                  # Эта документация
```

---

