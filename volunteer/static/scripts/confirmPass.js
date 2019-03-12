confirmPass = document.querySelector('#id_confirm_pass')
pass = document.querySelector('#id_password')
form = document.querySelector('#user_form')
invalid_label = document.querySelector('#invalid_pass')
register = document.querySelector('#register_new')


confirmPass.addEventListener('keyup', (e) => {
  if (e.target.value === pass.value) {
    register.removeAttribute("disabled")
    invalid_label.classList.add('d-none')
  }
  else if (e.target.value !== pass.value){
    invalid_label.classList.remove('d-none')
    register.setAttribute("disabled", true)
  }
})
