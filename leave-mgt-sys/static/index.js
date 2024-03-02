document.addEventListener('DOMContentLoaded', function () {
    const container = document.querySelector('.container');
    const toggleBtn = document.querySelector('#sidebarToggle');
    toggleBtn.innerHTML = ">";
    // Initial text of the button
    let isSidebarHidden = false;
    
    // Function to toggle sidebar and change button text
    function toggleSidebar() {
        container.classList.toggle('collapsed');
        
        // Update button text
        isSidebarHidden = !isSidebarHidden; // Toggle the state
        toggleBtn.innerHTML = isSidebarHidden ? ">" : "<";
    }

    // Event listener for toggle button click
    toggleBtn.addEventListener('click', toggleSidebar);
});
