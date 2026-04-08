function checkVisible() {
    document.querySelectorAll('.card, .equation-box, .code-card, h1, h2, .list, .content > p').forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight) {
            el.classList.add('show');
        }
    });
}

window.addEventListener('scroll', checkVisible);
window.addEventListener('load', checkVisible);
checkVisible();