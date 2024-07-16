# Pest Detection Project

This project aims to detect pests in images using a deep learning model trained with fastai.

## Project Structure

- **pest_model.pkl:** The trained deep learning model.
- **main.py:** The FastAPI application for serving the model as a REST API.

Run Jupyter notebook in /notebook to get the pest_model.pkl model and download to model/ directory before proceeding.

## Setup

1. **Install Dependencies:**
`pip install -r requirements.txt`
2. **Run the FastAPI Server:**
`uvicorn main:app --host 0.0.0.0 --port 8000`

## Usage

1. **Send a POST request to the `/predict` endpoint:**
2. **Receive a JSON response with the predicted class and probabilities:**

Based on this project, you can test using:
`python test/test_client.py`