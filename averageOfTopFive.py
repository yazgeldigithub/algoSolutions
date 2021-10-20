"""
Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.
Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.
Example 1:
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average student `1` is `87`.
The average of student `2` is `88.6`, but with integer division is `88`.
"""

import math


def csAverageOfTopFive(scores):
    """
    Input: a nested array of students ids and their scores
    Output: a nested array of the students average scores
    """
    students = {}
    answer = []

    for s in scores:
        if s[0] not in students:
            students[s[0]] = []
        students[s[0]].append(s[1])

    for stud in students:
        stud = students[stud].sort()

    for stu in students:
        if len(students[stu]) > 5:
            students[stu] = students[stu][-5:]

    for st in students:
        students[st] = math.floor(sum(students[st]) / len(students[st]))

    for key, value in students.items():
        answer.append([key, value])

    return answer


print(csAverageOfTopFive(
    [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))
# [[1, 87], [2, 88]]
# Explanation:
# The average student `1` is `87`.
# The average of student `2` is `88.6`, but with integer division is `88`.
