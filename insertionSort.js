// https://www.hackerrank.com/challenges/insertionsort1/submissions/code/297411630

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function () {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'insertionSort1' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY arr
 */

function insertionSort1(n, arr) {

    // Write your code here
    var el = arr[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        if (el < arr[i]) {
            let temp = arr[i];
            // arr[i] = arr[i-1];
            arr[i + 1] = arr[i];
            // arr[i-1] = temp;
            console.log(...arr);
        } else if (el > arr[i]) {
            arr[i + 1] = el;
            console.log(...arr);
            break;
        }
    }
    // Write your code here
    // var el = arr[n - 1];
    // var i = 0;
    // for (let i = n - 2; i >= 0 && el < arr[i]; i--) {
    //     arr[i + 1] = arr[i];
    //     console.log(...arr);
    // }
    // arr[i] = el;
    // console.log(...arr);
    //works for Test Case 2 but not 1
}



function main() {
    // const n = parseInt(readLine().trim(), 10);

    // const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));
    let n = 10;
    let arr = [2, 4, 6, 8, 3]
    // let arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

    insertionSort1(n, arr);
}