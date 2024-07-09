"""This Script will run only if added a new pdf """

from links import indix_path, project_folder
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
)

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

pdfs = os.path.join(project_folder, "PDFs")


def indexing():
    documents = SimpleDirectoryReader(pdfs).load_data()

    index = VectorStoreIndex.from_documents(documents)

    index.storage_context.persist(indix_path)
