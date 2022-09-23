Upgrading from older releases
-----------------------------

Upgrading from v3+
~~~~~~~~~~~~~~~~~~

Just upgrade Lekt using your :ref:`favorite installation method <install>` and run quickstart again::

    lekt local quickstart

Upgrading from v1 or v2
~~~~~~~~~~~~~~~~~~~~~~~

Versions 1 and 2 of Lekt were organized differently: they relied on many different ``Makefile`` and ``make`` commands instead of a single ``tutor`` executable. To migrate from an earlier version, you should first stop your platform::

    make stop

Then, install Lekt using one of the :ref:`installation methods <install>`. Then, create the Lekt project root and move your data::

    mkdir -p "$(lekt config printroot)"
    mv config.json data/ "$(lekt config printroot)"

Finally, launch your platform with::

    lekt local quickstart
