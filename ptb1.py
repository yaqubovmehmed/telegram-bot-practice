import os

from telegram.ext import CommandHandler, Updater


def start_func(update, context):
    user = update.effective_user
    if user is None:
        return

    username = f"@{user.username}" if user.username else "not set"
    update.message.reply_text(
        "Your Telegram profile information:\n"
        f"User ID: {user.id}\n"
        f"First name: {user.first_name or 'not set'}\n"
        f"Last name: {user.last_name or 'not set'}\n"
        f"Username: {username}"
    )


def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("Set the BOT_TOKEN environment variable before starting the bot.")

    updater = Updater(token=token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start_func))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
