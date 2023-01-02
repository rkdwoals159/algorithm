class Heap {
  constructor() {
    this.heap = [];
  }

  getLeftChildIndex = (parentIndex) => parentIndex * 2 + 1;
  getRightChildIndex = (parentIndex) => parentIndex * 2 + 2;
  getParentIndex = (childIndex) => Math.floor(childIndex - 1 / 2);
  peek = () => this.heap[0];

  heapifyDown = () => {
    let index = 0;
    const count = this.heap.length;
    const rootNode = this.heap[index];

    // 계속해서 left child 가 있을 때 까지 검사한다.
    while (this.getLeftChildIndex(index) < count) {
      const leftChildIndex = this.getLeftChildIndex(index);
      const rightChildIndex = this.getRightChildIndex(index);

      // 왼쪽, 오른쪽 중에 더 작은 노드를 찾는다
      // rightChild 가 있다면 key의 값을 비교해서 더 작은 값을 찾는다.
      // 없다면 leftChild 가 더 작은 값을 가지는 인덱스가 된다.
      const smallerChildIndex =
        rightChildIndex < count &&
        this.heap[rightChildIndex].key < this.heap[leftChildIndex].key
          ? rightChildIndex
          : leftChildIndex;

      // 자식 노드의 키 값이 루트노드보다 작다면 위로 끌어올린다.
      if (this.heap[smallerChildIndex].key <= rootNode.key) {
        this.heap[index] = this.heap[smallerChildIndex];
        index = smallerChildIndex;
      } else break;
    }

    this.heap[index] = rootNode;
  };
  heapifyUp = () => {
    let index = this.heap.length - 1;
    const lastInsertedNode = this.heap[index];

    while (index > 0) {
      const parentIndex = this.getParentIndex(index);

      if (this.heap[parentIndex].key > lastInsertedNode.key) {
        this.heap[index] = this.heap[parentIndex];
        index = parentIndex;
      } else break;
    }
    this.heap[index] = lastInsertedNode;
  };
  insert = (key, value, isPoint) => {
    const node = { key, value, isPoint };
    this.heap.push(node);
    this.heapifyUp();
  };
  remove = () => {
    const count = this.heap.length;
    const rootNode = this.heap[0];

    if (count <= 0) return undefined;
    if (count === 1) this.heap = [];
    else {
      this.heap[0] = this.heap.pop();
      this.heapifyDown();
    }
    return rootNode;
  };
}

class PriorityQueue extends Heap {
  constructor() {
    super();
  }
  enqueue = (priority, value, isPoint = false) =>
    this.insert(priority, value, isPoint);
  dequeue = () => this.remove();
  isEmpty = () => this.heap.length <= 0;
}

function Input() {
  const fs = require("fs");
  const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
  let input = fs.readFileSync(filePath).toString().split("\n");
  return input;
}
function setResult(result, n, start) {
  for (let i = 1; i <= n; i++) {
    result[i] = { priority: Infinity, visited: false, isPoint: false };
  }
  result[start] = { priority: 0, visited: false, isPoint: false };
  return result;
}
function main() {
  const input = Input();
  const tcCount = parseInt(input.shift());

  for (let tc = 0; tc < tcCount; tc++) {
    const [n, m, t] = input
      .shift()
      .split(" ")
      .map((e) => parseInt(e));
    const [start, g, h] = input
      .shift()
      .split(" ")
      .map((e) => parseInt(e));

    const roadArray = [];
    for (let i = 0; i < m; i++) {
      const temp = input
        .shift()
        .split(" ")
        .map((e) => parseInt(e));
      roadArray.push([temp[0], temp[1], temp[2]]);
      roadArray.push([temp[1], temp[0], temp[2]]);
    }
    let destinationArr = new Array(t)
      .fill()
      .map((e) => parseInt(input.shift()))
      .sort();

    destinationArr = dijkstra(start, n, roadArray, g, h, destinationArr);
    console.log(destinationArr.join(" "));
  }
}

function dijkstra(start, n, roadArray, saveA, saveB, destinationArr) {
  const Queue = new PriorityQueue();
  const result = setResult({}, n, start);
  Queue.enqueue(0, start);
  while (!Queue.isEmpty()) {
    const node = Queue.dequeue();

    const adjacent = roadArray.filter(
      ([start, end, priority]) => start === node.value
    );

    if (adjacent.length) {
      adjacent.forEach(([start, end, priority]) => {
        if (!result[end].visited) {
          if (node.key + priority < result[end].priority) {
            result[end].priority = node.key + priority;
            if (
              (start === saveA && end === saveB) ||
              (start === saveB && end === saveA) ||
              node.isPoint
            ) {
              Queue.enqueue(node.key + priority, end, true);
              result[end].isPoint = true;
            } else Queue.enqueue(node.key + priority, end, false);
          }
        }
      });
    }
  }
  return destinationArr.filter((endPoint) => {
    if (result[endPoint].isPoint) return true;
    else return false;
  });
}

main();
