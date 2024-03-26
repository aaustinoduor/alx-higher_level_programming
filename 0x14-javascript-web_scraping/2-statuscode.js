#!/usr/bin/node

const request = require('request');
// import 'request' module.

request.get(process.argv[2])
// Use 'request' module to perform an HTTP GET request to URL.

  .on('response', function (response) {
    // set up an event listener for 'response' event emitted by HTTP request.

    console.log(`code: ${response.statusCode}`);
    // log HTTP status code of response to console.
  });
