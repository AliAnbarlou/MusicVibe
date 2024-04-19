/*=============== SEARCH BAR JS ===============*/
const searchBar = document.querySelector("#search-bar")
const collapsePart = document.querySelector(".collapse-part")
const collapseButton = document.querySelector("#mobile-items")
const searchInput =document.querySelector("#search-desktop")
const searchBarMob = document.querySelector("#search-br")
const toggleSearchMob = () => {
    searchBarMob.classList.toggle("show-search")
}
const toggleSearch = () =>{
    searchBar.classList.toggle("show-search")
}
function collapse(){
    document.querySelector(".mobile-version").setAttribute("style","margin-top: 0;")
}
function closenav (){
    document.querySelector(".mobile-version").setAttribute("style","margin-top: -100vh;")
}
window.addEventListener('resize',()=>{
    if(window.innerWidth <= 450){
        searchInput.classList.add("d-none")
        document.querySelector(".search-mobile").classList.remove("d-none")
    }
    else{
        searchInput.classList.remove("d-none")
        document.querySelector(".search-mobile").classList.add("d-none")
    }
})
// mohkam kari
if(window.innerWidth <= 450){
    searchInput.classList.add("d-none")
    document.querySelector(".search-mobile").classList.remove("d-none")
}
else{
    searchInput.classList.remove("d-none")
    document.querySelector(".search-mobile").classList.add("d-none")
}
