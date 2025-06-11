def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nΕρώτηση {i}: {q['question']}")
        for idx, option in enumerate(q['options']):
            print(f"{idx + 1}: {option}")

        user_answer = int(input("Διάλεξε απάντηση (1-4): ")) - 1
        if user_answer == q['answer']:
            print("Σωστά!")
            score += 1
        else:
            print(f"Λάθος. Η σωστή απάντηση είναι {q['answer'] + 1}")

    print(f"\nΤελικό σκορ: {score}/{len(questions)}")

# Επιλογή αρχείου ερωτήσεων
print("Διάλεξε το αρχείο ερωτήσεων:")
print("1: Συνταγματικό Δίκαιο (Προεπιλογή)")
print("2: Διοικητικό Δίκαιο")
print("3: Ευρωπαϊκοί Θεσμοί και Δίκαιο")


choice = input("Εισάγετε 1, 2 ή 3: ")

if choice == "2":
    from questions2 import questions
elif choice == "3":
    from questions3 import questions
else:
    from questions import questions

run_quiz(questions)