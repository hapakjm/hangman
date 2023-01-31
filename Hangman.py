import random

word_list = [['m', 'a', 'r', 'y', 'h', 'o', 'n', 'e', 'y', 'l', 'y', 'n'],
             ['z', 'h', 'y', 'n', 'e', 'y', 'k', 'a', 'l', 'e', 'l'],
             ['k', 'e', 'l', 'v', 'i', 'n', 'j', 'o', 'h', 'n']]

choose_word_listed = random.choice(word_list)
choose_word = ""
blank_word = []
blank_word_str = ""
attempt = 0
is_finished = False
has_letter = False
chosen_letters = [""]
chosen_letters_str = ""
choose_letter = ""

for count in choose_word_listed:
    choose_word += count
    blank_word.append("_")

for count in blank_word:
    blank_word_str += count

while is_finished == False:
    print(blank_word_str)

    chosen = True

    while chosen is True:
        print(f"Your remaining attempt: {5 - attempt}")
        choose_letter = input("Guess a letter: ")

        for count in chosen_letters:
            if count == choose_letter:
                print("Guess another letter, this letter is already chosen.")
                break
            else:
                chosen = False

    chosen_letters.append(choose_letter)
    chosen_letters_str += choose_letter + " "

    print(f"Used letters: {chosen_letters_str}")

    cnt = 0

    for count in choose_word_listed:
        if count == choose_letter:
            blank_word[cnt] = choose_letter
            has_letter = True

        cnt += 1

    if has_letter != True:
        attempt += 1

    has_letter = False

    blank_word_str = ""

    for count in blank_word:
        blank_word_str += count

    if attempt == 5:
        break

    is_finished = True

    for count in blank_word:
        if count == "_":
            is_finished = False
