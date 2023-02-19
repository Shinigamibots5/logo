import os
import random
import requests
import json
from PIL import Image, ImageDraw, ImageFont
from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from config import OPENAI_API_KEY

# Your function to generate logos
def generate_logo(text: str, type: str):
    try:
        if type == '1':
            # Create a new PIL image with a black background
            img = Image.new('RGB', (500, 500), color=(0, 0, 0))
            draw = ImageDraw.Draw(img)

            # Set the font and color for the logo text
            font = ImageFont.truetype('fonts/Anton-Regular.ttf', size=80)
            color = (255, 255, 255)

            # Draw the logo text on the image
            text_size = draw.textsize(text, font=font)
            text_pos = ((500 - text_size[0]) / 2, (500 - text_size[1]) / 2)
            draw.text(text_pos, text, fill=color, font=font)

            # Save the image to a file
            filename = f'{text}_{random.randint(0, 999)}.png'
            img.save(filename)
            return filename

        elif type == '2':
            url = "https://api.deepai.org/api/text2img"

            payload = json.dumps({
              "text": text
            })
            headers = {
              'Content-Type': 'application/json',
              'api-key': OPENAI_API_KEY
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            data = response.json()
            img_url = data['output_url']
            img_response = requests.get(img_url)

            filename = f'{text}_{random.randint(0,
