# Скрипты

## 11. Скрипты без полноценного проекта

Иногда у вас есть один файл, и создавать проект не хочется.

### Скрипт без зависимостей

Файл `hello.py`:

```python
print("Hello from uv")
```

Запуск:

```bash
uv run hello.py
```

### Скрипт со стандартной библиотекой

Файл `home.py`:

```python
from pathlib import Path

print(Path.home())
```

Запуск:

```bash
uv run home.py
```

Ничего устанавливать не нужно, потому что `pathlib` входит в стандартную библиотеку Python.

### Скрипт с временной зависимостью

Файл `progress.py`:

```python
import time
from rich.progress import track

for i in track(range(10), description="Working"):
    time.sleep(0.1)
```

Запуск:

```bash
uv run --with rich progress.py
```

Минус подхода: зависимость указана в команде, а не в файле. Через неделю можно забыть, что нужно добавить `--with rich`.

Если вы запускаете такой файл из папки, где уже есть `pyproject.toml`, `uv run` добавит зависимости текущего проекта. Если скрипт должен быть полностью независимым от проекта, используйте `--no-project` до имени файла:

```bash
uv run --no-project --with rich progress.py
```

Правило простое: флаги `uv run`, например `--no-project`, пишутся до имени скрипта.

### Скрипт с inline metadata

Лучше записать зависимости прямо в скрипт.

Создать скрипт с metadata:

```bash
uv init --script example.py --python 3.12
```

Добавить зависимость в скрипт:

```bash
uv add --script example.py requests rich
```

В файле появится специальный блок:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
#     "rich",
# ]
# ///

import requests
from rich.pretty import pprint

response = requests.get("https://peps.python.org/api/peps.json")
pprint(list(response.json().items())[:3])
```

Запуск:

```bash
uv run example.py
```

`uv` сам создаст временное изолированное окружение с нужными зависимостями.

### Важный нюанс про scripts внутри проекта

Если у скрипта есть inline metadata, `uv run script.py` запускает его в окружении скрипта, изолированном от зависимостей проекта.

Это хорошо: скрипт становится самодостаточным.

Для такого скрипта `--no-project` обычно не нужен: inline metadata уже говорит `uv`, что зависимости нужно брать из самого файла.

### Lock-файл для скрипта

Для скриптов lock-файл нужно создать явно:

```bash
uv lock --script example.py
```

Рядом появится:

```text
example.py.lock
```

### Исполняемый скрипт с shebang

Файл `greet`:

```python
#!/usr/bin/env -S uv run --script

print("Hello, world!")
```

Сделать исполняемым:

```bash
chmod +x greet
```

Запустить:

```bash
./greet
```

---

[К оглавлению](README.md) | [В начало проекта](../README.md)
