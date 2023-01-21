from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "20543992"))
API_HASH = getenv("API_HASH", "93fb093637866a6a054c54ade94a7eff")
BOT_TOKEN = getenv("BOT_TOKEN", "5555731081:AAHASdvJZNBOMxTfmNByhq-9tyQZvsgKxZU")
SESSION_NAME = getenv("SESSION_NAME", "BABLX43yEt8bICJuE8Ux1fM4Ajny3PMnOlH5ahTgu7GmlxgiqsMk-ZP5-bh5RMfLsSh7bM4p6v0SIcw6WWk7B1FvI_YdKQflJkQmLvMXmjR3gMNNxdk1nDdThm9nECcbyboRAwawGBzwD_9IbJQTEsbEcd78oML1-vRHbrFLUwTatbFygqTSAXuSRF6g4i2CkfcKBPMEwUz-jHMtrq4H7BHZIZl_KrVr5npnSusJcsEylE_387gbU59ZOY9lt19vto_xcRDqQ-rpx7X1sAXFI1shwZaixLxn803anFNKke1Ra4h6PQDJLZONqGUO1YYcOb5D1juidKGjBCRqI42hKUwBAAAAAWPfkSEA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "ALAPATH")
ALIVE_NAME = getenv("ALIVE_NAME", "sonng")
BOT_USERNAME = getenv("BOT_USERNAME", "CASBAR_1BoT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ALAPATH")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ALAPATH")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5093806483").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5093806483").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
