#!/usr/bin/env python3
""" Log Stats """
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
log_collection = client.logs.nginx


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
print(f'\t method GET: {find_nd_count({"method": "GET"})}')
print(f'\t method POST: {find_nd_count({"method": "POST"})}')
print(f'\t method PUT: {find_nd_count({"method": "PUT"})}')
print(f'\t method PATCH: {find_nd_count({"method": "PATCH"})}')
print(f'\t method GET: {find_nd_count({"method": "DELETE"})}')
print(f'{log_collection.count_documents({"path": "/status"})} status check')
