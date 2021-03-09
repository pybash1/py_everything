.. sectionauthor:: Play 4 Tutorials <play.4.tutotials@gmail.com>

************************
py_everything.automation
************************

Import -
--------

How to import the module?

.. code:: python

   >>> import py_everything.automation as pyeAuto

Send a mail with Python
-----------------------

Function name - email_bot(send_addr, password, recv_addr, body, server,
port, sub='No Subject')

No. of Parameters - 7

Parameters - send_addr, password, recv_addr, body, server, port, sub='No
Subject'

Usage -
^^^^^^^

.. code:: python

   >>> my_addr = "your.email@add.ress"
   >>> my_pass = "your password"
   >>> to_addr = "recv.er@add.ress"
   >>> my_body = "Email body"
   >>> my_server = "your.smtp.server"
   >>> my_port = "123"
   >>> my_sub = "My Subject"
   >>> pye.email_bot(my_addr, my_pass, to_addr, my_body, my_server, my_port, my_sub)
   True


This function sends a mail to the address passed in `recv_addr`. `sub` is a optional parameter.
The mail is sent from the value of `sent_addr`. `sent_addr` and `password` are used to authenticate with the `server`.
The `port` is also very important. `body`, and `sub` are the Body and Subject of the email, respectively. 

Note - Speacial settings must be enabled for this function to work properly. For e.g. - In Gmail you need to enable Less secure app access.

Slice an email address
----------------------

Function name - email_address_slicer(full_addr)

No. of Parameters - 1

Parameters - full_addr

Usage -
^^^^^^^

.. code:: python

   >>> full_addr = 'long.demo.address@long-domain.com'
   >>> pye.email_address_slicer(full_addr)
   ['long.demo.address', 'long-domain.com']

This function is usefull to get the username and domain of a email
address seperately. ``full_addr`` takes in the the full email address
that is to sliced.

Roll the Dice!
--------------

Function name - roll_dice(dice1=True)

No. of Parameters - 1

Parameters - dice_1

Usage -
^^^^^^^

.. code:: python

   >>> pye.roll_dice(dice_1=True)
   4
   >>> pye.roll_dice(dice_1=False)
   8
   >>> pye.roll_dice(dice_1=True)
   6
   >>> pye.roll_dice(dice_1=False)
   11

This function doesn't need explanation but still. If ``dice_1`` is True
then the number will be within th range of 1 to 6 but if ``dice_1`` is
False the range is from 1 to 12. That is ``dice_1`` signifies the no. of
dice being rolled. If True, 1 dice, else 2 die. It is True by default.

Run a timer
-----------

Function name - timer(seconds, audio_file)

No. of Parameters - 2

Parameters - seconds, audio_file

Usage -
^^^^^^^

.. code:: python

   >>> pye.timer(10, 'path/to/audio/file.mp3')
   <---After 10 seconds, it plays the audio_file--->

This function countsdown ``seconds`` untill it reaches 0 and then plays
``audio_file``. Both parameters are required.

Start or run a app or executable.
---------------------------------

Function name - start_app(drive, app_path, exe_name)

No. of Parameters - 3

Parameters - drive, app_path, exe_name

Usage -
^^^^^^^

.. code:: python

   >>> pye.start_app('C', 'path/to/exe_file/file_name.exe')
   True

This function uses the 3 parameters to run any executable.

Note - In ``exe_path``, the full path, including exe name and extension
are to be provided, in ``drive``, only the letter is to be provided, the
colon(:) is to be ommited. For example - start_app('C', 'C:/Program
Files/company/exe_name.exe').

... toctree::
   :caption: Basic:

.. toctree::
   :caption: Functions:

.. toctree::
   :caption: About the Project:
