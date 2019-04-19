const express = require('express')
const bodyParser = require('body-parser')

const app = express()

app.use('/public', express.static(__dirname + '/public'))
app.use(bodyParser.json())

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html')
})

app.post('/process', (req, res) => {
    const data = req.body.data
    if (!data)
        return res.send('Error: data is missing')
    const binKey = convertToBin('ugra_it_was_very_easyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy_task ')
    const binData = convertToBin(data)
    let result = []
    for (let i = 0; i < binData.length; i++) {
        result.push(parseInt(binData[i], 2) ^ parseInt(binKey[i % binKey.length], 2))
    }
    for (let i = 0; i < result.length; i++) {
        result[i] = String.fromCharCode(result[i])
    }
    result = result.join('')
    res.send(result)
})

app.listen(3000, (e) => {
    if (e)
        console.log(e)
})

function convertToBin(s) {
    r = []
    for (let i = 0; i < s.length; i++)
        r.push(s[i].charCodeAt(0).toString(2))
    return r
}
