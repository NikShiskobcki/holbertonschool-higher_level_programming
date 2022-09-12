#!/usr/bin/node

const axios = require('axios');
const path = process.argv[2];
const pilot = 'https://swapi-api.hbtn.io/api/people/18/';
let count = 0;
axios.get(path).then(function (response) {
  const films = response.data.results;
  for (let i = 0; i < films.length; i++) {
    if (films[i].characters.includes(pilot)) {
      count += 1;
    }
  }
  console.log(count);
}).catch(function (error) {
  console.log(error);
});
