import io

def rename(x,y):
#x - message.text
#y - message.chat.id
    f = io.open('word/rating/players.txt', 'r', encoding='utf-8')
    text = f.read()
    f.close()
    number1 = text.find(y)
#    number1 - номер первого символа ID
    length = len(text)
    i = 0
    txet = ' '
#   txet - инверсированный text, но с лишним пробелом в начале
    while i < length:
        txet+=text[length-i-1] 
        i+=1
    rebmun1 = length + 1 - number1   
    rebmun2 = txet.find('\n', rebmun1) 
    number2 = length - rebmun2
    text_mass = []
    i = 0
    while i < length:
        text_mass+=text[i] 
        i+=1
    end = number1 - 3
    i = 0
    while i < number2 + 1:
        if i == 0:
            text_new = text_mass[0]
        else:
            text_new+=text_mass[i]
        i+=1
    text_new+=x
    i = end 
    while i < length:
        text_new+=text_mass[i]
        i+=1
    f = io.open('word/rating/players.txt', 'w', encoding='utf-8')
    f.write(text_new)
    f.close()
"""
y = str(218556652)
x = 'Bubl'
f = io.open('word/rating/players.txt', 'r', encoding='utf-8')
text = f.read()
f.close()
number1 = text.find(y)
#    number1 - номер первого символа ID
length = len(text)
i = 0
txet = ' '
#   txet - инверсированный text, но с лишним пробелом в начале
while i < length:
    txet+=text[length-i-1] 
    i+=1
rebmun1 = length + 1 - number1   
rebmun2 = txet.find('\n', rebmun1) 
number2 = length - rebmun2
text_mass = []
i = 0
while i < length:
    text_mass+=text[i] 
    i+=1
end = number1 - 3
i = 0
while i < number2 + 1:
    if i == 0:
        text_new = text_mass[0]
    else:
        text_new+=text_mass[i]
    i+=1
text_new+=x
i = end 
while i < length:
    text_new+=text_mass[i]
    i+=1
f = io.open('word/rating/players.txt', 'w', encoding='utf-8')
f.write(text_new)
f.close()"""
