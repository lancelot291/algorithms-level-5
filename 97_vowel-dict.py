def solution(word):
    dict_vowels = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    weights = [625+125+25+5+1, 125+25+5+1, 25+5+1, 5+1, 1]
    answer = 0
    for i in range(len(word)):
        answer += dict_vowels[word[i]] * weights[i] + 1
    return answer

# Test cases
print(solution("AAAAE")) # Output: 6
