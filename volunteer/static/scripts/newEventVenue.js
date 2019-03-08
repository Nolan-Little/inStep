let venueSelect = document.querySelector('#id_venue')
let nameInput = document.querySelector('#id_new_venue_name').parentElement
let locationInput = document.querySelector('#id_new_venue_location').parentElement


venueSelect.addEventListener('change', (e) => {
  if (e.target.value == '') toggleNewVenueInputs(false)
  else if (e.target.value !== '') toggleNewVenueInputs(true)
})

function toggleNewVenueInputs(boolean) {
  if (boolean){
    nameInput.setAttribute("hidden", boolean)
    locationInput.setAttribute("hidden", boolean)
  }
  else if (!boolean){
    nameInput.removeAttribute("hidden", boolean)
    locationInput.removeAttribute("hidden", boolean)
  }

}