import discord
client=discord.client()
@client.event
async def on_message(msg):
  if msg.content.includes(">"):
    msg.content=msg.content.replace(">","")
    msg.channel.send(msg.content)
client.run("NjU1NTA1ODM5ODM4NDYxOTgz.XjVEAQ.HGQHqi4K6rYGKdD7JXB3NOUSjxo")
