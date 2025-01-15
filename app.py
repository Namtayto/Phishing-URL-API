# test
import json
import uvicorn
import pickle
from fastapi import FastAPI
from UrlData import UrlData, DomainData
from Utils import getTypoSquattedDomains
from API import get_prediction
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)

# ------------------------------------------

# Enabling CORS policy

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------

# load the LightGBM classifier using pickle
print("Loading the model...")
with open('lightgbm_classifier.pkl', 'rb') as file:
    clf = pickle.load(file)


@app.post("/predict")
def predict(url: str):

    # predict price using ML model
    prediction = get_prediction(url, clf)
    print("Predicted Probability : ", prediction)
    
    
    i = prediction[0][0] * 100
    i = round(i, 3)
    print("Predicted % : ", i)
    
    # always return the output as dictionary/json.
    prediction = {"prediction": prediction}

    return prediction


@app.post("/get_typesquatted_urls")
def get_similar_urls(data: DomainData):

    # convert to dictionary
    data = data.dict()

    # the key has same name as you put in class
    url = data["url"]
    max_num = data["max_num"]

    if (max_num <= 0):
        max_num = 20

    # result
    output = getTypoSquattedDomains(url, max_num)
    print("API OUTPUT : ", output)
    output = {"output": output}

    # Convert the output dictionary to JSON-compatible format
    output_dict = json.loads(json.dumps(output, default=str))
    return output_dict




if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
