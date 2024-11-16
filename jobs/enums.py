import enum

class JobType(enum.Enum):
    FULL_TIME = 'full_time'
    INTERNSHIP = 'internship'

    @classmethod
    def choices(cls):
        return [(jobtype.value, jobtype.name.capitalize()) for jobtype in cls]
