const form = document.querySelector('#scheduleEventForm')
const selectAlert = document.querySelector('p.selectAlert')

const nextBtn = document.querySelector('#nextBtn')
const prevBtn = document.querySelector('#prevBtn')

// establish all calendar elements

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
    this.todayColor = "bg-danger",
    this.selectedColor = "bg-primary",
    this.scheduledDateColor = "bg-secondary"
    this.handleClick = this.handleClick.bind(this)
  }

  setEventListener() {
    let calEl = this.getCurrentCal()
    calEl.removeEventListener('click', this.handleClick)
    calEl.addEventListener('click', this.handleClick)
  }

  handleClick(e) {
    this.getMonthEvents()
    // only hanldes clicks on valid date cells(td element whose text content is a date that isn't in the past)
    let target = e.target
    if (Number(target.textContent) > 0 && Number(target.textContent) < 32 && !target.classList.contains("past-day")) {
      formattedDate = formatSelectedDate(target.textContent, this.getActiveMonth(), this.getActiveYear())

      if (!target.classList.contains("selected")) {
        this.selectDate(target)
        createDateInput(formattedDate)
      } else if (target.classList.contains("selected")) {
        this.deSelectDate(target)
        removeDateInput(formattedDate)
      }
    }
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
            day.classList.add("bg-dark", "text-dark", "past-day")
          }
        }
      }
    }
    this.markScheduledDay(this.getMonthEvents())
  }


  getCurrentCal() {
    return this.allMonths[this._currentIndex]
  }

  getActiveMonth() {
    let month = this.allMonths[this._currentIndex].getAttributeNode('data-month').value
    if (month.length === 1) month = 0 + month
    return month
  }

  getActiveYear() {
    return this.allMonths[this._currentIndex].getAttributeNode('data-year').value
  }

  increaseCurrentIndex() {
    this._currentIndex++
    this.setCurrentCal()
    this.markScheduledDay(this.getMonthEvents())
  }

  decreaseCurrentIndex() {
    this._currentIndex--
    this.setCurrentCal()
    this.markScheduledDay(this.getMonthEvents())
  }

  getMonthEvents() {
   let activeCalEvents =  Array.prototype.slice.call(this.schedEventsList).filter((event) => {
     if (event.value.substring(0, 7) === `${this.getActiveYear()}-${this.getActiveMonth()}`) {
        return event
      }
    })
    return activeCalEvents
  }

  markScheduledDay(eventList) {
    let cal = this.getCurrentCal()
    let tableRows = cal.children[0].children
    for (event of eventList) {
      for (let row of tableRows) {
        for (let day of row.children) {
          // find today
          if (day.textContent === event.value.substring(8,10)) {
            day.classList.add(this.scheduledDateColor, "text-white")
          }
        }
      }
    }
  }

  setCurrentCal() {
    this.allMonths.forEach((cal) => cal.hidden = true)
    let currentCal = this.getCurrentCal()
    currentCal.hidden = false
    togglePrevBtn()
    togglenextBtn()
    this.setEventListener()
  }

  firstMonthActive() {
    if (this.getCurrentCal() === this.firstMonth) return true
  }

  lastMonthActive() {
    if (this.getCurrentCal() === this.lastMonth) return true
  }

  selectDate(target) {
    if (Number(target.textContent) === this.todaysNum) {
      target.classList.remove(this.todayColor)
    }
    target.classList.add("selected")
    target.classList.add(this.selectedColor, "text-white", "selected")
  }

  deSelectDate(target) {
    target.classList.remove(this.selectedColor, "text-white", "selected")
    if (Number(target.textContent) === this.todaysNum) target.classList.add(this.todayColor, "text-white")
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
    if (day.textContent === event.value.split('-')[2]) {
      day.classList.add("text-danger", "scheduled_event")
    }
  }
}