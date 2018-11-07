==================
django-model-ident
==================

.. image:: https://badge.fury.io/py/django-model-ident.png
    :target: https://badge.fury.io/py/django-model-ident

.. image:: https://travis-ci.org/ckirby/django-model-ident.png?branch=master
    :target: https://travis-ci.org/ckirby/django-model-ident

.. image:: https://coveralls.io/repos/ckirby/django-model-ident/badge.png?branch=master
    :target: https://coveralls.io/r/ckirby/django-model-ident?branch=master

**django-model-ident** provides a quick lookup for django models by pk only.
Instead of writing ModelName.objects.get(pk=pk) write ModelName.ident_(pk)

Project
-------

The project can be found at https://github.com/ckirby/django-model-ident

Requirements
------------

* Django 1.11+
* Python 3.4+

Usage
-----

Add 'model-ident' to your INSTALLED_APPS

How Does It Work
----------------

ON ready() django-model-ident monkey patches all the models found in your INSTALLED_APPS with the method ident_(pk).
This calls <model>._base_manager.get(pk=pk). We use _base_manager so as not to get confused by changes in ModelManagers.