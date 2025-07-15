from server import mcp

from .schemas import WeatherData


@mcp.tool()
def get_weather(city: str) -> WeatherData:
    """Get weather for a city - returns structured data."""
    # Simulated weather data
    return WeatherData(
        temperature=72.5,
        humidity=45.0,
        condition="sunny",
        wind_speed=5.2,
    )
