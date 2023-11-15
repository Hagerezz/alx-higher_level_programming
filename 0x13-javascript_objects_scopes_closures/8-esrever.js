#!/usr/bin/node
exports.esrever = function (list) {
  const l = [];
  for (let i = 0; i < list.length; i++) {
    l[i] = list[list.length - i - 1];
  }
  return (l);
};
