const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
const count = parseInt(input[0]);
const realInput = input.slice(1);
let result = 0;
let beforeMinIdx = undefined;

for (let i = 0; i < count - 1; i++) {
  const now = realInput[i].split(" ").map((n) => parseInt(n));
  if (beforeMinIdx !== undefined) {
    now[beforeMinIdx] = 1001;
  }
  const after = realInput[i + 1].split(" ").map((n) => parseInt(n));
  console.log(now,after)
  const nowMinIdx = now.indexOf(Math.min(...now));

  const afterMinIdx = after.indexOf(Math.min(...after));

  const nowMinSum =
    Math.min(...now) + Math.min(...after.filter((e, i) => i !== nowMinIdx));
  const afterMinSum =
    Math.min(...after) + Math.min(...now.filter((e, i) => i !== afterMinIdx));

  if (nowMinSum < afterMinSum) {
    beforeMinIdx = nowMinIdx;
  } else {
    beforeMinIdx = now.indexOf(
      Math.min(...now.filter((e, i) => i !== afterMinIdx))
    );
  }
  result += now[beforeMinIdx];
  if (i === realInput.length - 2) {
    result += Math.min(...after.filter((e, i) => i !== beforeMinIdx));
  }
  realInput[i + 1] = after.join(" ");
}
console.log(result)
