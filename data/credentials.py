import os

from dotenv import load_dotenv
load_dotenv()

class Credentials:

    STAGE = os.getenv("STAGE")

    if STAGE == "dev":
        LOGIN = os.getenv("DEV_LOGIN")
        PASSWORD = os.getenv("DEV_PASSWORD")

    elif STAGE == "ift":
        LOGIN = os.getenv("IFT_LOGIN")
        PASSWORD = os.getenv("IFT_PASSWORD")

    elif STAGE == "pre":
        LOGIN = os.getenv("PRE_LOGIN")
        PASSWORD = os.getenv("PRE_PASSWORD")


