import requests

# Define the URL of the endpoint
url = 'http://localhost:8000/predict'

# Define the path to your test image
image_path = 'images/jpg_1.jpg'

# Open the image file
with open(image_path, 'rb') as f:
    # Send a POST request with the image file
    response = requests.post(url, files={'file': f})

# Print the response
print(response.json())
# print(response.text)