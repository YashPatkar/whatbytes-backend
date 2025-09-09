# Healthcare Backend API

## Requirements
- Python 3.13+
- PostgreSQL
- uv (pip install uv)

## Installation & Run

### Clone repository
```bash
git clone https://github.com/YashPatkar/whatbytes-backend.git
cd whatbytes-backend
```

### Environment Setup
```bash
# Create and activate a virtual environment
uv venv
.\.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file in the project root and add PostgreSQL database credentials.

### Run application
```bash
# Apply database migrations
python manage.py migrate

# Start server
python manage.py runserver
```

The API will be available at:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
