const topbar = document.querySelector('.navbar');
const topbarMenu = document.querySelector('.navbar__menu')
const topbarToggle = document.querySelector('.navbar__toggle')

window.addEventListener('scroll', function () {
    topbar.classList.toggle('sticky', window.scrollY > 0);
});

topbarToggle.addEventListener('click', () => {
    topbarMenu.classList.toggle('is-visible')
})