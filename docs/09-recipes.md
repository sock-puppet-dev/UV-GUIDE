# Практические рецепты

## 15. Практические рецепты

### Рецепт 1: новый учебный проект

```bash
uv init hello-uv
cd hello-uv
uv run main.py
uv add requests
uv run python -c "import requests; print(requests.__version__)"
```

Что вы получите:

- проект;
- `.venv`;
- `pyproject.toml`;
- `uv.lock`;
- установленный `requests`.

### Рецепт 2: проект с тестами

```bash
uv init calc-app
cd calc-app
uv add --dev pytest
```

Создайте файл `test_calc.py`:

```python
def add(a: int, b: int) -> int:
    return a + b


def test_add():
    assert add(2, 3) == 5
```

Запустите:

```bash
uv run pytest
```

### Рецепт 3: проект с Ruff

```bash
uv add --dev ruff
uv run ruff check .
uv run ruff format .
```

Если хотите сделать `ruff` частью проекта, добавляйте его как dev-зависимость, а не только через `uvx`.

### Рецепт 4: быстрый одноразовый запуск Ruff

```bash
uvx ruff check .
```

Подходит, если вы не хотите менять проект.

### Рецепт 5: FastAPI-приложение

```bash
uv init fastapi-demo
cd fastapi-demo
uv add fastapi uvicorn
```

`main.py`:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from uv and FastAPI"}
```

Запуск:

```bash
uv run uvicorn main:app --reload
```

### Рецепт 6: миграция с `requirements.txt` в проект uv

Допустим, есть:

```text
requirements.txt
```

Создайте `pyproject.toml` в текущей папке:

```bash
uv init
```

Добавьте зависимости:

```bash
uv add -r requirements.txt
```

Проверьте:

```bash
uv sync
uv run python -c "print('ok')"
```

После этого основной источник зависимостей - `pyproject.toml`, а точные версии - `uv.lock`.

### Рецепт 7: оставить старый workflow на `requirements.txt`

```bash
uv venv
uv pip install -r requirements.txt
uv run python main.py
```

Для более строгого воспроизведения:

```bash
uv pip sync requirements.txt
```

### Рецепт 8: скрипт с зависимостями прямо в файле

```bash
uv init --script fetch.py --python 3.12
uv add --script fetch.py requests rich
uv run fetch.py
```

Такой файл проще отправить другому человеку: зависимости описаны внутри скрипта.

### Рецепт 9: подготовить проект после `git clone`

```bash
git clone https://github.com/example/project
cd project
uv sync
uv run pytest
```

Если в проекте есть `uv.lock`, зависимости установятся в зафиксированных версиях.

### Рецепт 10: CI-проверка lock-файла

```bash
uv lock --check
uv run --locked pytest
```

Если кто-то изменил `pyproject.toml`, но не обновил `uv.lock`, CI это поймает.

---

[К оглавлению](README.md) | [В начало проекта](../README.md)
