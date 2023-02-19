import os

import random

from PIL import Image, ImageDraw, ImageFont

from telegram import Update, Bot, ParseMode

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Your function to generate logos

def generate_text_logo(text: str):

    # Create a new PIL image with a black background

    img = Image.new('RGB', (500, 500), color=(0, 0, 0))

    draw = ImageDraw.Draw(img)

    # Set the font and color for the logo text

    font = ImageFont.truetype('path/to/font.ttf', size=50)

    color = (255, 255, 255)

    # Draw the logo text on the image

    text_size = draw.textsize(text, font=font)

    text_pos = ((500 - text_size[0]) / 2, (500 - text_size[1]) / 2)

    draw.text(text_pos, text, fill=color, font=font)

    # Save the image to a file

    filename = f'{text}_{random.randint(0, 999)}.png'

    img.save(filename)

    return filename

def generate_image_logo(text: str):

    # Load the image to use as the logo

    logo_image = Image.open('path/to/logo_image.png')

    # Create a new PIL image with a black background

    img = Image.new('RGB', (500, 500), color=(0, 0, 0))

    # Scale the logo image to fit in the center of the new image

    logo_size = min(img.size[0], img.size[1])

    logo_image = logo_image.resize((int(logo_size * 0.8), int(logo_size * 0.8)))

    # Paste the logo image onto the new image

    logo_pos = ((500 - logo_image.size[0]) / 2, (500 - logo_image.size[1]) / 2)

    img.paste(logo_image, logo_pos)

    # Set the font and color for the logo text

    font = ImageFont.truetype('path/to/font.ttf', size=50)

    color = (255, 255, 255)

    # Draw the logo text on the image

    text_size = draw.textsize(text, font=font)

    text_pos = ((500 - text_size[0]) / 2, (500 - text_size[1]) / 2)

    draw.text(text_pos, text, fill=color, font=font)

    # Save the image to a file

    filename = f'{text}_{random.randint(0, 999)}.png'

    img.save(filename)

    return filename

# Your handler to handle the user's requests

def logo_handler(update: Update, context: CallbackContext):

    text = update.message.text[6:].strip() # Remove the '/logo ' prefix from the user's text

    # Determine which type of logo to generate based on the user's input

    if 'image' in text:

        text = text.replace('image', '').strip()

        filename = generate_image_logo(text)

    else:

        filename = generate_text_logo(text)

    # Send the generated logo back to the user

    with open(filename, 'rb') as f:

        update.message.reply_photo(photo=f)

    # Delete the image file

    os.remove(filename)
