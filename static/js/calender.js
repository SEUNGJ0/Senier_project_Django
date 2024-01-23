const date = new Date();
const monthNames = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"];
const daysOfWeek = ["일", "월", "화", "수", "목", "금", "토"];

// 현재 달력의 년도와 월 출력
const yearElem = document.querySelector('.year');
const monthElem = document.querySelector('.month');

function setYearMonth(year, month) {
    yearElem.textContent = year;
    monthElem.textContent = monthNames[month];
}

// showCalendar 함수 추가
function showCalendar(year, month) {
    // 현재 달력의 년도와 월 출력
    setYearMonth(year, month);

    // 달력에 날짜 채우기
    const datesElem = document.querySelector('.dates');
    datesElem.innerHTML = '';
    const currentMonthDays = new Date(year, month + 1, 0).getDate();
    const currentMonthFirstDay = new Date(year, month, 1).getDay();
    const today = new Date();
    for (let i = 0; i < currentMonthFirstDay; i++) {
        datesElem.innerHTML += '<div class="date"></div>';
    }
    for (let i = 1; i <= currentMonthDays; i++) {
        const dateElem = document.createElement('div');
        dateElem.classList.add('date');
        dateElem.textContent = i;
        dateElem.dataset.date = i;
        if (year === today.getFullYear() && month === today.getMonth() && i === today.getDate()) {
            dateElem.classList.add('current-date');
        }
        datesElem.appendChild(dateElem);
    }

    // 달력에 날짜가 없는 경우 클릭 이벤트 리스너를 등록하지 않음
    if (datesElem.children.length === 0) {
        return;
    }

    // 각 날짜를 클릭 이벤트에 바인딩
    const dateElems = document.querySelectorAll('.date');
    dateElems.forEach((elem) => {
        elem.addEventListener('click', handleClickDate);
    });
}


// 날짜를 클릭했을 때 실행할 함수
function handleClickDate(event) {
    // 선택한 날짜
    const selectedDateElem = event.target;
    const selectedDate = selectedDateElem.dataset.date;
    const selectedYear = yearElem.textContent;
    const selectedMonth = monthNames.indexOf(monthElem.textContent);

    // 기존에 선택한 날짜가 있다면 회색 배경을 없애기
    const selectedElems = document.querySelectorAll('.selected-date');
    selectedElems.forEach((elem) => {
        elem.classList.remove('selected-date');
    });

    // 선택한 날짜에 회색 배경 추가
    selectedDateElem.classList.add('selected-date');

    // 선택한 날짜 표시
    document.querySelector('.Select_dates').textContent = selectedDate;
    document.querySelector('.Select_year').textContent = selectedYear;
    document.querySelector('.Select_month').textContent = selectedMonth;
    document.querySelector('.resv-wrapper').style.display = 'block';

    // 지정된 URL에서 JSON 데이터를 가져온다.
    fetch('../api/daily-feeding-all')
    .then(response => response.json())
    .then(data => {
        // 날짜 양식 맞춤
        const ModifiedMonth = (selectedMonth + 1).toString().padStart(2, '0');
        const ModifiedDate = selectedDate.padStart(2, '0'); 
        // Find feeding records for the selected date
        const feedings = data.filter(feed => feed.feed_date === `${selectedYear}-${ModifiedMonth}-${ModifiedDate}`);
        // Check if there are feeding records for the selected date
        if (feedings.length > 0) {
            const feedingsList = document.querySelector('.feedings');
            feedingsList.innerHTML = ''; // Clear existing HTML

            // Loop through each feeding record for the selected date
            feedings.forEach(feeding => {
                const feedingElem = document.createElement('div');
                feedingElem.classList.add('feeding');
                feedingElem.innerHTML = `
                    <p>
                        <div class="feeding-feed_time">지급 시간 : ${feeding.feed_time}</div>
                        <div class="feeding-food">설정된 급여량 : ${feeding.feed_amount}g</div>
                        <div class="feeding-food">급여된 양 : ${feeding.feed_index ? '급여됨' : '급여되지 않음'}</div>
                        <div class="feeding-food">잔여 급식량 : ${feeding.remain_amount}g</div>
                        <div>-----------------</div>
                    </p>
                `;
                feedingsList.appendChild(feedingElem);
            });
        } else {
            // No feeding records found for the selected date
            document.querySelector('.feedings').innerHTML = '<div class="no-feedings">기록된 급식 데이터가 없습니다!</div>';
        }
    })
    .catch(error => console.error(error));

}


// 예약 창 닫기
const closeBtn = document.querySelector('.resv-close');
closeBtn.addEventListener('click', () => {
    document.querySelector('.resv-wrapper').style.display = 'none';
});

// 이전달/다음달/오늘 버튼에 이벤트 리스너 등록
const prevBtn = document.querySelector('.go-prev');
const nextBtn = document.querySelector('.go-next');
const todayBtn = document.querySelector('.go-today');

// 이전달
prevBtn.addEventListener('click', () => {
    const year = Number(yearElem.textContent);
    const month = monthNames.indexOf(monthElem.textContent) - 1;
    if (month < 0) {
        showCalendar(year - 1, 11);
    } else {
        showCalendar(year, month);
    }
});
  
// 다음달
nextBtn.addEventListener('click', () => {
const year = Number(yearElem.textContent);
const month = monthNames.indexOf(monthElem.textContent) + 1;
if (month > 11) {
    showCalendar(year + 1, 0);
} else {
    showCalendar(year, month);
}
});

// 오늘
todayBtn.addEventListener('click',() => {
    const today = new Date();
    showCalendar(today.getFullYear(), today.getMonth());
});

showCalendar(date.getFullYear(), date.getMonth());