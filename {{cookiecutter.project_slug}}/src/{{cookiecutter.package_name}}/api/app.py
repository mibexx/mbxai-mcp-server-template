from fastapi import FastAPI, Body
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field, ConfigDict
from typing import Any
from ..config import get_config

config = get_config()

# Import the tools
from ..project.weather import get_weather

class Tool(BaseModel):
    model_config = ConfigDict(strict=True)
    name: str = Field(description="The name of the tool")
    description: str = Field(description="The description of what the tool does")
    inputSchema: dict[str, Any] = Field(description="The input schema for the tool")
    strict: bool = Field(default=True, description="Whether the tool response is strictly validated")

# Create FastAPI app
app = FastAPI(
    title=config.name,
    description="A Model Context Protocol (MCP) tool server",
    version="0.1.0",
)

# Initialize MCP server
mcp_server = FastMCP(config.name)

# Register the tools with the MCP server
mcp_server.add_tool(get_weather)

# Legacy endpoints for backward compatibility
@app.get("/tools", response_model=list[Tool])
async def get_tools():
    """Get all available MCP tools."""
    # Use the list_tools() method to get the tools
    tools = await mcp_server.list_tools()
    return [Tool(
        name=tool.name,
        description=tool.description,
        inputSchema=tool.inputSchema,
        strict=True
    ) for tool in tools]

@app.post("/tools/{tool_name}/invoke")
async def invoke_tool(tool_name: str, arguments: dict[str, Any] = Body(...)):
    """Invoke a specific MCP tool."""
    try:
        result = await mcp_server.call_tool(tool_name, arguments=arguments)
        return result
    except Exception as e:
        return {"error": f"Error invoking tool {tool_name}: {str(e)}"}
