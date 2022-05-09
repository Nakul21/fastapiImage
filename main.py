import uvicorn
from fastapi import FastAPI, File
from starlette.responses import FileResponse

from process_image import parse_image

app = FastAPI()


@app.post("/uploadfile/")
def process_xray_image(file: bytes = File(...)) -> FileResponse:
    file_path = "input_image/xray.jpg"
    with open(file_path, 'wb') as image:
        image.write(file)
        image.close()
    parse_image(file_path)
    return FileResponse("./output_image/image.jpg", filename="xray.jpg")


