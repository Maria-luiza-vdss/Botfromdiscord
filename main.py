
import os
import discord
from discord.ext import commands

# Pega o token da variável de ambiente (Render)
TOKEN = os.environ["TOKEN"]

# Intents obrigatórios
intents = discord.Intents.default()
intents.message_content = True  # importante para comandos

# Criação do bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} está online!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

TOKEN = ()
CANAL_ID = 1463230667323211849


eventos = [
    {
        "titulo": "🚗 Acidente leve na zona sul",
        "descricao": [
            "Um carro derrapou e bloqueou parcialmente a rua. A polícia está no local fazendo a queixa do cidadão.",
            "O acidente deixou apenas o dono do carro levemente ferido, o cidadão continua reclamando sobre seu carro.",
            "O carro acabou quebrando no meio do caminho, uma bicicleta acabou sendo atingida."
        ],
        "imagens": [
            "https://i.imgur.com/exemploAcidente1.png",
            "https://i.imgur.com/exemploAcidente2.png"
        ]
    },
    {
        "titulo": "🚗💥 Acidente grave no noroeste",
        "descricao": [
            "Um carro acabou de bater de frente em uma camionete! Por enquanto temos duas pessoas feridas. A polícia continua no local...",
            "Uma motocicleta acaba de bater em um carro, os paramédicos chegam agora no local.",
            "Dois carros se batem, e deixa a pista interditada."
        ],
        "imagens": [
            "https://i.imgur.com/exemploAcidenteGrave1.png",
            "https://i.imgur.com/exemploAcidenteGrave2.png"
        ]
    },
    {
        "titulo": "🔥 Incêndio no centro",
        "descricao": [
            "Um pequeno incêndio começou em um prédio comercial.",
            "Uma casa acaba de pegar fogo no bairro de Rendenção em Custódia."
        ],
        "imagens": [
            "https://i.imgur.com/ExemploIncendio1.png",
            "https://i.imgur.com/ExemploIncendio2.png"
        ]
    },
    {
        "titulo": "⚡ Queda de energia em bairro residencial",
        "descricao": [
            "Alguns bairros ficaram sem energia temporariamente. As autoridades buscam a melhor solução momentânea."
        ],
        "imagens": [
            "https://i.pinimg.com/736x/43/f3/a5/43f3a50466b605df923b1f4b96afa3cc.jpg"
        ]
    },
    {
        "titulo": "🚓 Denúncia suspeita na região leste",
        "descricao": [
            "A polícia está investigando um chamado. Muitas viaturas nesta região."
        ],
        "imagens": []
    },
    {
        "titulo": "🚓💸 Numerosos crimes na cidade",
        "descricao": [
            "A polícia se preocupa, muitos cidadãos estão sendo assaltados na região norte de Recife.",
            "Suspeita de lavagem de dinheiro em loja comercial, autoridades estão indo ao local.",
            "Mulher é assaltada na região sul e busca as autoridades."
        ],
        "imagens": [
            "https://i.imgur.com/exemploAssalto1.png",
            "https://i.imgur.com/exemploAssalto2.png"
        ]
    },
    {
        "titulo": "🎉 As festas estão bombando!",
        "descricao": [
            "De acordo com os portais de notícias, estão tendo super lotações em bailes e festas."
        ],
        "imagens": [
            "https://i.imgur.com/exemploFesta1.png",
            "https://i.imgur.com/exemploFesta2.png"
        ]
    }
]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🎲 Bot de Eventos online como {bot.user}")
    bot.loop.create_task(loop_eventos())

async def loop_eventos():
    canal = bot.get_channel(CANAL_ID)
    if canal is None:
        print("❌ Canal não encontrado. ID errado ou bot sem permissão.")
        return

    while not bot.is_closed():
        await asyncio.sleep(600)  # 10 minutos reais para teste
        if random.random() < 0.5:  # 50% chance de evento
            evento = random.choice(eventos)
            descricao = (
                random.choice(evento["descricao"])
                if isinstance(evento["descricao"], list)
                else evento["descricao"]
            )
            embed = discord.Embed(
                title=evento["titulo"],
                description=descricao,
                color=0xE74C3C
            )

            # Escolhe uma imagem aleatória se houver
            if evento["imagens"]:
                embed.set_image(url=random.choice(evento["imagens"]))

            await canal.send(embed=embed)

@bot.command()
async def teste(ctx):
    await ctx.send("✅ Bot de Eventos funcionando!")

bot.run("TOKEN")






