# Python Wordle Game

A command-line implementation of the popular Wordle word guessing game.

## Description

This game challenges players to guess a 5-letter word in 6 attempts. After each guess, the game provides feedback using colors:

- Green: Letter is correct and in the right position
- Yellow: Letter is in the word but in the wrong position
- Gray: Letter is not in the word

## Requirements

- Python 3.x
- random-english-word-generator package

## Installation

1. Install the required package:

```
pip install random-english-word-generator
```

## How to Play

1. Run the game:

```
python wordle.py
```

2. Enter your 5-letter guess when prompted
3. Use the color-coded feedback to make your next guess
4. Try to guess the word in 6 attempts or fewer

## Features

- Random word selection from English dictionary
- Color-coded feedback
- Input validation
- 6 attempts per game
- Clear terminal display

## Author

Created by Sudharshan M Prabhu

## License

Free to use and modify
