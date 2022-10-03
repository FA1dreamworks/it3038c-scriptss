print("Please enter a word to count vowels and consonants: ")
word = input()

print('Your word is: ' + word)

vowel = 0
const = 0
for i in range(0,len(word)):

    if word[i] in ('a',"e","i","o","u"):
        vowel = vowel + 1 

    elif (word[i] >= 'a' and word[i] <= 'z'):
        const = const + 1

print('%s Total number of vowels' % vowel)
print('%s Total number of consonants' % const)
