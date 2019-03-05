let shiftInputContainer = document.querySelector('.shift-inputs')
let fragment = document.createDocumentFragment()
let addShiftBtn = document.querySelector('#addShiftInput')


addShiftBtn.addEventListener('click', (e) => {
  appendInput(e)
  shiftInputContainer.appendChild(fragment)
})


function appendInput(e) {
  current_num_input = numInputGroups(shiftInputContainer)
  let shiftInputGroup = createInputGroup(current_num_input)
  fragment.appendChild(shiftInputGroup)
}

// TODO: create input and label factory to refactor these next 1000000 lines in to something actually readable
function createInputGroup(current_num_input) {
  console.log(current_num_input)
  let inputGroupContainer = document.createElement('div')
  inputGroupContainer.setAttribute("class", "input--group")
  inputGroupContainer.setAttribute("id", `inputGroup${current_num_input}`)
  inputGroupContainer.setAttribute("name", `inputGroup${current_num_input}`)

  let startLabel = document.createElement('label')
  startLabel.setAttribute("for", `startTime${current_num_input}`)
  startLabel.textContent = "Shift Start Time"
  let startTime = document.createElement('input')
  startTime.setAttribute("type", "time")
  startTime.setAttribute("id", `startTime${current_num_input}`)
  startTime.setAttribute("name", `startTime${current_num_input}`)

  let endLabel = document.createElement('label')
  endLabel.setAttribute("for", `endTime${current_num_input}`)
  endLabel.textContent = "Shift end Time"
  let endTime = document.createElement('input')
  endTime.setAttribute("type", "time")
  endTime.setAttribute("id", `endTime${current_num_input}`)
  endTime.setAttribute("name", `endTime${current_num_input}`)

  let descriptionLabel = document.createElement('label')
  descriptionLabel.setAttribute("for", `description${current_num_input}`)
  descriptionLabel.textContent = "Shift Description"
  let description = document.createElement('input')
  description.setAttribute("type", "textArea")
  description.setAttribute("id", `description${current_num_input}`)
  description.setAttribute("name", `description${current_num_input}`)

  let numVolunteersLabel = document.createElement('label')
  numVolunteersLabel.setAttribute("for", `numVolunteers${current_num_input}`)
  numVolunteersLabel.textContent = "# Volunteers needed"
  let numVolunteers = document.createElement('input')
  numVolunteers.setAttribute("type", "number")
  numVolunteers.setAttribute("id", `numVolunteers${current_num_input}`)
  numVolunteers.setAttribute("name", `numVolunteers${current_num_input}`)


  let removeButton = document.createElement('button')
  removeButton.textContent = "Remove Shift"
  removeButton.setAttribute("type", "button")
  removeButton.addEventListener('click', (e) => {
    e.target.parentNode.remove()
  })

  inputGroupContainer.appendChild(startLabel)
  inputGroupContainer.appendChild(startTime)
  inputGroupContainer.appendChild(endLabel)
  inputGroupContainer.appendChild(endTime)
  inputGroupContainer.appendChild(numVolunteersLabel)
  inputGroupContainer.appendChild(numVolunteers)
  inputGroupContainer.appendChild(descriptionLabel)
  inputGroupContainer.appendChild(description)
  inputGroupContainer.appendChild(removeButton)

  return inputGroupContainer
}

function numInputGroups(container) {
  return container.childNodes.length
}