import json
from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_qa_with_sources_chain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
import os, sys

# Obtain the current direct
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)
sys.path.append(grandparent_dir)
sys.path.append(current_dir)

from configurations.config_llm import OPENAI_API_KEY

from scrape_utils_v2 import scrape_site
from embed_v2 import embed

import gradio

load_dotenv()

class VectorDatabase:
    def __init__(self, db_path="./chroma"):
        self.db = Chroma(
            persist_directory=db_path,
            embedding_function=OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=OPENAI_API_KEY),
        )

        self.llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)

        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        self.condense_question_prompt = """Given the following conversation and a follow-up question, rephrase the follow-up question to be a standalone question, in its original language. \
        Make sure to avoid using any unclear pronouns.

        Chat History:
        {chat_history}
        Follow Up Input: {question}
        Standalone question:"""
        self.condense_question_prompt = PromptTemplate.from_template(self.condense_question_prompt)
        self.condense_question_chain = LLMChain(
            llm=self.llm,
            prompt=self.condense_question_prompt,
        )

        self.qa_chain = create_qa_with_sources_chain(self.llm)

        self.doc_prompt = PromptTemplate(
            template="Content: {page_content}\nSource: {source}",
            input_variables=["page_content", "source"],
        )

        self.final_qa_chain = StuffDocumentsChain(
            llm_chain=self.qa_chain,
            document_variable_name="context",
            document_prompt=self.doc_prompt,
        )

        self.retrieval_qa = ConversationalRetrievalChain(
            question_generator=self.condense_question_chain,
            retriever=self.db.as_retriever(),
            memory=self.memory,
            combine_docs_chain=self.final_qa_chain,
        )

    def predict(self, message, history = None):
        response = self.retrieval_qa.run({"question": message})
        # print(response)

        responseDict = json.loads(response)
        answer = responseDict["answer"]
        sources = responseDict["sources"]

        if type(sources) == list:
            sources = "\n".join(sources)

        if sources:
            return answer + "\n\nSee more:\n" + sources
        return answer
    
class VectorCreator:
    def __init__(self, url=None, pdfs_folder_path=None, db_path=None):
        if not db_path:
            self.db_path = "./chroma"
        else:
            self.db_path = db_path
        if url:
            self.url = url
            self.cleaned_url = url.replace("https://", "").replace("/", "-").replace(".", "_")
            self.scrape_directory = f"./scrape_{self.cleaned_url}"
        if pdfs_folder_path:
            self.pdfs_folder_path = pdfs_folder_path
        
    def create_from_url(self):
        scrape_site(self.url)
        embed(self.scrape_directory, self.db_path, web = True)
    
    def create_from_pdfs(self):
        embed(self.pdfs_folder_path, self.db_path, web = False)
    


