from fastapi import FastAPI, File, UploadFile
from modules import utils
from modules import generate
app = FastAPI(title="Detect images to keywords Swagger")
col = utils.connect_db()

utils.connect_cloudinary()

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    public_id, image_url = utils.upload_image(file.file)
    list = generate._keywords(image_url)
    data = {"image_url": image_url, "public_id": public_id, "keywords": list}
    print(data)
    inserted_id = utils.insert_db(col, data)
    return {
        "message": "Image has been inserted!",
    }

@app.get("/")
def home():
    return 'hello'