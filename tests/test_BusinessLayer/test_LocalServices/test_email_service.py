import BusinessLayer.LocalServices.email_service as email_service
from unittest import TestCase


class TestEMailService(TestCase):

    def test_check_valid_email(self):
        # GIVEN
        email_valid_example = 'toto@mail.com'
        email_not_valid_example1 = '@gmail.com'
        email_not_valid_example2 = 'toto@nawak.com'
        # WHEN
        
        # THEN
        self.assertEqual(True, email_service.EMailService.check_valid_email(email_valid_example))
        self.assertEqual(False, email_service.EMailService.check_valid_email(email_not_valid_example1))
        self.assertEqual(False, email_service.EMailService.check_valid_email(email_not_valid_example2))