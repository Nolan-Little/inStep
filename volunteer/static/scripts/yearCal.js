const form = document.querySelector('#scheduleEventForm')

const mondays = document.querySelectorAll("td.mon")
const tuesdays = document.querySelectorAll("td.tue")
const wednesdays = document.querySelectorAll("td.wed")
const thursdays= document.querySelectorAll("td.thu")
const fridays = document.querySelectorAll("td.fri")
const saturdays = document.querySelectorAll("td.sat")
const sundays = document.querySelectorAll("td.sun")
const monthHeader = document.querySelector("th.month")

const today = Date().toString().split(' ')
const dayNum = Number(today[2])

console.log(today)

const months = {
  'January' : '01',
  'February' : '02',
  'March' : '03',
  'April' : '04',
  'May' : '05',
  'June' : '06',
  'July' : '07',
  'August' : '08',
  'September' : '09',
  'October' : '10',
  'November' : '11',
  'December' : '12'
}

allDays = [mondays, tuesdays, wednesdays, thursdays, fridays, saturdays, sundays]

for (dayList of allDays) {
  formatValidCalender(dayList)
}

// if item is selected removes hidden input with matching value and removes selected and styling classes
// if item is not selected add selected input and stores date value in hidden input
function toggleSelected(e) {
  if (e.target.classList.contains("selected")) {
    e.target.classList.remove("bg-primary", "text-white", "selected")
    if (Number(e.target.textContent) === dayNum) e.target.classList.add("bg-danger", "text-white")

    formattedDate = formatSelectedDate(e.target.textContent, monthHeader)
    removeDateInput(formattedDate)

  } else if (!e.target.classList.contains("selected")) {
    if (Number(e.target.textContent) === dayNum) e.target.classList.remove("bg-danger")

    e.target.classList.add("bg-primary", "text-white", "selected")
    formattedDate = formatSelectedDate(e.target.textContent, monthHeader)
    captureDateInput(formattedDate)
  }
}

// adds event listeners on current day and all future days. Greys out all past days
function formatValidCalender(dayList) {
  for (day of dayList) {
    if (Number(day.textContent) >= dayNum) {
      day.addEventListener("click", (e) => {
        toggleSelected(e)
      })
    }
    if (Number(day.textContent) === dayNum) day.classList.add("bg-danger", "text-white")
    if (Number(day.textContent) < dayNum) day.classList.add("bg-dark", "text-dark")
  }
}

// reformats the textContent of the calender square and the header into a date format
function formatSelectedDate(dayValue, monthYearHeader) {
  monthYearHeader = monthYearHeader.textContent.split(' ')
  if (dayValue.length === 1){
    dayValue =  "0" + dayValue
  }

  return formattedDate = `${monthYearHeader[1]}-${months[`${monthYearHeader[0]}`]}-${dayValue}`
}

// create a hidden input and set the value as the date parameter
function captureDateInput(date) {
  let input = document.createElement("input")
  input.setAttribute("hidden", true)
  input.setAttribute("type", "date")
  input.setAttribute("name", "selected_date")
  input.setAttribute("class", "date")
  input.value = date
  form.appendChild(input)
}

// remove hidden input of which the value is equal to the date parameter
function removeDateInput(date) {
  inputs = document.querySelectorAll('input.date')
  for (input of inputs) {
    if (input.value === date) {
      form.removeChild(input)
    }
  }
}