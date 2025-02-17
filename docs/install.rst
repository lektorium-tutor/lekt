.. _install:

Installing Lekt
================

.. _requirements:

Requirements
------------

* Supported OS: Lekt runs on any 64-bit, UNIX-based OS. It was also reported to work on Windows (with `WSL 2 <https://docs.microsoft.com/en-us/windows/wsl/install>`__).
* Architecture: support for ARM64 is a work-in-progress. See `this issue <https://github.com/lektorium-tutor/tutor/issues/510>`__.
* Required software:

    - `Docker <https://docs.docker.com/engine/installation/>`__: v18.06.0+
    - `Docker Compose <https://docs.docker.com/compose/install/>`__: v1.22.0+

.. warning::
    Do not attempt to simply run ``apt-get install docker docker-compose`` on older Ubuntu platforms, such as 16.04 (Xenial), as you will get older versions of these utilities.

* Ports 80 and 443 should be open. If other web services run on these ports, check the tutorial on :ref:`how to setup a web proxy <web_proxy>`.
* Hardware:

    - Minimum configuration: 4 GB RAM, 2 CPU, 8 GB disk space
    - Recommended configuration: 8 GB RAM, 4 CPU, 25 GB disk space

.. note::
    On Mac OS, by default, containers are allocated 2 GB of RAM, which is not enough. You should follow `these instructions from the official Docker documentation <https://docs.docker.com/docker-for-mac/#advanced>`__ to allocate at least 4-5 GB to the Docker daemon. If the deployment fails because of insufficient memory during database migrations, check the :ref:`relevant section in the troubleshooting guide <migrations_killed>`.

Download
--------

Choose **one** of the installation methods below. If you install Lekt in different ways, you will end up with multiple ``tutor`` executables, which is going to be very confusing. At any time, you can check the path to your ``tutor`` executable by running ``which tutor``.

Python package
~~~~~~~~~~~~~~

.. include:: download/pip.rst

Check the "tutor" package on Pypi: https://pypi.org/project/tutor. You will need Python >= 3.6 with pip and the libyaml development headers. On Ubuntu, these requirements can be installed by running::

    sudo apt install python3 python3-pip libyaml-dev

.. _install_binary:

Binary release
~~~~~~~~~~~~~~

The latest binaries can be downloaded from https://github.com/lektorium-tutor/tutor/releases. From the command line:

.. include:: download/binary.rst

This is the simplest and recommended installation method for most people who do not have Python 3 on their machine. Note however that **you will not be able to use custom plugins** with this pre-compiled binary. The only plugins you can use with this approach are those that are already bundled with the binary: see the :ref:`existing plugins <existing_plugins>`.

.. _install_source:

Installing from source
~~~~~~~~~~~~~~~~~~~~~~

To inspect the Lekt source code, install Lekt from `the Github repository <https://github.com/lektorium-tutor/tutor>`__::

    git clone https://github.com/lektorium-tutor/tutor
    cd tutor
    pip install -e .

Configuring DNS records
-----------------------

When running a server in production, it is necessary to define `DNS records <https://en.wikipedia.org/wiki/Domain_Name_System#Resource_records>`__ which will make it possible to access your Open edX platform by name in your browser. The precise procedure to create DNS records varies from one provider to the next and is beyond the scope of these docs. You should create a record of type A with a name equal to your LMS hostname (given by ``lekt config printvalue LMS_HOST``) and a value that indicates the IP address of your server. Applications other than the LMS, such as the studio, ecommerce, etc. typically reside in subdomains of the LMS. Thus, you should also create a CNAME record to point all subdomains of the LMS to the LMS_HOST.

For instance, the demo Open edX server that runs at https://demo.openedx.overhang.io has the following DNS records::

    demo.openedx 1800 IN A 172.105.89.208
    *.demo.openedx 1800 IN CNAME demo.openedx.overhang.io.

.. _cloud_install:

Zero-click AWS installation
---------------------------

Lekt can be launched on Amazon Web Services very quickly with the `official Lekt AMI <https://aws.amazon.com/marketplace/pp/B07PV3TB8X>`__. Shell access is not required, as all configuration will happen through the Lekt web user interface. For detailed installation instructions, we recommend watching the following video:

