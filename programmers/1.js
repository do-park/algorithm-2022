function solution(v) {
    var x = [];
    var y = [];

    v.forEach((item) => {
        x.push(item[0]);
        y.push(item[1]);
    })
    x.sort();
    y.sort();

    return [x[0] === x[1] ? x[2] : x[0], y[0] === y[1] ? y[2] : y[0]];
}