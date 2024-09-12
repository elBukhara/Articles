document.addEventListener('DOMContentLoaded', function() {
    showSuggestions();
});

function showSuggestions() {
    const searchInput = document.getElementById('search');
    const suggestionsList = document.getElementById('search-suggestions-select');

    let debounceTimer;

    searchInput.addEventListener('input', function(event) { 
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(function() {
            const query = searchInput.value;
            
            if (query.length == 0) {
                suggestionsList.innerHTML = "";
                return;
            }
            
            fetch(`/search_suggestions/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                const suggestions = searchResults(data);
                suggestionsList.innerHTML = suggestions;
            })
            .catch(error => console.error('Error fetching suggestions:', error));
        }, 300); // Adjust the delay as needed
    });
    
    // Hide suggestions when clicking outside
    document.addEventListener('click', function(event) {
        if (!searchInput.contains(event.target) && !suggestionsList.contains(event.target)) {
            suggestionsList.innerHTML = "";
        }
    });
}

function searchResults(data) {
    let suggestions = "";
    data.forEach(item => {
        suggestions += `<option value="${item.title}"></option>`;
    });

    return suggestions
}