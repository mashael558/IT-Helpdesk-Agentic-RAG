from pathlib import Path
from app.core.config import get_settings
from app.services.ingestion import load_file,chunk_documents
from app.rag.vectorstore import add_document
setting=get_settings()
folder=Path(setting.sample_kb_dir)
files=[p for p in folder.iterdir() if p.is_file()]
all_docs=[]
for path in files:
    #extend instead of append because we want flat document list [doc,doc..] not [[doc],[doc]]
    all_docs.extend(load_file(path)) 
chunks=chunk_documents(all_docs)
ids=add_document(chunks)
print(f"index {len(files)} files, {len(chunks)} chunks, {len(ids)} pinecone vectors")

    
