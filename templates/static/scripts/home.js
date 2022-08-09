const btnScroll = document.querySelector("#scrollTop");
const btnHome = document.querySelector("#home")

btnScroll.addEventListener("click", function (){
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth",
    })
})