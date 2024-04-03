from pymongo import MongoClient

def save_to_mongodb(data):
    """This function saves a dictionary to MongoDB database"""
    client = MongoClient('mongodb+srv://molakrzysztof:<tu wpisz hasło do bazy>@cars.uwewuw1.mongodb.net/?retryWrites=true&w=majority&appName=Cars')

    db = client["car_info"]
    collection = db["cars_info"]

    collection.insert_one(data)

    print("Data successfully saved to MongoDB.")