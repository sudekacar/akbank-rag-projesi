import os, glob, re
from pathlib import Path
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

load_dotenv()
DATA_DIRS = ["data/akbankdata", "data/finansalsozluk"]
STORE_DIR = os.getenv("VECTOR_STORE_DIR", "store")
API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

def iter_txt_docs():
    for d in DATA_DIRS:
        if not os.path.isdir(d): continue
        for fp in glob.glob(str(Path(d) / "*.txt")):
            text = Path(fp).read_text(encoding="utf-8", errors="ignore")
            meta = {"source": fp, "category": Path(d).name}
            m = re.match(r"^Source:\s*(.+)\s*\nCategory:\s*(.+)\s*\n(Updated:.*\n)?", text, re.IGNORECASE)
            if m:
                meta["source"] = m.group(1).strip()
                meta["category"] = m.group(2).strip()
                text = text[m.end():]
            text = re.sub(r"\n{3,}", "\n\n", text).strip()
            yield Document(page_content=text, metadata=meta)



def main():
    docs = list(iter_txt_docs())
    if not docs:
        raise SystemExit("⚠️ data/akbankdata ve data/finansalsozluk altında .txt bulunamadı.")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1600, chunk_overlap=120,
                                              separators=["\n\n","\n",". "," "])
    chunks = splitter.split_documents(docs)
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")  
    vectordb = Chroma.from_documents(chunks, embeddings, persist_directory=STORE_DIR)
    vectordb.persist()
    print(f"✅ Chroma index kaydedildi → {STORE_DIR}/")

if __name__ == "__main__":
    main()
