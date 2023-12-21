# Image-keywords

Image-keywords is a simple tool to save Image and extract keywords from it.


## Start the server

```bash
$ docker compose up -d
```
Omit the `-d` flag to see the logs.

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
