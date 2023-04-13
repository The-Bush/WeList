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
    
    let shareButton = document.getElementById('shareButton');
    let copyStatus = document.getElementById('copyStatus');

    shareButton.addEventListener('click', copyToClipboard)
    shareButton.addEventListener('touchstart', copyToClipboard);

    function copyToClipboard(){
        let valueToCopy = shareButton.value;

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
