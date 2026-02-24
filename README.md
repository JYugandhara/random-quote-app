# Random Quote Generator

A lightweight web application built with Python and Flask that displays random inspirational and entertaining quotes from multiple themes. Each page refresh delivers a new quote drawn from a curated collection spanning five categories.

---

## Features

- Random quote displayed on every page load
- Quotes from five themes: Motivational, Programming, Life, Funny, and Success
- Clean and modern dark-themed user interface
- REST API endpoint available at `/api/quote`
- Fully containerized with Docker

---

## Tech Stack

- **Language:** Python 3.11
- **Framework:** Flask
- **Containerization:** Docker
- **CI/CD:** Jenkins, GitHub Actions

---

## Project Structure

```
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
```

---

## Run Locally

```bash
# Clone the repository
git clone https://github.com/JYugandhara/random-quote-app.git
cd random-quote-app

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Open your browser and visit `http://localhost:5000`

---

## Run with Docker

```bash
# Build the Docker image
docker build -t random-quote-app .

# Run the container
docker run -p 5000:5000 random-quote-app
```

Open your browser and visit `http://localhost:5000`

---

## Pull from Docker Hub

```bash
docker pull yugan2125/random-quote-app:latest
docker run -p 5000:5000 yugan2125/random-quote-app:latest
```

---

## CI/CD Pipeline

### GitHub Actions

The workflow file at `.github/workflows/docker-pipeline.yml` automatically triggers on every push to the `main` branch and runs the following stages:

1. **Clone** - Checks out the source code
2. **Install Dependencies** - Installs Python packages
3. **Build** - Builds the Docker image
4. **Push** - Pushes the image to Docker Hub

To use GitHub Actions, add the following secrets in your repository settings under Settings > Secrets and variables > Actions:

| Secret Name | Description |
|---|---|
| DOCKER_USERNAME | Your Docker Hub username |
| DOCKER_PASSWORD | Your Docker Hub password |

### Jenkins

The `Jenkinsfile` defines a 3-stage pipeline:

1. **Clone** - Checks out the repository
2. **Build** - Builds the Docker image
3. **Push** - Pushes the image to Docker Hub

Add a Jenkins credential with ID `dockerhub-credentials` containing your Docker Hub username and password, then update the `DOCKER_IMAGE` variable in the Jenkinsfile with your Docker Hub username.

---

## Author

J Yugandhara - [GitHub](https://github.com/JYugandhara)