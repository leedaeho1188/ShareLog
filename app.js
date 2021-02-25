const toggleBtn = document.querySelector('.navbar_toogleBtn')
const menu = document.querySelector('.navbar_menu')
const writeBtn = document.querySelector('.navbar_writeBtn')


toggleBtn.addEventListener('click', () => {
  menu.classList.toggle('active');
  writeBtn.classList.toggle('active')
})
