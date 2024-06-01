# Genertive AI - Quiz App

This is a Flask-based web application that generates and evaluates quiz questions using the Cohere API. The application is containerized using Docker for easy deployment.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Generate quiz questions on selected topics using the Cohere API.
- Evaluate answers for correctness and relevance.
- Track the number of correct answers.
- Easy deployment with Docker.

## Installation

### Prerequisites

- Python 3.9
- Docker
- Docker Compose
- Cohere API Key

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/flask-cohere-quiz-app.git
    cd flask-cohere-quiz-app
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project root directory with the following content:

    ```env
    COHERE_API_KEY=your_cohere_api_key
    ```

## Usage

1. **Run the Flask application:**

    ```sh
    python app.py
    ```

2. **Open your browser and go to:**

    ```
    http://localhost:8000
    ```

## Docker

### Building and Running with Docker

1. **Clone the repository:**

    ```sh
    git clone https://github.com/dhiraj9087/flask-cohere-quiz-app.git
    cd flask-cohere-quiz-app
    ```

2. **Create a `.env` file** in the project root directory with the following content:

    ```env
    COHERE_API_KEY=your_cohere_api_key
    ```

3. **Build the Docker image:**

    ```sh
    docker-compose build
    ```

4. **Run the Docker container:**

    ```sh
    docker-compose up
    ```

5. **Access the application:**

    Open your browser and navigate to `http://localhost:8000`.


## Project Structure

```
flask-cohere-quiz-app/
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── templates/
│   ├── home.html
│   ├── index.html
│   └── result.html
├── .env
└── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
