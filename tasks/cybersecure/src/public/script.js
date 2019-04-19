document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById('form-button')
    const textField = document.getElementById('form-inp')
    const resultField = document.getElementById('result')

    button.addEventListener('click', () => {
        const text = textField.value

        const init = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data: text })
        }
        
        resultField.innerHTML = 'Происходит кибершифрование...'

        fetch('/process', init).then(r => r.text()).then((r) => {
            resultField.innerHTML = 'Результат отправлен файлом! Наслаждайтесь своей киберзашифрованной строкой!'
            const element = document.createElement('a')
            element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(r))
            element.setAttribute('download', 'result')

            element.style.display = 'none'
            document.body.appendChild(element)
            element.click()

            document.body.removeChild(element)
        })
    }, false)
})

