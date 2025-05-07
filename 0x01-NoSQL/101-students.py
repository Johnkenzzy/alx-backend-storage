#!/usr/bin/env python3
"""Defines top_students function"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    # Fetch all students from the collection
    students = mongo_collection.find()

    # Create a list to hold students with their average score
    students_with_avg = []

    for student in students:
        # Calculate the average score
        total_score = sum(topic['score'] for topic in student['topics'])
        average_score = total_score / len(
                student['topics']) if student['topics'] else 0

        # Add the student with the average score to the list
        student['averageScore'] = average_score
        students_with_avg.append(student)

    # Sort the students by the average score in descending order
    sorted_students = sorted(
            students_with_avg, key=lambda x: x['averageScore'], reverse=True)

    return sorted_students
