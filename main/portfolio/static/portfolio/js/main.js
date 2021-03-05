window.addEventListener('scroll', function() {
    const topbar = document.querySelector('.topbar');
    topbar.classList.toggle('sticky', window.scrollY > 0);
});