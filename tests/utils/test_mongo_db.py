import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("MONGO_ATLAS_USER")
db_password = os.getenv("MONGO_ATLAS_PW")


uri = f"mongodb+srv://{db_user}:{db_password}@quotemylife.80oxcl2.mongodb.net/?retryWrites=true&w=majority&appName=QuoteMyLife"


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
