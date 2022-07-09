let shiftInputContainer = document.querySelector('.shift-inputs')
let fragment = document.createDocumentFragment()
let addShiftBtn = document.querySelector('#addShiftInput')


addShiftBtn.addEventListener('click', (e) => {
  appendInput(e)
  shiftInputContainer.appendChild(fragment)
})

function appendInput(e) {
  unique_input_num = uniqueInputId(shiftInputContainer)
  let shiftInputGroup = createInputGroup(unique_input_num)
  fragment.appendChild(shiftInputGroup)
}

// TODO: create input and label factory to refactor these next 1000000 lines in to something actually readable
function createInputGroup(unique_input_num) {
  let inputGroupContainer = document.createElement('div')
  inputGroupContainer.setAttribute("class", "input--group m-2")
  inputGroupContainer.setAttribute("id", `inputGroup${unique_input_num}`)
  inputGroupContainer.setAttribute("name", `inputGroup${unique_input_num}`)

  let inputGroupHeader = document.createElement('h5')
  inputGroupHeader.textContent = `Shift #${unique_input_num}`

  let startLabel = document.createElement('label')
  startLabel.setAttribute("for", `startTime${unique_input_num}`)
  startLabel.textContent = "Shift Start Time"
  let startTime = document.createElement('input')
  startTime.setAttribute("type", "time")
  startTime.setAttribute("id", `startTime${unique_input_num}`)
  startTime.setAttribute("name", `startTime${unique_input_num}`)

  let endLabel = document.createElement('label')
  endLabel.setAttribute("for", `endTime${unique_input_num}`)
  endLabel.textContent = "Shift end Time"
  let endTime = document.createElement('input')
  endTime.setAttribute("type", "time")
  endTime.setAttribute("id", `endTime${unique_input_num}`)
  endTime.setAttribute("name", `endTime${unique_input_num}`)

  let descriptionLabel = document.createElement('label')
  descriptionLabel.setAttribute("for", `description${unique_input_num}`)
  descriptionLabel.textContent = "Shift Description"
  let description = document.createElement('input')
  description.setAttribute("type", "textArea")
  description.setAttribute("id", `description${unique_input_num}`)
  description.setAttribute("name", `description${unique_input_num}`)

  let numVolunteersLabel = document.createElement('label')
  numVolunteersLabel.setAttribute("for", `numVolunteers${unique_input_num}`)
  numVolunteersLabel.textContent = "# Volunteers needed"
  let numVolunteers = document.createElement('input')
  numVolunteers.setAttribute("type", "number")
  numVolunteers.setAttribute("id", `numVolunteers${unique_input_num}`)
  numVolunteers.setAttribute("name", `numVolunteers${unique_input_num}`)


  let removeButton = document.createElement('button')
  removeButton.textContent = "Remove Shift"
  removeButton.setAttribute("type", "button")
  removeButton.addEventListener('click', (e) => {
    e.target.parentNode.remove()
  })

  childArr = [inputGroupHeader, startLabel, startTime, endLabel, endTime, numVolunteersLabel, numVolunteers, descriptionLabel, description, removeButton]

  appendChildren(inputGroupContainer, childArr)

  return inputGroupContainer
}

// finds the unique Id # of the last line of inputs and returns the iterated num
function uniqueInputId(container) {
  if (container.childElementCount === 0) return 1
  return Number(container.lastChild.id.slice(-1)) + 1
}

function appendChildren(container, childArr) {
  for (child of childArr) {
    container.appendChild(child)
  }
}