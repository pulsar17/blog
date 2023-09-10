Having fun with keyboard mappings under Linux ⌨️
#################################################

:date: 2023-09-09 02:12
:modified: 2023-09-09 02:12 
:tags: linux, systemd, keyboard
:category: Configuration
:slug: keymapping
:authors: Ishaan Arora
:summary: Mapping keys and a little bit about how keyboards work

Context
****************
I've recently purchased a new laptop - it's a Xiaomi Notebook Ultra. The laptop is good and I like it,
but it has a non-standard keyboard, with non-standard meaning that it has a non-standard key on it. 
Xiaomi touts it as a feature, they call it the *Macro key*.

On this keyboard, this key is the rightmost key on the top row, usually where the ``Delete`` key is.

.. figure:: {static}images/macro-key.webp
   :width: 50 %
   :alt: A picture of Xiaomi Notebook Ultra's keyboard showing the position of the Macro key

   *The key on the top right is the Macro key*

Issue
*********
Well, this key does not work under Linux. Xiaomi provides an application under Windows to map this key to launch
any application, but no support for Linux as is expected from a vendor like Xiaomi.

An unrelated annoyance for me is that the keyboard doesn't have any Media Play/Pause key. I'm used to the convenience of
those keys on my full-size regular keyboard.

So I decided to look into mapping the Macro key to the Media Play/Pause key under Linux.

