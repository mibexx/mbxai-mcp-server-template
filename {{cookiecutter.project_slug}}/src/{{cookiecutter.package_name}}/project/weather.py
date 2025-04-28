from typing import Any
from modelcontextprotocol import Tool


async def get_weather(location: str) -> dict[str, Any]:
    """Get weather information for a location."""
    # This is a mock implementation
    return {
        "location": location,
        "temperature": 20,
        "condition": "sunny",
        "humidity": 65,
    }


weather_tool = Tool(
    name="get_weather",
    description="Get weather information for a location",
    function=get_weather,
    parameters={
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The location to get weather for",
            }
        },
        "required": ["location"],
    },
)
