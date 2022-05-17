import sys
N = int(input())
word = sys.stdin.readline().rstrip()
word_2 = sys.stdin.readline().rstrip()
vowel = ['a','e','i','o','u']
word_consonant= '' #자음만 모아두는 리스트
word_2_consonant = ''
is_consonant_same = False #is 자음 리스트 same?
is_pre_suf_same = False#is 앞뒤 same?
is_can_change = False#한 단어내 문자들로 다른단어만들기 가능?


#is_consonant_same
for i in word:
    if i not in vowel :
        word_consonant += i
for i in word_2:
    if i not in vowel :
        word_2_consonant += i
if word_consonant == word_2_consonant: is_consonant_same = True        

#is_pre_suf_same
if word[0] == word_2[0] and word[-1] == word_2[-1]:is_pre_suf_same = True

#is_can_change
if sorted(word) == sorted(word_2) : is_can_change = True

#is duramuri?
if is_consonant_same and is_pre_suf_same and is_can_change : print('YES')
else: print('NO')