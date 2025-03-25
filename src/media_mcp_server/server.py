from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("media-mcp-server")

from urllib.parse import urlparse
import os
import cloudinary
from cloudinary import uploader

# 配置Cloudinary
cloudinary.config(
  cloudinary_url=os.environ['CLOUDINARY_URL']
)

@mcp.tool()
async def upload_image(image_path: str) -> str:
    upload_result = uploader.upload(
        image_path,
        transformation=[
            {'quality': 'auto'}
        ]
    )
    return upload_result['secure_url']

    # url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    # data = await make_nws_request(url)

# def main():
#     print("Hello from media-mcp-server!")

# if __name__ == "__main__":
#     main()
