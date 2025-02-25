document.addEventListener('DOMContentLoaded', () => {
    const slider = document.querySelector('.features-slider');
    const cards = document.querySelectorAll('.feature-card');
    let index = 0;

    function slideNext() {
        index = (index + 1) % cards.length;
        slider.scrollTo({
            left: cards[index].offsetLeft,
            behavior: 'smooth'
        });
    }

    setInterval(slideNext, 5000); // Auto-slide every 5 seconds
});