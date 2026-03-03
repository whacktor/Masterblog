📝 Flask Blog Application

A simple CRUD blog application built with Flask that stores blog posts in a JSON file instead of a database.

This project demonstrates how to:

Display blog posts
Add new posts
Update existing posts
Delete posts
Use Jinja2 templates
Persist data using a JSON file

🚀 Features

📄 View all blog posts on the homepage
➕ Add new blog posts
✏️ Edit existing blog posts
❌ Delete blog posts
💾 Data persistence using posts.json
🎨 Custom styled UI with CSS
🔁 Automatic ID generation for each post

🛠️ Technologies Used

Python 3
Flask
Jinja2 Templates
HTML5
CSS3
JSON (as storage)

📁 Project Structure
project/
│
├── app.py
├── posts.json
├── README.md
│
├── templates/
│   ├── index.html
│   ├── add.html
│   └── update.html
│
└── static/
    └── style.css
    
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create a virtual environment (recommended)
python -m venv venv

Activate it:

Windows
venv\Scripts\activate
Mac/Linux

source venv/bin/activate
3️⃣ Install dependencies
pip install flask
4️⃣ Run the application
python app.py

The app will start at:

http://127.0.0.1:5000/

📌 How It Works

Data Storage
All blog posts are stored in:
posts.json
Each blog post has the following structure:

{
  "id": 1,
  "author": "John Doe",
  "title": "My First Post",
  "content": "This is my blog post."
}

The application automatically generates a unique ID for each new post.

🔄 Available Routes
Route	Method	Description
/	GET	Display all blog posts
/add	GET, POST	Add a new blog post
/update/<id>	GET, POST	Edit an existing post
/delete/<id>	GET	Delete a blog post
📚 Learning Purpose

This project was built to practice:

Flask routing
Handling GET and POST requests
Working with forms
JSON file manipulation
CRUD operations
Basic front-end styling
Template rendering with Jinja2

⚠️ Notes

This project does not use a database.
Data is stored locally in a JSON file.
This is intended for learning purposes, not production use.
The delete route currently uses GET (for simplicity). In production, DELETE or POST would be recommended.

🎯 Future Improvements

Add flash messages (success/error notifications)
Convert delete to POST method
Add user authentication
Add timestamps to blog posts
Use a real database (e.g., SQLite)
Add pagination
Add search functionality

👨‍💻 Author

Whacktor
GitHub: https://github.com/whacktor
