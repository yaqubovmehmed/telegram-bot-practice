# Telegram Bot Practice

Two small Python bot examples using \x60python-telegram-bot\x60 13.x. They demonstrate commands, keyboards, user information, text handling, and user-shared contacts and locations.

## Examples

### \x60ptb1.py\x60 — Telegram user info

The \x60/start\x60 command replies to the same user with their Telegram ID, name, and username. The bot does not forward this information to an admin.

### \x60ptb2.py\x60 — menu, contact, and location handlers

The \x60/menu\x60 command displays buttons to share a contact or location. When a user chooses one of these buttons, the bot sends that information to the configured admin ID.

**Privacy:** contact and location are personal information. Only use the share buttons when you intend to send those details to the bot owner. Keep the bot token private.

## Requirements

- Python 3.8+
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- The admin's numeric Telegram user ID for \x60ptb2.py\x60

## Setup

Create and activate a virtual environment, then install the pinned dependency:

**Windows PowerShell**
\x60\x60\x60powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:BOT_TOKEN="your-token-from-botfather"
$env:ADMIN_ID="123456789"
\x60\x60\x60

**Linux / macOS**
\x60\x60\x60bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export BOT_TOKEN="your-token-from-botfather"
export ADMIN_ID="123456789"
\x60\x60\x60

Start one example:

\x60\x60\x60bash
python ptb1.py
# or
python ptb2.py
\x60\x60\x60

Set \x60ADMIN_ID\x60 before running \x60ptb2.py\x60. Do not put a real bot token in source code or commit it to GitHub.

## Library version

These scripts use the version 13 API (\x60Updater\x60 and \x60Filters\x60); the dependency is pinned in \x60requirements.txt\x60.
