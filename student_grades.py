
students = {
    "Ali": 78,
    "Sara": 92,
    "John": 45,
    "Aisha": 66,
    "Mike": 30,
    "Lina": 88,
    "David": 55,
    "Zara": 49,
    "Omar": 73,
    "Noah": 61
}


def class_average(students):
    if not students:
        raise ValueError("No student provided")

    return sum(students.values()) / len(students)


def top_3(students):
    return sorted(students.items(), key=lambda x: x[1], reverse=True)[:3]


def get_failed_students(students):
    return [name for name, score in students.items() if score < 50]


def grade_distribution(students):
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for score in students.values():
        if score >= 80:
            distribution["A"] += 1
        elif score >= 70:
            distribution["B"] += 1
        elif score >= 60:
            distribution["C"] += 1
        elif score >= 50:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    return distribution


def normalize_scores(students):
    if not students:
        raise ValueError("No student provided")

    max_score = max(students.values())
    return {name: round(score / max_score * 100, 2) for name, score in students.items()}








# goals = {
#     "Ronaldo" : 234, 
#     "Messi" : 700, 
#     "Lewandowski" : 590
# }





# def all_time_goal_scorer(goals):
#     sorted_player = sorted(goals.items(), key= lambda x: x[1], reverse=True )
#     return sorted_player[:3]

# print(all_time_goal_scorer(goals))


# def all_time_goal_scorer(goals):
#     top = []

#     for player, goals in goals.items():
#         top.append((player, goals))
#         top.sort(key=lambda x: x[1], reverse=True)

#     return top[:3]

# print(all_time_goal_scorer(goals))










