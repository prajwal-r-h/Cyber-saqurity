'''python program to  implementation for hacking caser capher'''

message = 'UDZ WKLV VLGH'  # encrypted message
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(letters)):
    translated = ""

    for ch in message:
        if ch in letters:
            num = letters.find(ch)
            num = num - key

            if num < 0:
                num = num + len(letters)

            translated = translated + letters[num]
        else:
            translated = translated + ch

    print('Hacking key is %s: %s' % (key, translated))
