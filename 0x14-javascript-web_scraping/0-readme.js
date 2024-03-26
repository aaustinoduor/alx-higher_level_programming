#!/usr/bin/node

const fs = require('fs');
// Import the built-in Node.js 'fs' module.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // use fs.readFile() to read contents of file specified as a command-line argument
  // 'utf8' specifies the encoding of the file being read

  if (error) {
    // if an error occurs during file read operation, 'error' parameter will contain an error object.
    console.error('Error reading the file:', error);

  } else {
    // if file is read successfully, 'content' parameter will contain contents of file as a string.
    console.log(content);
  }
});
