document.addEventListener('DOMContentLoaded', function(){
    
    let tableRows = document.querySelectorAll('.trow')
    tableRows.forEach(row => {
        let button = row.querySelector('.hidden');

        row.addEventListener('mouseover', () =>{
            button.classList.remove('hidden');
        })

        row.addEventListener('mouseout', () =>{
            button.classList.add('hidden');
        })
    })
    
    // Locate the share button and the tooltip below it
    let shareButton = document.getElementById('shareButton');
    let copyStatus = document.getElementById('copyStatus');

    // Add event listeners for both click and touchstart events
    shareButton.addEventListener('click', copyToClipboard)
    shareButton.addEventListener('touchstart', copyToClipboard);

    // Function to update copyStatus tooltip to indicate text was copied
    function copyToClipboard(){
        let valueToCopy = shareButton.value;

        // Write share link to clipboard
        navigator.clipboard.writeText(valueToCopy)
            .then(() => {
            console.log('Text copied to clipboard');
            copyStatus.textContent = 'Text copied to clipboard';
            })
            .catch(err => {
            console.error('Error copying text to clipboard:', err);
            });
        
    };  
});
