from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Substitua pelo seu token
TOKEN = '7124394598:AAEvgfp2KdwQl-7C3CAB3l-QsCTkmh2yZwA'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Olá! Eu sou seu bot.')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    # Cria a aplicação do bot
    application = Application.builder().token(TOKEN).build()

    # Adiciona os handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Inicia o bot
    application.run_polling()

if __name__ == '__main__':
    main()