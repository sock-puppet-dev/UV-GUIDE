# Справочник, обучение и источники

## 18. Шпаргалка команд

### Установка и версия

| Команда | Что делает |
|---|---|
| `uv --version` | Показать версию uv |
| `uv self update` | Обновить uv, если установлен standalone-установщиком |
| `uv help` | Показать справку |
| `uv <command> --help` | Справка по конкретной команде |

### Python

| Команда | Что делает |
|---|---|
| `uv python list` | Показать доступные версии Python |
| `uv python install` | Установить последнюю подходящую версию |
| `uv python install 3.12` | Установить Python 3.12 |
| `uv python pin 3.12` | Закрепить Python 3.12 для проекта |
| `uv run --python 3.12 python --version` | Запустить команду с Python 3.12 |

### Проекты

| Команда | Что делает |
|---|---|
| `uv init my-app` | Создать новый проект |
| `uv init --package my-cli` | Создать пакетируемое приложение |
| `uv init --lib my-lib` | Создать библиотеку |
| `uv init my-minimal --bare` | Создать минимальный проект |
| `uv run main.py` | Запустить файл в окружении проекта |
| `uv run python` | Запустить Python в окружении проекта |
| `uv format` | Отформатировать Python-код проекта |
| `uv format --check` | Проверить форматирование без изменений |
| `uv audit` | Проверить зависимости на известные уязвимости |

### Зависимости

| Команда | Что делает |
|---|---|
| `uv add requests` | Добавить зависимость |
| `uv add "requests>=2.32,<3"` | Добавить зависимость с диапазоном |
| `uv add --dev pytest` | Добавить dev-зависимость |
| `uv add --group docs mkdocs` | Добавить зависимость в группу |
| `uv add httpx --optional network` | Добавить optional dependency |
| `uv add -r requirements.txt` | Импортировать зависимости из requirements |
| `uv remove requests` | Удалить зависимость |
| `uv tree` | Показать дерево зависимостей |
| `uv audit --no-dev` | Проверить runtime-зависимости без dev-группы |

### Lock и sync

| Команда | Что делает |
|---|---|
| `uv lock` | Создать или обновить `uv.lock` |
| `uv lock --check` | Проверить актуальность `uv.lock` |
| `uv lock --upgrade` | Обновить все зависимости в lock-файле |
| `uv lock --upgrade-package requests` | Обновить одну зависимость |
| `uv sync` | Синхронизировать `.venv` с `uv.lock` |
| `uv sync --no-dev` | Установить без dev-группы |
| `uv sync --extra name` | Установить extra |
| `uv run --locked pytest` | Запустить, не изменяя lock-файл |
| `uv export --format requirements.txt -o requirements.txt` | Экспортировать lock-файл в requirements |

### Скрипты

| Команда | Что делает |
|---|---|
| `uv run script.py` | Запустить скрипт |
| `uv run --with rich script.py` | Запустить с временной зависимостью |
| `uv init --script script.py` | Создать скрипт с inline metadata |
| `uv add --script script.py requests` | Добавить зависимость в metadata скрипта |
| `uv lock --script script.py` | Создать lock-файл для скрипта |

### Инструменты

| Команда | Что делает |
|---|---|
| `uvx ruff check .` | Разово запустить Ruff |
| `uvx ruff@latest check .` | Запустить последнюю версию Ruff |
| `uvx --from httpie http GET https://example.com` | Запустить команду из другого пакета |
| `uv tool install ruff` | Установить инструмент надолго |
| `uv tool upgrade ruff` | Обновить инструмент |
| `uv tool upgrade --all` | Обновить все инструменты |
| `uv tool list` | Показать установленные инструменты |
| `uv tool uninstall ruff` | Удалить инструмент |
| `uv tool dir` | Показать папку tools |
| `uv tool update-shell` | Добавить папку инструментов в PATH |

### `uv pip`

| Команда | Что делает |
|---|---|
| `uv venv` | Создать `.venv` |
| `uv venv --python 3.12` | Создать `.venv` с Python 3.12 |
| `uv pip install flask` | Установить пакет в окружение |
| `uv pip install -r requirements.txt` | Установить из requirements |
| `uv pip sync requirements.txt` | Точно синхронизировать окружение |
| `uv pip compile requirements.in -o requirements.txt` | Скомпилировать requirements |

### Сборка и публикация

| Команда | Что делает |
|---|---|
| `uv build` | Собрать wheel и sdist |
| `uv version` | Показать версию проекта |
| `uv version 1.0.0` | Установить версию |
| `uv version --bump patch` | Поднять patch-версию |
| `uv publish` | Опубликовать пакет |

## 19. Как учиться дальше

Лучший порядок для новичка:

