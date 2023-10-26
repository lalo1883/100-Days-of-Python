


PLACE_HOLDER = '[name]'

with open('./Input/Names/invited_names.txt') as names:
    names = names.readlines()
    print(names)

with open('./Input/Letters/starting_letter.txt') as letter:
    letter_content = letter.read()

for i in names:
    strp_name = i.strip()
    new_letter = letter_content.replace(PLACE_HOLDER, strp_name)
    with open(f'./Input/Letters/letter_for_{i}.txt', mode='w') as completed_letter:
        completed_letter.write(new_letter)

