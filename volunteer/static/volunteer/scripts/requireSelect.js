shifts = document.querySelectorAll('.form-check')
shiftContainer = document.querySelector('#div_id_shifts')
submitBtn = document.querySelector('#sign_up')
alert = document.querySelector('#alert')

submitBtn.setAttribute("disabled", true)
alert.removeAttribute("hidden")

shiftContainer.addEventListener('click', () => {
  isChecked(shifts)
})


function isChecked(shifts) {
  submitBtn.setAttribute("disabled", true)
  alert.removeAttribute("hidden")
  for(shift of shifts) {
    if (shift.firstElementChild.checked) {
      submitBtn.removeAttribute("disabled")
      alert.setAttribute("hidden", true)
    }
  }
}
