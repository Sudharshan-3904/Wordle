const gameBoard = document.getElementById('game-board');
const message = document.getElementById('message');
let currentRow = 0;
let currentCol = 0;
let gameOver = false;

document.addEventListener('keydown', handleKeyPress);

function handleKeyPress(event) {
    if (gameOver) return;

    if (event.key === 'Enter') {
        if (currentCol === 5) submitGuess();
        return;
    }

    if (event.key === 'Backspace') {
        if (currentCol > 0) {
            currentCol--;
            const cell = gameBoard.children[currentRow].children[currentCol];
            cell.textContent = '';
        }
        return;
    }

    if (currentCol < 5 && event.key.match(/^[a-zA-Z]$/)) {
        const cell = gameBoard.children[currentRow].children[currentCol];
        cell.textContent = event.key.toUpperCase();
        currentCol++;
    }
}

async function submitGuess() {
    const row = gameBoard.children[currentRow];
    const guess = Array.from(row.children)
        .map(cell => cell.textContent)
        .join('')
        .toLowerCase();

    const response = await fetch('/check_guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ guess }),
    });

    const data = await response.json();
    updateUI(data);
}

function updateUI(data) {
    const row = gameBoard.children[currentRow];
    
    data.feedback.forEach((result, index) => {
        const cell = row.children[index];
        cell.classList.add(result.status);
    });

    if (data.is_correct) {
        gameOver = true;
        message.textContent = 'Congratulations!';
        return;
    }

    if (currentRow === 5) {
        gameOver = true;
        message.textContent = 'Game Over!';
        return;
    }

    currentRow++;
    currentCol = 0;
}