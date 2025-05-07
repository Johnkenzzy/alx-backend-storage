#!/usr/bin/env python3
"""Improved Log Stats"""
from pymongo import MongoClient


def print_log_stats():
    """Prints stats of logs including methods and IPs"""
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Get the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Get methods stats
    methods_stats = collection.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ])

    print("Methods:")
    for method_stat in methods_stats:
        print(f"    method {method_stat['_id']}: {method_stat['count']}")

    # Get status codes stats
    status_stats = collection.aggregate([
        {"$group": {"_id": "$status", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ])

    print(f"{total_logs} status check")
    for status_stat in status_stats:
        print(f"    status {status_stat['_id']}: {status_stat['count']}")

    # Get IPs stats
    ip_stats = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("IPs:")
    for ip_stat in ip_stats:
        print(f"    {ip_stat['_id']}: {ip_stat['count']}")


if __name__ == "__main__":
    print_log_stats()
