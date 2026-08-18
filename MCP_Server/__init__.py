"""Ableton Live integration through the Model Context Protocol."""

__version__ = "0.1.0"

# Expose key classes and functions without importing the full MCP server when a
# lightweight submodule is run as a CLI (for example, ``python -m
# MCP_Server.failure_log``).
__all__ = ["AbletonConnection", "get_ableton_connection"]


def __getattr__(name):
    if name in __all__:
        from .server import AbletonConnection, get_ableton_connection

        value = {
            "AbletonConnection": AbletonConnection,
            "get_ableton_connection": get_ableton_connection,
        }[name]
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
