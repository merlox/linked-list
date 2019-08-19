const stringOne = 'loop'
const stringTwo = 'pool'

console.log(`Is ${stringOne} an anagram of ${stringTwo}:`, isValidAnagram(stringOne, stringTwo))

function isValidAnagram(string1, string2) {
    let isValid = true
    let sortedOne = mergeSort(string1)
    let sortedTwo = mergeSort(string2)
    sortedOne.map((letter, i) => {
        if(letter != sortedTwo[i]) {
            isValid = false
        }
    })
    return isValid
}

function mergeSort(myString) {
    if(myString.length <= 1) {
        return myString
    }

    let result = []
    const mid = Math.ceil(myString.length / 2)
    const left = mergeSort(myString.substring(0, mid))
    const right = mergeSort(myString.substring(mid, myString.length))
    let leftIndex = 0
    let rightIndex = 0

    while(leftIndex < left.length && rightIndex < right.length) {
        if(left[leftIndex] < right[rightIndex]) {
            result.push(left[leftIndex])
            leftIndex++
        } else {
            result.push(right[rightIndex])
            rightIndex++
        }
    }

    while(leftIndex < left.length) {
        result.push(left[leftIndex])
        leftIndex++
    }

    while(rightIndex < right.length) {
        result.push(right[rightIndex])
        rightIndex++
    }

    return result
}
// [a, b, c] [d, e]
//  ^            ^
//  ^         ^
