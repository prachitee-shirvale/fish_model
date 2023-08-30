import config
import pymongo

mongo_client = pymongo.MongoClient(f'mongodb://localhost:{config.MONGODB_PORT_NUMBER}')
db_name = 'fish_database'
db = mongo_client[db_name]
collection_prediction = db['prediction_details']

def save_predicted_details(length,height,width,species,pred_weight):

    collection_prediction.insert_one({'Length':length,'Height':height,'Width':width,'Species':species,'Pred_weight':pred_weight})
    return 

    