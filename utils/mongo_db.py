import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import certifi

load_dotenv()


class MongoDB:
    def __init__(self):
        self.db_user = os.getenv("MONGO_ATLAS_USER")
        self.db_password = os.getenv("MONGO_ATLAS_PW")
        self.mongo_db_name = os.getenv("MONGO_ATLAS_DB", "qmldb_dev")

        uri = f"mongodb+srv://{self.db_user}:{self.db_password}@quotemylife.80oxcl2.mongodb.net/?retryWrites=true&w=majority&appName=QuoteMyLife"

        # Create a new client and connect to the server
        self.client = MongoClient(
            uri, server_api=ServerApi("1"), tlsCAFile=certifi.where()
        )

        self.database = self.client[self.mongo_db_name]

        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command("ping")
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def add_user(self, user):
        coll = self.database.users
        user_id = user["user_id"]

        document = coll.find_one({"user_id": user_id})

        # Check if user exists
        if document is not None:
            new_user = False
            # if 'prompts_remaining' not in user:
            #     new_user = True
        else:
            new_user = True

        result = coll.update_one({"user_id": user_id}, {"$set": user}, upsert=True)

        if new_user:
            set_prompts_remaining = {"prompts_remaining": 3}
            coll.update_one(
                {"user_id": user_id}, {"$set": set_prompts_remaining}, upsert=True
            )

        print(f"User added/updated: {user_id}")

        return True

    def get_prompts_remaining(self, user_id):
        coll = self.database.users

        document = coll.find_one({"user_id": user_id})

        if document is not None:
            return document["prompts_remaining"]
        else:
            return 0

    def decrement_prompts_remaining(self, user_id):
        coll = self.database.users

        document = coll.find_one({"user_id": user_id})

        if document is not None:
            prompts_remaining = document["prompts_remaining"]
            if prompts_remaining > 0:
                prompts_remaining -= 1
                coll.update_one(
                    {"user_id": user_id},
                    {"$set": {"prompts_remaining": prompts_remaining}},
                )
                return prompts_remaining
            else:
                return 0
        else:
            return 0

    def store_qa(self, prompt, userid, response):
        coll = self.database.prompts

        mongo_doc = {"userid": userid, "prompt": prompt, "response": response}

        coll.insert_one(mongo_doc)
        return True

    def store_openai_response(self, object):
        coll = self.database.openai_responses

        coll.insert_one(object)
        return True


if __name__ == "__main__":
    mongo = MongoDB()
