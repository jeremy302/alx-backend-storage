#!/usr/bin/env python3
''' pymongo module '''
from pymongo import MongoClient


def main():
    ''' main function '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    # client = MongoClient('mongodb://172.18.0.2:27017')
    db = client.logs
    col = db.nginx

    print("{} logs".format(col.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    tally = list(db.nginx.aggregate([
        {'$group': {'_id': '$method', 'sum': {'$sum': 1}}}]))
    for m in methods:
        msum = next((v['sum'] for v in tally if v['_id'] == m), 0)
        print('\tmethod {}: {}'.format(m, msum))
    status_checks = db.nginx.count_documents(
        {'method': 'GET', 'path': '/status'})
    print('{} status check'.format(status_checks))


if __name__ == '__main__':
    main()
