
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




try:
    if __name__ == "__main__":
        print("Class Average:", class_average(students))
        print("Top 3 Students:", top_3(students))
        print("Failed Students:", get_failed_students(students))
        print("Grade Distribution:", grade_distribution(students))
        print("Normalized Scores:", normalize_scores(students))

except ValueError as e:
    print(e)





