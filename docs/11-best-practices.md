# Лучшие практики

## 17. Лучшие практики

### Для новых проектов используйте проектный workflow

Хорошо:

```bash
uv init my-project
uv add requests
uv run main.py
```

Менее желательно для нового проекта:

```bash
uv venv
uv pip install requests
python main.py
```

`uv pip` полезен, но для новых проектов `pyproject.toml` + `uv.lock` обычно понятнее и надежнее.

### Запускайте команды через `uv run`

Хорошо:

```bash
uv run pytest
uv run python main.py
uv run ruff check .
```

Так меньше шансов случайно использовать не тот Python или не то окружение.

### Коммитьте `uv.lock`

Для приложений почти всегда коммитьте:

```text
uv.lock
```

Это дает воспроизводимость.

Для библиотек тоже часто полезно коммитить `uv.lock`, чтобы разработчики библиотеки работали в одинаковом окружении. Публикуемые зависимости библиотеки все равно описываются в `pyproject.toml`.

### Не коммитьте `.venv`

`.venv` может быть большой и зависит от системы. Ее всегда можно восстановить:

```bash
uv sync
```

### Не редактируйте `uv.lock` руками

Используйте:

```bash
uv lock
uv lock --upgrade
uv lock --upgrade-package package-name
```

### Разделяйте runtime и dev-зависимости

Пакеты, которые нужны приложению во время работы:

```bash
uv add fastapi
```

Пакеты, которые нужны только разработчику:

```bash
uv add --dev pytest ruff
```

### Закрепляйте версию Python

```bash
uv python pin 3.12
```

Это уменьшает различия между машинами.

### Для CLI-инструментов выбирайте правильный способ

Разово:

```bash
uvx ruff check .
```

Глобально для себя:

```bash
uv tool install ruff
```

Как часть проекта:

```bash
uv add --dev ruff
uv run ruff check .
```

### Обновляйте зависимости осознанно

Не обновляйте все просто так перед важным релизом.

Одна зависимость:

```bash
uv lock --upgrade-package requests
```

Все зависимости:

```bash
uv lock --upgrade
```

После обновления обязательно запустите тесты:

```bash
uv run pytest
```

---

[К оглавлению](README.md) | [В начало проекта](../README.md)
