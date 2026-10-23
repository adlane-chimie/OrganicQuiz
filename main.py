
print("=== OrganicQuiz ===")
print("Quiz de chimie organique")

questions = [
    ("Quelle est la fonction de CH3-CH2-OH ?", "Alcool"),
    ("Quelle est la fonction de CH3-COOH ?", "Acide carboxylique"),
    ("Quelle est la fonction de CH3-CHO ?", "Aldehyde")
]

score = 0

for question, answer in questions:
    print("\n" + question)
    reponse = input("Votre reponse : ")

    if reponse.lower() == answer.lower():
        print("Bonne reponse !")
        score = score + 1
    else:
        print("La bonne reponse est :", answer)

print("\nScore final :", score, "/", len(questions))
