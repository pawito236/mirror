# Mirror
Reflect yourself with mirror line chatbot

![image](https://github.com/pawito236/mirror/assets/44425803/9b6ee3f3-3673-4b25-bafe-fd3c9f04d1f1)


## Technical part???

In this project we use Multimodal LLM to enable feed image as an input (to let LLM understand image) and then doing some prompt engineering (e.g. Describe the picture regarding clothing and posture and what they doing by using up to 4 sentence.) to guide the LLM how to respond back to user.

Multimodal LLM we use is gemini-1.5-flash: https://ai.google.dev/gemini-api

Learn some prompt engineer: https://www.promptingguide.ai/techniques

## Resource
Gemini cookbook: https://github.com/google-gemini/cookbook/blob/main/quickstarts/Gemini_Flash_Introduction.ipynb

Flask api with line-bot-sdk: https://github.com/line/line-bot-sdk-python/blob/master/examples/flask-kitchensink/app.py

Create Line messaging api: https://developers.line.biz/en/

From local to public url with ngrok: https://ngrok.com/

Local env variable (อย่าลืมสร้างไฟล์ .env กันนะ): https://pypi.org/project/python-dotenv/

Line image profile: https://in.pinterest.com/pin/740490363732068915/
