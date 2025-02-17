.. _web_proxy:

Running Open edX behind a web proxy
===================================

The containerized web server (`Caddy <https://caddyserver.com/>`__) needs to listen to ports 80 and 443 on the host. If there is already a webserver running on the host, such as Apache or Nginx, the caddy container will not be able to start. Lekt supports running behind a web proxy. To do so, add the following configuration::

       lekt config save --set ENABLE_WEB_PROXY=false --set CADDY_HTTP_PORT=81

In this example, the caddy container port would be mapped to 81 instead of 80. You must then configure the web proxy on the host. As of v11.0.0, configuration files are no longer provided for the automatic configuration of your web proxy. You should set up a reverse proxy to `localhost:CADDY_HTTP_PORT` from the following hosts: LMS_HOST, PREVIEW_LMS_HOST, CMS_HOST, as well as any additional host exposed by your plugins.

.. warning::
    In this setup, the Caddy HTTP port will be exposed to the world. Make sure to configure your server firewall to block unwanted connections to your server's ``CADDY_HTTP_PORT``. Alternatively, you can configure the Caddy container to accept only local connections::

        lekt config save --set CADDY_HTTP_PORT=127.0.0.1:81
