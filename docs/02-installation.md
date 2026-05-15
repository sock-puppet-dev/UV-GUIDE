# Установка и первый запуск

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

---

[К оглавлению](README.md) | [В начало проекта](../README.md)
