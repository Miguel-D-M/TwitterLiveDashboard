import sys
import dataconf
from mongodb_cluster import MongoDbCluster
from config import Config


def read_arguments(arguments):
    try:
        if len(arguments) > 1:
            config_file = arguments[1]
            config = dataconf.load(config_file, Config)
            return config
        else:
            raise Exception("json configuration file is required")
    except Exception as ex:
        print(ex)


def main():
    try:
        config = read_arguments(sys.argv)
        db = MongoDbCluster(config.mongo_db)
        results = db.get_last_relevant_tweet ()
        print(results)
    except Exception as ex:
        print(ex)


main()