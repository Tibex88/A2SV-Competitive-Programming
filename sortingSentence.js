// https: //leetcode.com/submissions/detail/829194842/
/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function (s) {
    s = s.split(" ");
    let wordArr = [];
    s.forEach(word => {
        let n = word.charAt(word.length - 1)
        wordArr[n - 1] = word.replace(/[0-9]/, "")
    })
    return wordArr.join(" ");
};