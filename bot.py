import os
import random
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

WELCOME_MESSAGES = [
    "🎉 Hey there, lucky one! Ready to test your fate? Type /toss to flip the coin! 🪙",
    "👋 Welcome to the Toss Game! Feeling lucky today? Use /toss to flip the coin.",
    "✨ Hello! Let's see if fortune smiles on you today. Try /toss to flip the coin!",
]

TOSS_RESULTS = {
    "Heads 🪙": [
        "It's Heads! 🍀 Looks like luck is on your side!",
        "Heads it is! Feeling like a winner? 🥳",
        "You got Heads! The coin favors you today.",
    ],
    "Tails 🪙": [
        "It's Tails! Sometimes you win, sometimes you learn. 😉",
        "Tails! Better luck next time! 🍀",
        "You got Tails! Keep trying, your luck will turn!",
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = random.choice(WELCOME_MESSAGES)
    await update.message.reply_text(msg)

async def toss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create a little suspense
    message = await update.message.reply_text("Flipping the coin... 🪙")
    await asyncio.sleep(2)  # pause for 2 seconds to build suspense

    result = "Heads 🪙" if random.random() < 0.5 else "Tails 🪙"
    response = random.choice(TOSS_RESULTS[result])
    
    await message.edit_text(f"You tossed: {result}\n{response}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("toss", toss))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
