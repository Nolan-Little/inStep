confirmPass = document.querySelector('#id_confirm_pass')
pass = document.querySelector('#id_password')
form = document.querySelector('#user_form')
invalid_label = document.createElement('p')
register = document.querySelector('#register_new')

invalid_label.textContent = "Passwords must match"
invalid_label.classList.add('text-danger', 'font-weight-bold')

confirmPass.addEventListener('keyup', (e) => {
  console.log(e)
  if (e.target.value === pass.value) {
    register.removeAttribute("disabled")
    confirmPass.parentNode.removeChild(invalid_label)
  }
  else if (e.target.value !== pass.value){
    register.setAttribute("disabled", true)
    confirmPass.parentNode.appendChild(invalid_label)
  }
})
