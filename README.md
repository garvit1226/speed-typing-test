# ⌨️ Speed Typing Test (CLI)

A simple and interactive **terminal-based typing speed test** built using Python’s `curses` library.
It measures your typing speed in **Words Per Minute (WPM)** and provides **real-time accuracy feedback**.

---

## 🚀 Features

* 🧠 Random text for every test
* ⚡ Live WPM calculation
* 🎯 Color-coded accuracy:

  * ✅ Green → Correct characters
  * ❌ Red → Incorrect characters
* ⌫ Backspace support
* 🔁 Continuous retry mode
* ⛔ Press `Esc` to exit anytime

---
🎥 Demo

![Recording 2026-04-01 190618](https://github.com/user-attachments/assets/81cb9695-8d02-4c2f-bac4-3d3ef29a1163)


---
## 🛠️ Tech Stack

* Python
* `curses` (terminal UI)
* `time`
* `random`

---

## 📂 Project Structure

```
.
├── main.py
├── text.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/garvit1226/speed-typing-test.git
cd speed-typing-test
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

> 📌 **Note for Windows users:**
> This project uses `windows-curses` to enable `curses` support on Windows.

---

### 3. Run the program

```
python main.py
```

---

## 📄 requirements.txt

```
windows-curses
```

---

## 📄 text.txt Format

Add multiple lines of text. One line will be randomly selected:

EXAMPLE:
```
The quick brown fox jumps over the lazy dog.
Practice makes perfect.
Consistency beats speed.
```

---

## 🎮 How to Use

1. Run the script
2. Press any key to start
3. Type the displayed text
4. Monitor your WPM live
5. Complete the sentence to finish

Controls:

* `Backspace` → Delete character
* `Esc` → Exit

---

## 🧮 WPM Formula

```
WPM = (Characters Typed / 5) / (Time in Minutes)
```

---

## 🖥️ Requirements

* Python 3.x
* Terminal/Command Prompt

---

## 💡 Future Improvements

* ⏳ Timer mode
* 🏆 High score tracking
* 🎯 Difficulty levels
* 🖼️ GUI version

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
