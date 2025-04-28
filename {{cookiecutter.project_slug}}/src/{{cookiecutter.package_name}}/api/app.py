from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
from ..project.weather import weather_tool
from ..config import settings

# Create FastAPI app
app = FastAPI(
    title=settings.name,
    description="A Model Context Protocol (MCP) tool server",
    version="0.1.0",
)

# Initialize MCP server
mcp = FastMCP(settings.name)

# Register tools
mcp.register_tool(weather_tool)

# Mount MCP server to FastAPI app
app.mount("/mcp", mcp.app)

# Legacy endpoints for backward compatibility
@app.get("/tools")
async def get_tools():
    """Get all available MCP tools."""
    return list(mcp.tools.values())

@app.post("/tools/{tool_name}/invoke")
async def invoke_tool(tool_name: str, **kwargs):
    """Invoke a specific MCP tool."""
    if tool_name not in mcp.tools:
        return {"error": f"Tool {tool_name} not found"}
    return await mcp.tools[tool_name].invoke(**kwargs) 