function Input() {
  const fs = require("fs");
  const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
  let input = fs.readFileSync(filePath).toString().split("\n");
  return input;
}

module.exports = Input;
