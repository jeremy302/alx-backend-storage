#!/usr/bin/env python3
''' pymongo module '''


def schools_by_topic(mongo_collection, topic):
    ''' schools by topic  '''
    return mongo_collection.find({'topics': {'$in': [topic]}})
