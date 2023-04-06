#!/usr/bin/env python3
''' pymongo module '''


def top_students(mongo_collection):
    ''' top students '''
    return list(mongo_collection.aggregate([
        {'$addFields':
         {'averageScore': {'$avg': '$topics.score'}}},
        {'$sort': {'averageScore': -1}}]))
