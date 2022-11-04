const CONTAINER = document.querySelector(".game-grid");
const STATUS = document.querySelector(".game-status");
const RESTART = document.querySelector(".game-restart");

let currentPlayer = "X";
let gameGrid = ["", "", "", "", "", "", "", "", ""];

//Winning possible combinations on the grid:
let arrayValidation = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
];
let templateGrid = [...CONTAINER.children];

statusRender();

//CellRender
function cellRender(cell, el) {
  cell.innerHTML = el;
}

//StatusRender
function statusRender() {
  STATUS.innerHTML = `It's ${currentPlayer} turn`;
}

//PlayerChange ok
function playerChange() {
  currentPlayer = currentPlayer === "X" ? "O" : "X";
  statusRender();
}

//ResultValidation
function resultValidation() {
  for (let i = 0; i < arrayValidation.length; i++) {
    let a = arrayValidation[i][0];
    let b = arrayValidation[i][1];
    let c = arrayValidation[i][2];
    if (
      gameGrid[a] === gameGrid[b] &&
      gameGrid[b] === gameGrid[c] &&
      gameGrid[a] !== ""
    ) {
      alert(`${currentPlayer} won!!`);
      restartGame();
      return;
    }
  }
  playerChange();
}

//CellClick
function cellClick() {
  console.log("cell clicked", this.id + " " + currentPlayer);
  if (gameGrid[this.id] !== "") {
    return;
  } // evita el click en una celda ya seleccionada
  gameGrid[this.id] = currentPlayer; // salva la jugada en el array grid
  cellRender(this, currentPlayer); //rendering de la jugada
  resultValidation();
  // fase di stallo(parità)
  if (!gameGrid.includes("")) {
    alert("no winner!");
    restartGame();
  }
}

//RestartGame
function restartGame() {
  for (let i = 0; i < gameGrid.length; i++) {
    gameGrid[i] = "";
    cellRender(templateGrid[i], "");
  }
  currentPlayer = "X";
  statusRender();
  console.log("game reseted", gameGrid);
}

// Listeners
CONTAINER.querySelectorAll(".cell").forEach((cell) =>
  cell.addEventListener("click", cellClick)
);

RESTART.addEventListener("click", restartGame);
