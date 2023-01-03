# Percona Distribution for MongoDB 6.0.3 (2022-12-07)

| Release date:     | December 7, 2022      |
|:------------------|:----------------------|
| **Installation**: | [Installing Percona Distribution for MongoDB](installation.md)


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.3-2](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.3-2.html) and [Percona Backup for MongoDB 2.0.2](https://docs.percona.com/percona-backup-mongodb/release-notes/2.0.2.html).


## Release Highlights
  
Bug fixes and improvements introduced in MongoDB and included in Percona Distribution for MongoDB are the following:

* Fixed the condition where issuing concurrent ``removeShard`` and ``movePrimary`` commands may delete unsharded collections in a database thus causing data loss.
* Fixed the issue with the resharding command failure if the required projection sort relating to sample chunks and planned number of initial chunks is greater than 100MB.
* Corrected a situation where the order of Resharding steps could cause segmentation faults
* Corrected a situation where a requested stepdown could run into an uninterruptible lock during the election process and cause a deadlock.
* Prevented yielding strong locks upon startup recovery when ``_id`` index is missing
* Fixed the issue with how the server handles batches of writes when running $out with secondary read preference by updating write size estimation logic in ``DocumentSourceWriter``
* Prevented dropping empty path component from `elemMatch` path during index selection
* Prevented yielding strong locks upon startup recovery when ``_id`` index is missing

  
Percona Backup for MongoDB 2.0.2 fixes the usability issues for applications operating with it by providing the error messages for the status output in the JSON format.  
  
