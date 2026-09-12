# Pomodoro-in-Py

A tiny **command-line Pomodoro timer** for Windows, written in Python. It counts
down your focus and break intervals right in the terminal and fires a native
Windows toast notification (with a sound) whenever a Pomodoro or a break ends —
so you can stay in flow and let the timer tap you on the shoulder.

## What it does

- Runs a classic **Pomodoro cycle**: focus session → short break → focus → … and a
  **long break** after a configurable number of Pomodoros, then repeats.
- Live `MM:SS` countdown printed to the terminal.
- **Windows toast notification + alert sound** at the end of every focus block and break.

## Requirements

- Windows (uses Windows toast notifications and PowerShell for the alert sound)
- Python 3.7+
- [`win10toast`](https://pypi.org/project/win10toast/)

```bash
pip install win10toast
```

## Usage

All four values are **positional** and given in **seconds**:

```bash
python main.py <pomodoro_time> <short_break_time> <long_break_time> <num_pomodoros>
```

| Argument            | Meaning                                        |
| ------------------- | ---------------------------------------------- |
| `pomodoro_time`     | Length of one focus session (seconds)          |
| `short_break_time`  | Length of a short break (seconds)              |
| `long_break_time`   | Length of the long break (seconds)             |
| `num_pomodoros`     | Number of Pomodoros before the long break      |

### Example — the classic 25/5/15, long break every 4th

```bash
python main.py 1500 300 900 4
```

The script loops until you stop it with **Ctrl + C**.

## License

Free to use and modify.
