const form = document.querySelector('#scheduleEventForm')
const events = document.querySelectorAll('input.scheduled_date')
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
  constructor(allCalendars) {
    this._currentIndex = 0,
      this.allCalendars = document.querySelectorAll("table.month"),
      this.today = Date().toString().split(' '),
      this.todaysNum = Number(this.today[2]),
      this.currentMonthNum = months[this.today[1]],
      this.firstMonth = this.allCalendars[0],
      this.lastMonth = this.allCalendars[12],
      this.todayColor = "bg-warning",
      this.selectedColor = "bg-primary",
      this.handleClick = this.handleClick.bind(this)
  }

  setEventListener() {
    let calEl = this.getCurrentCal()
    calEl.removeEventListener('click', this.handleClick)
    calEl.addEventListener('click', this.handleClick)
  }

  handleClick(e) {
    // only hanldes clicks on valid date cells
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
    let cal = this.getCurrentCal()
    let tableRows = cal.children[0].children
    for(let row of tableRows) {
        for (let day of row.children) {
          // make sure its not a blank cell
          if (!day.classList.contains("noday")){
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
  }


  getCurrentCal() {
    return this.allCalendars[this._currentIndex]
  }

  getActiveMonth() {
    return this.allCalendars[this._currentIndex].getAttributeNode('data-month').value
  }

  getActiveYear() {
    return this.allCalendars[this._currentIndex].getAttributeNode('data-year').value
  }

  increaseCurrentIndex() {
    this._currentIndex++
    this.setCurrentCal()
  }

  decreaseCurrentIndex() {
    this._currentIndex--
    this.setCurrentCal()
  }

  setCurrentCal() {
    this.allCalendars.forEach((cal) => cal.hidden = true)
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
calendar.setCurrentCal()
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


// adds event listeners on current day and all future days. Greys out all past days
function formatValidCalendar(dayList) {
  for (day of dayList) {
    if (Number(day.textContent) >= dayNum) {
      day.addEventListener("click", (e) => {
        toggleSelectedDate(e)
      })
    }
    if (Number(day.textContent) === dayNum) day.classList.add(todayColor, "text-white")
    if (Number(day.textContent) < dayNum) day.classList.add("bg-dark", "text-dark, past-day")
    evaluateEvents(day, events)
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
  console.log(input.value)
}

// remove hidden input of which the value is equal to the date parameter
function removeDateInput(date) {
  inputs = document.querySelectorAll('input.date')
  inputs.forEach((input) => {
    if (input.value === date) {
      form.removeChild(input)
      console.log(input.value)
    }
  })
}

function evaluateEvents(day, events) {
  for (event of events) {
    if (day.textContent === event.value.split('-')[2]) {
      day.classList.add("text-danger", "scheduled_event")
    }
  }
}