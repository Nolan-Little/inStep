const copyBtn = document.querySelectorAll('.copyLink')

copyBtn.forEach((btn) => {
  btn.addEventListener('click', (e) => {
    url = e.target.nextElementSibling
    url.select()
    document.execCommand("copy")
  })
})