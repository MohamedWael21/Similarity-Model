# Similarity Model Api

This project provides a Flask-based API for finding similar images using a pre-trained EfficientNetB0 model and Milvus as the vector database.

## Features

- **Get Recommendations**: Find similar items based on vector similarity.
- **Add Items**: Upload an image and its metadata to the database.
- **Delete Items**: Remove an item from the database by its ID.
- **Dockerized**: Includes a Dockerfile for easy containerization.

## Prerequisites

- Python 3.11+
- Docker (optional, for containerized deployment)
- Access to a Milvus instance (e.g., Zilliz Cloud)

---

## Local Setup

### 1. Create a Virtual Environment

Create and activate a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv .venv

# Activate on Windows
.venv\Scripts\activate

# Activate on macOS/Linux
source .venv/bin/activate
```

### 2. Install Dependencies

Install all required packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root and add your Milvus credentials.

```env
# .env
MILVUS_URI="YOUR_MILVUS_URI"
MILVUS_TOKEN="YOUR_MILVUS_TOKEN"
```

Replace `YOUR_MILVUS_URI` and `YOUR_MILVUS_TOKEN` with your actual credentials.

### 4. Run the Application

Start the Flask development server.

```bash
python main.py
```

The API will be available at `http://127.0.0.1:5000`.

---

## Docker Deployment

### 1. Run the Docker Container

Build the Docker image using the provided `Dockerfile`.

```bash
docker-compose up --build
```

The API will be available at `http://localhost:5000`.

---

## API Endpoints

### Health Check

- **GET /health**
  - **Description**: Checks if the API is running.
  - **Success Response (200)**:
    ```json
    {
      "status": "healthy",
      "message": "Similarity Model API is running"
    }
    ```

### Get Recommendations

- **GET /api/v1/items/recommendations/:id**
  - **Description**: Finds similar items to the given `id`.
  - **Query Parameters**: `top_k` (optional, default: 5).
  - **Example**:
    ```bash
    curl "http://localhost:5000/api/v1/items/recommendations/1?top_k=3"
    ```
  - **Success Response (200)**:
    ```json
    {
      "recommendations": [2, 3, 4]
    }
    ```

### Add an Item

- **POST /api/v1/items**
  - **Description**: Adds a new item to the database.
  - **Request Body**: `multipart/form-data` with fields `id`, `category`, and `image`.
  - **Example**:
    ```bash
    curl -X POST http://localhost:5000/api/v1/items \
      -F "id=101" \
      -F "category=jackets" \
      -F "image=@/path/to/your/image.jpg"
    ```
  - **Success Response (201)**:
    ```json
    {
      "message": "Item added successfully",
      "item_id": 101,
      "vector_dimension": 1280
    }
    ```

### Delete an Item

- **DELETE /api/v1/items/:id**
  - **Description**: Deletes an item from the database by its `id`.
  - **Example**:
    ```bash
    curl -X DELETE http://localhost:5000/api/v1/items/101
    ```
  - **Success Response (200)**:
    ```json
    {
      "message": "Item with ID 101 deleted successfully"
    }
    ```
