let venueSelect = document.querySelector('#id_venue')
let nameInput = document.querySelector('#id_new_venue_name')
let locationInput = document.querySelector('#id_new_venue_location')

if (venueSelect.value == '') toggleNewVenueInputs('show')
if (venueSelect.value !== '') toggleNewVenueInputs('hide')

venueSelect.addEventListener('change', (e) => {
  if (e.target.value == '') toggleNewVenueInputs('show')
  else if (e.target.value !== '') toggleNewVenueInputs('hide')
})

function toggleNewVenueInputs(state) {
  if (state === 'hide'){
    nameInput.removeAttribute("required")
    locationInput.removeAttribute("required")
    nameInput.setAttribute("disabled", true)
    locationInput.setAttribute("disabled", true)
    nameInput.parentElement.setAttribute("hidden", true)
    locationInput.parentElement.setAttribute("hidden", true)
  }
  else if (state === 'show'){
    nameInput.setAttribute("required", true)
    locationInput.setAttribute("required", true)
    nameInput.removeAttribute("disabled")
    locationInput.removeAttribute("disabled")
    nameInput.parentElement.removeAttribute("hidden")
    locationInput.parentElement.removeAttribute("hidden")
  }

}