import os

from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


def start_command(update, context):
    update.message.reply_text(
        "Hello! Send /menu to open the contact and location buttons."
    )


def show_menu(update, context):
    buttons = [
        [
            KeyboardButton("Share my contact", request_contact=True),
            KeyboardButton("Share my location", request_location=True),
        ],
        [KeyboardButton("Menu item 3"), KeyboardButton("Menu item 4")],
    ]
    update.message.reply_text(
        "Choose an option:",
        reply_markup=ReplyKeyboardMarkup(
            buttons,
            resize_keyboard=True,
            one_time_keyboard=True,
        ),
    )


def message_handler(update, context):
    update.message.reply_text(
        f"You sent: {update.message.text}\\n"
        "This practice bot does not process that message."
    )


def contact_handler(update, context):
    contact = update.message.contact
    admin_id = int(os.environ["ADMIN_ID"])
    context.bot.send_message(
        chat_id=admin_id,
        text=f"User shared a phone number: {contact.phone_number}",
    )
    update.message.reply_text("Your contact was sent to the configured admin.")


def location_handler(update, context):
    location = update.message.location
    admin_id = int(os.environ["ADMIN_ID"])
    context.bot.send_location(
        chat_id=admin_id,
        latitude=location.latitude,
        longitude=location.longitude,
    )
    update.message.reply_text("Your location was sent to the configured admin.")


def main():
    token = os.getenv("BOT_TOKEN")
    admin_id = os.getenv("ADMIN_ID")
    if not token:
        raise RuntimeError("Set the BOT_TOKEN environment variable before starting the bot.")
    if not admin_id or not admin_id.isdigit():
        raise RuntimeError("Set ADMIN_ID to the numeric Telegram user ID of the bot admin.")

    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("menu", show_menu))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
