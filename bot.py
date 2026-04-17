
import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8394853752:AAE-biieG_ER0UwqXN9rit22Yiuu3qLVshQ"


# ------------------ TELEGRAM BOT ------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot chal raha hai 🚀")

def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

# ------------------ WEB PANEL ------------------

web = Flask("__name__")

@web.route("/")
def home():
    return "Admin Panel Running ✅"

# ------------------ RUN BOTH ------------------

if __name__ == "__main__":
    # bot background me
    threading.Thread(target=run_bot).start()

    # Railway port
    port = int(os.environ.get("PORT", 8000))
    web.run(host="0.0.0.0", port=port)
