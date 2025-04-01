# Setup
# pip install --upgrade google-genai
# gcloud auth application-default login

import base64

from google import genai
from google.genai import types

from . import constants
from .pdf_utils import download_and_encode_pdf_to_base64


def generate_script(text=constants.TEXT_TO_SCENES_PROMPT) -> str:
    client = genai.Client(
        vertexai=True,
        project=constants.GCP_PROJECT_ID,
        location="global",
    )

    text1 = types.Part.from_text(text=text)

    model = "gemini-2.0-flash-001"
    contents = [
        types.Content(role="user", parts=[text1]),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        max_output_tokens=8192,
        response_modalities=["TEXT"],
        safety_settings=[
            types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="OFF"),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="OFF"
            ),
            types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="OFF"),
        ],
        response_mime_type="application/json",
        response_schema={
            "type": "OBJECT",
            "properties": {
                "scenes": {
                    "type": "ARRAY",
                    "items": {
                        "type": "OBJECT",
                        "properties": {
                            "visual": {
                                "type": "STRING",
                                "example": "A close-up of a TV screen",
                            },
                            "audio": {
                                "type": "STRING",
                                "example": "Oha, ein grauer organischer Leuchtdioden-Fernsehbildschirm",
                            },
                        },
                    },
                }
            },
        },
        system_instruction=[
            types.Part.from_text(text=constants.TEXT_TO_SCENES_SYSTEM_INSTRUCTION)
        ],
    )

    text_output = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        text_output += chunk.text
        print(chunk.text, end="")
    return text_output
