def character_count (word):
    character_statistic = {}
    for char in word:
            if char in character_statistic:
                character_statistic[char] += 1
            else:
                character_statistic[char] = 1
    return character_statistic

string1 = 'Happiness'
print(character_count(string1))

string2 = 'smiles'
print(character_count(string2))


