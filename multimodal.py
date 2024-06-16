import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import os

from dotenv import load_dotenv

load_dotenv()


GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

version = 'models/gemini-1.5-flash' # @param ["models/gemini-1.5-flash", "models/gemini-1.5-pro", "models/gemini-pro-vision"]
model = genai.GenerativeModel(version)
model_info = genai.get_model(version)
print(f'{version} - input limit: {model_info.input_token_limit}, output limit: {model_info.output_token_limit}')

import PIL
from IPython.display import display, Image

img = PIL.Image.open('static/tmp/B2CC29A8-24CC-486C-AF08-90729FFBD302 (1).jpg')
# display(Image('static/tmp/jpg-zmus1zga.jpg', width=300))

print(img.size)
print(model.count_tokens(img))


prompt = """
Describe the picture regarding clothing and posture and what they doing by using up to 4 sentence. And you will predict the future of those person in a good way (e.g. predict future for freshy computer engineer student on study or love or getting good grade or something related based on their look) use up to 1 sentence for prediction.
"""

response = model.generate_content([prompt, img], safety_settings={
                            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                        })
print(response.text)