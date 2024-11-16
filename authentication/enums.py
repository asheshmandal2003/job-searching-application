import enum

class UserRole(enum.Enum):
    STUDENT = "student"
    TPO = "tpo"
    COMPANY = "company"
    ADMIN = "admin"

    @classmethod
    def choices(cls):
        return [(role.value, role.name.capitalize()) for role in cls]
