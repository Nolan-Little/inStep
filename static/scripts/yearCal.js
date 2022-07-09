const form = document.querySelector('#scheduleEventForm')
const selectAlert = document.querySelector('p.selectAlert')

const nextBtn = document.querySelector('#nextBtn')
const prevBtn = document.querySelector('#prevBtn')
const submitBtn = document.querySelector('#scheduleSubmit')

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


// define color classes for any calendar indicators
class Calendar {
  constructor() {
    this._currentIndex = 0,
      this.allMonths = document.querySelectorAll("table.month"),
      this.schedEventsList = document.querySelectorAll('input.scheduled_date'),
      this.today = Date().toString().split(' '),
      this.todaysNum = Number(this.today[2]),
      this.currentMonthNum = months[this.today[1]],
      this.firstMonth = this.allMonths[0],
      this.lastMonth = this.allMonths[12],
      this.todayColor = "bg-today",
      this.selectedBgColor = "bg-selected",
      this.selectedTextColor = "text-selected",
      this.scheduledDateColor = "text-sched-date",
      this.handleClick = this.handleClick.bind(this)
  }

  setEventListener() {
    let calEl = this.getCurrentCal()
    calEl.removeEventListener('click', this.handleClick)
    calEl.addEventListener('click', this.handleClick)
  }

  handleClick(e) {
    this.getMonthEvents()
    // only hanldes clicks on valid date cells
    // (<td> element whose text content is a date that isn't in the past or doesnt already have the event scheduled)
    let target = e.target
    if (Number(target.textContent) > 0
      && Number(target.textContent) < 32
      && !target.classList.contains("past-day")
      && !target.classList.contains("sched-date")) {

      formattedDate = formatSelectedDate(target.textContent, this.getActiveMonth(), this.getActiveYear())

      if (!target.classList.contains("selected")) {
        this.selectDate(target)
        createDateInput(formattedDate)
      } else if (target.classList.contains("selected")) {
        this.deSelectDate(target)
        removeDateInput(formattedDate)
      }
    }
    toggleSubmitBtn()
  }


  setInitialState() {
    this.setCurrentCal()
    let cal = this.getCurrentCal()
    let tableRows = cal.children[0].children

    for (let row of tableRows) {
      for (let day of row.children) {
        // make sure its not a blank cell
        if (!day.classList.contains("noday")) {
          // find today
          if (Number(day.textContent) === this.todaysNum) {
            day.classList.add(this.todayColor, "text-white")
          }
          // find days before today
          if (Number(day.textContent) < this.todaysNum) {
            day.classList.add("text-dark", "past-day")
          }
        }
      }
    }
    this.markScheduledDay(this.getMonthEvents())
  }

  // returns currently active event table from allMonths nodelist
  getCurrentCal() {
    return this.allMonths[this._currentIndex]
  }

  // returns value of month as a 2 char long string i.e. 04 = april, 11 = november
  getActiveMonth() {
    let month = this.allMonths[this._currentIndex].getAttributeNode('data-month').value
    if (month.length === 1) month = 0 + month
    return month
  }

  // returns value of the year as a 4 char long string
  getActiveYear() {
    return this.allMonths[this._currentIndex].getAttributeNode('data-year').value
  }

  // iterate calender index positively set current cal state and mark dates that are scheduled for that month
  increaseCurrentIndex() {
    this._currentIndex++
    this.setCurrentCal()
    this.markScheduledDay(this.getMonthEvents())
  }

  // iterate calender index negatively set current cal state and mark dates that are scheduled for that month
  decreaseCurrentIndex() {
    this._currentIndex--
    this.setCurrentCal()
    this.markScheduledDay(this.getMonthEvents())
  }

  // filter ALL known scheduled events to a list of only those occuring with the active month
  getMonthEvents() {
    let activeCalEvents = Array.prototype.slice.call(this.schedEventsList).filter((event) => {
      if (event.value.substring(0, 7) === `${this.getActiveYear()}-${this.getActiveMonth()}`) {
        return event
      }
    })
    return activeCalEvents
  }

