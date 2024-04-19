document.addEventListener("DOMContentLoaded", () => {
        const images = document.querySelectorAll(".loading-image");
        images.forEach((item) => {
            item.setAttribute("style", "display: block;");
            item.previousElementSibling.setAttribute("style", "display: none;");
        });
});
