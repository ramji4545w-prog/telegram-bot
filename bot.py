
import os
import asyncio
import requests
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Read token from environment variable — never hardcode secrets
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
RAILWAY_PUBLIC_DOMAIN = os.environ["RAILWAY_PUBLIC_DOMAIN"]
WEBHOOK_URL = f"https://{RAILWAY_PUBLIC_DOMAIN}/webhook"

# ------------------ TELEGRAM BOT ------------------

application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot chal raha hai 🚀")

application.add_handler(CommandHandler("start", start))

# ------------------ WEB PANEL ------------------

web = Flask(__name__)

@web.route("/")
def home():
    return "Admin Panel Running ✅"

@web.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "ok", 200

# ------------------ REGISTER WEBHOOK & RUN ------------------

if __name__ == "__main__":
    # Register the webhook with Telegram so it knows where to send updates
    resp = requests.get(
        f"https://api.telegram.org/bot{TOKEN}/setWebhook",
        params={"url": WEBHOOK_URL},
        timeout=10,
    )
    print("setWebhook response:", resp.json())

    port = int(os.environ.get("PORT", 8000))
    web.run(host="0.0.0.0", port=port)
