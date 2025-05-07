#!/usr/bin/env python3
"""Function to find schools by a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """
    Finds all schools that have a specific topic in their 'topics' field.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of schools that have the given topic.
    """
    return list(mongo_collection.find({"topics": topic}))
