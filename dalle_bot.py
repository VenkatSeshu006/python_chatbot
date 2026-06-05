from openai import OpenAi
from dotenv import  load_dotenv
import os
#load_dotenv('openai.env')

"""
api_key= os.environ.get('OPENAI_API_KEY')
from openai import Openai
client=OpenAi()
"""

response =  client.images.generate(
    model="dall-e-3",
    prompt="A brown wolf walking in dark night.",
    size="1080x1080",
    n=1,
)

image_url = response.data[0].url
print(image_url)