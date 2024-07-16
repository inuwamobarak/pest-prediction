from fastapi import FastAPI, File, UploadFile
from fastai.vision.all import *
from PIL import Image
import io

# Load the trained model
learn = load_learner('model/pest_model.pkl')

# Create the FastAPI app
app = FastAPI()


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read the image file
    img = await file.read()

    # Open the image using PIL
    img = Image.open(io.BytesIO(img))

    # Resize the image (replace 128 with the size used during training)
    img = img.resize((128, 128))

    # Get the model prediction
    pred_class, pred_idx, probabilities = learn.predict(img)

    # Return the prediction result
    return {"predicted_class": pred_class, "probabilities": probabilities.tolist()}