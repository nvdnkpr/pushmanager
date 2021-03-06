import mock

import core.mail
import testing as T

class MailQueueTest(T.TestCase):

    def test_send_mail(self):
        with mock.patch.object(core.mail.MailQueue, "smtp") as mocked_smtp:
            with mock.patch.object(core.mail.MailQueue, "message_queue"):
                recipient = "test@test.com"
                message = "test message"
                subject = "test subject"
                from_email = "fromtest@test.com"

                core.mail.MailQueue._send_email(recipient, message, subject, from_email)

                T.assert_equal(mocked_smtp.sendmail.called, True)
