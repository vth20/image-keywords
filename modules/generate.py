from ultralytics import YOLO
model = YOLO('yolov8n.pt')

def _keywords(filepath):
    """
    handle get keywords in image from file
    """
    results = model.predict(
    source=filepath,
    conf=0.25
    )
    names = results[0].names
    keywords = []
    for result in results[0].boxes.cls:
        keywords.append(names[int(result)])
    # -------------------------

    return keywords