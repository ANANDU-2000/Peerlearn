// Add this to your base.html before closing body tag
// page-transitions.js

document.addEventListener('DOMContentLoaded', () => {
    // Add transition container to body
    const transitionElement = document.createElement('div');
    transitionElement.className = 'page-transition';
    document.body.appendChild(transitionElement);

    // Handle all auth button clicks
    document.querySelectorAll('.glass-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const targetUrl = this.getAttribute('href');
            
            // Start transition
            document.body.classList.add('transition-active');
            
            // Animate current page out
            document.querySelector('.landing-container').classList.add('page-exit');
            
            // Wait for animation to complete then navigate
            setTimeout(() => {
                window.location.href = targetUrl;
            }, 800);
        });
    });
});