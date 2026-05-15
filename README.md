# uv: актуальный гайд для новичка

Русскоязычный гайд по [Astral uv](https://docs.astral.sh/uv/) для новичков: от установки и первого проекта до lock-файла, скриптов, CLI-инструментов, совместимости с `pip`, сборки пакетов и troubleshooting.

Гайд проверен 15 мая 2026 года на `uv 0.11.14`.

```bash
uv --version
```

## Быстрый старт

```bash
uv init hello-uv
cd hello-uv
uv python pin 3.12
uv add requests
uv run main.py
```

Что здесь происходит:

- `uv init` создает проект.
- `uv python pin 3.12` закрепляет версию Python.
- `uv add requests` добавляет зависимость в `pyproject.toml` и обновляет `uv.lock`.
- `uv run main.py` запускает файл в окружении проекта без ручной активации `.venv`.

## Как читать

Если вы новичок, не читайте весь материал за один раз. Идите так:

1. Прочитайте основы и установку.
2. Создайте маленький проект.
3. Разберитесь с зависимостями, `uv.lock`, `uv sync` и `uv run`.
4. Вернитесь к скриптам, tools, `uv pip` и публикации, когда они понадобятся.
5. Используйте рецепты, troubleshooting и шпаргалку как справочник.

## Полный гайд

1. [Основы uv](docs/01-intro.md)
2. [Установка и первый запуск](docs/02-installation.md)
3. [Проекты и версии Python](docs/03-projects.md)
4. [Зависимости, lock, sync и run](docs/04-dependencies-lock-sync-run.md)
5. [Скрипты](docs/05-scripts.md)
6. [CLI-инструменты](docs/06-tools.md)
7. [Совместимость с pip](docs/07-uv-pip.md)
8. [Сборка и публикация](docs/08-packaging.md)
9. [Практические рецепты](docs/09-recipes.md)
10. [Частые ошибки](docs/10-troubleshooting.md)
11. [Лучшие практики](docs/11-best-practices.md)
12. [Справочник, обучение и источники](docs/12-reference.md)

Общее оглавление глав лежит в [docs/README.md](docs/README.md).

## Репозиторий

Этот репозиторий сам оформлен как минимальный `uv`-проект:

| Файл | Назначение |
|---|---|
| `pyproject.toml` | Метаданные документационного проекта |
| `.python-version` | Учебная версия Python |
| `uv.lock` | Воспроизводимый lock-файл |
| `docs/` | Полный гайд по главам |
| `scripts/` | Локальные проверки документации |
| `.github/workflows/validate.yml` | CI-проверки |

## Проверки

Локально, без доступа в интернет:

```bash
uv lock --check
python3 scripts/validate_markdown.py
python3 scripts/check_links.py
```

С проверкой внешних ссылок:

```bash
python3 scripts/check_links.py --external
```

CI выполняет эти проверки автоматически для pull request и push в `main`/`master`.
