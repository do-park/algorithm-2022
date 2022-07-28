function solution(s){
    let stack = [];
    
    for (let i=0; i < s.length; i+=1 ) {
        if (s[i] === '(') {
            stack.push('(');
        } else {
            if (stack.length > 0) {
                stack.pop();
            } else {
                return false;
            }
        }
    }
    return stack.length > 0 ? false : true;
}
