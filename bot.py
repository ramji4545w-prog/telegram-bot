
import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = import os
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)

# ------------------ TELEGRAM BOT ------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot chal raha hai 🚀")

def run_bot():
    import asyncio
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    asyncio.run(app.run_polling())


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
