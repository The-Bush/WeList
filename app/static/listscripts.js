document.addEventListener('DOMContentLoaded', function(){
    
    let tableRows = document.querySelectorAll('.trow')
    tableRows.forEach(row => {
        let button = row.querySelector('.hidden');

        row.addEventListener('mouseover', () =>{
            button.classList.toggle('hidden');
        })

        row.addEventListener('mouseout', () =>{
            button.classList.toggle('hidden');
        })
    })
    
    let shareButton = document.getElementById('shareButton');
    let copyStatus = document.getElementById('copyStatus');

    shareButton.addEventListener('click', () => {
    let valueToCopy = shareButton.value;
    
    navigator.clipboard.writeText(valueToCopy)
        .then(() => {
        console.log('Text copied to clipboard');
        copyStatus.textContent = 'Text copied to clipboard';
        })
        .catch(err => {
        console.error('Error copying text to clipboard:', err);
        });
    });
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    /*
    // Get the hidden buttons and the "edit" button to toggle them
    let hiddenButtons = document.querySelectorAll('.hidden');
    let editBtn = document.getElementById('edit');
    
    // Check if the toggle state is stored in sessionStorage
    let isToggled = sessionStorage.getItem('isToggled');
    if (isToggled === 'false') {
        hiddenButtons.forEach(button => button.classList.toggle('hidden'));
    }

    editBtn.addEventListener('click', function(){
        hiddenButtons.forEach(button => button.classList.toggle('hidden'));

        // Store the toggle state in sessionStorage
        sessionStorage.setItem('isToggled', hiddenButtons[0].classList.contains('hidden') ? 'true' : 'false');
    });

    */
      
});

    //let priceInput = document.getElementById("price-input");

    //priceInput.addEventListener("input", function() {
        // Get the input value
        //let value = priceInput.value;

        // Remove any non-numeric characters
        //value = value.replace(/[^\d.-]/g, "");

        // Format the value as a decimal with two decimal places
        //value = parseFloat(value).toFixed(2);

        // Add the currency symbol to the formatted value
        //value = "$" + value;

        // Set the input value to the formatted value
        //priceInput.value = value;
    //});
//})