********************************
:mod:`py_everything.automation`
********************************

.. module:: py_everything.automation

**Source code:** `py_everything/automation.py <https://github.com/pybash1/py_everything/blob/master/py_everything/automation.py>`_

This module contains methods that automate certain things or tasks such as sending a mail.

.. function:: sendEmail(sendAddr, password, recvAddr, body, server, port, sub='No Subject')

   Sends email to :attr:`recvAddr` from :attr:`sendAddr`. With :attr:`body` as mail body and :attr:`sub` as mail subject.
   Uses :attr:`server` and :attr:`port` to send the mail.

   :param str sendAddr: The address you want the mail to be sent from.
   :param str password: To login to the email account.
   :param str recvAddr: The address to which the mail is to be sent.
   :param str body: The main body of the email.
   :param str server: The server through which the mail should be sent.
   :param str port: The port at which the server is listening.
   :param str sub: The optional subject of the mail. Defaults to 'No Subject' if not specified.
   :returns bool: True if mail gets sent successfully.

   .. note::

      Less secure app access should be turned on for Gmail. IMAP/POP Forwarding should be enabled in mail settings
      for this to work. Alos, the server and port should be correct.

.. function:: emailAddressSlicer(fullAddr)

   Slices an email address and returns username and domain separately.

   :param str fullAddr: The full address you want to slice.
   :returns tuple: Contaning username and domain..;

.. function:: rollDice(dice1=True)

   Rolls dice and returns value between 1 and 6 if dice1=True else returns value between 1 and 12.

   :param str dice1: Boolean to understand if 1 dice to roll or 2 dice.
   :returns int: Value between 1 and 6 or 1 and 12.

.. function:: timer(seconds, audioFile)

   Starts a timer for ``seconds`` and plays ``audioFile`` when finished.

   :param int seconds: How many seconds should the timer be for.

.. function:: startApp(exePath)

   Starts ``exePath``.

   :param str exePath: Full path to the exe to be launched.
   :returns bool: True if exe starts successfully.
   :raises error.startAppFailedError: This exception is raised if exe was not started successfully. Maybe due to an incorrect path.
