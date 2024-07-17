#!/usr/bin/env python3
""" Update a Document in Python """


def update_topics(mongo_collection: list, name: str, topics: list) -> None:
    """
    Changes all topics of a school document based on the name

    Args:
        mongo_collection (list): collection object
        name (str): school name to update
        topics (list): list of topics approached in the school
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
