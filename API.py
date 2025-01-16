
import Utils

def get_prediction(url, model):
    print("Checking if the URL is malicious...")

    # if Utils.url_in_reporting_database(url):
    #     return 1
    
    # Use the isURLMalicious function to get the prediction
    prediction = Utils.isURLMalicious(url, model)


    return prediction