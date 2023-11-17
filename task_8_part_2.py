import math

# Данные о письмах
SPAM_LETTERS = 13
NO_SPAM_LETTERS = 23
all_letters = SPAM_LETTERS + NO_SPAM_LETTERS

# Данные о словах
SPAM_WORDS = 61
NO_SPAM_WORDS = 92
all_words = SPAM_WORDS + NO_SPAM_WORDS

# Первое число - вхождение в СПАМ, второе в НЕ СПАМ
list_unique_words = {
    'Prize': (1, 4),
    'Coupon': (2, 3),
    'Offer': (0, 0),
    'Million': (3, 9),
    'Cash': (5, 6),
    'Investment': (2, 1),
    'Purchase': (2, 4),
    'Money': (17, 12),
    'Gift': (28, 29),
    'Refund': (1, 24),
}

r = 0

check_letter = 'Online Money Purchase Gift Coupon Remove Investment'
words_in_check_letter = check_letter.split(' ')

# Определите вероятность того, что письмо является спамом, исходя из тренировочного набора данных.
P_letter_is_spam = SPAM_LETTERS / all_letters
P_letter_is_no_spam = NO_SPAM_LETTERS / all_letters

#Считаем количество слов, не входящих в словарь, для сглаживания по Лаплассу
for word in words_in_check_letter:
    if word not in list_unique_words.keys():
        r += 1

def calculateWordClassProbably(word, list_unique_words, check_class):
    num_unique_words = (len(list_unique_words))

    if check_class == 'спам':
        num_word_in_spam = 0

        for key in list_unique_words:
            if key == word:
                num_word_in_spam = list_unique_words[key][0]

        probably = (1 + num_word_in_spam) / (num_unique_words + r + SPAM_WORDS)
    
    elif check_class == 'не спам':
        num_word_in_no_spam = 0

        for key in list_unique_words:
            if key == word:
                num_word_in_no_spam = list_unique_words[key][1]
        
        probably = (1 + num_word_in_no_spam) / (num_unique_words + r + NO_SPAM_WORDS)

    return probably

f_spam = math.log(P_letter_is_spam)

for word in words_in_check_letter:
    probably = calculateWordClassProbably(word, list_unique_words, 'спам')
    f_spam += math.log(probably)

f_no_spam = math.log(P_letter_is_no_spam)

for word in words_in_check_letter:
    probably = calculateWordClassProbably(word, list_unique_words, 'не спам')
    f_no_spam += math.log(probably)

#Вероятность отнесения письма Online Money Purchase Gift Coupon Remove Investment к классу СПАМ
probably_letter_is_spam = 1 / (1 + math.e ** (f_no_spam - f_spam))

print(f'Вероятность, что письмо - это спам: {round(P_letter_is_spam, 3)}')
print(f'F(спам): {round(f_spam, 3)}')
print(f'F(не спам): {round(f_no_spam, 3)}')
print(f'Вероятность отнесения письма Online Money Purchase Gift Coupon Remove Investment к классу СПАМ: {round(probably_letter_is_spam, 3)}')
