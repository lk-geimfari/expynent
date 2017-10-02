How to use patterns
===================

The most common use for re is to search for patterns in text. With expynent, pattern recognition is usefull.

.. code-block:: bash

    >>> import re
    >>> from expynent import *

.. code-block:: bash

	>>> if re.match(CREDIT_CARD, '3519 2073 7960 3241'):
		    print('Valid')

Output
------

.. code-block:: bash

	Valid
