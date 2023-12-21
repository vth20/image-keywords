import modules.prepocess as pp
import modules.generate as gen
import pymongo
import cloudinary
import cloudinary.uploader as uploader
import cloudinary.api
from dotenv import load_dotenv
import os
load_dotenv()

def wordify(file, filepath, wordarts_path):
    try:
        text = pp.extract_text(filepath)
        text = pp.clean_text(text)
        words = pp.process_text(text)
        print(words)
        wordlist, top_ten_kw = gen._keywords(words)

    except Exception:
        return {"message": "There was an error while generating keywords"}

    try:
        wordart = gen._wordart(wordlist)
        wordart_name = file.filename.split('.')[0] + '.png'
        wordart.to_file(wordarts_path + wordart_name)
    except Exception:
        return {"message": "There was an error while generating wordart"}


    return wordart_name, top_ten_kw

def connect_db():
    try:
        print('connectdb')
        client = pymongo.MongoClient(os.getenv("MONGO_URL"))
        mydb = client["mnm"]
        mycol = mydb["images"]
        return mycol
    except Exception:
        print("Can't connect mongodb")

def insert_db(col, data):
    try:
        x = col.insert_one(data)
        return x.inserted_id
    except Exception:
        print("Can't insert data")

def connect_cloudinary():
    cloudinary.config(
        cloud_name = os.getenv("CLOUD_NAME"),
        api_key = os.getenv("API_KEY"),
        api_secret = os.getenv("API_SECRET"),
        secure = True
    )

def upload_image(file):
    if file:
        upload_result = uploader.upload(file)
        public_id = upload_result['public_id']
        image_url = upload_result['url']

        return public_id, image_url