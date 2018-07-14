const express = require('express')
const path = require('path')
const { get } = require('request')

const app = express()

app.use(express.json())
app.use(express.urlencoded({ extended: true }))

const viewsDir = path.join(__dirname, 'views')
app.use(express.static(viewsDir))
app.use(express.static(path.join(__dirname, './public')))
app.use(express.static(path.join(__dirname, './weights')))
app.use(express.static(path.join(__dirname, './dist')))
app.use(express.static(path.join(__dirname, './node_modules/axios/dist')))

app.get('/', (req, res) => res.redirect('/reconhecimento'))
app.get('/deteccao', (req, res) => res.sendFile(path.join(viewsDir, 'faceDetection.html')))
app.get('/landmarks', (req, res) => res.sendFile(path.join(viewsDir, 'detectAndDrawLandmarks.html')))
app.get('/alinhamento', (req, res) => res.sendFile(path.join(viewsDir, 'faceAlignment.html')))
app.get('/reconhecimento', (req, res) => res.sendFile(path.join(viewsDir, 'detectAndRecognizeFaces.html')))

app.listen(8000, () => console.log('Listening on port 8000!'))

function request(url, returnBuffer = true, timeout = 10000) {
  return new Promise(function(resolve, reject) {
    const options = Object.assign(
      {},
      {
        url,
        isBuffer: true,
        timeout,
        headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
      },
      returnBuffer ? { encoding: null } : {}
    )

    get(options, function(err, res) {
      if (err) return reject(err)
      return resolve(res)
    })
  })
}