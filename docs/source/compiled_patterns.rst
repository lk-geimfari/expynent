Compiled patterns
=================

You need to import pattern that you want to use ant use math() method.
Example that illustrate a basic of expyment.

.. code-block:: bash

    >>> import expynent
    >>> from expynent.compiled import *

.. code-block:: bash

	>>> credit_cards = (
	    '3519 2073 7960 3241',
	    '3519-2073-7960-3241',
	    '3519207379603241'
	)

.. code-block:: bash

	>>> for card in credit_cards:
	        if CREDIT_CARD.match(card):
	            print('Valid')
	        else:
	            print('Invalid')

Output
------

.. code-block:: bash

	Valid
	Valid
	Valid