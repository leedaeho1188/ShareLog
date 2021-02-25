const toggleBtn = document.querySelector('.navbar_toogleBtn')
const menu = document.querySelector('.navbar_menu')
const button = document.querySelector('.navbar_writeBtn')

toggleBtn.addEventListener('click', () => {
  menu.classList.toggle('active');
  button.classList.toggle('active')
})

