================
collective.hello
================

This module provides video conferencing to Plone events using Hello conversation. `Hello <https://www.mozilla.org/firefox/hello/>`_ is a free web application developed by Mozilla to quickly and easily make video conferencies (nothing to install / without registration) and it works on all modern web browsers.

> `Demo video <https://www.youtube.com/watch?v=-e3ZesIFeK4>`_


Installation
============

To deploy collective.hello, you need to edit your ``buildout.cfg`` file
and add the following in the ``eggs`` section::

    eggs =
         ...
         collective.hello

Then you have to run ``buildout`` to realize your configuration::

             bin/buildout -N

How to use it ?
===============

1. On the edit page of your event, check ``Hello join button``

2. When the event starts, press the create room button on the event page.

3. During event, your users (logged or not) can reach the room from the event page.

Support
=======

You can use `GitHub issue tracker <https://github.com/collective/collective.hello/issues>`_

Credits
=======

Contributors
------------

* Simon Prévidente <simon.previdente@makina-corpus.com>
* You ? :)

Companies
---------

|makinacom|_

* `Makina Corpus <http://www.makina-corpus.org>`_
* `Contact us <mailto:python@makina-corpus.org>`_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