  // iterate over the known scheduled event and the days of the active month to mark scheduled dates
  markScheduledDay(eventList) {
    let cal = this.getCurrentCal()
    let tableRows = cal.children[0].children
    for (event of eventList) {
      for (let row of tableRows) {
        for (let day of row.children) {
          // find today
          let date = day.textContent
          if (date.length === 1) date = "0" + date

          if (date === event.value.substring(8, 10) ) {
            day.classList.add(this.scheduledDateColor, "sched-date")
          }
        }
      }
    }
  }

  // hide all calenders then mark current active calender as not hidden.
  // ensure proper state of toggle btns and calender eventlistener
  setCurrentCal() {
    this.allMonths.forEach((cal) => cal.hidden = true)
    let currentCal = this.getCurrentCal()
    currentCal.hidden = false
    togglePrevBtn()
    togglenextBtn()
    toggleSubmitBtn()
    this.setEventListener()
  }

  firstMonthActive() {
    if (this.getCurrentCal() === this.firstMonth) return true
  }

  lastMonthActive() {
    if (this.getCurrentCal() === this.lastMonth) return true
  }

  // apply and remove proper classes to show visual selection feedback
  selectDate(target) {
    if (Number(target.textContent) === this.todaysNum) {
      target.classList.remove(this.todayColor)
    }
    target.classList.remove("text-white")
    target.classList.add(this.selectedBgColor, this.selectedTextColor, "selected")
  }

  // to find today, getCurrentCalendar() === this.firstCalendar
  deSelectDate(target) {
    target.classList.remove(this.selectedBgColor, this.selectedTextColor, "selected")
    if (Number(target.textContent) === this.todaysNum && this._currentIndex === 0) target.classList.add(this.todayColor, "text-white")
  }

}




// set current display state
let calendar = new Calendar()
calendar.setInitialState()


nextBtn.addEventListener('click', () => calendar.increaseCurrentIndex())
prevBtn.addEventListener('click', () => calendar.decreaseCurrentIndex())

// hide and display prev and next btns
function togglePrevBtn() {
  if (calendar.firstMonthActive()) {
    prevBtn.classList.add("invisible")
    prevBtn.setAttribute("disabled", true)
  } else {
    prevBtn.classList.remove("invisible")
    prevBtn.removeAttribute("disabled")
  }
}

function togglenextBtn() {
  if (calendar.lastMonthActive()) {
    nextBtn.classList.add("invisible")
    nextBtn.setAttribute("disabled", true)
  } else {
    nextBtn.classList.remove("invisible")
    nextBtn.removeAttribute("disabled")
  }
}


// if no selected dates. disables submit btn
function toggleSubmitBtn() {
  inputs = document.querySelectorAll('input.date')
  if (inputs.length === 0 ) {
    submitBtn.setAttribute('disabled', true)
  } else if (inputs.length !== 0 ) {
    submitBtn.removeAttribute('disabled')
  }
}

// reformats the textContent of the calendar square and the header into a date format
function formatSelectedDate(day, month, year) {
  if (day.length === 1) day = "0" + day
  if (month.length === 1) month = "0" + month

  return formattedDate = `${year}-${month}-${day}`
}

// create a hidden input and set the value as the date parameter
function createDateInput(date) {
  let input = document.createElement("input")
  input.setAttribute("hidden", true)
  input.setAttribute("type", "date")
  input.setAttribute("name", "selected_date")
  input.setAttribute("class", "date")
  input.value = date
  form.appendChild(input)
  console.log("selection saved", input.value)
}

// remove hidden input of which the value is equal to the date parameter
function removeDateInput(date) {
  inputs = document.querySelectorAll('input.date')
  inputs.forEach((input) => {
    if (input.value === date) {
      form.removeChild(input)
      console.log("selection removed", input.value)
    }
  })
}


// TODO: refactor evaluating current events.
function evaluateEvents(day, events) {
  for (event of events) {
    console.log(day.textContent)
    if (day.textContent === event.value.split('-')[2]) {
      day.classList.add("text-danger", "scheduled_event")
    }
  }
}