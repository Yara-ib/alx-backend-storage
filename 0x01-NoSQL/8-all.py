#!/usr/bin/env python3
""" List all documents in Python """
from typing import List


def list_all(mongo_collection: List) -> List:
    """
    Lists all documents in a collection

    Args:
        mongo_collection (List): The name of the collection

    Returns:
        List: All documents in mentioned collection
    """
    return list(mongo_collection.find())
