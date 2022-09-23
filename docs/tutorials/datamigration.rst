Making backups and migrating data
---------------------------------

With Lekt, all data are stored in a single folder. This means that it's extremely easy to migrate an existing platform to a different server. For instance, it's possible to configure a platform locally on a laptop, and then move this platform to a production server.

1. Make sure `tutor` is installed on both servers with the same version.
2. Stop any running platform on server 1::

    lekt local stop

3. Transfer the configuration, environment, and platform data from server 1 to server 2::

    rsync -avr "$(lekt config printroot)/" username@server2:/tmp/tutor/

4. On server 2, move the data to the right location::

    mv /tmp/lekt "$(lekt config printroot)"

5. Start the instance with::

    lekt local start -d

Making database dumps
---------------------

To dump all data from the MySQL and Mongodb databases used on the platform, run the following commands::

    lekt local exec \
        -e USERNAME="$(lekt config printvalue MYSQL_ROOT_USERNAME)" \
        -e PASSWORD="$(lekt config printvalue MYSQL_ROOT_PASSWORD)" \
        mysql sh -c 'mysqldump --all-databases --user=$USERNAME --password=$PASSWORD > /var/lib/mysql/dump.sql'
    lekt local exec mongodb mongodump --out=/data/db/dump.mongodb

The ``dump.sql`` and ``dump.mongodb`` files will be located in ``$(lekt config printroot)/data/mysql`` and ``$(lekt config printroot)/data/mongodb``.
