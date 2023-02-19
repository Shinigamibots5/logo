import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TELEGRAM_TOKEN, TELEGRAM_APP_NAME
from command import logo_handler, start_handler, help_handler, dc_handler, status_handler, broadcast_handler, about_handler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register handlers
    dp.add_handler(CommandHandler("logo", logo_handler))
    dp.add_handler(CommandHandler("start", start_handler))
    dp.add_handler(CommandHandler("help", help_handler))
    dp.add_handler(CommandHandler("dc", dc_handler))
    dp.add_handler(CommandHandler("status", status_handler))
    dp.add_handler(CommandHandler("broadcast", broadcast_handler))
    dp.add_handler(CommandHandler("about", about_handler))

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TELEGRAM_TOKEN)
    updater.bot.setWebhook('https://{}.herokuapp.com/{}'.format(TELEGRAM_APP_NAME, TELEGRAM_TOKEN))

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
