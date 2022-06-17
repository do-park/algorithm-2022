from re import sub


def solution(new_id):
    answer = sub('[^a-z\d\-\_\.]', '', new_id.lower())
    answer = sub('\.\.+', '.', answer)
    answer = sub('^\.|\.$', '', answer)
    if answer == '':
        answer = 'a'
    answer = sub('\.$', '', answer[0:15])
    while len(answer) < 3:
        answer += answer[-1:]
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi")
print(solution("z-+.^.") == "z--")
print(solution("=.=") == "aaa")
print(solution("123_.def") == "123_.def")
print(solution("abcdefghijklmn.p") == "abcdefghijklmn")
