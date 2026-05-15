# Частые ошибки

## 16. Частые ошибки и решения

### Ошибка: `uv: command not found`

Причины:

- `uv` не установлен;
- терминал не перезапущен после установки;
- папка с `uv` не добавлена в `PATH`.

Что сделать:

```bash
uv --version
```

Если команда не найдена, переоткройте терминал. Если не помогло, повторите установку или проверьте подсказки установщика.

### Ошибка: `ModuleNotFoundError: No module named 'requests'`

Причина: пакет не установлен в окружение, где запускается код.

Если это проект:

```bash
uv add requests
uv run main.py
```

Если это разовый скрипт:

```bash
uv run --with requests script.py
```

Если это скрипт с inline metadata:

```bash
uv add --script script.py requests
uv run script.py
```

### Ошибка: пакет установлен, но импорт все равно не работает

Частая причина: вы установили пакет в одно окружение, а запускаете код в другом.

Решение для проекта:

```bash
uv run python -c "import requests; print(requests.__version__)"
```

Если через `uv run` работает, а через `python` не работает, значит обычный `python` указывает не на окружение проекта.

### Ошибка: IDE не видит пакеты

Сначала подготовьте окружение:

```bash
uv sync
```

Потом в IDE выберите интерпретатор:

```text
<project>/.venv/bin/python
```

На Windows:

```text
<project>\.venv\Scripts\python.exe
```

### Ошибка: lock-файл устарел

Если команда говорит, что `uv.lock` неактуален:

```bash
uv lock
```

Потом:

```bash
uv sync
```

И закоммитьте обновленный `uv.lock`.

### Ошибка в CI: `uv run --locked` падает

Причина: `pyproject.toml` и `uv.lock` не совпадают.

Локально выполните:

```bash
uv lock
uv run pytest
```

Потом закоммитьте:

```bash
git add pyproject.toml uv.lock
git commit
```

### Ошибка сборки пакета

Если в выводе есть что-то вроде:

```text
Failed to build ...
The build backend returned an error
```

это часто проблема не самого `uv`, а пакета, build backend, версии Python или системных библиотек.

Что проверить:

1. Поддерживает ли пакет вашу версию Python.
2. Есть ли готовый wheel для вашей платформы.
3. Не слишком ли старая версия пакета.
4. Нужны ли системные зависимости: компилятор, headers, библиотеки.
5. Что написано в `[stderr]` в ошибке.

Полезные действия:

```bash
uv run -v ...
uv pip install -v ...
```

Иногда помогает обновить проблемный пакет:

```bash
uv lock --upgrade-package package-name
```

Или использовать более подходящую версию Python:

```bash
uv python pin 3.12
uv sync
```

### Ошибка: случайно установил лишние пакеты в `.venv`

Приведите окружение к lock-файлу:

```bash
uv sync
```

`uv sync` по умолчанию удаляет лишние пакеты, которых нет в lock-файле.

### Ошибка: не понимаю, какая версия Python используется

Проверьте:

```bash
uv run python --version
```

Посмотрите `.python-version`:

```bash
cat .python-version
```

Закрепите нужную:

```bash
uv python pin 3.12
```

### Ошибка: команда работает у меня, но не у коллеги

Проверьте, что в Git есть:

- `pyproject.toml`;
- `uv.lock`;
- `.python-version`;
- нужные исходные файлы.

Коллеге нужно выполнить:

```bash
uv sync
uv run <command>
```

Если ошибка остается, соберите минимальный воспроизводимый пример: операционная система, архитектура, версия `uv`, версия Python, `pyproject.toml`, `uv.lock` и точные команды.

---

[К оглавлению](README.md) | [В начало проекта](../README.md)
