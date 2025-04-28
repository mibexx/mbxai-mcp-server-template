from fastapi import FastAPI
from modelcontextprotocol import Tool, ToolRegistry
from {{cookiecutter.package_name}}.project.weather import weather_tool

app = FastAPI(
    title="{{cookiecutter.project_name}}",
    description="{{cookiecutter.description}}",
    version="0.1.0",
)

# Initialize tool registry
tool_registry = ToolRegistry()
tool_registry.register_tool(weather_tool)

@app.get("/tools")
async def get_tools() -> list[Tool]:
    """Get all available MCP tools."""
    return list(tool_registry.get_tools().values())

@app.post("/tools/{tool_name}/invoke")
async def invoke_tool(tool_name: str, **kwargs):
    """Invoke a specific MCP tool."""
    tool = tool_registry.get_tool(tool_name)
    if not tool:
        return {"error": f"Tool {tool_name} not found"}
    return await tool.invoke(**kwargs) 