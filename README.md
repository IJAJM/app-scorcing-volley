# 🏐 Volleyball Score Tracker Web App  
**Real-Time Match Scoring System for Casual Games**  

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A minimalist yet powerful web application for tracking volleyball scores in real-time. Perfect for casual matches, tournaments, or practice games.

## 🚀 Features

- ⚡ **Real-Time Updates** - Instant score synchronization
- 🎯 **Smart Scoring Rules**
  - Default maximum score cap (25 points)
  - Configurable winning points threshold
- 🔄 **One-Click Reset** - Instant match restart
- 📱 **Responsive Design** - Works on desktop and mobile
- 🛡 **Session-Based Tracking** - Maintains scores between page refreshes

## 🛠️ Installation Guide

### Prerequisites
- Python 3.7+
- pip package manager

### Quick Setup

1. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/app-scorcing-volley.git
   cd app-scorcing-volley
   ```

2. **Initialize Virtual Environment**
   ```bash
   python -m venv venv
   # Linux/MacOS
   source venv/bin/activate
   # Windows
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Application**
   ```bash
   python app.py
   ```

5. **Access Dashboard**
   Visit `http://localhost:5000` in your browser

## 📂 Project Structure

```
├── app.py                 - Main application logic
├── templates/
│   └── index.html         - Scoreboard interface
├── static/
│   └── styles.css         - Custom styling
├── requirements.txt       - Dependency list
└── README.md              - Project documentation
```

## 🌐 API Endpoints

| Endpoint         | Method | Description                     |
|------------------|--------|---------------------------------|
| `/`              | GET    | Main scoreboard interface       |
| `/update_score`  | POST   | Modify team scores (+1 point)   |
| `/reset_score`   | POST   | Reset both teams to 0           |

## 🎮 Usage Example

```python
# Sample cURL command to update Team A's score
curl -X POST -d "team=a" http://localhost:5000/update_score

# Reset all scores
curl -X POST http://localhost:5000/reset_score
```

## 🔧 Customization Options

1. **Change Maximum Score**
   ```python
   # In app.py
   max_score = 30  # Change from default 25
   ```

2. **Modify Team Names**
   ```html
   <!-- In index.html -->
   <h2>Team Panthers 🐾</h2>
   <h2>Team Hawks 🦅</h2>
   ```

3. **Add Sound Effects**
   ```javascript
   // Add to index.html
   function playScoreSound() {
       new Audio('/static/score-beep.mp3').play();
   }
   ```

## 🤝 Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/awesome-feature`)
3. Commit changes (`git commit -m 'Add awesome feature'`)
4. Push to branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

## ☕ Support Development

Love this project? Help us keep it updated:

[![Support via Saweria](https://img.shields.io/badge/☕_Support-Saweria-FF5E5B)](https://saweria.co/ijajkeyboard)

## 📜 License

Distributed under MIT License. See `LICENSE` for details.

---

**Pro Tip**: Use a large screen tablet or monitor for the best tournament experience! 📺
