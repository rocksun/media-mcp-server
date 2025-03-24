from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("media-mcp-server")

@mcp.tool()
async def upload_image(image_path: str) -> str:

    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

def main():
    print("Hello from media-mcp-server!")

if __name__ == "__main__":
    main()
