const copyBtn = document.querySelectorAll('.copyLink')

copyBtn.forEach((btn) => {
  btn.addEventListener('click', (e) => {
    url = e.target.nextElementSibling
    url.select()
    url.focus()
    url.setSelectionRange(0,999)
    document.execCommand("copy")
    url.blur()
  })
})