from fastapi import FastAPI, File, UploadFile
from modules import utils
from modules import generate
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="Detect images to keywords Swagger")
col = utils.connect_db()

utils.connect_cloudinary()
# Cấu hình CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class UploadResponse:
    def __init__(self, _id: str, image_url: str, public_id: str, keywords: list):
        self._id = _id
        self.image_url = image_url
        self.public_id = public_id
        self.keywords = keywords

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    public_id, image_url = utils.upload_image(file.file)
    keywords = generate._keywords(image_url)
    data = {"image_url": image_url, "public_id": public_id, "keywords": keywords}
    print(data)
    inserted_id = utils.insert_db(col, data)
    response = UploadResponse(_id=str(inserted_id), image_url=image_url, public_id=public_id, keywords=keywords)
    return response

@app.get("/")
def getAllImages():
    all_data = col.find({}, {"_id": False})
    return list(all_data)

@app.get("/search")
def searchKeywords(keywords: str):
    if keywords == 'all':
        return getAllImages()
    else:
        search_result = list(col.find({"keywords": {"$regex": keywords, "$options": "i"}}, {"_id": False}))
        return search_result

@app.get("/keywords")
def getKeywords():
    unique_keywords = set()
    items = col.find({}, {"keywords": True, "_id": False})
    for item in items:
        keywords = item.get("keywords", [])
        unique_keywords.update(keywords)
    return unique_keywords