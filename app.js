
function loading(state) {
  const loading = document.querySelector('.loading')
  if (state) {
    loading.classList.add('active')
  } else {
    loading.classList.remove('active')

  }
}

async function loadContent() {
  const rawData = await fetch(`http://127.0.0.1:8000/api?items=10`)
  const data = await rawData.json()

  return data
}

async function injectContent() {
  loading(true)

  const container = document.querySelector('.container')
  const div = document.createElement('div')
  div.classList.add('box')

  const data = await loadContent();

  data && data.forEach(content => {
    const newDiv = div.cloneNode()

    if (content.image) {
      const img = document.createElement('img')
      img.src = content.image
      newDiv.appendChild(img)
    }

    const p = document.createElement('p')
    p.innerText = content.text
    newDiv.appendChild(p)

    loading(false)
    counter = 0;
    container.appendChild(newDiv)
  });
}

let counter = 0;

document.addEventListener('scroll', () => {

  if ((window.innerHeight + window.scrollY) >= document.body.scrollHeight) {
    counter == 0 && injectContent()
    counter++;
  }
})

window.onload = () => {
  injectContent()

}



