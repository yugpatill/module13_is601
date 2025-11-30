# app/auth/redis.py

"""
Fallback in-memory blacklist used for Module 12.
Redis is NOT required for this assignment.
All tests expect only add/check functionality.
"""

BLACKLIST = set()

async def add_to_blacklist(jti: str, exp: int = None):
    """Add a token JTI to the in-memory blacklist."""
    BLACKLIST.add(jti)

async def is_blacklisted(jti: str) -> bool:
    """Check if a token JTI is blacklisted."""
    return jti in BLACKLIST