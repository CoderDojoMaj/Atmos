import telegram.ext.Handler as Handler

class ArduinoHandler(Handler):
    def __init__(self, callback):
        self.pass_update_queue = False
        self.pass_job_queue = False
        self.pass_user_data = False
        self.pass_user_data = False
        self.callback = callback

    def check_update(self, update):
        return True

    def handle_update(self, update, dispatcher):
        return self.callback()
