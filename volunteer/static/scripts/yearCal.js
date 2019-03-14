const form = document.querySelector('#scheduleEventForm')
const events = document.querySelectorAll('input.scheduled_date')
const selectAlert = document.querySelector('p.selectAlert')

const nextBtn = document.querySelector('#nextBtn')
const prevBtn = document.querySelector('#prevBtn')

// establish all calendar elements
const mondays = document.querySelectorAll("td.mon")
const tuesdays = document.querySelectorAll("td.tue")
const wednesdays = document.querySelectorAll("td.wed")
const thursdays = document.querySelectorAll("td.thu")
const fridays = document.querySelectorAll("td.fri")
const saturdays = document.querySelectorAll("td.sat")
const sundays = document.querySelectorAll("td.sun")
const monthHeader = document.querySelector("th.month")

const allCalendars = document.querySelectorAll("table.month")

const months = {
  'Jan': '01',
  'Feb': '02',
  'Mar': '03',
  'Apr': '04',
  'May': '05',
  'Jun': '06',
  'Jul': '07',
  'Aug': '08',
  'Sep': '09',
  'Oct': '10',
  'Nov': '11',
  'Dec': '12'
}

const today = Date().toString().split(' ')
const dayNum = Number(today[2])
const currentMonthNum = months[today[1]]

// define color classes for any calendar indicators
const todayColor = "bg-warning"
const selectedColor = "bg-primary"

class Calendar {
  constructor(allCalendars) {
    this._currentIndex = 0,
    this.allCalendars = allCalendars
  }
  // set current display state

  getCurrentCal() {
    return this.allCalendars[this._currentIndex]
  }

  increaseCurrentIndex() {
    this._currentIndex++
  }

  decreaseCurrentIndex() {
    this._currentIndex--
  }

  setCurrentCal() {
    this.allCalendars.forEach((cal) => cal.hidden = true)
    let currentCal = this.getCurrentCal()
    currentCal.hidden = false
    togglePrevBtn(currentCal)
    togglenextBtn(currentCal)
  }
}


// set current display state
let calendar = new Calendar(allCalendars)
togglePrevBtn(calendar.getCurrentCal())

nextBtn.addEventListener('click',() => toggleCurrentCalendar(nextBtn))
prevBtn.addEventListener('click',() => toggleCurrentCalendar(prevBtn))


// iterate current cal + or - and determine cal state
function toggleCurrentCalendar(btn) {
  if (btn === prevBtn) {
    calendar.decreaseCurrentIndex()
  } else if (btn === nextBtn) {
    calendar.increaseCurrentIndex()
    }
  calendar.setCurrentCal()
}


// hide and display prev and next btns
function togglePrevBtn(currentCalendarDisplayed) {
  if (currentCalendarDisplayed === allCalendars[0]) {
    prevBtn.classList.add("invisible")
    prevBtn.setAttribute("disabled", true)
  } else if (currentCalendarDisplayed !== allCalendars[0]) {
    prevBtn.classList.remove("invisible")
    prevBtn.removeAttribute("disabled")
  }
}

function togglenextBtn(currentCalendarDisplayed) {
  if (currentCalendarDisplayed === allCalendars[12]) {
    nextBtn.classList.add("invisible")
    nextBtn.setAttribute("disabled", true)
  } else if (currentCalendarDisplayed !== allCalendars[12]) {
    nextBtn.classList.remove("invisible")
    nextBtn.removeAttribute("disabled")
  }
}


// if item is selected removes hidden input with matching value and removes selected and styling classes
// if item is not selected add selected input and stores date value in hidden input
function toggleSelectedDate(e) {
  if (e.target.classList.contains("selected")) {
    e.target.classList.remove(selectedColor, "text-white", "selected")
    if (Number(e.target.textContent) === dayNum) e.target.classList.add(todayColor, "text-white")
    if (e.target.classList.contains("scheduled_event")) selectAlert.classList.remove("text-danger")
    formattedDate = formatSelectedDate(e.target.textContent, monthHeader)
    removeDateInput(formattedDate)

  } else if (!e.target.classList.contains("selected")) {
    if (Number(e.target.textContent) === dayNum) e.target.classList.remove(todayColor)
    if (e.target.classList.contains("scheduled_event")) selectAlert.classList.add("text-danger")
    e.target.classList.add(selectedColor, "text-white", "selected")
    formattedDate = formatSelectedDate(e.target.textContent, monthHeader)
    captureDateInput(formattedDate)
  }
}

// adds event listeners on current day and all future days. Greys out all past days
function formatValidCalendar(dayList) {
  for (day of dayList) {
    if (Number(day.textContent) >= dayNum) {
      day.addEventListener("click", (e) => {
        toggleSelectedDate(e)
      })
    }
    if (Number(day.textContent) === dayNum) day.classList.add(todayColor, "text-white")
    if (Number(day.textContent) < dayNum) day.classList.add("bg-dark", "text-dark")
    evaluateEvents(day, events)
  }
}

// reformats the textContent of the calendar square and the header into a date format
function formatSelectedDate(dayValue, monthYearHeader) {
  monthYearHeader = monthYearHeader.textContent.split(' ')
  if (dayValue.length === 1) {
    dayValue = "0" + dayValue
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


function evaluateEvents(day, events) {
  for (event of events) {
    if (day.textContent === event.value.split('-')[2]) {
      day.classList.add("text-danger", "scheduled_event")
    }
  }
}