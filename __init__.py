# agent/__init__.py
"""
Smart Concierge Agent Package

This package contains the main agent builder and support modules
used in the Smart Personal Task & Mail Assistant.
"""

from .builder import build_concierge_agent

__all__ = [
    "build_concierge_agent",
]
