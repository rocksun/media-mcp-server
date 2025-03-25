# Media MCP Server

Professional implementation of Media Metadata Control Protocol server

## Features
- Built on FastMCP framework
- Multimedia metadata management
- RESTful API interfaces

## Installation
```bash
uv pip install -e .
```

## Running
```bash
uv run media-mcp-server
```

## Development
```bash
uv venv
uv pip install -e .[dev]
```

## Installation

**Development/Unpublished Server Configuration**

```json
{
  "mcpServers": {
    "media-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/rocksun/Projects/media-mcp-server",
        "run",
        "media-mcp-server"
      ],
      "env": {
        "CLOUDINARY_URL": "cloudinary://my_key:my_secret@my_cloud_name"
      }
    }
  }
}
```