from typing import Dict, Optional
import imaplib
import json
import email
from datetime import datetime
from Ticket import Ticket
from Notification import Notification
from FabDB import FabDB
import time


class FabBot:
    def __init__(self, email_credentials: Dict[str, str], db_credentials: Dict[str, str]):
        self.email_credentials = email_credentials
        self.db_credentials = db_credentials

        self.POLL_DELAY = 30  # seconds

        self.imap = imaplib.IMAP4_SSL(self.email_credentials["host"], 993)

        self.fab_db = FabDB(self.db_credentials)

    @staticmethod
    def parse_entry(entry: str, text: str) -> Optional[str]:
        entry_location = text.find(entry)
        if entry_location == -1:
            return None

        end_div_location = text.find("<", entry_location)
        if end_div_location == -1:
            return None

        entry_line = text[entry_location:end_div_location]
        entry_line = entry_line.replace("=\r\n", "")
        entry_line = entry_line.replace("\n", "")
        entry_line = entry_line.replace("\r", "")
        before_value = entry_line.rfind(";")
        if before_value == -1:
            before_value = len(entry)
        before_value += 1
        value = entry_line[before_value:]
        value = value.strip()
        return value

    def parse_text(self, text) -> Optional[Ticket]:
        ticket_name = self.parse_entry("Ticket Name", text)
        if not ticket_name:
            return None

        ticket_number = self.parse_entry("Ticket Number", text)
        if not ticket_number:
            return None
        ticket_number = int(ticket_number)

        email_address = self.parse_entry("Email", text)
        if not email_address:
            return None

        status = self.parse_entry("Status", text)
        if not status:
            return None

        entered_on = self.parse_entry("Entered on", text)
        if not entered_on:
            return None

        date = entered_on.split()[0]
        time = entered_on.split()[2]

        return Ticket(ticket_name, ticket_number, email_address, status, date, time)

    @staticmethod
    def notification_for_ticket(ticket: Ticket):
        title = "Ticket Updated"
        email_address = ticket.email_address

        message = None
        if ticket.status == "Created":
            message = "Your ticket has been created!"
        elif ticket.status == "Waiting on client input":
            message = "Your project is waiting on client input."
        elif ticket.status == "Ready for pickup":
            message = "Your project is ready for pickup!"
        elif ticket.status == "Closed":
            message = "Your ticket has been closed."
        else:
            message = ticket.status

        return Notification(title, message, email_address)

    def poll_forever(self) -> None:
        self.imap.login(self.email_credentials["user"], self.email_credentials["password"])
        self.imap.select('Inbox')

        while True:
            print("polling...")
            ret, indicies = self.imap.search(None, 'ALL')
            for num in indicies[0].split():
                ret, data = self.imap.fetch(num, '(RFC822)')
                message = email.message_from_bytes(data[0][1])
                subject = message["subject"]
                if "UVM FabLab" in subject:
                    payload = message.get_payload()
                    ticket = self.parse_text(payload)
                    if not ticket:
                        print("invalid ticket, skipping")
                        continue

                    if self.fab_db.ticket_is_new(ticket):
                        self.fab_db.update_ticket(ticket)
                        self.fab_db.send_notification(self.notification_for_ticket(ticket))
                        print("ticket updated, notification sent: ", ticket)
                    else:
                        print("ticket has already been updated, skipping: ", ticket)
            time.sleep(self.POLL_DELAY)


if __name__ == "__main__":
    bot = FabBot(json.load(open("email_credentials.json", "r")),
                 json.load(open("db_credentials.json")))
    bot.poll_forever()
