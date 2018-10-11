EtoF = {'bread': 'pain', 'wine': 'vin', 'with': 'avec', 'I': 'Je',
        'eat': 'mange', 'drink': 'bois', 'John': 'Jean',
        'friends': 'amis', 'and': 'et', 'of': 'du', 'red': 'rouge'}

FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I', 'mange':'eat',
        'bois':'drink', 'Jean':'John', 'amis':'friends', 'et':'and', 'du':'of',
        'rouge':'red'}

dict = {'English to French':EtoF,'French to English': FtoE}

# Splitting the phrase
phrase = 'I drink good red wine, and eat bread.'
split = []

split = phrase.split(' ')
print split

direction = 'English to French'

dictionary = dict[direction]
new_phrase = []


for x in split[:]:
    if x in dictionary.keys():
        new_phrase.append(dictionary[x])
    elif x.endswith('.'):
        join = x.split('.')
        str = join[0]
        new_phrase.append(dictionary[str])
        for c in x:
            if c == '.':
                new_phrase.append(c)
    elif x.endswith(','):
        join = x.split(',')
        str = join[0]
        new_phrase.append(dictionary[str])
        for c in x:
            if c == ',':
                new_phrase.append(c)


print new_phrase

str = ''
for x in new_phrase:
    str += x
    str += ' '

print str



