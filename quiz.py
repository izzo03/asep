def run_quiz(questions, start, end):
    selected_questions = questions[start - 1:end]  # Επιλογή ερωτήσεων από start έως end
    score = 0

    for i, q in enumerate(selected_questions, 1):
        print(f"\nΕρώτηση {i + start - 1}: {q['question']}")  # Εμφανίζει τον πραγματικό αριθμό ερώτησης
        for idx, option in enumerate(q['options']):
            print(f"{idx + 1}: {option}")

        while True:
            try:
                user_answer = int(input("Διάλεξε απάντηση (1-4): ")) - 1
                if 0 <= user_answer <= 3:
                    break
                else:
                    print("Παρακαλώ εισάγετε αριθμό μεταξύ 1 και 4.")
            except ValueError:
                print("Παρακαλώ εισάγετε έγκυρο αριθμό.")

        if user_answer == q['answer']:
            print("Σωστά!")
            score += 1
        else:
            print(f"Λάθος. Η σωστή απάντηση είναι {q['answer'] + 1}")

    print(f"\nΤελικό σκορ: {score}/{len(selected_questions)}")


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

# Εμφάνιση συνολικού αριθμού ερωτήσεων
total_questions = len(questions)
print(f"\nΤο επιλεγμένο αρχείο έχει {total_questions} ερωτήσεις.")

# Επιλογή εύρους ερωτήσεων
while True:
    try:
        print(f"\nΕπιλέξτε εύρος ερωτήσεων (1-{total_questions})")
        start = int(input("Από ερώτηση: "))
        end = input("Έως ερώτηση: ")

        if end == '':
            end = total_questions
        end = int(end)
        if 1 <= start <= end <= total_questions:
            break
        else:
            print(f"Παρακαλώ εισάγετε έγκυρο εύρος (1 έως {total_questions}).")
    except ValueError:
        print("Παρακαλώ εισάγετε αριθμούς.")

run_quiz(questions, start, end)