import tempfile

def persist_uploaded_file(upload):
    suffix = upload.name.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as f:
        f.write(upload.read())
        return f.name
