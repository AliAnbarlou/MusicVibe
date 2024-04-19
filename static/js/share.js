
document.querySelector('#shareButton').addEventListener('click', ()=>{
    const urlToShare = window.location.href;
    
    if (navigator.share) { // Check if the Web Share API is supported
        navigator.share({
            title: document.title,
            url: urlToShare
        }).then(() => {
            console.log('Sharing success!');
        }).catch((error) => {
            console.error('Error sharing:', error);
        });
    } else {
        // Copy the URL to clipboard
        const dummyTextArea = document.createElement('textarea');
        dummyTextArea.value = urlToShare;
        document.body.appendChild(dummyTextArea);
        dummyTextArea.select();
        document.execCommand('copy');
        document.body.removeChild(dummyTextArea);
        
        // Alert that URL has been copied to clipboard
        alert("URL copied to clipboard!");
    }
});
const description = document.querySelector('.discription');
const marq = document.querySelector("#charkhande")
const txm = marq.textContent
const txd = description.textContent
function firstLetter(text) {
    let final = []
    let array = text.split(" ")
    array.forEach(item => {
        let firstLetter = item.charAt(0).toUpperCase()
        let other = item.slice(1).toLowerCase()
        final.push(firstLetter+other)
    });
    return final.join(" ")
}
marq.textContent = firstLetter(txm)
description.textContent = firstLetter(txd)
