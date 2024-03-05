# Image-keywords

Image-keywords is a simple tool to save Image and extract keywords from it.

src FE: https://github.com/vth20/images-gallery


## Start the server

```bash
$ docker compose up -d
```
Omit the `-d` flag to see the logs.

## API
- Use to get all images in your database;\
$ http://localhost:8001/
- Use to upload new images in your database;\
$ http://localhost:8001/upload
- Use to search images with keyword in your database;\
$ http://localhost:8001/search?keywords='example'
## Response

The response is a JSON object with the following structure:

```json
{
  "image_url": "The URL of the image in cloudinary",
  "keywords": [
    "keyword1",
    "keyword2",
    "keyword3"
    ...
    ...
  ]
}
```
