Conclusion of my GSoC project 🍕
###################################

:date: 2021-08-25 16:48
:modified: 2021-08-25 16:48
:tags: python, django, inkscape
:category: GSoC
:slug: gsoc-work 
:authors: Ishaan Arora
:summary: This is what I learned during the program and how I intend to continue my work
         

About My Project
**************************************
My GSoC Project was to upgrade the Django-based Inkscape website to Django version ``2.x`` (and ultimately to ``3.x``). The website used version ``1.11`` which had its *End of extended support* as Django calls it in 2020. Using this old version was a security risk and it would make the maintenance of the website much harder going forward.

Here is the link to the official GSoC page for my project:

.. list-table::
   :widths: 100

   * - `<https://summerofcode.withgoogle.com/projects/#6584906785751040>`_

An overview of what I did
********************************************

The way I tackled this problem was that I didn't go head-on first with the upgrade but instead I started writing tests for the individual Django apps. I started with the ``forums`` app, then went on to the ``releases`` app. 

Here are the Merge Requests for those tests:

.. list-table::
   :widths: 30 70

   * - **Tests for Forums**
     - https://gitlab.com/inkscape/inkscape-web/-/merge_requests/88
   * - **Tests for Releases**
     - https://gitlab.com/inkscape/inkscape-web/-/merge_requests/89

The reason I wrote tests first is simple - to provide a safety net while upgrading. When I had completed the tests for the previously mentioned apps, I went on to write more tests 🙂  for the ``resources`` app but by then I had exhausted my **testing creativity** (what might someday be known as a Tester's Block.)

So, I instead starting working on the upgrade. Django has a really nice guide [#upgrade-guide]_ on upgrading Django versions in its official docs. It gave a good overview of what needed to be done for an upgrade.

What is left
***************
I have successfully upgraded the website from Django version ``1.11`` to ``2.0``.

As of writing this post, I am currently in the process of upgrading the website to Django ``2.2``. I also intend to finish writing tests for the remaining apps. This is going to take a while but I am happy that at least the upgrade will be complete within a week or so.

Here is the MR for the upgrade:

.. list-table::
   :widths: 100

   * - https://gitlab.com/inkscape/inkscape-web/-/merge_requests/90

What I learned
****************
There are many things that I learned while doing the project. I wasn't familiar with web development in any way. I got to know about the backend side of things. I also gained a better understanding of how the web works in general - the request-response cycle, HTTP headers, and many such things.

I also have become more proficient in using vim. Particularly, I am at a level where I can write macros to do things quickly and I don't have to think while pressing ``dd`` to delete a line. I still feel though that there is much to learn in this marvelous editor that is vim.

I've gained an intermediate understanding of the Django framework. I can now think where I should use a Middleware or which Generic View would make sense in a particular situation. The part of Dango with which I became the most familiar is the testing framework. I also came to a realisation that writing unit tests within a framework is difficult! - because of so many moving parts. There is so much that Django does, sometimes it's difficult to just test that piece of code. Writing tests is hard in general I think 🤷

I advanced my Python knowledge too. I wrote a context manager to clear the cache which I am very much proud of. It's not the most functional piece of code, but just increases the quality-of-life. Like most other things, there is much much more to learn within Python. I haven't touched the ML side of things yet, just Django. GUI stuff interests me too, so I might try that... Who knows where Python will take me next 🚀

Finally, I've become a part of the Inkscape community, which is a very helpful and great community of contributors from various parts of the world, very different professions even. I am proud to have been able to contribute to such a great project that I myself use. (The favicon for my blog was designed by me in Inkscape 😉)

I would also like to thank my mentor Martin and the general Inkscape community for selecting me for the project. This was a very new experience for me, my first real contributions to FOSS, in many ways my *magnum opus*.

That's all I have to say for now, adieu...

        | *Beginnings always hide themselves in ends*
        | - *Move On, Mike Posner*

.. rubric:: **Footnotes**
.. [#upgrade-guide] `<https://docs.djangoproject.com/en/3.2/howto/upgrade-version/>`_ 


