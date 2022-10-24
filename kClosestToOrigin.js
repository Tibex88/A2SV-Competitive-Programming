// https://leetcode.com/submissions/detail/829234314/

/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function (points, k) {
    let sumOfSquare = (a, b) => {
        return Math.pow(a, 2) + Math.pow(b, 2)
    }
    points.sort((p1, p2) => {
        const dA = sumOfSquare(p1[0], p1[1])
        const dB = sumOfSquare(p2[0], p2[1])
        return dA - dB
    });
    let temp = []
    for (let i = 0; i < k; i++) {
        temp.push(points[i])
    };
    return temp;
};