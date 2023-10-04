import random


def pomiesaj(retazec):
    final_result = ''

    with open(retazec, 'r', encoding='utf-8') as fp:
        for line in fp:
            without_enter = line.replace('\n', '')
            words = without_enter.split(' ')

            for word in words:
                temp = ''
                bad_temp = ''

                for char in word:
                    if char.isalpha():
                        temp += char
                    else:
                        bad_temp += char

                if len(temp) > 2:
                    middle_part = random.sample(temp[1:-1], len(temp) - 2)
                    shuffled_word = temp[0] + ''.join(middle_part) + temp[-1] + bad_temp
                    final_result += shuffled_word + ' '
                else:
                    final_result += temp + bad_temp + ' '

            final_result = final_result.rstrip(' ')
            final_result += '\n'

        print(final_result)

    with open('poprehadzovany_text_vstup2.txt', 'w', encoding='utf-8') as fr:
        fr.write(final_result)


pomiesaj('poprehadzovany_text_vstup2.txt')