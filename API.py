
import Utils

def get_prediction(url, model):
    print("Checking if the URL is malicious...")

    # Use the isURLMalicious function to get the prediction
    prediction = Utils.isURLMalicious(url, model)


    return prediction