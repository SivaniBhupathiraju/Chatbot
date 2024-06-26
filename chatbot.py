
from transformers import AutoModelWithLMHead, AutoTokenizer                         
import torch
import discord
import os

tokenizer = AutoTokenizer.from_pretrained(“microsoft/DialoGPT-small”,padding_side=‘left’)
model = AutoModelWithLMHead.from_pretrained(“microsoft/DialoGPT-small”)
intents = discord.Intents().all()
class MyClient(discord.Client):
async def on_ready(self):
print(‘Logged on as {0}!’.format(self.user))
programmingaddicted's profile picture



async def on_message(self, message):
if message.author == client.user:
return
bot_input_ids = tokenizer.encode(message.content + tokenizer.eos_token, return_tensors=‘pt’)
chat_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
messagebot = tokenizer.decode(chat_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
tosend = “no comment” if messagebot == “” else messagebot
await message.channel.send(tosend)
print(‘Message from {0.author}: {0.content}’.format(message))
print(‘Message from bot {}’.format(tosend))
client = MyClient(intents = intents)
client.run(os.environ[‘DISCORD_TOKEN’])

