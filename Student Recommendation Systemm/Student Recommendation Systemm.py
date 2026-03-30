# Student Recommendation System

def calculate_score(interest, strength, marks, subject):
    scores = {
        "AI/Data Science": 0,
        "Web Development": 0,
        "Business/Marketing": 0,
        "Finance": 0,
        "UI/UX Design": 0,
        "Animation": 0
    }

    # Interest
    if interest == "coding":
        scores["AI/Data Science"] += 2
        scores["Web Development"] += 2
    elif interest == "management":
        scores["Business/Marketing"] += 2
        scores["Finance"] += 2
    elif interest == "design":
        scores["UI/UX Design"] += 2
        scores["Animation"] += 2

    # Strength
    if strength == "math":
        scores["AI/Data Science"] += 2
        scores["Finance"] += 2
    elif strength == "communication":
        scores["Business/Marketing"] += 2
    elif strength == "creativity":
        scores["UI/UX Design"] += 2
        scores["Animation"] += 2

    # Marks
    if marks >= 85:
        scores["AI/Data Science"] += 2
        scores["Finance"] += 1
    elif marks >= 70:
        scores["Web Development"] += 1
        scores["Business/Marketing"] += 1

    # Subject
    if subject == "computer":
        scores["Web Development"] += 2
        scores["AI/Data Science"] += 1
    elif subject == "commerce":
        scores["Finance"] += 2
    elif subject == "arts":
        scores["Animation"] += 2
        scores["UI/UX Design"] += 1

    return scores


def get_best_career(scores):
    return max(scores, key=scores.get)


def save_to_file(data):
    file = open("student_data.txt", "a")
    file.write(data + "\n")
    file.close()


def main():
    print("\nStudent Recommendation System")
    print("--------------------------------")

    interest = input("Enter interest (coding/management/design): ").lower()
    strength = input("Enter strength (math/communication/creativity): ").lower()
    marks = int(input("Enter marks (0-100): "))
    subject = input("Enter favourite subject (computer/commerce/arts): ").lower()

    scores = calculate_score(interest, strength, marks, subject)
    result = get_best_career(scores)

    print("\nRecommended Career Path:")
    print(result)

    data = interest + ", " + strength + ", " + str(marks) + ", " + subject + " -> " + result
    save_to_file(data)


def menu():
    while True:
        print("\nMenu")
        print("1. Get Recommendation")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            main()
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


menu()