import chromadb
from chromadb.utils import embedding_functions
import pypdf
import os

DB_PATH = "database/chromadb"

_collection = None

def get_collection():
    global _collection
    
    if _collection is not None:
        return _collection
    
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    client = chromadb.PersistentClient(path=DB_PATH)
    
    try:
        _collection = client.get_collection(
            name="gate_notes",
            embedding_function=embedding_fn
        )
        count = _collection.count()
        if count > 0:
            print(f"Database ready! {count} pages!")
            return _collection
        else:
            client.delete_collection("gate_notes")
    except:
        pass

    print("Building database...")
    _collection = client.create_collection(
        name="gate_notes",
        embedding_function=embedding_fn
    )

    pdf_folder = "data/pdfs"
    pages = []

    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            try:
                reader = pypdf.PdfReader(pdf_path)
                for i, page in enumerate(reader.pages):
                    try:
                        text = page.extract_text()
                        if text and len(text.strip()) > 50:
                            pages.append({
                                "id": f"{filename}_p{i}",
                                "text": text,
                                "source": filename,
                                "page": i+1
                            })
                    except:
                        continue
            except:
                continue

    batch_size = 100
    for i in range(0, len(pages), batch_size):
        batch = pages[i:i+batch_size]
        _collection.add(
            documents=[p["text"] for p in batch],
            ids=[p["id"] for p in batch],
            metadatas=[{"source": p["source"],
                       "page": p["page"]} for p in batch]
        )
        print(f"Stored {min(i+batch_size, len(pages))}/{len(pages)}...")

    print(f"Done! {len(pages)} pages ready!")
    return _collection