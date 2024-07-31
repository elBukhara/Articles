document.addEventListener('DOMContentLoaded', function() {
    // Function to save scroll position
    function saveScrollPosition() {
        localStorage.setItem('scrollPosition', window.scrollY);
        localStorage.setItem('isManualNavigation', 'true'); // Set flag for manual navigation
    }

    // Function to restore scroll position
    function restoreScrollPosition() {
        const savedPosition = localStorage.getItem('scrollPosition');
        const isManualNavigation = localStorage.getItem('isManualNavigation');

        if (savedPosition && isManualNavigation === 'true') {
            window.scrollTo(0, parseInt(savedPosition));
            localStorage.removeItem('isManualNavigation'); // Clear the flag after restoring position
        }
    }

    // Select all elements with the class 'scrollable-link'
    let scrollableLinks = document.querySelectorAll('.scrollable-link');

    // Add click event listener to each element
    scrollableLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            // Prevent the default action to avoid immediate navigation
            event.preventDefault();

            // Save scroll position before navigating
            saveScrollPosition();

            // Perform the navigation manually
            window.location.href = this.getAttribute('href');
        });
    });

    // Restore scroll position when the page loads
    restoreScrollPosition();
});
