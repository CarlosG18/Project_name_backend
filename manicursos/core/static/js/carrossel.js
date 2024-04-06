const circles_nav = document.querySelectorAll('.circle-carrossel')
const img1 = document.querySelector('.img1')
const img2 = document.querySelector('.img2')
const img3 = document.querySelector('.img3')
var index_auto = 0

function Troca_circle_nav(){
    if(index_auto == 0){
        circles_nav[0].classList.add('active')
        circles_nav[1].classList.remove('active')
        circles_nav[2].classList.remove('active')
    }else if(index_auto == 1){
        circles_nav[0].classList.remove('active')
        circles_nav[1].classList.add('active')
        circles_nav[2].classList.remove('active')
    }else{
        circles_nav[0].classList.remove('active')
        circles_nav[1].classList.remove('active')
        circles_nav[2].classList.add('active')
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
    Troca_circle_nav()

    if(index_auto > 1){
        index_auto = 0
    }else{
        index_auto++
    }

    console.log(index_auto)
}, 6000)