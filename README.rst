================
collective.hello
================

This module provides video conferencing to Plone events using appear.in :

- Free service without registration
- Works on all modern web browsers.
- Nothing to install

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

1. On the edit page of your event, check ``Video conversation``

2. When the event starts, video conferencing is available

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
