from pymongo import MongoClient

def save_to_mongodb(data_list):
    """This function saves the list of dictionaries to MongoDB database"""
    client = MongoClient('mongodb+srv://molakrzysztof:papiez69xD*@cars.uwewuw1.mongodb.net/?retryWrites=true&w=majority&appName=Cars')

    db = client["car_info"]
    collection = db["cars_info"]

    for data in data_list:
        collection.insert_one(data)

    print("Data successfully saved to MongoDB.")