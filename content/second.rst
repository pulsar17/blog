GSoC Update - Week 1 🚀
###################################

:date: 2021-06-15 00:40
:modified: 2021-06-20 00:01
:tags: python, django, inkscape
:category: GSoC
:slug: the-beginnings
:authors: Ishaan Arora
:summary: This is what I did in the first week of GSoC
         

Before The Coding Period (For context)
**************************************
My exams were to start on 7th June. Knowing that, I started working a week or so before. Mind you, I am fairly new to Django - with no experience in Web Development. I knew that this was going to be a hurdle for me, so I started a little early to compensate for my lack of experience and the time required for my exams.

I created custom Django TestCase classes so that I could easily test views, then wrote some tests, learned some Vim shortcuts.

I had some trouble initially when I was trying to test a view that created comments on the Inkscape Forum [#Forum]_ using Django's Test Client. To me, it should have been a simple matter of passing a POST request to a URL. Turns out, *django_comments*, the package the website uses for comments, does some special things under the hood for security reasons (which I won't go into too much detail). It *attaches* some security information to the form and sets that info as ``type=hidden`` in the HTML so that the browser sends it back to the backend. It works in the browser because the browser first sends a GET request on the URL, which renders an empty form. The form has those ``hidden`` inputs. It has the complete state essentially for the browser to send a complete valid POST request.

Since I was using the Django Test Client, I could only send a POST or a GET request to that URL ( I could theoretically send a GET request first, then parse the HTML to extract those fields, and then send the POST request... ) but no, I was adamant in doing it the browser way. I blatantly suggested to my mentor, Martin that we should use Selenium for these tests...

He politely asked me to send that extra information in the POST data itself instead of adding Selenium as a dependency. Little do you know when you want to add yet another dependency for no prominent reason. You can go as deep as you want in that rabbit hole 😉  [#maybe]_ (Why not add ``numpy`` while we're at it?) 

Now, the problem was - how to retrieve that security data?

Anyways, this was before the coding period.

The Coding Period Begins
************************
| So, the coding period officially started on 7th of June. (Should have made this update on 13th of June, anyways...)  
| I figured out a way, it wasn't very pretty but worked. I could now test forms*, yay! (If you're wondering what was it, it was an internal method ``get_security_data()`` that *django_comments* uses. I had to go into the source to dig this method out... but it was worth it)
| * I should be clear here that I am not testing the forms currently but views that use those forms. 

Mocking and Patching
====================
I also looked into Mocking and Patching this week. Basically, mocks are *blank* stubs that you can substitute for real objects while testing. They are an extremely handy tool. You can mock almost anything (almost... more on this later) - databases, external APIs, UFOs 😉... Mocks are part of the Python standard library, present in the ``unittest`` testing framework. So, mocks are stubs and you replace real objects with them using **patching** (also a part of ``unittest``).

| *Why you might ask was I looking for that?*
| Testing obviously 😀

The need was to mock and patch ``datetime.now()`` for a test. This test was going through all the topics in a forum and filtering the topics which were created in last ``n`` number of days. Since test data is static, the tests run on data you created a month ago will show different results when you run ``datetime.now()``, well, now. You might get a false sense of test correctness when you run them now but after a month, a year, those tests will suddenly start to fail. I hope I was able to convince you that the need for mocking dates in tests is real.

Turns out it is hard, real hard to mock ``datettime.now()``, especially when using third party code like Django.
I won't go into the details of why it is so, there are some great articles about that. I'll link to them in the footnotes.

With my novice Python skills, I came up with a solution of my own:

.. code:: python

        from contextlib import contextmanager

        @contextmanager
        def freeze(datetime_module, set_to):
                patcher = mock.patch.object(
                datetime_module, 'datetime', mock.Mock(wraps=datetime_module.datetime)
                )
                mocked_date = patcher.start()
                mocked_date.now.return_value = set_to
                yield
                patcher.stop()

Then you would use it as:

.. code:: python

        import datetime
        
        def test_view_displays_topics_from_last_week():
                with freeze(datetime, set_to=datetime.datetime(2021, 6, 8):
                        # do actual work
                        pass

| Pretty neat, isn't it 😎 ?
| Except that it **doesn't** work (*in some cases*). 🙃 
| Here's why - 

.. code:: python

        isinstance(value, datettime.datetime)

The problem is that the only way that the ``datetime.now()`` method can be patched is if we mock the parent ``datetime`` class. That is ``datetime.datetime``. In doing so, we essentially replace ``datetime.datetime`` with an instance of ``Mock`` class.

So, now roughly

.. code:: python

        datetime.datetime == Mock()
        
Those ``isinstance`` checks will now fail when the ``value`` argument is a real ``datetime.datetime`` object. Since it would be asking if a date is an instance of a ``Mock`` instance (yes, an instance, not even a class!).

| These shenanigans arise because a Mocked object is being used as the second argument in ``isinstance`` where a proper *Class* should be used. And since this is third party code (Django in my case), there isn't really much you can do about it. 
| Those ``isinstance`` checks lie sprinkled here and there, while you just ponder over the meaning of life...

*So, what's the solution then?*
+++++++++++++++++++++++++++++++

| **None**. Atleast I couldn't find one... And yes, I looked at SO answers, many articles alike. I just couldn't find a solution. These were the limits of my *novice Pythonista* mind that were being tested.
| If you're not using third party code though, and don't want to use a library like Freezegun (yes, I should have told that earlier. A library exists solely for patching datetimes), by all means use the one solution that I provided 😉

GSoC Mentors and Mentees Meet (G3M)
===================================

We had our first G3M (I gave it that name, it's not official) on 11th June. All the mentors introduced themselves and told us about their backgrounds and what part of Inkscape they work on. Then students told about what they're doing currently, which university/school they're from and what project they will be doing for GSoC (We also have one project from Outreachy). There are many interesting projects this year - on canvas bool ops, markers, alignment guides, actions improvements, etc.

In the meeting, Marc, one of the developers, suggested us to write blogs, and communicate regularly with our mentors about our work. This G3M was scheduled on a :abbr:`BBB (Big Blue Button)` instance. This is how all the developers usually communicate. That, the RocketChat instance and :abbr:`IRC (Internet Relay Chat)` are the modes at our disposal.
We were also told that we will be having more such G3Ms in the future.

This was a fun experience. I got to know about the people who develop Inkscape. Together with the community they create an awesome piece of software that is Inkscape. I am glad I chose Inkscape as my org.

Final Thoughts
==============
This week was a light one with respect to how much I could do. I learned many new things and got to know such great people. I hope I will be able to contribute more in the coming weeks.

Bonus Tip: Just Grep It!
++++++++++++++++++++++++
If you are trying to find correlations between how a thing is done in the codebase, an intuitive way is to search for it. Should you use your IDE's search? Nah... I found VSCodium's search to be ineffective sometimes so I have given up on it. Instead, I use this:

.. code:: sh
        
        grep -Rin "?next" .

**Example output for this search.**

.. code:: 

           ./content/second.rst:121:        grep -Rin "?next" .
           ./content/second.rst:132:        grep -i "?next" $(find . -print) 2>/dev/null
           ./output/2021/06/the-beginnings.html:244:grep -Rin <span class="s2">&quot;?next&quot;</span> .
           ./output/2021/06/the-beginnings.html:255:grep -i <span class="s2">&quot;?next&quot;</span> <span class="k">$(</span>find . -print<span class="k">)</span> <span class="m">2</span>&gt;/dev/null


| This is a trick I learned from one of Martin's videos [#vid]_ (He has a YouTube channel!)
| The important thing here are the options, ``-R`` is for recursive search, ``-i`` is for case insensitiveness, ``-n`` is for displaying line numbers along with the filename.

| Super super useful. I can't stress enough the importance of this one command 😀

Before I knew this command, I used to use this:

.. code:: sh
        
        grep -i "?next" $(find . -print) 2>/dev/null

| An abomination (still somewhat UNIXy though) which would make the GNU/Gods frown ...
| Not to mention, how awfully slow it is.

Anyways, that's all I have to say for now, adieu...

        | *Too many mountains to climb*
        | *Too many thoughts for my pen to write...*
        | 
        | - *Too Many, Winterbourne*

        
.. rubric:: **Footnotes**
.. [#Forum] `Inkscape Forum <https://inkscape.org/forums/>`_: If you haven't checked it out, have a look, there's lots of cool things the community has shared.
.. [#maybe]  I have nothing against Selenium, I have everything against my tendency to complicate things when things can be simpler. Selenium is an excellent tool, I was going for the chainsaw instead of a knife.
.. [#article1] `<https://nedbatchelder.com/blog/201209/mocking_datetimetoday.html>`_ - Ned Batchelder talks about his need to mock ``today()``, similar to my need to mock ``now()``.
.. [#article2] `<http://lists.idyll.org/pipermail/testing-in-python/2011-July/004296.html>`_ A conversation with Michael Foord - the original author of mock, that highlights exactly the problem I was having.
.. [#vid] https://youtu.be/FEQstRH73WI - A great learning resource. Teaches how to navigate/search a big codebase such as Inkscape. The thought process is the most important takeaway from this video.


