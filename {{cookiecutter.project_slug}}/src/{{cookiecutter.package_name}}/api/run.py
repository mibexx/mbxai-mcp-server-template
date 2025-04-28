import uvicorn
from .app import app, mcp_server
from ..config import settings

def main():
    """Run the FastAPI application with MCP server."""
    # Print available tools
    print(f"Available tools: {', '.join(mcp_server.tools.keys())}")
    
    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main() 