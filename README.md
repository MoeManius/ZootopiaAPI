# 🦁 Zootopia — Animal Info Website Generator

---

## 🌟 Overview

**Zootopia** is a Python project that fetches animal data dynamically from the [API Ninjas Animals API](https://api-ninjas.com/api/animals) based on user input, then generates a beautiful, responsive HTML website displaying detailed animal information.

It’s designed with a modular architecture separating **data fetching** and **website generation**, making it easy to extend or swap data sources without affecting the site rendering.

---

## 🚀 Features

- Fetch animal data by name directly from the API  
- Generate a clean, styled HTML page listing animal details (diet, lifespan, type, location, etc.)  
- Friendly message if the animal is not found  
- Uses environment variables for secure API key management  
- Responsive layout with CSS grid for cards  
- Easy to extend and maintain with clear code separation  

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.7 or newer  
- `pip` package manager  

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/zootopia.git
   cd zootopia
Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate       # On Windows use: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Create a .env file in the project root with your API key:
API_KEY=your_api_key_here
API_URL=https://api.api-ninjas.com/v1/animals

Ensure the HTML template animals_template.html is present in the directory.
▶️ Usage
Run the generator:
python animals_web_generator.py
Enter the name of an animal when prompted:
Please enter an animal: Fox

This will fetch animal data from the API and generate an animals.html file.

Open animals.html in your browser to explore the animals info!


