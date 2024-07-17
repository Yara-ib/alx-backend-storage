#!/usr/bin/env python3
""" Sort students by average score in Python """


def top_students(mongo_collection):
    """
    Sort students by average score

    Args:
        mongo_collection (_type_): collection

    Returns:
        list: students sorted by average score
    """
    return mongo_collection.aggregate(
        [
            {
                "$group": {
                    "_id": "$name",
                    "averageScore": {"$avg": "$topics.score"},
                }
            },
            {"$sort": {"averageScore": -1}},
        ]
    )
