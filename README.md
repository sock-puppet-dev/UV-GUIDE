# uv: актуальный гайд для новичка

Этот гайд объясняет `uv` простым языком: что это за инструмент, зачем он нужен, какие команды использовать каждый день и как не запутаться в проектах, виртуальных окружениях, зависимостях и lock-файлах.

Гайд составлен по официальной документации `uv` и проверен 15 мая 2026 года. В рабочем окружении при проверке была установлена версия:

```bash
uv 0.11.14
```

Если у вас версия отличается, это нормально. Проверьте свою версию командой:

```bash
uv --version
```

## Как читать этот гайд

Если вы новичок, не пытайтесь читать все 20 разделов за один раз.

Лучший маршрут:

1. Прочитайте разделы 1-5, чтобы понять базовые слова и главную идею `uv`.
2. Выполните разделы 6-10 на маленьком учебном проекте.
3. Вернитесь к разделам 11-14, когда понадобятся скрипты, CLI-инструменты, старые `requirements.txt` или публикация пакетов.
4. Используйте разделы 15-18 как справочник и набор рецептов.
5. В конце проверьте мини-тренировку из раздела 19.

Так гайд работает как учебник и как справочник: сначала короткий путь, потом детали.

## Содержание

1. [Что такое uv](#1-что-такое-uv)
2. [Что нужно знать перед началом](#2-что-нужно-знать-перед-началом)
3. [Установка uv](#3-установка-uv)
4. [Первый запуск](#4-первый-запуск)
5. [Главная идея uv](#5-главная-идея-uv)
6. [Управление версиями Python](#6-управление-версиями-python)
7. [Проекты uv](#7-проекты-uv)
8. [Зависимости проекта](#8-зависимости-проекта)
9. [`uv.lock`, `uv sync` и воспроизводимость](#9-uvlock-uv-sync-и-воспроизводимость)
10. [Запуск команд через `uv run`](#10-запуск-команд-через-uv-run)
11. [Скрипты без полноценного проекта](#11-скрипты-без-полноценного-проекта)
12. [Инструменты через `uvx` и `uv tool`](#12-инструменты-через-uvx-и-uv-tool)
13. [`uv pip`: совместимость со старым подходом](#13-uv-pip-совместимость-со-старым-подходом)
14. [Сборка и публикация пакетов](#14-сборка-и-публикация-пакетов)
15. [Практические рецепты](#15-практические-рецепты)
16. [Частые ошибки и решения](#16-частые-ошибки-и-решения)
17. [Лучшие практики](#17-лучшие-практики)
18. [Шпаргалка команд](#18-шпаргалка-команд)
19. [Как учиться дальше](#19-как-учиться-дальше)
20. [Как устроен этот репозиторий](#20-как-устроен-этот-репозиторий)
21. [Источники](#21-источники)

## 1. Что такое uv

`uv` - это быстрый менеджер Python-проектов и Python-пакетов от Astral, написанный на Rust.

Проще говоря, `uv` помогает:

- установить сам Python;
- создать проект;
- создать виртуальное окружение;
- установить зависимости;
- зафиксировать точные версии зависимостей;
- запускать код в правильном окружении;
- запускать одноразовые CLI-инструменты;
- заменить многие привычные команды из `pip`, `pip-tools`, `pipx`, `virtualenv`, частично `pyenv`, `poetry` и `twine`.

Если совсем коротко: `uv` делает для Python то, чего новичкам часто не хватает - объединяет установку Python, зависимости, окружения, lock-файл и запуск команд в один понятный инструмент.

### Почему новичкам обычно сложно без uv

В классическом Python-подходе новичок быстро встречает много отдельных инструментов:

- `python` - запускает Python;
- `pip` - устанавливает пакеты;
- `venv` или `virtualenv` - создает виртуальное окружение;
- `pip-tools` - фиксирует версии зависимостей;
- `pipx` - устанавливает CLI-инструменты;
- `pyenv` - управляет версиями Python;
- `twine` - публикует пакеты.

Каждый инструмент полезен, но вместе они создают много вопросов:

- куда установился пакет;
- почему `import requests` не работает;
- почему у коллеги другая версия зависимости;
- как запустить проект без ручной активации `.venv`;
- что коммитить в Git, а что не коммитить;
- чем отличается `requirements.txt` от `pyproject.toml`.

`uv` не отменяет Python-экосистему, но дает более цельный рабочий процесс.

## 2. Что нужно знать перед началом

Перед командами важно понять несколько базовых слов.

### Python

`Python` - язык программирования и одновременно программа, которая исполняет файлы `.py`.

Пример:

```bash
python main.py
```

Команда говорит: запусти файл `main.py` с помощью Python.

### Пакет

Пакет - это чужой или ваш Python-код, который можно установить и использовать.

Примеры пакетов:

- `requests` - HTTP-запросы;
- `fastapi` - создание API;
- `pytest` - тесты;
- `ruff` - линтер и форматтер;
- `rich` - красивый вывод в терминал.

### Зависимость

Зависимость - это пакет, который нужен вашему проекту.

Если ваш код делает так:

```python
import requests
```

то проект зависит от пакета `requests`.

### Виртуальное окружение

Виртуальное окружение - это отдельная папка с Python и установленными пакетами для конкретного проекта.

Обычно она называется:

```text
.venv/
```

Зачем она нужна: чтобы зависимости одного проекта не смешивались с зависимостями другого проекта и с системным Python.

### `pyproject.toml`

`pyproject.toml` - главный файл современного Python-проекта.

В нем описывают:

- имя проекта;
- версию проекта;
- минимальную версию Python;
- зависимости;
- настройки инструментов.

Минимальный пример:

```toml
[project]
name = "hello-uv"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []
```

### `uv.lock`

`uv.lock` - lock-файл проекта.

`pyproject.toml` говорит: "мне нужен `requests`".

`uv.lock` говорит точнее: "для этого проекта выбрана конкретная версия `requests`, конкретные версии ее зависимостей и конкретные источники".

Lock-файл нужен, чтобы проект одинаково устанавливался у вас, у коллег и в CI.

Важно:

- `uv.lock` нужно коммитить в Git;
- `uv.lock` не нужно редактировать вручную;
- обновлять его нужно командами `uv`.

### CLI-инструмент

CLI-инструмент - программа, которую запускают из терминала.

Например:

```bash
ruff check .
pytest
http GET https://example.com
```

Некоторые CLI-инструменты написаны на Python и распространяются как Python-пакеты. `uv` умеет запускать их через `uvx` или устанавливать через `uv tool`.

## 3. Установка uv

Официальная документация рекомендует standalone-установщик или пакетный менеджер вашей системы.

### macOS и Linux

Официальный standalone-установщик:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Если нет `curl`, можно использовать `wget`:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

Установить конкретную версию можно через URL с номером версии:

```bash
curl -LsSf https://astral.sh/uv/0.11.14/install.sh | sh
```

Если вы хотите сначала посмотреть install script:

```bash
curl -LsSf https://astral.sh/uv/install.sh | less
```

После установки перезапустите терминал или выполните команду, которую установщик покажет в конце. Это нужно, чтобы shell увидел путь к `uv`.

### Windows PowerShell

Официальный standalone-установщик:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Установить конкретную версию:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.11.14/install.ps1 | iex"
```

Посмотреть install script перед запуском:

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | more"
```

После установки откройте новое окно PowerShell.

### Homebrew на macOS

Если вы используете Homebrew:

```bash
brew install uv
```

Обновление:

```bash
brew upgrade uv
```

### MacPorts на macOS

Если вы используете MacPorts:

```bash
sudo port install uv
```

### WinGet на Windows

```powershell
winget install --id=astral-sh.uv -e
```

### Scoop на Windows

```powershell
scoop install main/uv
```

### Через pipx

Если у вас уже есть `pipx`:

```bash
pipx install uv
```

### Через pip

Можно так:

```bash
pip install uv
```

Но для новичков лучше standalone-установщик, Homebrew или `pipx`, потому что так меньше шансов установить `uv` в не то окружение.

### Docker

`uv` также доступен как Docker image:

```bash
docker run --rm ghcr.io/astral-sh/uv:latest uv --version
```

Для новичка Docker-вариант обычно нужен не для установки на компьютер, а для CI, контейнеров и воспроизводимых сборок.

### GitHub Releases

Готовые бинарные файлы можно скачать со страницы релизов:

```text
https://github.com/astral-sh/uv/releases
```

Этот способ полезен, если вы не хотите запускать install script или package manager.

### Cargo

Если у вас уже есть Rust toolchain:

```bash
cargo install --locked uv
```

Новичкам этот способ обычно не нужен: он собирает `uv` из исходников и требует Rust.

### Обновление uv

Если `uv` установлен standalone-установщиком:

```bash
uv self update
```

Если `uv` установлен через Homebrew, pipx, pip, WinGet или другой менеджер, обновляйте его этим же менеджером.

Примеры:

```bash
brew upgrade uv
pipx upgrade uv
pip install --upgrade uv
```

### Автодополнение команд

Автодополнение необязательно, но удобно. Сначала узнайте свой shell:

```bash
echo $SHELL
```

Для `zsh`:

```bash
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
```

Для `bash`:

```bash
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
echo 'eval "$(uvx --generate-shell-completion bash)"' >> ~/.bashrc
```

Для `fish`:

```bash
echo 'uv generate-shell-completion fish | source' > ~/.config/fish/completions/uv.fish
echo 'uvx --generate-shell-completion fish | source' > ~/.config/fish/completions/uvx.fish
```

Для PowerShell:

```powershell
if (!(Test-Path -Path $PROFILE)) {
  New-Item -ItemType File -Path $PROFILE -Force
}
Add-Content -Path $PROFILE -Value '(& uv generate-shell-completion powershell) | Out-String | Invoke-Expression'
Add-Content -Path $PROFILE -Value '(& uvx --generate-shell-completion powershell) | Out-String | Invoke-Expression'
```

После этого перезапустите терминал.

### Удаление uv

Если нужно полностью удалить `uv`, сначала можно очистить данные, которые он хранит:

```bash
uv cache clean
rm -r "$(uv python dir)"
rm -r "$(uv tool dir)"
```

Потом удалите бинарные файлы `uv` и `uvx` тем способом, которым они были установлены.

Примеры:

```bash
brew uninstall uv
pipx uninstall uv
pip uninstall uv
```

Для standalone-установки на macOS и Linux бинарные файлы обычно лежат в `~/.local/bin/`. Перед удалением проверьте путь:

```bash
which uv
which uvx
```

## 4. Первый запуск

Проверьте, что `uv` доступен:

```bash
uv
```

Вы должны увидеть справку со списком команд.

Проверьте версию:

```bash
uv --version
```

Посмотрите помощь по конкретной команде:

```bash
uv init --help
uv add --help
uv run --help
```

Полезная привычка: если команда непонятна, добавьте `--help`.

## 5. Главная идея uv

В `uv` есть несколько основных сценариев.

| Сценарий | Что использовать |
|---|---|
| Новый Python-проект | `uv init`, `uv add`, `uv run`, `uv lock`, `uv sync` |
| Один файл-скрипт | `uv run script.py`, `uv add --script`, `uv init --script` |
| Разовый CLI-инструмент | `uvx tool-name` |
| Часто используемый CLI-инструмент | `uv tool install tool-name` |
| Старый проект на `requirements.txt` | `uv pip` или миграция в `pyproject.toml` |
| Нужна конкретная версия Python | `uv python install`, `uv python pin`, `uv run --python` |
| Нужно отформатировать код | `uv format` |
| Нужно проверить зависимости на известные уязвимости | `uv audit` |

### Как выбрать правильный путь

Если вы начинаете новый проект, используйте проектный workflow:

```bash
uv init my-project
cd my-project
uv add requests
uv run main.py
```

Если вам нужно просто запустить один файл, используйте script workflow:

```bash
uv run script.py
```

Если нужно запустить инструмент без установки в проект:

```bash
uvx ruff check .
```

Если вы поддерживаете старый проект с `requirements.txt`:

```bash
uv venv
uv pip install -r requirements.txt
```

Но для новых проектов лучше `pyproject.toml` и `uv.lock`, а не ручной `requirements.txt`.

## 6. Управление версиями Python

`uv` может использовать уже установленный Python, а может скачать нужную версию сам.

### Посмотреть доступные версии Python

```bash
uv python list
```

Команда показывает версии Python, которые `uv` видит или может установить.

### Установить последнюю подходящую версию Python

```bash
uv python install
```

### Установить конкретную версию

```bash
uv python install 3.12
```

Можно установить несколько версий:

```bash
uv python install 3.11 3.12 3.13
```

### Закрепить версию Python для проекта

Внутри проекта:

```bash
uv python pin 3.12
```

После этого появится или обновится файл:

```text
.python-version
```

Он говорит `uv`, какую версию Python использовать в этом каталоге.

### Запустить команду с конкретным Python

```bash
uv run --python 3.12 python --version
```

Если Python 3.12 еще не установлен, `uv` может скачать его автоматически.

### Что такое `requires-python`

В `pyproject.toml` часто есть строка:

```toml
requires-python = ">=3.12"
```

Она означает: проект требует Python 3.12 или новее.

Это не просто комментарий. Это влияет на выбор версий зависимостей: `uv` будет подбирать такие пакеты, которые совместимы с указанным диапазоном Python.

## 7. Проекты uv

Проект - основной способ работать с приложением, библиотекой, API, CLI или учебным кодом.

### Создать новый проект

```bash
uv init hello-uv
cd hello-uv
```

`uv` создаст примерно такую структуру:

```text
hello-uv/
├── .git/
├── .gitignore
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

Файл `main.py` можно запустить:

```bash
uv run main.py
```

### Что делает `uv run`

Команда:

```bash
uv run main.py
```

означает:

1. Найди проект.
2. Проверь `pyproject.toml`.
3. Создай `.venv`, если его еще нет.
4. Обнови `uv.lock`, если нужно.
5. Установи нужные зависимости.
6. Запусти `main.py` внутри окружения проекта.

Новичку важно запомнить: чаще всего не нужно вручную активировать `.venv`. Используйте `uv run`.

Важный нюанс: `uv run` следит, чтобы нужные зависимости были установлены, но по умолчанию не удаляет из `.venv` лишние пакеты, которых нет в lock-файле. Если вы хотите именно очистить окружение и привести его к `uv.lock`, используйте `uv sync`.

### Что появится после первого запуска

После `uv run`, `uv sync` или `uv lock` структура станет примерно такой:

```text
hello-uv/
├── .git/
├── .gitignore
├── .python-version
├── .venv/
├── README.md
├── main.py
├── pyproject.toml
└── uv.lock
```

### Что значит каждый файл

| Файл или папка | Что это |
|---|---|
| `pyproject.toml` | Описание проекта и зависимостей |
| `uv.lock` | Точные версии зависимостей |
| `.venv/` | Виртуальное окружение проекта |
| `.python-version` | Версия Python для проекта |
| `main.py` | Стартовый Python-файл |
| `.gitignore` | Что не попадет в Git |
| `README.md` | Описание проекта |

### Что коммитить в Git

Обычно нужно коммитить:

- `pyproject.toml`;
- `uv.lock`;
- `.python-version`;
- исходный код;
- README и документацию.

Обычно не нужно коммитить:

- `.venv/`;
- `__pycache__/`;
- `.pytest_cache/`;
- локальные настройки IDE, если команда проекта так решила.

### `pyproject.toml` в простом проекте

Пример:

```toml
[project]
name = "hello-uv"
version = "0.1.0"
description = "A small project for learning uv"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []
```

Пояснение:

| Поле | Значение |
|---|---|
| `name` | Имя проекта |
| `version` | Версия проекта |
| `description` | Короткое описание |
| `readme` | Файл с документацией |
| `requires-python` | Поддерживаемые версии Python |
| `dependencies` | Основные зависимости проекта |

### Типы проектов

`uv init` поддерживает несколько шаблонов.

#### Обычное приложение

```bash
uv init my-app
```

Подходит для:

- учебного проекта;
- простого скриптового приложения;
- небольшого сервиса;
- приложения без публикации на PyPI.

#### Пакетируемое приложение

```bash
uv init --package my-cli
```

Подходит, если вы хотите:

- сделать CLI-команду;
- использовать `src/`-структуру;
- запускать тесты как у полноценного пакета;
- позже опубликовать пакет.

#### Библиотека

```bash
uv init --lib my-library
```

Подходит, если вы пишете код, который будут импортировать другие проекты.

`--lib` подразумевает пакетируемый проект.

#### Минимальный проект

```bash
uv init my-minimal --bare
```

Создает только `pyproject.toml`, без README, `.python-version`, Git и стартового кода.

Новичкам обычно лучше начинать без `--bare`, потому что стандартная структура понятнее.

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

## 12. Инструменты через `uvx` и `uv tool`

Многие Python-пакеты предоставляют команды для терминала. Например, `ruff`, `black`, `httpie`, `mypy`, `pytest`.

### Запустить инструмент без установки

```bash
uvx ruff check .
```

`uvx` - удобный псевдоним для:

```bash
uv tool run ruff check .
```

`uvx` создает временное изолированное окружение для инструмента.

### Передать аргументы инструменту

```bash
uvx pycowsay hello from uv
```

Общий формат:

```bash
uvx tool-name arguments
```

### Когда использовать `uvx`

Используйте `uvx`, когда:

- нужно один раз запустить инструмент;
- не хотите добавлять инструмент в проект;
- хотите быстро проверить что-то;
- инструмент не должен видеть зависимости вашего проекта.

### Когда использовать `uv run`, а не `uvx`

Если инструмент должен работать с вашим проектом, чаще нужен `uv run`.

Например:

```bash
uv add --dev pytest
uv run pytest
```

Почему: `pytest` должен видеть зависимости и код проекта.

### Запустить конкретную версию инструмента

```bash
uvx ruff@latest check .
uvx ruff@0.11.0 check .
```

Синтаксис `tool@version` подходит для точной версии или `latest`.

### Если имя команды отличается от имени пакета

Например, команда `http` находится в пакете `httpie`.

```bash
uvx --from httpie http GET https://example.com
```

### Запустить инструмент с extra

```bash
uvx --from "mypy[faster-cache,reports]" mypy --xml-report mypy_report
```

### Запустить инструмент из Git

```bash
uvx --from git+https://github.com/httpie/cli httpie
```

Новичкам это редко нужно. Обычно берите инструмент из PyPI.

### Установить инструмент надолго

Если вы часто используете инструмент:

```bash
uv tool install ruff
```

После этого можно запускать:

```bash
ruff --version
```

Если папка с инструментами не в `PATH`, `uv` покажет предупреждение. Тогда выполните:

```bash
uv tool update-shell
```

После этого перезапустите терминал.

### Обновить инструмент

```bash
uv tool upgrade ruff
```

Обновить все установленные инструменты:

```bash
uv tool upgrade --all
```

### Посмотреть установленные инструменты

```bash
uv tool list
```

### Удалить установленный инструмент

```bash
uv tool uninstall ruff
```

### Узнать папку с установленными инструментами

```bash
uv tool dir
```

### Установить инструмент с конкретным Python

```bash
uv tool install --python 3.12 ruff
```

### Важная разница между `uv tool install` и зависимостью проекта

Команда:

```bash
uv tool install ruff
```

устанавливает `ruff` как отдельную программу для терминала.

Она не добавляет `ruff` в ваш проект.

Если `ruff` нужен именно проекту и должен быть одинаковым у всех участников, лучше:

```bash
uv add --dev ruff
uv run ruff check .
```

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

## 14. Сборка и публикация пакетов

Этот раздел нужен не всем. Если вы просто учитесь Python или пишете внутреннее приложение, можно пропустить.

### Когда нужна сборка

Сборка нужна, если вы хотите:

- опубликовать библиотеку;
- создать wheel;
- отдать пакет другим проектам;
- сделать CLI, который можно установить.

### Создать библиотеку

```bash
uv init --lib my-library
cd my-library
```

`uv init --lib` создает пакетируемый проект. Для существующего проекта перед публикацией важно проверить, что в `pyproject.toml` есть `[build-system]`.

Пример для uv build backend:

```toml
[build-system]
requires = ["uv_build>=0.11.14,<0.12"]
build-backend = "uv_build"
```

`uv_build` хорошо подходит для большинства pure Python-проектов. Если у библиотеки есть C/Rust extension modules или сложные build scripts, может понадобиться другой backend, например Hatchling, Maturin или Setuptools.

### Собрать пакет

```bash
uv build
```

Артефакты появятся в:

```text
dist/
```

Обычно это:

```text
my_library-0.1.0-py3-none-any.whl
my_library-0.1.0.tar.gz
```

Перед публикацией лучше проверить сборку так:

```bash
uv build --no-sources
```

Почему это важно: `uv build` по умолчанию учитывает локальные источники из `tool.uv.sources`. Флаг `--no-sources` проверяет, что пакет соберется и без этих локальных подсказок, то есть ближе к тому, как его увидят другие build-инструменты и пользователи.

### Изменить версию проекта

Точная версия:

```bash
uv version 1.0.0
```

Поднять patch:

```bash
uv version --bump patch
```

Поднять minor:

```bash
uv version --bump minor
```

Посмотреть версию:

```bash
uv version
uv version --short
```

### Опубликовать пакет

```bash
uv publish
```

Для PyPI обычно нужен токен:

```bash
uv publish --token <PYPI_TOKEN>
```

Или через переменную окружения:

```bash
export UV_PUBLISH_TOKEN="<PYPI_TOKEN>"
uv publish
```

Не храните токены в Git.

Если публикуете из GitHub Actions или другой CI-системы с Trusted Publisher, токен может быть не нужен: PyPI может выдать временные credentials для конкретного workflow. Для новичка самый простой локальный путь - PyPI token, но в командных проектах лучше изучить Trusted Publishing.

### Проверить, что пакет устанавливается

После публикации:

```bash
uv run --with your-package --no-project -- python -c "import your_package"
```

`--no-project` нужен, чтобы не импортировать локальный код из текущей папки.

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
