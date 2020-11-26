let nomserie = document.getElementById("search")
let boton = document.getElementById("boton")
let datos = document.getElementById("salida")


boton.addEventListener('click', () => {
    getDataFromApiHernan()
})

function getDataFromApiHernan(){
    const paso = 'https://cors-anywhere.herokuapp.com/'
    let url = 'http://127.0.0.1:5100/movies/' + nomserie.value
    fetch(paso+url)
    .then(response =>response.json())
    .then(data => {
        console.log(data)
    })
    .catch(err => console.log(err))
}