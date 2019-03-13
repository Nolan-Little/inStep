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
  daysEventListeners(dayList)
}

monthHeader.addEventListener('click', (e) => {
  selectedDates()
})

function toggleSelected(e) {
  if (e.target.classList.contains("selected")) {
    if (Number(e.target.textContent) === dayNum) e.target.classList.add("bg-danger", "text-white")

    e.target.classList.remove("bg-primary", "text-white", "selected")
    formattedDate = formatSelectedDate(e.target.textContent, monthHeader)
    removeDateInput(formattedDate)

  } else if (!e.target.classList.contains("selected")) {
    if (Number(e.target.textContent) === dayNum) e.target.classList.remove("bg-danger", "text-white")

    e.target.classList.add("bg-primary", "text-white", "selected")
    formattedDate = formatSelectedDate(e.target.textContent, monthHeader)
    captureDateInput(formattedDate)
  }
}

function daysEventListeners(dayList) {
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

function formatSelectedDate(dayValue, monthYearHeader) {
  monthYearHeader = monthYearHeader.textContent.split(' ')
  if (dayValue.length === 1){
    dayValue =  "0" + dayValue
  }

  return formattedDate = `${monthYearHeader[1]}-${months[`${monthYearHeader[0]}`]}-${dayValue}`
}

function captureDateInput(date) {
  let input = document.createElement("input")
  input.setAttribute("hidden", true)
  input.setAttribute("type", "date")
  input.setAttribute("name", "selected_date")
  input.setAttribute("class", "date")
  input.value = date
  form.appendChild(input)
}

function removeDateInput(date) {
  inputs = document.querySelectorAll('input.date')
  for (input of inputs) {
    if (input.value === date) {
      form.removeChild(input)
    }
  }
}