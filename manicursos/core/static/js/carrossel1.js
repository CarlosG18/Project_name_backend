const circles_nav1 = document.querySelectorAll('.circle-carrossel1')
const img4 = document.querySelector('.img4')
const img5 = document.querySelector('.img5')
const img6 = document.querySelector('.img6')
var index_auto_1 = 0

function Troca_circle_nav1(){
    if(index_auto_1 == 0){
        circles_nav1[0].classList.add('active1')
        circles_nav1[1].classList.remove('active1')
        circles_nav1[2].classList.remove('active1')
    }else if(index_auto_1 == 1){
        circles_nav1[0].classList.remove('active1')
        circles_nav1[1].classList.add('active1')
        circles_nav1[2].classList.remove('active1')
    }else{
        circles_nav1[0].classList.remove('active1')
        circles_nav1[1].classList.remove('active1')
        circles_nav1[2].classList.add('active1')
    }
}

circles_nav1.forEach((button, index) => {
    button.addEventListener('click', () => {
        if(index == 0){
            img4.style.right = "0"
            img5.style.right = "-100%"
            img6.style.right = "-100%"
            index_auto_1 = 0
            Troca_circle_nav1()
        }else if(index == 1){
            img4.style.right  = "100%"
            img5.style.right = "0"
            img6.style.right = "-100%"
            index_auto_1 = 1
            Troca_circle_nav1()
        }else{
            img4.style.right = "100%"
            img5.style.right = "100%"
            img6.style.right = "0"
            index_auto_1 = 2
            Troca_circle_nav1()
        }
    })
    
})

setInterval(() => {
    if(index_auto_1 == 0){
        img4.style.right = "0"
        img5.style.right = "-100%"
        img6.style.right = "-100%"
    }else if(index_auto_1 == 1){
        img4.style.right  = "100%"
        img5.style.right = "0"
        img6.style.right = "-100%"
    }else{
        img4.style.right = "100%"
        img5.style.right = "100%"
        img6.style.right = "0"
    }
    Troca_circle_nav1()

    if(index_auto_1 > 1){
        index_auto_1 = 0
    }else{
        index_auto_1++
    }

}, 6000)