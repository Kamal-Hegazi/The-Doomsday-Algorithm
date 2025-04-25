# 🗓️ Doomsday Algorithm in Python

This project implements John Conway's **Doomsday Algorithm** to calculate the **day of the week** for any given date — completely offline and fast!

## 📌 What is the Doomsday Algorithm?

The Doomsday Algorithm is a method for determining the day of the week for any date in history. It uses anchor days, leap year adjustments, and known "doomsday" dates for each month.

> Example: July 4, 1776 ➜ **Thursday**

---

## 🚀 Features

- Calculates weekday for any valid date
- Handles leap years accurately
- Pure Python, no dependencies
- Easily extendable or embeddable in apps or tools

---

## 🧠 How It Works

- Calculates the **anchor day** for the century
- Applies the **doomsday rule** for the year
- Uses known **doomsday dates** for each month
- Adjusts using modular arithmetic

---

## 📦 Usage

```python
from doomsday import get_weekday

# Format: get_weekday(day, month, year)
print(get_weekday(4, 7, 1776))   # ➜ Thursday
print(get_weekday(1, 1, 2000))   # ➜ Saturday
print(get_weekday(25, 12, 2023)) # ➜ Monday
```

## 📖 References

- [Wikipedia: Doomsday Rule](https://en.wikipedia.org/wiki/Doomsday_rule)


## 💡 License

MIT License. Use it freely, contribute, or build on it!

## 🙌 Contributions
Feel free to fork, improve, or open issues. PRs are welcome!
