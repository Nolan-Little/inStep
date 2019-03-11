copyBtn = document.querySelector('#copyLink')
url = document.querySelector('#url')

copyBtn.addEventListener('click', (e) => {
  url.select()
  document.execCommand("copy")
  console.log(url.value)
})