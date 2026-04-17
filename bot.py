
import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


# ------------------ TELEGRAM BOT ------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot chal raha hai 🚀")




# ------------------ WEB PANEL ------------------

web = Flask("__name__")

@web.route("/")
def home():
    return "Admin Panel Running ✅"

# ------------------ RUN BOTH ------------------
if __name__ == "__main__":
    # Flask web panel in background thread
    port = int(os.environ.get("PORT", 8000))

    def run_flask():
        web.run(host="0.0.0.0", port=port, use_reloader=False)

    threading.Thread(target=run_flask, daemon=True).start()

    # Bot in main thread
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
