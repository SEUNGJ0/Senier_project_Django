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
    fetch('../wsc/json/feeddata')
        // 응답 데이터를 JSON으로 파싱한다.
        .then(response => response.json())
        // 파싱된 데이터를 처리한다.
        .then(data => {
            // 선택된 날짜의 먹이 기록을 찾는다.
                // 날짜 양식 맞춤
            const ModifiedMonth = (selectedMonth + 1).toString().padStart(2, '0'); 
            const feedings = data.Pet_daily_feed.find(feed => feed.date === `${selectedYear}-${ModifiedMonth}-${selectedDate}`);
            // 선택된 날짜에 먹이 기록이 있다면
            if (feedings) {
                // HTML에서 먹이 기록 리스트 요소를 찾는다.
                const feedingsList = document.querySelector('.feedings');
                // 기존에 있는 먹이 기록 리스트 요소의 HTML을 지운다.
                feedingsList.innerHTML = '';
                // 선택된 날짜의 모든 먹이 기록에 대해
                feedings.feedings.forEach(feeding => {
                    // 새로운 HTML 요소를 생성한다.
                    const feedingElem = document.createElement('div');
                     // 생성한 요소에 "feeding" CSS 클래스를 추가한다.
                    feedingElem.classList.add('feeding');
                    // 생성한 요소의 innerHTML을 먹이 시간, 음식, 양으로 설정한다.
                    feedingElem.innerHTML= `
                        <p>
                            <div class="feeding-time">지급 시간 : ${feeding.time}</div>
                            <div class="feeding-food">설정된 급여량 : ${feeding.feed_amount}g</div>
                            <div class="feeding-time">급여된 양 : ${feeding.feed_index}g</div>
                            <div class="feeding-amount">잔여량 : ${feeding.remain_amount}g</div>
                            <div>-----------------</div>
                        </p>
                    `;
                    // 새로운 먹이 기록 요소를 먹이 기록 리스트 요소에 추가한다.
                    feedingsList.appendChild(feedingElem);
                });
            } else {
                console.log('실패!')
                // 선택된 날짜에 먹이 기록이 없다면, 먹이 기록 리스트 요소의 HTML을 변경해 메시지를 표시한다.
                document.querySelector('.feedings').innerHTML = '<div class="no-feedings">No feedings found for this day</div>';
            }
        })
        // fetch 및 데이터 처리 중에 발생하는 모든 오류를 처리한다.
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