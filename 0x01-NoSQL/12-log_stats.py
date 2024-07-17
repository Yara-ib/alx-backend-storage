#!/usr/bin/env python3
""" Log Stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    get_count = log_collection.count_documents({"path": "/status"})


    def find_nd_count(method):
        """
        Find the count for each method

        Args:
            method (key): ["GET", "POST", "PUT", "PATCH", "DELETE"]

        Returns:
            int: count of each
        """
        return log_collection.count_documents(method)


    print(f'{find_nd_count({})} logs')
    print("Methods:")
    print(f'\tmethod GET: {find_nd_count({"method": "GET"})}')
    print(f'\tmethod POST: {find_nd_count({"method": "POST"})}')
    print(f'\tmethod PUT: {find_nd_count({"method": "PUT"})}')
    print(f'\tmethod PATCH: {find_nd_count({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {find_nd_count({"method": "DELETE"})}')
    print(f'{get_count} status check')
