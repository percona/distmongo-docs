.. _DISTMONGO-6.0.2:

================================================================================
*Percona Distribution for MongoDB* 6.0.2 (2022-10-31)
================================================================================

:Date: October 31, 2022
:Installation: :ref:`install`

We are pleased to announce the release of the Percona Distribution for MongoDB  for the recent major version 6.0.x.

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
|mongodb| efficiently with the data being consistently backed up.

|pdmdb| includes the following components:

* |PSMDB| is a fully compatible source-available, drop-in replacement
  for MongoDB.
* |pbm| is a distributed, low-impact solution for achieving
  consistent backups of |mongodb| sharded clusters and replica sets.

This release of |pdmdb| is based on the production release of `Percona Server for MongoDB 6.0.2-1 <https://www.percona.com/doc/percona-server-for-mongodb/6.0/release_notes/6.0.2-1.html>`_ and `Percona Backup for MongoDB 2.0.2 <https://www.percona.com/doc/percona-backup-mongodb/release-notes/2.0.2.html>`_.


Release Highlights
==================

* `Data-at-rest encryption using the Key Management Interoperability Protocol (KMIP) <https://docs.percona.com/percona-server-for-mongodb/6.0/kmip.html>`_  is generally available enabling you to use it in your production environment
* ``$backupCursor`` and ``$backupCursorExtended`` functionality is generally available, enabling your application developers to use it for building custom backup solutions. 
  
  .. note::

     |pdmdb| includes `Percona Backup for MongoDB <https://docs.percona.com/percona-backup-mongodb/index.html>`_ - the open source tool for consistent backups and restores in MongoDB sharded clusters.

* |PSMDB| packages now include ``mongosh`` instead of ``mongo`` CLI. If you `install Percona Server for MongoDB from tarballs <https://docs.percona.com/percona-server-for-mongodb/6.0/install/tarball.html#tarball>`_, you must install ``mongosh`` from a separate tarball.

|pdmdb| 6.0.2 includes all the features of MongoDB 6.0.2 Community Edition, among which are the following:

* `Enhanced time series collections <https://www.mongodb.com/docs/v6.0/core/timeseries-collections/#std-label-manual-timeseries-collection>`_ enable you to:
  
  - Get deeper data analysis insights by building compound and `secondary indexes <https://www.mongodb.com/docs/v6.0/core/timeseries/timeseries-secondary-index/#std-label-timeseries-add-secondary-index-mongodb-6.0>`_ on time, metadata and measurement fields.  
  - Distribute the load among nodes in the cluster by `sharding new and existing time series collections <https://www.mongodb.com/docs/v6.0/core/timeseries/timeseries-shard-collection/#std-label-manual-timeseries-shard-collection>`_.
  - Benefit from faster reads and improved performance by applying the sorting on the most recent entry instead of the whole collection.
    
* The following `change streams <https://www.mongodb.com/docs/v6.0/changeStreams/#std-label-changeStreams>`_ optimizations help you enhance your event-driven solutions:
  
  - Improve in-app notifications, reference deleted documents or feed the updated version of the entire doc to the downstream system using the `before and after states of a document that was changed <https://www.mongodb.com/docs/v6.0/reference/method/db.collection.watch/#std-label-db.collection.watch-change-streams-pre-and-post-images-example>`_.
  - React not only to data changes but also to database change events like creating or dropping of collections with the Data Definition Language (DDL) support.

* New aggregation stages like ``$densify``, ``$documents``, ``$fill`` and operators like ``$bottom``, ``$firstN``, ``$lastN``, ``$maxN`` / ``$minN`` and others enable you to off load work from your developers to the database. These operators allow automating key commands, getting required data insights by combining individual operators into aggregation pipelines. As a result, your developers spend less time on writing complex code or manipulating data manually and can focus on other activities.  
* `Cluster-wide configuration parameters <https://www.mongodb.com/docs/v6.0/reference/cluster-parameters/#std-label-cluster-parameters>`_ and commands save your DBAs' time on cluster administration.
* The `Stable API <https://www.mongodb.com/docs/v6.0/reference/stable-api/#std-label-stable-api>`_ (formerly known as versioned API) features the extended set of new database commands and aggregation operators which enables you to improve communication of your apps and MongoDB.
* Speed up data processing and save on storage costs with `clustered collections <https://www.mongodb.com/docs/v6.0/core/clustered-collections/#std-label-clustered-collections>`_. Clustered collections don’t require secondary indexes and thus, result in faster queries. A single read/write for the index and the document improves performance for inserts, updates, deletes and queries. With less storage space required by clustered connections, bulk updates and inserts are performed faster. And by turning clustered indexes to TTL indexes with a single field, you benefit from simplified delete operations and reduced storage costs.
  
|PBM| 2.0.x improvements are the following:

* Physical backups and restores are now generally available. This enables you to use them in production environments.
* `Data-at-rest encryption <https://docs.percona.com/percona-backup-mongodb/usage/restore.html#physical-restores-with-data-at-rest-encryption>`_ is supported for physical backups and restores. This enables you to comply to data security regulations and save time on operating with large data sets.
* By `tracking physical restore progress <https://docs.percona.com/percona-backup-mongodb/usage/restore-progress.html>`_, you have a clear picture of your restore operations and can timely react to any changes or issues.
* `Logical backups and restores can now be done selectively <https://docs.percona.com/percona-backup-mongodb/usage/selective-backup.html>`_. This is a tech preview feature [1]_ yet it enables you to work only with the desired subset of data and thereby save time on database maintenance and costs on storage.
  
|PBM| 2.0.2 fixes the usability issues for applications operating with Percona Backup for MongoDB by providing the error messages for the status output in the JSON format.  
  

.. [1] Tech Preview Features are not yet ready for enterprise use and are not included in support via SLA. They are included in this release so that users can provide feedback prior to the full release of the feature in a future GA release (or removal of the feature if it is deemed not useful). This functionality can change (APIs, CLIs, etc.) from tech preview to GA. 
.. include:: .res/replace.txt
