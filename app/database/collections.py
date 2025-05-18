from enum import Enum


class Collections(str, Enum):
    """
    Enum for collections to be used in database
    Args:
        str (Enum): Enum for collections to be used in database
    """

    AGENCIES = "agencies"
    USERS = "users"
    CLIENTS = "clients"
    PACKAGES = "packages"
    RESERVATIONS = "reservations"
    PAYMENTS = "payments"
    DESTINES = "destines"
    ITINERARIES = "itineraries"
    NOTIFICATIONS = "notifications"
    LOGS = "logs"

