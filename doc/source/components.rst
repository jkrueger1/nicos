.. _components:

Components of the NICOS system
==============================


.. digraph:: Components

    rankdir = LR;

    subgraph cluster0 {
        node [style=filled,color=white];
        style = "rounded,filled";
        color = lightsalmon;


        "nicos-watchdog" {rank = same; "nicos-elog"; "nicos-poller";
                          "nicos-collector"; "nicos-watchdog"}
        "nicos-cache" {rank = same; "nicos-daemon";}

        "nicos-cache"   -> "nicos-daemon"
        "nicos-cache"   -> "nicos-poller"
        "nicos-cache"   -> "nicos-watchdog"
        "nicos-cache"   -> "nicos-elog"
        "nicos-cache"   -> "nicos-collector"
        "nicos-watchdog"-> "nicos-cache"
        "nicos-daemon"  -> "nicos-cache"
        "nicos-poller"  -> "nicos-cache"
        "nicos-collector" -> "nicos-cache"

        edge[style=invis];
        "nicos-watchdog" -> "nicos-poller" -> "nicos-elog"

        label = "Servers";
    }

    subgraph cluster1 {
        node [style=filled,color=white];
        style = "rounded,filled";
        color = lightblue;

        "nicos-gui"{rank = same; "nicos-history";}
        "nicos-history"
        "nicos-monitor"
        "nicos-client"

        edge[style=invis];
        "nicos-gui" -> "nicos-history" -> "nicos-monitor" -> "nicos-client"

        label = "Clients";
    }


    "nicos-cache"   -> "nicos-gui"
    "nicos-cache"   -> "nicos-client"
    "nicos-cache"   -> "nicos-monitor"
    "nicos-cache"   -> "nicos-history"
    "nicos-daemon"  -> "nicos-gui"
    "nicos-daemon"  -> "nicos-client"
    "nicos-gui"     -> "nicos-daemon"
    "nicos-client"  -> "nicos-daemon"


The NICOS components come in the form of executables located in the ``bin``
subdirectory of the NICOS source:


.. index:: nicos-aio, nicos-gui, nicos-client

Shells
------

These components allow the user -- in some form or other -- to interact with the
NICOS system and execute commands.

.. describe:: nicos-gui

   This is the GUI client part of the server-client execution shell.  It
   connects to a ``nicos-daemon`` instance (see below) that controls the
   instrument.  The GUI uses `Qt <http://qt.nokia.com>`_ for the basic
   functionality, and `GR <http://gr-framework.org/>`_ for the data plotting and
   analysis windows.

.. describe:: nicos-client

   This is a text based client for the server-client execution shell.

.. describe:: nicos-aio

   This is the most basic NICOS shell.  ``nicos-aio`` (short for "all-in-one")
   takes the job of the daemon and gui, and presents to the user a slightly
   enhanced builtin Python shell, where commands can be executed.


.. index:: nicos-monitor, nicos-history

Other clients
-------------

These programs are clients that don't provide shell functionality.

.. describe:: nicos-monitor

   This program implements a graphical status monitor that displays current
   values of the instrument status from the NICOS cache.

   See :ref:`monitor`.

.. describe:: nicos-history

   This GUI program plots values (e.g. temperatures) from the cache over time.

   See :ref:`history`.


.. index:: nicos-cache, nicos-daemon, nicos-poller, nicos-elog, nicos-watchdog

Daemons
-------

These programs provide services and are designed to run as daemons once per
instrument.

.. describe:: nicos-cache

   The NICOS cache collects all values and parameters read from NICOS devices,
   so that individual components do not need to access the hardware too often.
   It also serves as an archival system for the instrument status.  For
   situation where excessive caching is not required, NICOS can also run without
   the cache component.

   See :ref:`cache`.

.. describe:: nicos-daemon

   This is the server part of the server-client execution shell.  It can be
   controlled via a TCP connection using a custom protocol designed for this
   purpose, with the ``nicos-gui`` component.  Multiple GUI clients can connect
   to one daemon.

   See :ref:`daemon`.

.. describe:: nicos-poller

   The poller periodically queries volatile information such as current sensor
   readings from all devices in the instrument setup, and pushes updates to the
   NICOS cache.

   See :ref:`poller`.

.. describe:: nicos-elog

   This daemon provides the "electronic logbook".  It collects information about
   special events such as "new sample" or "scan finished", and writes them to
   disk in an HTML file, which can serve as an electronic logbook of the
   experiment that is easier to read than a mere plain-text logfile.

   See :ref:`elog`.

.. describe:: nicos-watchdog

   This daemon reacts to cache events and checks against a configured list of
   error conditions (e.g. cooling water overheating).  If an error condition is
   detected, it can be configured to send notifications via email/short message,
   to execute a NICOS command and/or to stop counting until the condition is
   eliminated.

   See :ref:`watchdog`.

.. describe:: nicos-collector

   This daemon provides the possibility to forward cache events from one cache
   instance to another one.

   See :ref:`collector`.
