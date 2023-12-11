# Percona Distribution for MongoDB 7.0.4 (2023-12-11)

[Installation](installation.md){.md-button}

We are pleased to announce the release of the Percona Distribution for MongoDB  for the recent major version 7.0.x.

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 7.0.4-2](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.4-2.html) and [Percona Backup for MongoDB 2.3.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.3.1.html).


## Release Highlights
  
* [AWS IAM authentication](https://docs.percona.com/percona-server-for-mongodb/7.0/aws-iam.html) is now generally available, enabling you to use this functionality in production environments.
* Added the ability to configure the retry behavior for Percona Server for MongoDB to connect to the KMIP server when using [data-at-rest encryption](https://docs.percona.com/percona-server-for-mongodb/7.0/kmip.html)
* Percona Server for MongoDB now includes telemetry that fills in the gaps in our understanding of how you use our products and how we can better improve them. Participation in the anonymous program is optional. You can opt-out if you prefer not to share this information. [Read more about Telemetry](https://docs.percona.com/percona-server-for-mongodb/7.0/telemetry.html).  
* Fixed the routing issue with sharded time series collections which could result in metadata inconsistency. The issue occurred when the documents that have the shard key containing the embedded object composed of multiple fields are routed to an incorrect shard and become orphanated. As a result orphanated documents may not be returned when queried through the mongos and/or may be deleted. The issue affects time series sharded collections starting in MongoDB version 5.0.6 through versions 5.0.21, 6.0.11 and 7.0.2. 

   If you are using time series collections, upgrade to MongoDB 7.0.4 or Percona Server for MongoDB 7.0.4-2 as soon as possible. Please follow closely the upstream recommendations for how to identify and preserve orphanated documents. 

* Fixed the order of execution of data inserts/updates and deletes into `config.image_collection` 
* Fixed the behaviour of the `$merge` aggregation stage on sharded clusters when the default read concern has been set to "majority"
* Optimized large group keys by adding the document shredder stage
* Speeded up the logic that persist routing table cache
* Fixed the $densify stage processing where documents are generated outside of range
* Fixed the issue with the data and the ShardVersion mismatch for sharded multi-document transactions by adding the check that no chunk has moved for the collection being referenced since transaction started
* Improved the slot-based execution engine (SBE) multi-planner performance for query which returns zero results
* Improved the recipient shard behavior during the chunk migration to wait for changes to catalog cache to be persisted before the cloning phase.
* Fixed the issue that caused the modification of the original ChunkMap vector during the chunk migration and that could lead to data loss. The issue affects MongoDB versions 4.4.25, 5.0.21, 6.0.10 through 6.0.11 and 7.0.1 through 7.0.2. Requires stopping all chunk merge activities and restarting all the binaries in the cluster (both `mongod` and `mongos`). 
* Fixed the rollback-to-stable behavior to read the newest transaction value only when it exists in the checkpoint.

  
Percona Backup for MongoDB 2.3.1 improvements are the following:

* Support for Percona Server for MongoDB 7.0.x
* The ability to define custom endpoints when using Microsoft Azure Blob Storage for backups
* Improved PBM Docker image to allow making physical backups with the shared mongodb data volume
* Updated Golang libraries that include fixes for the security vulnerability CVE-2023-39325.