A bit about how keyboards work
*******************************
After searching a bit, I landed on the Arch wiki page on *Mapping scancodes to keycodes* [#mapping]_ and 
then eventually on *Keyboard Input* [#input]_.

The Keyboard Input page [#input]_ explains very nicely how a keypress on a keyboard translates to a key on the
desktop.

The short version is that a keyboard sends what is known as a *scancode* to the computer. The scancode
is a sequence of one or more bytes, and it is sent on key press and on key release. Often the scancodes sent
on press and release of the same key are different. 

The scancodes are raw information that the keyboard sends. These are then translated to *keycodes*. From ``man showkey``:

    | Keycodes are numbers assigned by the kernel to each individual physical key.

Two commands are relevant here, ``showkey`` and ``evtest``, ``evtest`` being the more general one for other input devices as well, not just keyboards.

First, I tried ``showkey`` as mentioned in the wiki [#input]_. I pressed the ``a`` key:

.. code:: sh

   $ showkey --scancodes

   kb mode was UNICODE
   [ if you are trying this under X, it might not work
   since the X server is also reading /dev/console ]
   
   press any key (program terminates 10s after last keypress)...
   0x9c 
   0x1e 
   0x9e 

Here, on the first line, ``0x9c`` is the release scan code for the ``Enter`` key. Below those are the press (``0x1e``) and release (``0x9e``) scancodes for the letter ``a`` [#keyset]_. 

However, pressing the Macro key on my keyboard did not show any output!

I repeated this exercise with ``evtest``. You need to first select the input device, which in this case
was device event number 2, the one with ``keyboard`` in it. Then I pressed the ``a`` key:

.. code:: sh

   $ sudo evtest

   No device specified, trying to scan all of /dev/input/event*
   Available devices:
   /dev/input/event0:	Lid Switch
   /dev/input/event1:	Power Button
   /dev/input/event2:	AT Translated Set 2 keyboard
   # --- a bunch of devices ---

   Select the device event number [0-14]: # 2
   Input driver version is 1.0.1
   Input device ID: bus 0x11 vendor 0x1 product 0x1 version 0xab83
   Input device name: "AT Translated Set 2 keyboard"
   Supported events:
     Event type 0 (EV_SYN)
     Event type 1 (EV_KEY)
       Event code 1 (KEY_ESC)
       Event code 2 (KEY_1)
       Event code 3 (KEY_2)
       Event code 4 (KEY_3)
       # --- a bunch of event codes ---
       Event code 158 (KEY_BACK)
       Event code 159 (KEY_FORWARD)
       Event code 163 (KEY_NEXTSONG)
       Event code 164 (KEY_PLAYPAUSE)
       Event code 165 (KEY_PREVIOUSSONG)
     Event type 4 (EV_MSC)
       Event code 4 (MSC_SCAN)
     Event type 17 (EV_LED)
       Event code 0 (LED_NUML) state 0
       Event code 1 (LED_CAPSL) state 0
       Event code 2 (LED_SCROLLL) state 0
   Key repeat handling:
     Repeat type 20 (EV_REP)
       Repeat code 0 (REP_DELAY)
         Value    250
       Repeat code 1 (REP_PERIOD)
         Value     33
   Properties:
   Testing ... (interrupt to exit)
   Event: time 1694216196.712488, type 4 (EV_MSC), code 4 (MSC_SCAN), value 1c
   Event: time 1694216196.712488, type 1 (EV_KEY), code 28 (KEY_ENTER), value 0
   Event: time 1694216196.712488, -------------- SYN_REPORT ------------
   Event: time 1694216208.594231, type 4 (EV_MSC), code 4 (MSC_SCAN), value 1e
   Event: time 1694216208.594231, type 1 (EV_KEY), code 30 (KEY_A), value 1
   Event: time 1694216208.594231, -------------- SYN_REPORT ------------
   Event: time 1694216208.704429, type 4 (EV_MSC), code 4 (MSC_SCAN), value 1e
   Event: time 1694216208.704429, type 1 (EV_KEY), code 30 (KEY_A), value 0
   Event: time 1694216208.704429, -------------- SYN_REPORT ------------


Pressing the Macro key yields this event:

.. code:: sh

   Event: time 1694348296.562252, -------------- SYN_REPORT ------------
   Event: time 1694348297.590653, type 4 (EV_MSC), code 4 (MSC_SCAN), value 72
   Event: time 1694348297.590653, -------------- SYN_REPORT ------------
   Event: time 1694348297.684777, type 4 (EV_MSC), code 4 (MSC_SCAN), value 72
   Event: time 1694348297.684777, -------------- SYN_REPORT ------------

At this point, I wasn't sure the code ``evtest`` was giving me was the scancode or the keycode, but I knew it was one of them.

Just to make sure, I checked the output of ``dmesg -W`` as suggested by the wiki [#input]_:

.. code:: sh

   $ dmesg -W

   [ 7400.724249] atkbd serio0: Unknown key pressed (translated set 2, code 0x72 on isa0060/serio0).
   [ 7400.724259] atkbd serio0: Use 'setkeycodes 72 <keycode>' to make it known.
   [ 7400.857064] atkbd serio0: Unknown key released (translated set 2, code 0x72 on isa0060/serio0).
   [ 7400.857072] atkbd serio0: Use 'setkeycodes 72 <keycode>' to make it known.

This indicated that the scancode for the Macro key was ``72``. It also helpfully suggested the fix.

At this point, I went back to the ``evtest``'s output [#evtest]_ , it shows all the keycodes that my keyboard supports (and also what the kernel recognizes). I was particularly interested in:

.. code:: sh

   Event code 164 (KEY_PLAYPAUSE)

This is what I want the Macro key to be mapped to. The keycode for ``KEY_PLAYPAUSE`` is ``164``.

Finally, I ran:

.. code:: sh

   $ sudo setkeycodes 72 164


Now I can play/pause media using the Macro key 🕪🎉

..  rubric:: **Footnotes**
.. [#mapping]  `Mapping scancodes to keycodes [Arch Wiki] <https://wiki.archlinux.org/title/Map_scancodes_to_keycodes>`_
.. [#input]  `Keyboard Input [Arch Wiki] <https://wiki.archlinux.org/title/Keyboard_input>`_
.. [#keyset]  The table on `<https://en.wikipedia.org/wiki/Scancode#PC_compatibles>`_ seems to suggest that my keyboard is using the IBM PC XT set of scancodes.
   `This article <https://www.berrange.com/posts/2010/07/04/a-summary-of-scan-code-key-codes-sets-used-in-the-pc-virtualization-stack/>`_ [by Daniel P. Berrangé] gives a terse history of various scancode sets.
.. [#evtest] I am not sure why ``evtest`` reports the value as ``1e`` for both key press and release for ``a`` key. Booting the kernel with ``atkbd.softraw=0`` command line parameter gives the actual scancodes when printed with ``evtest``. Even ``showkey`` shows the scancodes when the kernel is booted with this parameter.

   .. code:: sh

      $ sudo evtest

      # truncated output

      Event: time 1694219065.861887, type 4 (EV_MSC), code 3 (MSC_RAW), value 9c
      Event: time 1694219065.861887, type 4 (EV_MSC), code 4 (MSC_SCAN), value 1c
      Event: time 1694219065.861887, type 1 (EV_KEY), code 28 (KEY_ENTER), value 0
      Event: time 1694219065.861887, -------------- SYN_REPORT ------------
      Event: time 1694219068.552098, type 4 (EV_MSC), code 3 (MSC_RAW), value 1e
      Event: time 1694219068.552098, type 4 (EV_MSC), code 4 (MSC_SCAN), value 1e
      Event: time 1694219068.552098, type 1 (EV_KEY), code 30 (KEY_A), value 1
      Event: time 1694219068.552098, -------------- SYN_REPORT ------------
      aEvent: time 1694219068.656286, type 4 (EV_MSC), code 3 (MSC_RAW), value 9e
      Event: time 1694219068.656286, type 4 (EV_MSC), code 4 (MSC_SCAN), value 1e
      Event: time 1694219068.656286, type 1 (EV_KEY), code 30 (KEY_A), value 0
      Event: time 1694219068.656286, -------------- SYN_REPORT ------------
      Event: time 1694219069.340110, type 4 (EV_MSC), code 3 (MSC_RAW), value 72
      Event: time 1694219069.340110, type 4 (EV_MSC), code 4 (MSC_SCAN), value 72
      Event: time 1694219069.340110, -------------- SYN_REPORT ------------
      Event: time 1694219069.472099, type 4 (EV_MSC), code 3 (MSC_RAW), value f2
      Event: time 1694219069.472099, type 4 (EV_MSC), code 4 (MSC_SCAN), value 72


   The ``2.6 KERNELS`` section of ``man showkey`` does explain how the kernel presents scancodes to a program in absence of ``atkbd.softraw`` parameter.
   Maybe that's the reason ``evtest`` prints the output this way.
