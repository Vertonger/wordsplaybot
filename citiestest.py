import io
import random
import os
from count import count

def word(ente, user):
    q = 0
    random.seed()
    enter = ente.lower()
    x = enter + '\n'
    j = io.open('word/'+str(user)+'FOR.REPORT.txt', 'w', encoding='utf-8')
    j.write(x)
    j.close()
    a = len(enter)
    L1 = enter[0]
    L0 = enter[a-1]
    y = io.open('word/'+str(user)+'.txt', 'a', encoding='utf-8')
    y.write('\n')
    y.close()
    y = io.open('word/'+str(user)+'.txt', 'r', encoding='utf-8')  
    text1 = y.read()
    y.close()
    c1 = text1.count(x)
    f = io.open('word_rus.txt', 'r', encoding='utf-8')
    text = f.read()
    f.close()
    c = text.count(x)
    if L0 == 'ы' or L0 == 'ъ' or L0 == 'ь':
        L0 = enter[a-2]
  #  last_word = text1[len(text1)-2]
  #  last_letter = last_word[len(last_word)-2] 
    if os.path.exists('word/'+str(user)+'LAST.txt'):
            z = io.open('word/'+str(user)+'LAST.txt', 'r', encoding='utf-8')
            text2 = z.readline()
            last_letter = text2[len(text2)-2]
            if last_letter == 'ы' or last_letter == 'ъ' or last_letter == 'ь':
                last_letter = text2[len(text2)-3]
            z.close() 
    else:
        if os.path.exists('word/'+str(user)+'.txt'):
            last_letter = L1
  #  if last_letter == 'ё' or last_letter == 'е':
  #      last_letter1 = 'е'
  #      last_letter2 = 'ё'
    if c == 0:
        word = "Я не знаю такого слова, попробуй другое"
    elif last_letter != L1 and text1 != '\n':
        z = io.open('word/'+str(user)+'LAST.txt', 'r', encoding='utf-8')
        text2 = z.readline()
        last_letter = text2[len(text2)-2]
        if last_letter == 'ы' or last_letter == 'ъ' or last_letter == 'ь':
            last_letter = text2[len(text2)-3]
        z.close() 
        word = "Ты должен назвать слово, начинающееся на букву " + last_letter.upper()
    else:
        if c1 == 0:
            f = io.open('word_rus.txt', 'r', encoding='utf-8')
            lines = f.readlines()
            r = len(lines)
            while q < 60000:
                q+=1
                i=random.randint(0,r-1)
                if lines[i][0] == L0:
                    word = lines[i].title()
                    c2 = text1.count(lines[i])
                    if c2 == 0:
                         y = io.open('word/'+str(user)+'.txt', 'a', encoding='utf-8')
                         y.write(ente.lower()+'\n')
                         y.write(word.lower()) 
                         y.close()
                         z = io.open('word/'+str(user)+'LAST.txt', 'w', encoding='utf-8')
                         z.write(word)
                         z.close()
                         count(str(user), '.R.word')
                         break
                    else:
                        word = "Поздравляю! Ты выиграл! Нажми /reset для начала новой игры"
        else:
            word = "Это слово уже было, придумай другое"
        
           
    f.close()
    return word



            