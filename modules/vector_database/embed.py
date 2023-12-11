import os
import json

from langchain.document_loaders import (
    BSHTMLLoader,
    DirectoryLoader,
)
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

from dotenv import load_dotenv
root_path = os.path.sep.join(os.path.dirname(os.path.realpath(__file__)).split(os.path.sep)[:-2])
import os, sys; sys.path.append(root_path)
from configurations.config_llm import OPENAI_API_KEY

def embed():
    load_dotenv()
    if os.path.exists("./chroma"):
        print("already embedded")
        exit(0)

    loader = DirectoryLoader(
        "./scrape",
        glob="*.html",
        loader_cls=BSHTMLLoader,
        show_progress=True,
        loader_kwargs={"get_text_separator": " ", "open_encoding": "latin-1"},
    )
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    data = loader.load()
    documents = text_splitter.split_documents(data)

    # map sources from file directory to web source
    with open("./scrape/sitemap.json", "r") as f:
        sitemap = json.loads(f.read())

    for document in documents:
        # ask for operative system
        if os.name == "nt":
            document.metadata["source"] = sitemap[
                document.metadata["source"].replace(".html", "").replace("scrape\\", "")
            ]
        else:
            document.metadata["source"] = sitemap[
                document.metadata["source"].replace(".html", "").replace("scrape/", "")
            ]

    embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=OPENAI_API_KEY)
    db = Chroma.from_documents(documents, embedding_model, persist_directory="./chroma")
    db.persist()