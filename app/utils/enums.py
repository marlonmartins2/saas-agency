from enum import Enum


class Plans(str, Enum):
    """
    Enum for plans to be used in database
    Args:
        str (Enum): Enum for plans to be used in database
    """

    FREE = "free"
    BASIC = "basic"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class Status(str, Enum):
    """
    Enum for status to be used in database
    Args:
        str (Enum): Enum for status to be used in database
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    SUSPENDED = "suspended"