1. Установите `uv`.
2. Создайте пустой проект через `uv init`.
3. Запустите `uv run main.py`.
4. Добавьте `requests` через `uv add requests`.
5. Напишите маленький запрос к `https://example.com`.
6. Добавьте `pytest` через `uv add --dev pytest`.
7. Напишите один тест и запустите `uv run pytest`.
8. Посмотрите `pyproject.toml`.
9. Посмотрите `uv.lock`, но не редактируйте его.
10. Удалите `.venv` и восстановите окружение через `uv sync`.
11. Запустите разовый инструмент через `uvx`.
12. Создайте скрипт через `uv init --script`.

После этого у вас будет понимание всех основных частей `uv`.

### Мини-тренировка на 20 минут

Выполните:

```bash
uv init weather-demo
cd weather-demo
uv python pin 3.12
uv add requests rich
uv add --dev pytest ruff
uv run python --version
uv tree
```

Замените `main.py`:

```python
import requests
from rich import print


def main() -> None:
    response = requests.get("https://example.com", timeout=10)
    print(f"[green]Status:[/green] {response.status_code}")


if __name__ == "__main__":
    main()
```

Запустите:

```bash
uv run main.py
uv run ruff check .
uv run ruff format .
```

Потом удалите окружение. Делайте это только внутри учебного проекта `weather-demo`, чтобы случайно не удалить нужную папку в другом месте.

macOS и Linux:

```bash
rm -rf .venv
```

Windows PowerShell:

```powershell
Remove-Item -Recurse -Force .venv
```

И восстановите:

```bash
uv sync
uv run main.py
```

Главная мысль тренировки: `.venv` можно пересоздать, потому что проект описан в `pyproject.toml` и `uv.lock`.

## 20. Как устроен этот репозиторий

Этот репозиторий сам настроен как маленький `uv`-проект, чтобы его структура не противоречила гайду.

| Файл | Зачем нужен |
|---|---|
| `README.md` | Основной учебный гайд |
| `pyproject.toml` | Минимальные метаданные проекта |
| `.python-version` | Закрепленная учебная версия Python |
| `uv.lock` | Воспроизводимый lock-файл проекта |
| `.gitignore` | Исключает `.venv`, IDE-настройки, Python/tool cache, build-артефакты и `.DS_Store` |
| `.github/workflows/validate.yml` | Минимальная CI-проверка lock-файла и Markdown code fences |

В проекте нет runtime-зависимостей, потому что это документационный репозиторий. Но `uv.lock` все равно полезен: он показывает правильную практику и фиксирует состояние проекта.

Проверки, которые стоит запускать после правок:

```bash
uv lock --check
git diff --check
```

В CI уже есть базовая проверка `uv lock --check` и проверка четности Markdown code fences. Если добавите Markdown lint или link checker, хорошо вынести их в dev-зависимости и запускать через `uv run`.

## 21. Источники

Основные официальные страницы, по которым составлен гайд:

- [uv Introduction](https://docs.astral.sh/uv/)
- [Installing uv](https://docs.astral.sh/uv/getting-started/installation/)
- [First steps with uv](https://docs.astral.sh/uv/getting-started/first-steps/)
- [Installing Python](https://docs.astral.sh/uv/guides/install-python/)
- [Running scripts](https://docs.astral.sh/uv/guides/scripts/)
- [Using tools](https://docs.astral.sh/uv/guides/tools/)
- [Working on projects](https://docs.astral.sh/uv/guides/projects/)
- [Creating projects](https://docs.astral.sh/uv/concepts/projects/init/)
- [Managing dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/)
- [Running commands in projects](https://docs.astral.sh/uv/concepts/projects/run/)
- [Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/)
- [Configuring projects](https://docs.astral.sh/uv/concepts/projects/config/)
- [Exporting lockfiles](https://docs.astral.sh/uv/concepts/projects/export/)
- [Build backend](https://docs.astral.sh/uv/concepts/build-backend/)
- [Using uv in GitHub Actions](https://docs.astral.sh/uv/guides/integration/github/)
- [Command reference](https://docs.astral.sh/uv/reference/cli/)
- [The pip interface](https://docs.astral.sh/uv/pip/)
- [Using Python environments](https://docs.astral.sh/uv/pip/environments/)
- [Managing packages with uv pip](https://docs.astral.sh/uv/pip/packages/)
- [Locking environments with uv pip](https://docs.astral.sh/uv/pip/compile/)
- [Building and publishing a package](https://docs.astral.sh/uv/guides/package/)
- [Troubleshooting build failures](https://docs.astral.sh/uv/reference/troubleshooting/build-failures/)
- [Reproducible examples](https://docs.astral.sh/uv/reference/troubleshooting/reproducible-examples/)

---

[К оглавлению](README.md) | [В начало проекта](../README.md)
