// 'resv-wrapper' element
const resvWrapper = document.querySelector('.resv-wrapper');

// 'dates' element
const dates = document.querySelector('.dates');

// Add click event listener to each date element
dates.addEventListener('click', (event) => {
    // Get the selected date
    const selectedDate = event.target.getAttribute('data-date');
    const selectedYear = document.querySelector('.year').innerHTML;
    const selectedMonth = document.querySelector('.month').innerHTML;

    // Set the date information to the reservation window
    const selectYearElem = document.querySelector('.Select_year');
    const selectMonthElem = document.querySelector('.Select_month');
    const selectDateElem = document.querySelector('.Select_dates');

    selectYearElem.innerHTML = selectedYear;
    selectMonthElem.innerHTML = selectedMonth;
    selectDateElem.innerHTML = selectedDate;

    // Show the reservation window
    resvWrapper.style.display = 'block';
});

// Add click event listener to the close button
const resvCloseBtn = document.querySelector('.resv-close');
resvCloseBtn.addEventListener('click', () => {
    // Hide the reservation window
    resvWrapper.style.display = 'none';
});