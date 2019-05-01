from Ticket import Ticket
from Notification import Notification
import mysql.connector
from typing import Any


class FabDB:
    def __init__(self, credentials):
        self.credentials = credentials

    def update_ticket(self, ticket: Ticket) -> None:
        self._execute("DELETE FROM tickets WHERE ticket_number=%s;" % str(ticket.number))
        self._execute("INSERT INTO tickets (ticket_number, date, time, ticket_name, email, status)"
                      "VALUES (%s, '%s', '%s', '%s', '%s', '%s');" % (ticket.number,
                                                                      ticket.date,
                                                                      ticket.time,
                                                                      ticket.name,
                                                                      ticket.email_address,
                                                                      ticket.status))

    def send_notification(self, notification: Notification) -> None:
        self._execute("INSERT INTO notifications (email, title, message)"
                      "VALUES ('%s', '%s', '%s');" % (notification.email_address,
                                                      notification.title,
                                                      notification.message))

    def ticket_is_new(self, ticket: Ticket) -> bool:
        ret = self._execute_ret("SELECT * FROM tickets where ticket_number=%d;" % ticket.number)
        if len(ret) == 0:
            return True
        ret = ret[0]

        db_ticket = Ticket(ret[3], ret[0], ret[4], ret[5], ret[1], ret[2])

        if ticket.status_rank > db_ticket.status_rank:
            return True
        else:
            return False

    def _execute(self, command: str) -> None:
        database = mysql.connector.connect(
            host=self.credentials["host"],
            user=self.credentials["user"],
            passwd=self.credentials["password"],
            database=self.credentials["database"]
        )
        cursor = database.cursor()

        cursor.execute(command)
        database.commit()

        cursor.close()
        database.close()

    def _execute_ret(self, command: str) -> [Any]:
        database = mysql.connector.connect(
            host=self.credentials["host"],
            user=self.credentials["user"],
            passwd=self.credentials["password"],
            database=self.credentials["database"]
        )
        cursor = database.cursor()

        cursor.execute(command)
        data = cursor.fetchall()

        cursor.close()
        database.close()

        return data
