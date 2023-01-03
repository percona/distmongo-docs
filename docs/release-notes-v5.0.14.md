# Percona Distribution for MongoDB* 5.0.14 (2022-12-08)

| Release date:     | December 8, 2022      |
|:------------------|:----------------------|
| **Installation**: | [Installing Percona Distribution for MongoDB](installation.md) |

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of |pdmdb| is based on [Percona Server for MongoDB 5.0.14-12](https://docs.percona.com/percona-server-for-mongodb/5.0/release_notes/5.0.14-12.html) and [Percona Backup for MongoDB 2.0.2](https://docs.percona.com/percona-backup-mongodb/release-notes/2.0.2.html).

## Release Highlights

With this release, [`$backupCursor and $backupCursorExtend aggregation stages](https://docs.percona.com/percona-server-for-mongodb/5.0/backup-cursor.html) is now generally available, enabling you to use it for building custom backup solutions.

The bug fixes and improvements provided by MongoDB and included in Percona Server for MongoDB 5.0.14-12 are the following:

* Fixed the bug where an unexpected behavior could negatively impact existing TTL indexes with improper configuration and could cause the sudden expiration of TTL-indexed documents in a collection. This sudden expiration could cause data to be aged out prior than planned and could negatively impact write performance.

  This bug involves TTL indexes with the ``expireAfterSeconds`` value of NaN (not-a-number). The TTL indexes are treated as 0 instead of NaN and that resulted in the sudden expiration of TTL-indexed documents in a collection. The bug affects MongoDB 5.0.0 through 5.0.13 and MongoDB 6.0.0 through 6.0.1.

  It could be hit on MongoDB 4.4/4.2 when initially syncing from a 5.0.0-5.0.13 or 6.0.0-6.0.1 node and on MongoDB 5.0.0-5.0.13 when restoring from a ``mongodump`` of 4.2 / 4.4 collection or initially syncing from a 4.2/4.4 node that has a TTL configured with expireAfterSeconds: NaN.

  The issue is fixed upstream in version 5.0.14 and 6.0.2. As the general recommendation, avoid using expireAfterSeconds: NaN as a configuration and correct this config anywhere it exists.
  
  Follow closely the upstream recommendations to detect affected indexes and modify them using the collMod command.

* Corrected a potential race condition where multiple writing threads can update collection metadata in a way where overwrites could possibly happen. This could cause data/documents to be either unavailable or lost.
* Fixed the issue with how the server handles batches of writes when running $out with secondary read preference by updating write size estimation logic in ``DocumentSourceWriter``
* Improved the performance of inserts into unique indexes
* Prevented dropping empty path component from `elemMatch` path during index selection


Percona Backup for MongoDB 2.0.2 fixes the usability issues for applications operating with it by providing the error messages for the status output in the JSON format.

