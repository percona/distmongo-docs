# Percona Distribution for MongoDB 4.4.18 (2022-12-19)


| **Release date** | December 19, 2022 |
|----------------- | ---------------- | 
| **Installation** | [Install Percona Distribution for MongoDB](installation.md) |

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of |pdmdb| is based on [Percona Server for MongoDB 4.4.18-18])https://www.percona.com/doc/percona-server-for-mongodb/4.4/release_notes/4.4.18-18.html) and [Percona Backup for MongoDB 2.0.2](https://www.percona.com/doc/percona-backup-mongodb/release-notes/2.0.2.html).


## Release Highlights

This release of Percona Distribution for MongoDB includes improvements and bug fixes, provided by MongoDB and included in Percona Server for MongoDB. The most notable from them are the following:

* Fixed the issue with how the server handles batches of writes when running $out with secondary read preference by updating write size estimation logic in ``DocumentSourceWriter``
* Improved the performance of inserts into unique indexes
* Prevented dropping empty path component from elemMatch path during index selection
* Avoided sending the "keyValue" field to drivers on duplicate key error
* Disallowed the use of the ``allowSpeculativeMajorityReads`` flag for the ``find`` command in transactions
  

Percona Backup for MongoDB 2.0.2 fixes the usability issues for applications operating with it by providing the error messages for the status output in the JSON format.  

