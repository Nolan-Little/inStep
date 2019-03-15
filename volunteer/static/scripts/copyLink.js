const copyBtn = document.querySelectorAll('.copyLink')
const url = document.querySelector('#url')

copyBtn.forEach((btn) => {
  btn.addEventListener('click', (e) => {
    url.select()
    document.execCommand("copy")
  })
})