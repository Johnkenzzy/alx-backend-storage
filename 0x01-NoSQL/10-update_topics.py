#!/usr/bin/env python3
"""Function to update the topics of a school document."""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list): A list of topics to be set for the school.
    """
    mongo_collection.update_many(
        {"name": name},  # Find the school by name
        {"$set": {"topics": topics}}  # Update the topics
    )
