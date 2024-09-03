from functools import reduce

def find_logest_word(word1,word2):
    word1_lenth = len(word1)
    word2_length = len(word2)
    if word1_lenth > word2_length:
        return word1
    else:
        return word2
word_list = ["search","Longest","word","bottle"]
result = reduce(find_logest_word,word_list)
print(result)