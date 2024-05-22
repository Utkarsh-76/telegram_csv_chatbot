import os
from dotenv import load_dotenv
load_dotenv()

bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
bot_user_name = os.getenv('TELEGRAM_BOT_USERNAME')
