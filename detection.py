import os
import openai
from google.cloud import vision

# Set up Google Vision API client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/google-credentials.json'
vision_client = vision.ImageAnnotatorClient()

# Set OpenAI API Key
openai.api_key = 'your-openai-api-key'

def detect_adult_content(image_path):
    """
    Detects adult content in images using Google Vision API and OpenAI.
    """
    # Load image file
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Perform label detection with Google Vision
    image = vision.Image(content=content)
    response = vision_client.label_detection(image=image)
    labels = response.label_annotations

    adult_labels = [label.description for label in labels if 'adult' in label.description.lower()] 

    # Check with OpenAI if needed
    if adult_labels:
        openai_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Does the following content fall under adult content? Labels: {}".format(adult_labels),
            max_tokens=5
        )
        return openai_response.choices[0].text.strip().lower() == 'yes'
    return False

# Example usage
# print(detect_adult_content('path/to/image.jpg'))