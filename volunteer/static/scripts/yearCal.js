const mondays = document.querySelectorAll("td.mon")
const tuesdays = document.querySelectorAll("td.tue")
const wednesdays = document.querySelectorAll("td.wed")
const thursdays= document.querySelectorAll("td.thu")
const fridays = document.querySelectorAll("td.fri")
const saturdays = document.querySelectorAll("td.sat")
const sundays = document.querySelectorAll("td.sun")

allDays = [mondays, tuesdays, wednesdays, thursdays, fridays, saturdays, sundays]

for (dayList of allDays) {
  daysEventListeners(dayList)
}


function toggleSelected(e) {
  if (e.target.classList.contains("selected")) {
    e.target.classList.remove("bg-primary", "text-white", "selected")
  } else if (!e.target.classList.contains("selected")) {
    e.target.classList.add("bg-primary", "text-white", "selected")
  }
}

function daysEventListeners(dayList) {
  for (day of dayList) {
    day.addEventListener("click", (e) => {
      console.log(e)
      toggleSelected(e)
    })
  }
}

