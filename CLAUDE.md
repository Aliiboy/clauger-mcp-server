# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Reference Documentation

For comprehensive MCP development reference, see:
- @.claude/python-sdk.md - Complete MCP Python SDK documentation with examples


## Development Environment Setup

This is a Python MCP (Model Context Protocol) server project using `uv` as the package manager.

### Environment Commands
- `uv venv .venv` - Create virtual environment
- `.\.venv\Scripts\activate` - Activate virtual environment (Windows)
- `uv add <package>` - Add dependencies
- `uv sync` - Install dependencies from lock file

### Running the Server
- `python main.py` - Run the MCP server directly
- `uv run python main.py` - Run with uv

## Architecture

This MCP server follows a modular architecture with FastMCP:

### Core Structure
- `server.py` - Defines the shared FastMCP instance named "Mes Outils Personnalisés"
- `main.py` - Entry point that imports all modules and runs the server
- `src/` - Contains tool and prompt modules organized by functionality

### Module Organization
Each feature module in `src/` contains:
- `tools.py` - MCP tools decorated with `@mcp.tool()`
- `prompts.py` - MCP prompts decorated with `@mcp.prompt()` (optional)
- `schemas.py` - Pydantic models for structured data (optional)
- `__init__.py` - Module initialization

### Current Modules
- `multiply` - Simple multiplication tool
- `weather` - Weather data tools with structured WeatherData schema

### Adding New Features
1. Create new module directory in `src/`
2. Add tools in `tools.py` using `@mcp.tool()` decorator
3. Import from shared `server` instance: `from server import mcp`
4. Import the module in `main.py` to register tools
5. Use Pydantic models in `schemas.py` for structured data returns

### Key Dependencies
- `mcp[cli]>=1.11.0` - MCP server framework
- `python-docx>=1.2.0` - Document processing
- Python 3.13+ required