.. youtube:: xtXP52qGphA

.. _upgrade:

Upgrading
---------

To upgrade Open edX or benefit from the latest features and bug fixes, you should simply upgrade Lekt. Start by upgrading the "tutor" package and its dependencies::

    pip install --upgrade "tutor[full]"

Then run the ``quickstart`` command again. Depending on your deployment target, run one of::

    lekt local quickstart # for local installations
    lekt dev quickstart   # for local development installations
    lekt k8s quickstart   # for Kubernetes installation

Upgrading with custom Docker images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you run :ref:`customised <configuration_customisation>` Docker images, you need to rebuild them before running ``quickstart``::

    lekt config save
    lekt images build all # specify here the images that you need to build
    lekt local quickstart

Upgrading to a new Open edX release
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Major Open edX releases are published twice a year, in June and December, by the Open edX `Build/Test/Release working group <https://discuss.openedx.org/c/working-groups/build-test-release/30>`__. When a new Open edX release comes out, Lekt gets a major version bump (see :ref:`versioning`). Such an upgrade typically includes multiple breaking changes. Any upgrade is final because downgrading is not supported. Thus, when upgrading your platform from one major version to the next, it is strongly recommended to do the following:

1. Read the changes listed in the `CHANGELOG.md <https://github.com/lektorium-tutor/tutor/blob/master/CHANGELOG.md>`__ file. Breaking changes are identified by a "💥".
2. Perform a backup. On a local installation, this is typically done with::

    lekt local stop
    sudo rsync -avr "$(lekt config printroot)"/ /tmp/tutor-backup/

3. If you created custom plugins, make sure that they are compatible with the newer release.
4. Test the new release in a sandboxed environment.
5. If you are running edx-platform, or some other repository from a custom branch, then you should rebase (and test) your changes on top of the latest release tag (see :ref:`edx_platform_fork`).

The process for upgrading from one major release to the next works similarly to any other upgrade, with the ``quickstart`` command (see above). The single difference is that if the ``quickstart`` command detects that your lekt environment was generated with an older release, it will perform a few release-specific upgrade steps. These extra upgrade steps will be performed just once. But they will be ignored if you updated your local environment (for instance: with ``lekt config save``) before running ``quickstart``. This situation typically occurs if you need to re-build some Docker images (see above). In such a case, you should make use of the ``upgrade`` command. For instance, to upgrade a local installation from Maple to Nutmeg and rebuild some Docker images, run::

    lekt config save
    lekt images build all # list the images that should be rebuilt here
    lekt local upgrade --from=maple
    lekt local quickstart

.. _autocomplete:

Shell autocompletion
--------------------

Lekt is built on top of `Click <https://click.palletsprojects.com>`_, which is a great library for building command line interface (CLI) tools. As such, Lekt benefits from all Click features, including `auto-completion <https://click.palletsprojects.com/en/8.x/bashcomplete/>`_. After installing Lekt, auto-completion can be enabled in bash by running::

    _LEKT_COMPLETE=bash_source lekt >> ~/.bashrc

If you are running zsh, run instead::

    _LEKT_COMPLETE=zsh_source lekt >> ~/.zshrc

After opening a new shell, you can test auto-completion by typing::

    lekt <tab><tab>

Uninstallation
--------------

It is fairly easy to completely uninstall Lekt and to delete the Open edX platforms that are running locally.

First of all, stop any locally-running platform and remove all Lekt containers::

    lekt local dc down --remove-orphans
    lekt dev dc down --remove-orphans

Then, delete all data associated with your Open edX platform::

    # WARNING: this step is irreversible
    sudo rm -rf "$(lekt config printroot)"

Finally, uninstall Lekt itself::

    # If you installed lekt from source
    pip uninstall tutor

    # If you downloaded the lekt binary
    sudo rm /usr/local/bin/tutor

    # Optionally, you may want to remove Lekt plugins installed.
    # You can get a list of the installed plugins:
    pip freeze | grep tutor
    # You can then remove them using the following command:
    pip uninstall <plugin-name>
