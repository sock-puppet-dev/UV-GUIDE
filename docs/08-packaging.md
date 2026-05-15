# Сборка и публикация

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

---

[К оглавлению](README.md) | [В начало проекта](../README.md)
