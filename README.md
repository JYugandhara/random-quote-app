# 🌟 Random Quote Generator

A simple Python Flask web application that displays random quotes from various themes including Motivational, Programming, Life, Funny, and Success.

## 🚀 Features

- Displays a random quote on every page load
- Quotes from 5 different themes
- Clean, modern dark UI
- REST API endpoint for quotes (`/api/quote`)

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Containerization:** Docker
- **CI/CD:** Jenkins

## 📦 Run Locally

```bash
# Clone the repository
git clone https://github.com/JYugandhara/random-quote-app.git
cd random-quote-app

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Visit `http://localhost:5000` in your browser.

## 🐳 Run with Docker

```bash
# Build the image
docker build -t random-quote-app .

# Run the container
docker run -p 5000:5000 random-quote-app
```

Visit `http://localhost:5000` in your browser.

## 🔁 CI/CD Pipeline (Jenkins)

The `Jenkinsfile` defines a 3-stage pipeline:

1. **Clone** — Checks out the source code from GitHub
2. **Build** — Builds the Docker image
3. **Push** — Pushes the image to Docker Hub

### Jenkins Setup

1. Create a Jenkins credential with ID `dockerhub-credentials` (username + password)
2. Update `DOCKER_IMAGE` in the `Jenkinsfile` with your Docker Hub username
3. Create a Pipeline job pointing to this repository

## 📁 Project Structure

random-quote-app/
├── .github/
│   └── workflows/
│       └── docker-pipeline.yml  
├── templates/
│   └── index.html
├── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── .gitignore
└── README.md

## 👤 Author

## 👤 Author
J Yugandhara — [GitHub](https://github.com/JYugandhara)