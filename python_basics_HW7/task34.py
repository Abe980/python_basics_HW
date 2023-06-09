# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку 
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может 
# состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу
# с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке

def get_score_a(word):
  aaa = 'еёыаояюу'
  score = 0
  for letter in word:
    if letter in aaa: score += 1
  return score

def is_rhythmicity(song):
  if len(set(map(get_score_a, song.split()))) == 1:
    return 'Парам пам-пам'
  else:
    return 'Пам парам'

print(is_rhythmicity('пара-ра-рам рам-пам-папам па-ра-па-да'))