# Telegram Logo Bot

This is a Telegram bot that generates logos based on user requests. 
The logos are generated using OpenAI's DALL-E 2 API, which uses deep learning to create high-quality images from textual descriptions.

**Requirements**
- Python 3.x
- telegram library
- openai library
- Pillow library

You will also need an OpenAI API key to use the DALL-E 2 API. 
You can sign up for an API key here

**OPENAI API KEY**

To get an OpenAI API key, you can follow these steps:

- Go to the OpenAI website at https://openai.com/.
- Click on the "Get started for free" button in the top right corner of the page.
- Follow the prompts to create an account and sign up for the OpenAI API service.
- Once you have signed up, you will be provided with an API key. Keep this key safe, as it will be needed to authenticate your requests to the OpenAI API.

**Usage**

- Clone the repository: git clone https://github.com/yourusername/telegram-logo-bot.git
- Install the required libraries: pip install -r requirements.txt
- Set up a Telegram bot and obtain its API token from the BotFather.
- Create a file named config.py in the project directory and add the following code, replacing <YOUR BOT TOKEN> with your bot's API token:
TOKEN = '<YOUR BOT TOKEN>'
- Run python main.py to start the bot.

**Commands**

Here are the available commands for the bot:
```
/logo <text>: Generates a logo with the specified text.
/status: Shows the current status of the bot.
/about: Shows information about the bot.
/help: Shows help information for the bot.
/start: Starts the conversation with the bot.
/dc: Shows which data center the bot is using
/broadcast <message>: Sends a message to all users (only the bot owner can use this command).
```
