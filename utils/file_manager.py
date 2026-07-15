import os

UPLOAD_DIR = "assets/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


async def save_resume(document):
    file = await document.get_file()

    file_path = os.path.join(UPLOAD_DIR, document.file_name)

    await file.download_to_drive(file_path)

    return file_path