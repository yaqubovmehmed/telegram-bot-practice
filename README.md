# Telegram Bot Practice

Two small Python bot examples using `python-telegram-bot` 13.x. They demonstrate commands, keyboards, user information, text handling, and user-shared contacts and locations.

## Examples

### `ptb1.py` — Telegram user info

The `/start` command replies to the same user with their Telegram ID, name, and username. The bot does not forward this information to an admin.

### `ptb2.py` — menu, contact, and location handlers

The `/menu` command displays buttons to share a contact or location. When a user chooses one of these buttons, the bot sends that information to the configured admin ID.

**Privacy:** contact and location are personal information. Only use the share buttons when you intend to send those details to the bot owner. Keep the bot token private.

## Requirements

- Python 3.8+
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- The admin's numeric Telegram user ID for `ptb2.py`

## Setup

Create and activate a virtual environment, then install the pinned dependency:

**Windows PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:BOT_TOKEN="your-token-from-botfather"
$env:ADMIN_ID="123456789"
```

**Linux / macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export BOT_TOKEN="your-token-from-botfather"
export ADMIN_ID="123456789"
```

Start one example:

```bash
python ptb1.py
# or
python ptb2.py
```

Set `ADMIN_ID` before running `ptb2.py`. Do not put a real bot token in source code or commit it to GitHub.

## Library version

These scripts use the version 13 API (`Updater` and `Filters`); the dependency is pinned in `requirements.txt`.
