const dynamicText = [
    'From all genres.',
    'From all nationalities.',
    'From all languages.'
];
const dynamicTextElement = document.querySelector('.dynamic-text');
let sum = 0;
let test = 0;
setInterval(() => {
    if (test === dynamicText[sum].length) {
        setTimeout(() => {
            test = 0;
            sum++;
            if (sum === dynamicText.length) {
                sum = 0;
            }
        }, 2000);
    }
    dynamicTextElement.innerText = dynamicText[sum].substring(0, test);
    test++;
}, 200);

 