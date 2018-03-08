from telegram.ext import Handler

class ArduinoHandler(Handler):
    def __init__(self, callback):
        self.pass_update_queue = False
        self.pass_job_queue = False
        self.pass_user_data = False
        self.pass_chat_data = False
        self.callback = callback
        self.data=[]

    def check_update(self, update):
        return True

    def handle_update(self, update, dispatcher):
        self.data = self.callback(self.data)

    def getData(self):
        return self.data
