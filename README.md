# 🪨📄✂️ Rock Paper Scissors Game

A terminal-based Rock Paper Scissors game built in Python — featuring two versions:
a beginner brute-force approach and a refactored, logic-driven version using dictionaries and functions.

---

## 🗂️ Project Architecture

```
r_p_s_game/
│
├── main.py                  # Entry point — runs the game
├── rock-paper-scissors.py   # Core game logic (both versions)
├── pyproject.toml           # Project metadata & dependency config
└── README.md                # Project documentation (this file)
```

### What Each File Does

| File | Purpose |
|------|---------|
| `main.py` | Entry point — calls `game()` from the core module |
| `rock-paper-scissors.py` | Contains V1 (brute-force) and V2 (refactored) game logic |
| `pyproject.toml` | Defines project name, version, Python version requirement |
| `README.md` | Project documentation |

---

## 🎮 How to Play

```bash
# Clone the repo
git clone https://github.com/Rohitghosh14/r_p_s_game.git
cd r_p_s_game

# Run the game
python main.py
```

### Controls

| Input | Action |
|-------|--------|
| `r` | Rock |
| `p` | Paper |
| `s` | Scissors |
| `w` | View current score / points |
| `q` | Quit the game |

---

## ✨ Features

- ✅ Random computer choice using `random.choice()`
- ✅ Win / Loss / Draw detection via dictionary lookup
- ✅ Points system (+5 win, +2.5 draw, -5 loss)
- ✅ Match counter (wins, losses tracked separately)
- ✅ Input validation with helpful error messages
- ✅ Clean exit with score summary

---

## 🔁 Version History (Inside the File)

### V1 — Brute Force (Commented Out)
The first version uses **9 separate `if` statements** to handle every possible
win/draw/loss combination manually. It works, but it's repetitive.

```python
# Example from V1:
if user_input == "rock" and computer_choice == "scissors":
    print("you win!!")
    user_win += 1
```

**Problem:** 9 conditions, lots of repeated code — hard to maintain.

---

### V2 — Refactored with Dictionary Logic ✅ (Active Version)

The second version uses a **win-map dictionary** to eliminate all that repetition:

```python
win_situation = {
    "r": "s",   # rock beats scissors
    "s": "p",   # scissors beats paper
    "p": "r"    # paper beats rock
}
```

Now win detection becomes a single lookup:

```python
elif win_situation[user_input] == pc_choice:
    print("you win!!")
```

**Much cleaner, scalable, and Pythonic.**

---

## 📚 Study Notes — Python Concepts Used

### 1. `random.choice()` vs `random.randint()`
```python
# V1 used randint to pick an index:
random_num = random.randint(0, 2)
computer_choice = op[random_num]

# V2 directly picks from the list — cleaner:
pc_choice = random.choice(choises)
```
> 💡 `random.choice(list)` is preferred when you want a random element directly.

---

### 2. Dictionary as a Logic Map
```python
win_situation = {
    "r": "s",
    "s": "p",
    "p": "r"
}
```
Instead of writing multiple `if` conditions, a dictionary maps
"what does X beat?" — turning 9 conditions into 1 lookup.

> 💡 This is called **data-driven logic** — your data (dict) drives behavior instead of hard-coded conditionals.

---

### 3. `global` Keyword
```python
win, points, losse = 0, 0, 0  # defined outside function

def game(win_situation, choises):
    global win, points, losse   # tells Python: use the outer variable, don't create a new one
    win += 1
```
> 💡 Variables inside a function are **local** by default. `global` lets a function read AND write an outer variable.
> ⚠️ Use `global` sparingly — it's better practice to return values or use a class to manage state.

---

### 4. `while True` Loop with `break`
```python
while True:
    user_input = input("...").lower()
    if user_input == "q":
        break      # exits the loop cleanly
    if user_input not in choises:
        continue   # skips to next iteration without crashing
```
> 💡 `break` = exit the loop. `continue` = skip this round, go back to top.

---

### 5. Multiple Assignment on One Line
```python
win, points, losse = 0, 0, 0
```
> 💡 Python lets you assign multiple variables at once — equivalent to three separate lines.

---

### 6. `if __name__ == "__main__"` Guard
```python
if __name__ == "__main__":
    game(win_situation, choises)
```
> 💡 This ensures `game()` only runs when you execute the file directly —
> not when it's imported as a module by another file (like `main.py`).
> This is a **best practice** for every Python script.

---

### 7. `.upper()` and `.lower()` for Input Normalization
```python
start = input("PLAY? Enter [Y]: ").upper()   # converts "y" → "Y"
user_input = input("...").lower()             # converts "R" → "r"
```
> 💡 Always normalize user input so your comparisons don't break
> when the user types uppercase by accident.

---

## 🔮 Possible Upgrades (for Portfolio Enhancement)

| Idea | Concept Practiced |
|------|-------------------|
| Add best-of-5 mode | Loop control, counters |
| Save high scores to a `.json` file | File I/O, JSON module |
| Add a GUI with `tkinter` or `CustomTkinter` | GUI development |
| Refactor state into a `Game` class | OOP, encapsulation (replaces `global`) |
| Add a leaderboard | Lists, sorting, file persistence |

---

## 👤 Author

**Rohit Ghosh** — [@Rohitghosh14](https://github.com/Rohitghosh14)

*Python learning path: Fundamentals → OOP → Projects → AI/ML Engineering*