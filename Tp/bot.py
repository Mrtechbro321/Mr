from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start ya /hello command ka response
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!")

# Bot setup
if __name__ == "__main__":
    
    # Yahan apna Telegram bot token daalein
    app = ApplicationBuilder().token("8285296504:AAGz-HmKa61FUslaGdziwrDhvkkHgf9nz64").build()

    # Command handler add karo
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("start", hello))

    # Bot run karo
    print("Bot chal raha hai...")
    app.run_polling()