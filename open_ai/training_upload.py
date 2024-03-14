import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from training_utils import dataset_error_checks

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def dataset_upload(filepath):
    if not filepath:
        raise ValueError("Filepath is required")
    if os.path.exists(filepath) and not os.path.isfile(filepath):
        raise ValueError("Filepath must be a file")

    
    client = OpenAI()

    client.files.create(
      file=open(filepath, "rb"),
      purpose="fine-tune"
    )

    return client.files.list()


def create_fine_tune_model(filename, model_name = "gpt-3.5-turbo"):
    client = OpenAI()
    client.fine_tuning.jobs.create(
        training_file=filename, 
        model=model_name
        )
    
    return client.fine_tuning.jobs.list()


def return_fine_tune_model_list():
    client = OpenAI()
    return client.fine_tuning.jobs.list()


def return_files_list():
    client = OpenAI()
    return client.files.list()


if __name__ == "__main__":

    training_file = "open_ai/response_training_file.jsonl"
    filename = "response_training_file.jsonl"
    # print(return_files_list())

    # print(dataset_upload(training_file))

    # print(create_fine_tune_model("file-dnswWflLjmdgOzncvyJFV3YC"))

    print(return_fine_tune_model_list())
