

function handleCellClick(clickedCellEvent) {

    const clickedCell = clickedCellEvent.target;

    // console.log(clickedCellEvent.target);
    // console.log(clickedCell.classList.contains("bingo-number-marked"))

    if (clickedCell.classList.contains("bingo-number-marked")) {
        clickedCell.className = "col game-cell bingo-number";
    } else {
        clickedCell.className = "col game-cell bingo-number-marked";
    }

    console.log(clickedCell);

}



document.querySelectorAll('.game-cell').forEach(cell => cell.addEventListener('click', handleCellClick));


