import os
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
# LLM (Cevap Üretme) için Gemini kalmalı
from langchain_google_genai import ChatGoogleGenerativeAI
# Embedding (Gömme) için yerel model kullanılıyor
from langchain_community.embeddings import SentenceTransformerEmbeddings 
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

load_dotenv()
STORE_DIR = os.getenv("VECTOR_STORE_DIR", "store")
# EMB_MODEL kaldırıldı veya yorumlandı, çünkü yerel model kullanıyoruz.
LLM_MODEL = "gemini-2.5-flash"
API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

# Gemini LLM'i kullanmak için API anahtarını yapılandır
genai.configure(api_key=API_KEY)

prompt = PromptTemplate(
    input_variables=["question", "context"],
    template=(
        "Aşağıdaki BAĞLAMI kullanarak soruyu yanıtla.\n"
        "Bağlam yetersizse açıkça söyle ve tahmin yürütme.\n\n"
        "BAĞLAM:\n{context}\n\nSORU: {question}\nCEVAP (Türkçe, net ve kısa):"
    ),
)

_chain = None  # global olarak tanımla

def build_chain(k=10):
    # Gömme fonksiyonu olarak yerel modeli kullanma
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    
    db = Chroma(persist_directory=STORE_DIR, embedding_function=embeddings)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": k})
    
    # LLM (Gemini)
    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL, temperature=0.2, google_api_key=API_KEY
    ) 
    
    # RAG zincirini oluştur
    return RunnableParallel(
        {"context": retriever, "question": RunnablePassthrough()}
    ) | prompt | llm


def get_chain():
    global _chain
    if _chain is None:
        _chain = build_chain()
    return _chain


def answer(question: str) -> str:
    chain = get_chain()
    resp = chain.invoke(question) 
    return resp.content

def answer(question: str) -> str:
    chain = get_chain()
    resp = chain.invoke(question)
    return resp.content