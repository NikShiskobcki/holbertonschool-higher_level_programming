#!/usr/bin/node

const axios = require('axios');
const path = process.argv[2];
axios.get(path).then(function (response)) {
    console.log('code: ' + response.status);
}).catch(function (error) {
    console.log('code: ' + error.response.status);
});
