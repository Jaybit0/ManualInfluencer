import base64

from google.cloud import storage

from . import constants


def download_and_encode_pdf_to_base64() -> str:
    """
    Downloads a PDF file from a Google Cloud Storage bucket, encodes it to base64, and returns the encoded string.
    """
    # Instantiates a client
    storage_client = storage.Client()

    # The name for the bucket
    bucket_name = constants.BUCKET_NAME

    # Get bucket
    bucket = storage_client.bucket(bucket_name)

    # Specify the blob name
    blob_name = constants.PDF_FILE_NAME

    # Get blob
    blob = bucket.blob(blob_name)

    # Download as bytes and encode to base64
    content = blob.download_as_bytes()
    base64_content = base64.b64encode(content).decode("utf-8")

    # print(f"Downloaded and encoded {blob_name}")
    return base64_content
