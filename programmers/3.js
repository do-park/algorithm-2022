function solution(n) {
    var answer = [];
    for(var i=0; i<n; i++) {
        answer.push(i+1);
    }
    return answer;
}

console.log(solution(3)); // [1, 2, 3]
console.log(solution(5)); // [1, 2, 3, 4, 5]