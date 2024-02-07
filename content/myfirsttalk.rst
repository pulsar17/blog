My first ever talk 🐍🗣
####################################

:date: 2022-07-28 12:27
:modified: 2024-02-08 01:52
:changelog: fixed dead link to teach plugin
:tags: python, talk, pydelhi, meetup, neovim, lua
:category: Talks
:slug: my-first-talk
:authors: Ishaan Arora
:summary: It was both exciting and frightening


.. list-table:: Some pictures from the meetup
   :class: borderless

   * - .. figure:: {static}images/first-speaker.jpeg
          :width: 50%
          :alt: A Developer Advocate at Twitter

          *Workshop: Getting started with the Twitter API v2 in Python*

   * - .. figure:: {static}images/second-speaker.jpeg
          :width: 50%
          :alt: Me explaining a slide

          *Having fun with text in Python or 🐍❤🔠*

   * - .. figure:: {static}images/third-speaker.jpeg
          :width: 50%
          :alt: A Senior Engineering Manager at Innovacer

          *Name and Pattern Matching at Innovacer*

.. figure:: {static}images/talk-by-me.jpeg
   :width: 512
   :scale: 100%
   :alt: Me explaining a slide

   Me explaining a slide
   

✅ Give a talk at a meetup
***************************

So on 23rd of July, 2022, I gave a talk at the local `PyDelhi <https://pydelhi.org/>`_ meetup about Unicode and Python.
You can find all the information about my talk in this GitHub issue - `pydelhi/talks#200 <https://github.com/pydelhi/talks/issues/200>`_

I talked about text, Unicode, and Python's support for Unicode. The talk was around 45 minutes long.

After explaining some basic concepts of Unicode, like what is a character, what is a codepoint, I also explained how these concepts are accessible in Python. I ran a script that I had created for this talk. I then went on to making small tweaks in the script and explaining the output of those changes.

After that I explained the concept of encodings, and why you should default to the ``utf-8`` encoding. I wasn't able to spend as much time on it as I would have liked to. Admittedly, I prepared the first half of my talk better than I did the second part.

Many people also had questions which I tried my best to answer.

How I prepared for this talk
****************************
I proposed the talk on 29 June, 2022. So, I had around a month to prepare this talk. First I had to select 'where' and 'in what' I would write the slides. I did not want to make a ppt(*they are boring*), I was also aware of some javascript libraries that would allow me to present my slides in the browser.
But it was a Python conference and I am not too fond of javascript. After sifting through Reddit, I stumbled upon `lookatme <https://pypi.org/project/lookatme/>`_.

The gist is - you write your slides in Markdown and then lookatme renders it in the terminal which I felt was very very cool!

So I both wrote and presented my slides on the terminal.

I also went as far as writing a Lua plugin for neovim to help present the output of scripts.

.. image:: {static}images/talk-unicodify.gif
   :alt: Teach plugin for neovim
   :width: 100%

The plugin just displays the output of current script in a beautiful yellow colored floating window.
I set up some keybindings too for it, namely:

.. code:: lua

    -- Teach.nvim - a local plugin
    vim.keymap.set({'n', 'i', 'v'}, '<F5>', require('teach').openTeachWindow)
    vim.keymap.set({'n', 'v'}, '<Leader>rr', require('teach').openTeachWindow)
    vim.keymap.set({'n', 'v'}, '<Leader>ee', require('teach').closeTeachWindows)
    vim.keymap.set({'n', 'v'}, '<Leader>ea', require('teach').closeAllTeachWindows)

For now this plugin lives in the `talks <https://github.com/pulsar17/talks/blob/main/pydelhi/2022/july/teach.lua>`_ repo. I might release it as a separate plugin someday if I get enough time.

Final thoughts
***************
I had so much fun - both before while preparing the slides and on the meetup day itself. I plan to give more talks in the future. I met so many new people there, each with a different background (I met a professional diver 🤿 from the Andamans, who could have thought that!?). I also hope that I meet more such people.
