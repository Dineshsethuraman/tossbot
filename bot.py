import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()  # Load variables from .env

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Toss Game Bot! Type /toss to toss the coin.")

async def toss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import random
    result = "Heads 🪙" if random.random() < 0.5 else "Tails 🪙"
    await update.message.reply_text(f"You tossed: {result}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("toss", toss))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
