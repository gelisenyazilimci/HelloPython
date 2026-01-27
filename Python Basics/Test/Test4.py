person = {'first_name': 'Burak', 'last_name': 'Bakir'}

test = {'a': 1, 'b': 2, 'c': 3}

test_numbers = {3.14: 'pi', 7: 'is prime', 13: 'is prime'}


print(test)
def mergeAlternately(word1, word2):
    merged_string = str()
    for i in range(len(word1)):
        merged_string += word1[i]
        merged_string += word2[i]
    return merged_string


print(mergeAlternately('abc', 'pqr'))

