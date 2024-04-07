const circles_nav = document.querySelectorAll('.circle-carrossel')
const img1 = document.querySelector('.img1')
const img2 = document.querySelector('.img2')
const img3 = document.querySelector('.img3')
var index_auto = 0

console.log(circles_nav)

function Troca_circle_nav(){
    console.log("entrou")
    if(index_auto == 0){
        circles_nav[0].classList.add('active')
        circles_nav[1].classList.remove('active')
        circles_nav[2].classList.remove('active')
        console.log("entrou 0")
    }else if(index_auto == 1){
        circles_nav[0].classList.remove('active')
        circles_nav[1].classList.add('active')
        circles_nav[2].classList.remove('active')
        console.log("entrou 1")
    }else{
        circles_nav[0].classList.remove('active')
        circles_nav[1].classList.remove('active')
        circles_nav[2].classList.add('active')
        console.log("entrou 2")
    }
}

circles_nav.forEach((button, index) => {
    button.addEventListener('click', () => {
        if(index == 0){
            img1.style.right = "0"
            img2.style.right = "-100%"
            img3.style.right = "-100%"
            index_auto = 0
            Troca_circle_nav()
        }else if(index == 1){
            img1.style.right  = "100%"
            img2.style.right = "0"
            img3.style.right = "-100%"
            index_auto = 1
            Troca_circle_nav()
        }else{
            img1.style.right = "100%"
            img2.style.right = "100%"
            img3.style.right = "0"
            index_auto = 2
            Troca_circle_nav()
        }
    })
    
})

setInterval(() => {
    if(index_auto == 0){
        img1.style.right = "0"
        img2.style.right = "-100%"
        img3.style.right = "-100%"
    }else if(index_auto == 1){
        img1.style.right  = "100%"
        img2.style.right = "0"
        img3.style.right = "-100%"
    }else{
        img1.style.right = "100%"
        img2.style.right = "100%"
        img3.style.right = "0"
    }
    console.log("auto")
    Troca_circle_nav()

    if(index_auto > 1){
        index_auto = 0
    }else{
        index_auto++
    }
}, 6000)