from dotenv import load_dotenv
import os
from telegram import Update
import random
from telegram.ext import ContextTypes, Application, MessageHandler, CommandHandler, filters
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_API")
BOT_NAME = "friendly_neighborhood_bot"

async def start_message(update: Update, context: ContextTypes):
    await update.message.reply_text(f"Hello! I am Icaris! I was created by my Otou-San, ShadowCon")

async def help_message(update: Update, context: ContextTypes):
    await update.message.reply_text(f"Go Fuck Yourself!")

async def random_num(update: Update, context: ContextTypes.DEFAULT_TYPE):
    randNum = random.randint(0,10)
    await update.message.reply_text(randNum)

def handle_response(text: str):
    processed: str = text.lower()

    greetings = ["Hi there", "Hello mate", "hi"]
    if processed == 'hello':
        return f"{random.choice(greetings)}, Nice to meet you!"
    
    return "wakarimasen"

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User {update.message.chat.id} : {text} ({message_type})')

    if message_type == 'group':
        if BOT_NAME in text:
            new_text = text.replace(BOT_NAME, '').strip()
            response = handle_response(new_text)
            await update.message.reply_text(response)
        else:
            return
    else:
        response = handle_response(text)
        await update.message.reply_text(response)

    print(f'Bot: {response}')

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused {context.error}')


def main():
    print('Starting up...')
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # commands handler
    app.add_handler(CommandHandler('start', start_message))
    app.add_handler(CommandHandler('help', help_message))
    app.add_handler(CommandHandler('random', random_num))

    # Message Handler
    app.add_handler(MessageHandler(filters.TEXT, handle_messages))
    print('Polling...')
    app.run_polling(poll_interval=3)

if __name__ == '__main__':
    main()