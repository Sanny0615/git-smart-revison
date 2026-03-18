from groq import Groq
import os
from dotenv import load_dotenv
import pypdf
import chromadb
from chromadb.utils import embedding_functions

load_dotenv()

pdf_folder = "data/pdfs"
pages = []
pdf_count = 0

print("Reading all GATE PDFs...")

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        try:
            reader = pypdf.PdfReader(pdf_path)
            pdf_count += 1
            for i, page in enumerate(reader.pages):
                try:
                    text = page.extract_text()
                    if text and len(text.strip()) > 50:
                        pages.append({
                            "id": f"{filename}_page_{i}",
                            "text": text,
                            "source": filename,
                            "page": i+1
                        })
                except:
                    continue
        except:
            print(f"Skipping {filename}")
            continue

print(f"Read {pdf_count} PDFs!")
print(f"Total {len(pages)} pages stored!")

print("Storing in database...")

client = chromadb.Client()
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.create_collection(
    name="gate_notes",
    embedding_function=embedding_fn
)

batch_size = 100
for i in range(0, len(pages), batch_size):
    batch = pages[i:i+batch_size]
    collection.add(
        documents=[p["text"] for p in batch],
        ids=[p["id"] for p in batch],
        metadatas=[{"source": p["source"], "page": p["page"]} for p in batch]
    )
    print(f"Stored {min(i+batch_size, len(pages))}/{len(pages)} pages...")

print("Database ready!")
print()
print("================================")
print("  GATE PYQ AI ASSISTANT READY!  ")
print("================================")
print()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

while True:
    question = input("Ask a GATE question (or type 'exit'): ")

    if question == "exit":
        print("Goodbye!")
        break

    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    context = ""
    for j, doc in enumerate(results["documents"][0]):
        source = results["metadatas"][0][j]["source"]
        page = results["metadatas"][0][j]["page"]
        context += f"[From {source}, Page {page}]:\n{doc}\n\n"

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a GATE exam coach. Answer using ONLY the provided GATE question papers. Mention which year the question is from."},
            {"role": "user", "content": f"GATE Papers:\n{context}\n\nQuestion: {question}"}
        ]
    )

    print()
    print("AI Answer:")
    print("-----------")
    print(response.choices[0].message.content)
    print()
