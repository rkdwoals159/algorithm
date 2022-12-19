// const example = [10, 100, 120, 130, 240, 3400, 2570, 450, 290, 660];
// const coinTypes = [500, 100, 50, 10];
// function answer() {
//   const ans = example.map((e) => {
//     let cnt = 0;
//     coinTypes.forEach((coin) => {
//       cnt += parseInt(e / coin);
//       e %= coin;
//     });

//     return cnt;
//   });
//   console.log(ans);
// }
// answer();
const red = "빨간색";
const blue = "파란색";
function favoriteColors(texts, ...values) {
  console.log(texts);
  console.log(values);
}

favoriteColors`제가 좋아하는색은 ${red}과 ${blue}입니다.`;
