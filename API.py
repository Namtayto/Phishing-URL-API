
import Utils

def get_prediction(url, model):
    print("Checking if the URL is malicious...")

    # Use the isURLMalicious function to get the prediction
    prediction = Utils.isURLMalicious(url, model)

    # # Calculate the percentage
    # i = prediction[0][0] * 100
    # i = round(i, 3)

    print("There is", prediction, "% chance the URL is malicious!")
    return prediction