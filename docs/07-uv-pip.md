# Совместимость с pip

## 13. `uv pip`: совместимость со старым подходом

`uv` поддерживает интерфейс, похожий на `pip`, `pip-tools` и `virtualenv`.

Он нужен, если:

- у проекта уже есть `requirements.txt`;
- вы не готовы мигрировать на `pyproject.toml`;
- нужно быстро заменить `pip` на более быстрый инструмент;
- вы работаете в Docker или CI со старым workflow.

Для новых проектов лучше использовать `uv init`, `uv add`, `uv run`, `uv lock`, `uv sync`.

### Создать виртуальное окружение

```bash
uv venv
```

Будет создана папка:

```text
.venv/
```

Создать окружение с конкретным Python:

```bash
uv venv --python 3.12
```

### Установить пакет в `.venv`

```bash
uv pip install flask
```

Установить несколько пакетов:

```bash
uv pip install flask ruff
```

Установить с ограничением:

```bash
uv pip install "ruff>=0.11"
```

Установить из `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

### Синхронизировать окружение с `requirements.txt`

```bash
uv pip sync requirements.txt
```

Разница:

- `uv pip install -r requirements.txt` установит недостающие пакеты, но может оставить лишние;
- `uv pip sync requirements.txt` приведет окружение к точному составу файла.

Для воспроизводимости лучше `sync`.

### Скомпилировать `requirements.txt`

Если есть `requirements.in`:

```text
fastapi
pydantic>2
```

Сделайте lock в формате `requirements.txt`:

```bash
uv pip compile requirements.in -o requirements.txt
```

Если зависимости указаны в `pyproject.toml`:

```bash
uv pip compile pyproject.toml -o requirements.txt
```

Обновить одну зависимость:

```bash
uv pip compile requirements.in -o requirements.txt --upgrade-package fastapi
```

Обновить все:

```bash
uv pip compile requirements.in -o requirements.txt --upgrade
```

### Почему `uv pip` требует виртуальное окружение

В отличие от классического `pip`, `uv pip` по умолчанию не хочет менять системный Python. Это сделано специально, чтобы не ломать систему.

Типичный порядок:

```bash
uv venv
uv pip install flask
uv run python -c "import flask; print(flask.__version__)"
```

Если вы точно понимаете, что делаете, можно использовать системный Python:

```bash
uv pip install --system flask
```

Новичкам лучше избегать `--system`.

---

[К оглавлению](README.md) | [В начало проекта](../README.md)
