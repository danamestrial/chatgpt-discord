import discord
import openai

bot = discord.Client()

openai.api_key = open("API_KEY").read().strip("\n")


@bot.event
async def on_ready():
    print("ChatGPT discord bot is ready!")


@bot.event
async def on_message(message):
    prompt = message.content
    if message.author == bot.user:
        return
    if prompt.startswith("!ask"):
        question = prompt.split("!ask", 1)[1]
        output = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ],
        )
        await message.channel.send(output["choices"][0]["message"]["content"])


bot.run(open("TOKEN.txt").read())
