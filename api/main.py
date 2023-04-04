from fastapi import FastAPI, UploadFile, Form
import os, time
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = Form(...), chunk_index: int = Form(...), num_chunks: int = Form(...), file_name: str = Form(...)):
    chunk_size = 100000000 # 1MB
    chunk_offset = chunk_index * chunk_size

    # Write incoming chunk to file
    with open(f"uploads/temp/{file_name}_{chunk_index}", "wb") as buffer:
        file.seek(chunk_offset)
        buffer.write(await file.read(chunk_size))

    if chunk_index == num_chunks - 1:
        # All chunks have been uploaded, reassemble the file
        with open(f"uploads/{time.time()}", "wb") as buffer:
            for i in range(num_chunks):
                chunk_path = f"uploads/temp/{file_name}_{i}"
                with open(chunk_path, "rb") as chunk:
                    buffer.write(chunk.read())

        # Delete the individual chunks
        for i in range(num_chunks):
            chunk_path = f"uploads/temp/{file_name}_{i}"
            os.remove(chunk_path)

    return {"filename": file_name}
