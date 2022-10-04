// https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'countSwaps' function below.
 *
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function countSwaps(a) {
    let swaps = 0;
    for(let n=0;n<a.length;n++){
        for(let m=0;m<a.length - 1;m++){
            if(a[m] > a[m+1]){
                let temp = "";
                temp = a[m]
                a[m] = a[m+1]
                a[m+1] = temp
                swaps+=1
            }
        }
    }
console.log(
`Array is sorted in ${swaps} swaps.
First Element: ${a[0]}
Last Element: ${a[a.length-1]}`)
    // Write your code here

}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const a = readLine().replace(/\s+$/g, '').split(' ').map(aTemp => parseInt(aTemp, 10));

    countSwaps(a);
}
