import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    keyboard = [
        [
            InlineKeyboardButton("Play game", web_app={"url": "https://franciscoquinteros.github.io/telegram-mini-app/juego.html"}),
            InlineKeyboardButton("Exit", callback_data='exit'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Welcome! Please choose an option:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button press."""
    query = update.callback_query
    await query.answer()
    if query.data == 'exit':
        await query.edit_message_text(text="Goodbye!")
    else:
        await query.edit_message_text(text=f"Selected option: {query.data}")

def main() -> None:
    """Start the bot."""
    application = ApplicationBuilder().token("7154857416:AAHmlxA1BaPn3XdHuE1DReQssipXiQ3lwa4").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()
