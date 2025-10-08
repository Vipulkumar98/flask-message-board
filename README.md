# Flask Message Board

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.2-lightgrey.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A modern, lightweight message board application built with Flask, featuring clean UI and SQLite database integration.

## Table of Contents
- [About the Project](#about-the-project)
  - [Key Features](#key-features)
  - [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Setup](#environment-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features and Roadmap](#features-and-roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About the Project

Flask Message Board is a web application that allows users to create and view messages in a simple, clean interface. It's built using Flask framework and incorporates modern Python web development practices including blueprint organization, error handling, and proper logging.

### Key Features

- 📝 Create and view messages
- 🎨 Clean, responsive user interface
- ⚡ Fast SQLite database integration
- 🔍 Custom error pages (404 handling)
- 📱 Mobile-friendly design
- 📢 Flash messages for user feedback
- 📋 Organized code structure using Blueprints
- 🔄 Environment-based configuration
- 📝 Comprehensive logging system

### Technologies Used

- **Backend Framework**: Flask 3.1.2
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3
- **Template Engine**: Jinja2
- **Python Version**: 3.13
- **Additional Libraries**:
  - python-dotenv (Environment management)
  - Werkzeug (WSGI utilities)
  - Click (Command line interface)
  - Blinker (Signals and events)

## Getting Started

### Prerequisites

- Python 3.13 or higher
- pip (Python package installer)
- Git

### Installation

1. Clone the repository
```bash
git clone https://github.com/Vipulkumar98/flask-message-board.git
cd flask-message-board
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# OR
source venv/bin/activate      # On Unix/MacOS
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

### Environment Setup

1. Create a `.env` file in the root directory:
```bash
FLASK_APP=board
FLASK_DEBUG=True
ENVIRONMENT=development
```

2. Initialize the database:
```bash
flask init-db
```

## Usage

1. Start the development server:
```bash
python -m flask run --port 8000
```

2. Open your browser and navigate to `http://localhost:8000`

<!-- Add a screenshot of the home page here -->

3. Create a new message:
   - Click "New Post" in the navigation
   - Fill in your name and message
   - Click "Save" to post

## Project Structure

```
flask-message-board/
│
├── board/                  # Main application package
│   ├── __init__.py        # Application factory
│   ├── database.py        # Database connections
│   ├── errors.py          # Error handlers
│   ├── posts.py           # Posts blueprint
│   ├── pages.py           # Pages blueprint
│   ├── schema.sql         # Database schema
│   ├── static/            # Static files (CSS)
│   └── templates/         # Jinja2 templates
│
├── .env                   # Environment variables
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Features and Roadmap

Current Features:
- ✅ Basic message board functionality
- ✅ Error handling
- ✅ User feedback system
- ✅ Responsive design
- ✅ Logging system

Planned Features:
- [ ] User authentication
- [ ] Message categories
- [ ] Rich text editor
- [ ] Image uploads
- [ ] Message search functionality
- [ ] User profiles
- [ ] Admin dashboard



## Contact

Vipulkumar98 - [GitHub Profile](https://github.com/Vipulkumar98)

Project Link: [https://github.com/Vipulkumar98/flask-message-board](https://github.com/Vipulkumar98/flask-message-board)