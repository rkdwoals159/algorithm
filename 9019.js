const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const realInput = input.slice(1);
let minLenResult = "aaaaaaaaaaaaaaaaaaaaaaaaaaa";
function main() {
  for (let numbers of realInput) {
    const [start, end] = numbers.split(" ").map((n) => n.padStart(4, "0"));
    move(start, end, "", ["D"], 1);
    console.log(minLenResult);
    minLenResult = "aaaaaaaaaaaaaaaaaaaaaaaaaaa";
  }
}

function move(start, end, result, queue, len) {
  console.log(result);
  if (check(start, end)) {
    if (minLenResult.length >= result.length) {
      minLenResult = result;
    }
    return;
  }
  if (result.length > len) result = result.slice(0, -1);

  const now = queue.shift();
  switch (now) {
    case "D":
      start = setDouble(start);
      queue = queue.concat(["D", "S", "L", "R"]);
      result += "D";
      break;
    case "S":
      start = setSub(start);
      queue = queue.concat(["D", "S", "L", "R"]);
      result += "S";
      break;
    case "L":
      start = goLeft(start);
      queue = queue.concat(["D", "S", "L"]);
      result += "L";
      break;
    case "R":
      start = goRight(start);
      queue = queue.concat(["D", "S", "R"]);
      result += "R";
      len += 1;
      break;
  }

  move(start, end, result, queue, len);
}
function check(now, end) {
  return now === end ? true : false;
}

function setDouble(numStr) {
  const value = (parseInt(numStr) * 2) % 10000;
  return String(value).padStart(4, "0");
}

function setSub(numStr) {
  const value =
    numStr === "0000" ? "9999" : String(parseInt(numStr) - 1).padStart(4, "0");
  return value;
}
function goLeft(numStr) {
  return numStr.slice(1) + numStr[0];
}
function goRight(numStr) {
  return numStr.at(-1) + numStr.slice(0, -1);
}

main();
