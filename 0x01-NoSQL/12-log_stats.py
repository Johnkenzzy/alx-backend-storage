#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats():
    """Logs MongoDB stats"""
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs  # Access the 'logs' database
    nginx_collection = db.nginx  # Access the 'nginx' collection

    # Count the total number of logs in the collection
    total_logs = nginx_collection.count_documents({})

    # Count the number of logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        method_counts[method] = nginx_collection.count_documents(
                {"method": method})

    # Count the number of logs with method=GET and path=/status
    status_check = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"})

    # Display the results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
