#!/usr/bin/env python3
"""Function to insert a new document into a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the specified MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The document fields and values to be inserted.

    Returns:
        The new document's _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
