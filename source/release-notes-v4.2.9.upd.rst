.. _DISTMONGO-4.2.9_update

================================================================================
*Percona Distribution for MongoDB* 4.2.9 Update
================================================================================

:Date: October 9, 2020
:Installation: :ref:`install`

|pdmdb| is a collection of solutions to run and operate your
|mongodb| efficiently with the data being consistently backed up.  

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This update to the |pdmdb| fixes the security vulnerability `CVE-2020-26542 <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-26542>`_ and is based on |PSMDB| |psmdb-version| and |pbm| |pbm-version|. 

.. |psmdb-version| replace:: 4.2.9-10
.. |pbm-version| replace:: 1.3.1 			    

.. include:: .res/replace.txt