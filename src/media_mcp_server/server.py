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
    """Uploads an image to Cloudinary.

    Args:
        image_path: Local file path of the image to upload.

    Returns:
        str: Secure URL of the uploaded image on Cloudinary CDN.
    """
    upload_result = uploader.upload(
        image_path,
        transformation=[
            {'quality': 'auto'}
        ]
    )
    return upload_result['secure_url']

if __name__ == "__main__":
    import asyncio
    path = asyncio.run(upload_image('C:\\Users\\sdj21\\Pictures\\76c83370-barriers-to-genai-adoption_boomi-1024x688.jpg'))
    print(path)
