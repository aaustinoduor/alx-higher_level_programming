#!/usr/bin/node

const fs = require('fs');
// import built-in Node.js 'fs' module.

fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
  // use fs.writeFile() to write data to file specified as third command-line argument (process.argv[2]).
  // the data to be written is taken from fourth command-line argument (process.argv[3]).

  if (error) {
    // if an error occurs during write operation, 'error' parameter will contain an error object.
    console.error(error);
  }
});
