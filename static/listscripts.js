document.addEventListener('DOMContentLoaded', function(){

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