import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
from credentials import bot_token
from process_request import get_file
from data_to_db import upload_data_to_db
from chatbot import query_csv

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Welcome to csv chatbot.\nUpload a csv to get started")


async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles document receiving. Accepts only CSV files."""
    document = update.message.document
    print(document.mime_type)
    if document.mime_type == 'text/comma-separated-values':
        file_ = get_file(update.message)
        upload_data_to_db(file_)
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="CSV is uploaded. Start asking questions")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Please upload a csv file')


async def handle_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles text messages and queries the database."""
    query = update.message.text
    response = query_csv(query)  # Assuming this function takes the query and returns a string response

    file_path = 'output.csv'
    response.to_csv(file_path, index=False)
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_path, 'rb'))
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=text_response)


if __name__ == '__main__':
    application = ApplicationBuilder().token(bot_token).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.Document.ALL, handle_document)
    text_handler = MessageHandler(filters.TEXT, handle_question)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(text_handler)

    application.run_polling()