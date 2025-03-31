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
async def upload_image(image: str) -> str:
    """Uploads an image to Cloudinary.

    Args:
        image: Image file path or url of the image to upload.

    Returns:
        str: Secure URL of the uploaded image on Cloudinary CDN.
    """
    upload_result = uploader.upload(
        image,
        transformation=[
            {'quality': 'auto'}
        ]
    )
    return upload_result['secure_url']

if __name__ == "__main__":
    import asyncio
    path = asyncio.run(upload_image('https://assets-eu-01.kc-usercontent.com/8c150fae-fba4-0115-ef12-b10a8a4e2715/bdac1871-464e-4051-88db-7df20c3bfffa/SQ_Logo_Server_Light%20Backgrounds.svg?w=176&h=48&auto=format&fit=crop'))
    print(path)
