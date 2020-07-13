const homeBtn = document.querySelector('.home-btn')
const navLinks = document.querySelector('.nav_links')

homeBtn.addEventListener('click',()=>{
    homeBtn.classList.toggle('open');
    navLinks.classList.toggle('open');
})