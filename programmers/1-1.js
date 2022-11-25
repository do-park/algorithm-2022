function solution(v) {
    var answer = [0, 0];

    answer[0] = v[0][0] ^ v[1][0] ^ v[2][0];
    answer[1] = v[0][1] ^ v[1][1] ^ v[2][1];

    return answer;
}