# Daily Horoscope App

A Python desktop application that delivers your daily horoscope based on your zodiac sign. Built with **Tkinter** for the graphical user interface and powered by **The Astrologer API** (http://sandipbgt.com/theastrologer/api/).

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![API](https://img.shields.io/badge/API-The%20Astrologer-purple)

---

## Features

* Select your zodiac sign from a dropdown menu
* Fetch today's horoscope instantly
* Elegant astrology-themed user interface
* User-friendly error handling and notifications
* Desktop application built entirely with Python

---

## Getting Started

### Prerequisites

Make sure you have:

* Python 3.8 or later installed
* Internet connection (required to fetch horoscope data)

### Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/daily-horoscope-app.git
cd daily-horoscope-app
```

2. Install the required package:

```bash
pip install requests
```

3. Run the application:

```bash
python horoscope_app.py
```

---

## Dependencies

This project uses:

* `tkinter` (included with most Python installations)
* `requests`

Install requests if you don't already have it:

```bash
pip install requests
```

---

## How It Works

1. The application retrieves available zodiac signs from the API.
2. The user selects their star sign.
3. Clicking **"Reveal My Horoscope"** sends a request to the horoscope endpoint.
4. The returned horoscope is displayed in the application window.

### API Endpoints Used

Get available signs:

```http
GET http://sandipbgt.com/theastrologer/api/sunsigns/
```

Get today's horoscope:

```http
GET http://sandipbgt.com/theastrologer/api/horoscope/{sign}/today
```

---

## Project Structure

```text
daily-horoscope-app/
│
├── horoscope_app.py
├── README.md
└── requirements.txt
```

---

## Technologies Used

* Python
* Tkinter
* Requests
* REST API Integration

---

## Error Handling

The application handles:

* API connection failures
* Invalid user selections
* Unexpected server responses

Helpful pop-up messages guide the user whenever an issue occurs.

---

## Future Improvements

Potential enhancements include:

* Weekly and monthly horoscopes
* Zodiac sign descriptions
* Lucky numbers and lucky colors
* Horoscope history tracking
* Dark/light theme switching
* Packaging as a standalone executable

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request
