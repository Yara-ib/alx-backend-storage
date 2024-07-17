#!/usr/bin/env python3
""" Insert a Document in Python """


def insert_school(mongo_collection: list, **kwargs: dict) -> int:
    """
    Inserts a new document in a collection based on kwargs

    Args:
        mongo_collection (list): collection object

    Returns:
        int: The _id of created document
    """
    return (mongo_collection.insert_one(kwargs)).inserted_id
