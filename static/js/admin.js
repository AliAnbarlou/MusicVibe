const inputName = document.querySelectorAll("input")
const textArea = document.querySelectorAll("textarea")
inputName.forEach((item) => {
    if (item.getAttribute("type") !== "file" && item.getAttribute("type") !== "hidden") {
        item.classList.add("form-control")
    }
})
textArea.forEach((item) => {
    item.classList.add("form-control")
})