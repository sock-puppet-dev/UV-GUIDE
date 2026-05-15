# Полный гайд по uv

Эта папка содержит полную версию гайда, разбитую на главы. Начинайте с первых трех глав, если вы новичок, а остальные используйте как справочник.

## Главы

1. [Основы uv](01-intro.md)
2. [Установка и первый запуск](02-installation.md)
3. [Проекты и версии Python](03-projects.md)
4. [Зависимости, lock, sync и run](04-dependencies-lock-sync-run.md)
5. [Скрипты](05-scripts.md)
6. [CLI-инструменты](06-tools.md)
7. [Совместимость с pip](07-uv-pip.md)
8. [Сборка и публикация](08-packaging.md)
9. [Практические рецепты](09-recipes.md)
10. [Частые ошибки](10-troubleshooting.md)
11. [Лучшие практики](11-best-practices.md)
12. [Справочник, обучение и источники](12-reference.md)

## Проверки документации

Из корня проекта:

```bash
python3 scripts/validate_markdown.py
python3 scripts/check_links.py
```

Для проверки внешних ссылок нужен доступ в интернет:

```bash
python3 scripts/check_links.py --external
```
