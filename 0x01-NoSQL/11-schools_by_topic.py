#!/usr/bin/env python3
""" Find a Document by topic in Python """


def schools_by_topic(mongo_collection: list, topic: str) -> list:
    """
    Find list of school having a specific topic

    Args:
        mongo_collection (list): collection object
        topic (str): topic searched

    Returns:
        list: list of school having a specific topic
    """
    return mongo_collection.find({'topics': topic})
