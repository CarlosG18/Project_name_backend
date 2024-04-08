const arrow_down = document.querySelectorAll('.arrow-down')
const descricoes = document.querySelectorAll('.slide')
const footers = document.querySelectorAll('.footersmall')

arrow_down.forEach((button, index) => {
    button.addEventListener('click', () => {
        console.log(index)
        console.log(descricoes[index])
        if(descricoes[index].classList.contains('hidden')){
            descricoes[index].classList.add('show')
            descricoes[index].classList.remove('hidden')
            button.classList.add('rotate')
            footers[index].classList.remove('.margin-small-start')
            footers[index].classList.add('margin-small-end')
        }else{
            descricoes[index].classList.add('hidden')
            descricoes[index].classList.remove('show')
            button.classList.remove('rotate')
            footers[index].classList.add('.margin-small-start')
            footers[index].classList.remove('margin-small-end')
        }
        
    })
})

