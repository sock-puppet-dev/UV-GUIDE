# Зависимости, lock, sync и run

## 8. Зависимости проекта

Зависимости нужно добавлять через `uv add`.

### Добавить обычную зависимость

```bash
uv add requests
```

Что произойдет:

1. `requests` добавится в `pyproject.toml`.
2. `uv.lock` обновится.
3. Пакет установится в `.venv`.

После этого в коде можно писать:

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
```

И запускать:

```bash
uv run main.py
```

### Добавить зависимость с ограничением версии

```bash
uv add "requests>=2.32,<3"
```

Так вы говорите: нужна версия `requests` от 2.32 включительно, но меньше 3.

### Добавить конкретную версию

```bash
uv add "requests==2.32.3"
```

Для новичков это нужно редко. Чаще лучше указывать разумный диапазон или позволить `uv` выбрать актуальную совместимую версию.

### Добавить зависимость из Git

```bash
uv add "httpx @ git+https://github.com/encode/httpx"
```

`uv` добавит обычную зависимость и отдельную запись в `[tool.uv.sources]`, где будет указан Git-источник.

Новичкам лучше использовать PyPI-пакеты, если нет явной причины брать пакет из Git.

### Добавить локальную зависимость

Например, если соседний проект лежит рядом:

```bash
uv add ../my-local-package
```

Если хотите editable-режим для локального проекта:

```bash
uv add --editable ../my-local-package
```

Editable означает: изменения в исходниках локального пакета видны без переустановки.

### Добавить dev-зависимость

Dev-зависимости нужны для разработки, но не являются обязательными для пользователей вашего проекта.

Примеры:

- `pytest` для тестов;
- `ruff` для проверки и форматирования;
- `mypy` для проверки типов.

Команда:

```bash
uv add --dev pytest ruff
```

В современном формате такие зависимости попадают в `dependency-groups`, обычно в группу `dev`.

Пример:

```toml
[dependency-groups]
dev = [
    "pytest>=8.0.0",
    "ruff>=0.11.0",
]
```

### Добавить зависимость в отдельную группу

Например, зависимости для документации:

```bash
uv add --group docs mkdocs mkdocs-material
```

Запустить окружение с этой группой:

```bash
uv sync --group docs
```

### Добавить optional dependency

Optional dependencies нужны библиотекам, у которых есть дополнительные возможности.

Пример: базовая библиотека работает без HTTP-клиента, но пользователь может установить extra `network`.

```bash
uv add httpx --optional network
```

В `pyproject.toml` появится примерно:

```toml
[project.optional-dependencies]
network = [
    "httpx>=0.28.0",
]
```

Пользователь сможет установить пакет с extra:

```bash
pip install "your-package[network]"
```

Внутри `uv` extra можно синхронизировать так:

```bash
uv sync --extra network
```

### Импортировать зависимости из `requirements.txt`

Если у вас уже есть файл:

```text
requirements.txt
```

то можно добавить зависимости в проект:

```bash
uv add -r requirements.txt
```

Если есть constraints:

```bash
uv add -r requirements.txt -c constraints.txt
```

### Удалить зависимость

```bash
uv remove requests
```

Для dev-зависимости:

```bash
uv remove --dev pytest
```

Для группы:

```bash
uv remove --group docs mkdocs
```

### Обновить одну зависимость в lock-файле

```bash
uv lock --upgrade-package requests
```

Обновить до конкретной версии:

```bash
uv lock --upgrade-package requests==2.32.3
```

### Обновить все зависимости в lock-файле

```bash
uv lock --upgrade
```

Важно: `uv` не обновляет зависимости только потому, что в интернете появились новые версии. Если версия уже зафиксирована в `uv.lock`, она остается прежней, пока вы явно не попросите обновление.

### Посмотреть дерево зависимостей

```bash
uv tree
```

Это помогает понять, какие пакеты установлены напрямую, а какие пришли как зависимости зависимостей.

### Проверить зависимости на уязвимости

В актуальном `uv` есть команда аудита зависимостей:

```bash
uv audit
```

Она проверяет зависимости проекта на известные уязвимости через сервис уязвимостей. Для такой проверки обычно нужен доступ в интернет.

Проверить без dev-зависимостей:

```bash
uv audit --no-dev
```

Проверить только dev-зависимости:

```bash
uv audit --only-dev
```

Проверить и не менять lock-файл:

```bash
uv audit --locked
```

Проверить PEP 723 script:

```bash
uv audit --script example.py
```

## 9. `uv.lock`, `uv sync` и воспроизводимость

### Что такое locking

Locking - процесс, при котором `uv` решает, какие точные версии пакетов подходят проекту, и записывает результат в `uv.lock`.

Команда:

```bash
uv lock
```

### Что такое syncing

Syncing - процесс, при котором `uv` устанавливает в `.venv` пакеты из `uv.lock`.

Команда:

```bash
uv sync
```

### В чем разница

| Команда | Что делает |
|---|---|
| `uv lock` | Обновляет `uv.lock` |
| `uv sync` | Устанавливает окружение по `uv.lock` и по умолчанию удаляет лишние пакеты |
| `uv run ...` | Перед запуском автоматически lock + sync, если нужно, но не делает точную очистку окружения |

### Почему `uv run` обычно достаточно

Когда вы выполняете:

```bash
uv run python main.py
```

`uv` сам проверяет:

- актуален ли `uv.lock`;
- актуальна ли `.venv`;
- установлены ли нужные зависимости.

Поэтому новичку не нужно каждый раз думать о ручной установке пакетов.

Но если в `.venv` случайно появились лишние пакеты, `uv run` обычно оставит их на месте. Для точной очистки выполните:

```bash
uv sync
```

### Когда использовать `uv sync`

Используйте `uv sync`, когда:

- вы только склонировали проект;
- хотите подготовить `.venv` для IDE;
- хотите явно привести окружение к `uv.lock`;
- работаете в CI;
- хотите установить dev-группы, extras или исключить их.

Пример после клонирования:

```bash
git clone https://github.com/example/project
cd project
uv sync
uv run pytest
```

### Точный sync

По умолчанию `uv sync` делает точную синхронизацию: пакеты, которых нет в lock-файле, будут удалены из окружения.

Если нужно оставить лишние пакеты:

```bash
uv sync --inexact
```

Обычно для проекта лучше точный sync.

### Проверить, что lock-файл актуален

```bash
uv lock --check
```

Если `pyproject.toml` изменился, а `uv.lock` не обновлен, команда завершится ошибкой.

### Запустить без изменения lock-файла

```bash
uv run --locked pytest
```

Если lock-файл устарел, будет ошибка. Это полезно в CI.

### Запустить строго по существующему lock-файлу

```bash
uv run --frozen pytest
```

`--frozen` использует существующий lock-файл без проверки актуальности относительно `pyproject.toml`.

Новичку чаще нужен `--locked`, а не `--frozen`.

### Не синхронизировать окружение перед запуском

```bash
uv run --no-sync pytest
```

Используйте осторожно. Если окружение устарело, результат может быть непонятным.

### Установить без dev-зависимостей

```bash
uv sync --no-dev
```

Это полезно для production-сценариев.

### Установить только dev-зависимости

```bash
uv sync --only-dev
```

### Установить extra

```bash
uv sync --extra network
```

### Установить все extras

```bash
uv sync --all-extras
```

### Экспортировать `uv.lock` в другой формат

Иногда нужно отдать зависимости другому инструменту, который не понимает `uv.lock`.

Экспорт в `requirements.txt`:

```bash
uv export --format requirements.txt -o requirements.txt
```

Экспорт в `pylock.toml`:

```bash
uv export --format pylock.toml -o pylock.toml
```

Экспорт CycloneDX SBOM:

```bash
uv export --format cyclonedx1.5 -o sbom.json
```

CycloneDX SBOM полезен для security, compliance и supply-chain анализа. В официальной документации экспорт CycloneDX помечен как preview, поэтому его поведение может измениться в будущих версиях `uv`.

Для обычной разработки экспорт чаще не нужен. Основной файл проекта с точными версиями - `uv.lock`.

## 10. Запуск команд через `uv run`

`uv run` - одна из главных команд.

### Запустить Python

```bash
uv run python
```

### Запустить файл

```bash
uv run main.py
```

### Запустить модуль

```bash
uv run python -m http.server
```

### Запустить тесты

Сначала добавьте `pytest`:

```bash
uv add --dev pytest
```

Потом:

```bash
uv run pytest
```

### Запустить Ruff

```bash
uv add --dev ruff
uv run ruff check .
uv run ruff format .
```

### Отформатировать проект через `uv format`

В актуальном `uv` есть отдельная команда:

```bash
uv format
```

Она форматирует Python-код в проекте с помощью Ruff formatter.

Проверить форматирование без изменения файлов:

```bash
uv format --check
```

Посмотреть diff без изменения файлов:

```bash
uv format --diff
```

Передать дополнительные аргументы Ruff можно после `--`:

```bash
uv format -- --line-length 100
```

Если проекту важно зафиксировать версию Ruff для всей команды, добавьте `ruff` в dev-зависимости и запускайте `uv run ruff ...`.

### Запустить FastAPI

```bash
uv add fastapi uvicorn
uv run uvicorn main:app --reload
```

Пример `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from uv"}
```

### Добавить временную зависимость только для одного запуска

```bash
uv run --with rich python -c "from rich import print; print('[green]Hello uv[/green]')"
```

Эта зависимость не добавится в `pyproject.toml`. Она нужна только для конкретного запуска.

### Когда нужна активация `.venv`

Обычно не нужна.

Можно делать так:

```bash
uv run python main.py
uv run pytest
uv run ruff check .
```

Но иногда IDE или привычный workflow требуют активировать окружение.

macOS и Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\activate
```

Выйти из окружения:

```bash
deactivate
```

---

[К оглавлению](README.md) | [В начало проекта](../README.md)
