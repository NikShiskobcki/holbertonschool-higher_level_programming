#!/usr/bin/node

const axios = require('axios');
const path = process.argv[2];
const usr = {};
axios.get(path).then(function (response) {
  const tasks = response.data;
  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed === false) {
      continue;
    }
    if (String(tasks[i].userId) in usr) {
      usr[String(tasks[i].userId)] += 1;
    } else {
      usr[String(tasks[i].userId)] = 1;
    }
  }
  console.log(usr);
}).catch(function (error) {
  console.log(error);
});
