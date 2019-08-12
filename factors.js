const factors = ['1/2+2/6', '124/921+193/344', '43/55+31/94', '822/455+532/812', '23/54+16/55', '10/8+8/4']

function start() {
    const results = []
    for(let i = 0; i < factors.length; i++) {
        const denominadorOne = parseInt(factors[i].split('+')[0].split('/')[1])
        const denominadorTwo = parseInt(factors[i].split('+')[1].split('/')[1])
        let upOne = parseInt(factors[i].split('+')[0].split('/')[0])
        let upTwo = parseInt(factors[i].split('+')[1].split('/')[0])

        const commonDivisor = mcm(denominadorOne, denominadorTwo)
        upOne = commonDivisor / denominadorOne * upOne
        upTwo = commonDivisor / denominadorTwo * upTwo
        const fullUp = upOne + upTwo
        results.push(reduceFraction(fullUp, commonDivisor).join('/'))
    }
    console.log('Input', factors)
    console.log('Output', results)
}

function mcd(a, b) {
    if(b == 0) return a
    else return mcd(b, a % b)
}

function mcm(a, b) {
    return (a * b) / mcd(a, b)
}

function greatestCommonDivisor(a, b) {
    if(a < b) return greatestCommonDivisor(b, a)
    if(b == 0) return a
    return greatestCommonDivisor(b, a % b)
}

function reduceFraction(a, b) {
    const gcd = greatestCommonDivisor(a, b)
    return [a / gcd, b / gcd]
}

start()
