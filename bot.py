import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Join Now", url="https://t.me/+ubKdvq2fjv1lM2Q1")],
        [InlineKeyboardButton("Join Now", url="https://t.me/+ubKdvq2fjv1lM2Q1")],
        [InlineKeyboardButton("Join Now", url="https://t.me/+ubKdvq2fjv1lM2Q1")],
        [InlineKeyboardButton("Join Now", url="https://t.me/+ubKdvq2fjv1lM2Q1")],
        [InlineKeyboardButton("Join Now", url="https://t.me/+ubKdvq2fjv1lM2Q1")],
        [InlineKeyboardButton("Join Now", url="https://t.me/+ubKdvq2fjv1lM2Q1")],
        [InlineKeyboardButton("Claim Now", url="https://t.me/+ubKdvq2fjv1lM2Q1")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("image.png", "rb") as img:
        update.message.reply_photo(photo=img, caption="🔥 Join Our Top Telegram Channels 🔥", reply_markup=reply_markup)

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN is not set in environment variables!")
        return

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
