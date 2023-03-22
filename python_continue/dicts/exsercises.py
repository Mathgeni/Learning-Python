letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']

morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
         '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
         '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
         '-.--', '--..', '-----', '.----', '..---', '...--', '....-',
         '.....', '-....', '--...', '---..', '----.']
d = dict(zip(letters, morse))

sentence = input()

for i in sentence:
    for key, value in d.items():
        if i.lower() in key.lower():
            print(value, end=' ')
