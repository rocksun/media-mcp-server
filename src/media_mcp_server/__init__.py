"""
Media MCP Server

A server for interacting with many media service through MCP.
"""

from .server import mcp


def main() -> None:
    """Run the Media MCP server"""
    mcp.run()


__all__ = ['mcp', 'main']