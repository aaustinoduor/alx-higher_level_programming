#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const i in valsUniq) {
  const list = [];
  for (const r in totalist) {
    if (totalist[r][1] === valsUniq[i]) {
      list.unshift(totalist[r][0]);
    }
  }
  newDict[valsUniq[i]] = list;
}
console.log(newDict);
