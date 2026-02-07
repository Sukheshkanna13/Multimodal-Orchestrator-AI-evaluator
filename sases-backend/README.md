# SASES Backend

This project is a backend service for the SASES (Student Assessment System Evaluation Service) application. It provides APIs for handling file uploads, image alignment, and evaluation of answers.

## Project Structure

```
sases-backend
├── src
│   ├── main.py               # Entry point of the application
│   ├── api
│   │   └── v1
│   │       ├── router.py     # API routing setup
│   │       ├── endpoints
│   │       │   ├── upload.py  # File upload handling
│   │       │   ├── align.py   # Image alignment processing
│   │       │   └── evaluate.py # Answer evaluation processing
│   │       └── deps.py       # Dependency injection functions
│   ├── core
│   │   └── config.py         # Configuration settings
│   ├── services
│   │   ├── alignment.py       # Image alignment service logic
│   │   ├── ocr.py            # Optical Character Recognition service logic
│   │   └── template_map.py    # Template map management logic
│   ├── models
│   │   └── schemas.py        # Data models and schemas
│   └── utils
│       ├── images.py         # Image processing utilities
│       └── io.py             # Input and output utilities
├── tests
│   ├── test_alignment.py      # Unit tests for alignment service
│   └── test_evaluate.py       # Unit tests for evaluation service
├── requirements.txt           # Python dependencies
├── pyproject.toml            # Project dependencies and configurations
├── Dockerfile                 # Docker image build instructions
├── docker-compose.yml         # Docker services configuration
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd sases-backend
   ```

2. **Install dependencies**:
   You can install the required Python packages using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the FastAPI application:
   ```
   uvicorn src.main:app --reload
   ```

4. **Access the API**:
   Open your browser and navigate to `http://localhost:8000/docs` to view the API documentation and interact with the endpoints.

## Usage Guidelines

- **File Upload**: Use the `/api/v1/upload` endpoint to upload files for processing.
- **Image Alignment**: Use the `/api/v1/align` endpoint to align images.
- **Evaluation**: Use the `/api/v1/evaluate` endpoint to evaluate answers based on aligned images.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.