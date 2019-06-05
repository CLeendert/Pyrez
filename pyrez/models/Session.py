from .APIResponse import APIResponse
class Session(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sessionId = kwargs.get("session_id", None) if kwargs else None
        self.timestamp = kwargs.get("timestamp", None) if kwargs else None
        if self.timestamp:
        	from ..utils.datetime import string_datetime_utc_to_datetime
        	self.timestamp = string_datetime_utc_to_datetime(self.timestamp)
    def isApproved(self):
        return self.errorMsg.lower().find("approved") != -1
