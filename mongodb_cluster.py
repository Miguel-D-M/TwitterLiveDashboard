from dataclasses import dataclass
from datetime import datetime
from pymongo import MongoClient
from config import MongoDbConfig


@dataclass
class MongoDbCluster :
    _mongo_client: MongoClient

    def __init__(self , mongo_db: MongoDbConfig) :
        self._mongo_client = MongoClient (
            f'mongodb+srv://{mongo_db.username}:{mongo_db.password}@{mongo_db.host}' )
        print('test')


    def get_last_relevant_tweet(self) :
        try :
            results = list ( self._mongo_client.data_lake [ "search_tweets" ]
                             .find ( {} )
                             .sort ( "{$natural:-1}" ).limit ( 20 ) )
            if len ( results ) != 0 :
                return results
        except Exception as ex :
            print ( ex )



