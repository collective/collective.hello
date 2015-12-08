# collective.hello

It is a Plone module that adds interactivity to your events by linking them with [hello conversation](https://www.mozilla.org/firefox/hello/). Hello is a free web application developed by Mozilla to quickly and easily make video conferencies (nothing to install / without registration).


## Installation

To deploy ```collective.hello```, you just have to edit your ```buildout.cfg``` file and add the following in the eggs section:
```
eggs =
    ...
    collective.hello
```

Then you have to run ``buildout`` to realize your configuration:
```
  bin/buildout -N
```



## How to use it ?

1. On the edit page of your event, check ```Hello join button```

2. When the event starts, press the create room button on the event page.

3. During event, your users (logged or not) can reach the room from the event page.

## Support

You can use [GitHub issue tracker](https://github.com/collective/collective.hello/issues).

## Credits

### Contributors

* Simon Prévidente <simon.previdente@makina-corpus.com>
* You ? :)

### Companies

[![Makina Corpus](http://depot.makina-corpus.org/public/logo.gif)](http://www.makina-corpus.com)

* [Planet Makina Corpus](http://www.makina-corpus.org)
* [Contact us](mailto:python@makina-corpus.org)
