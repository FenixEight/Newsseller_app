class User:
    def __init__(self):
        self.user_id = None
        self.full_name = None
        self.email = None


class Newsletter:
    def __init__(self):
        self.newsletter_id = None
        self.newsletter_name = None
        self.from_name = None
        self.from_email = None
        self.subject = None
        self.body_text = None
        self.body_html = None


class Status:
    def __init__(self):
        self.last_id = None
        self.status = None
        self.error = None