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
print("4: Οικονομικές Επιστήμες")
print("5: Δημόσια Διοίκηση και Διαχείριση Ανθρώπινου Δυναμικού")
print("6: Πληροφορική και Ψηφιακή Διακυβέρνηση")
print("7: Σύγχρονη Ιστορία της Ελλάδος (1875-σήμερα)")



choice = input("Εισάγετε 1-7: ")

if choice == "2":
    from questions2 import questions
elif choice == "3":
    from questions3 import questions
elif choice == "4":
    from questions4 import questions
elif choice == "5":
    from questions5 import questions
elif choice == "6":
    from questions6 import questions
elif choice == "7":
    from questions7 import questions

else:
    from questions import questions

run_quiz(questions)