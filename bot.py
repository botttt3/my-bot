import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("8149384320:AAFPF9kAEG8oESzACP9xaW8ETvCaHN5_gfY")

def start(update, context):
    update.message.reply_text("Hello! ✅ Bot is running 24/7 on Render!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
