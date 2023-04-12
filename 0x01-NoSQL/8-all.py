#!/usr/bin/env python3
''' pymongo module '''


def list_all(mongo_collection):
    ''' list all '''
    return (list(mongo_collection.find())
            if mongo_collection is not None else [])
