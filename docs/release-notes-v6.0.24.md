# Percona Distribution for MongoDB 6.0.24 ({{date.6_0_24}})

[Upgrade now](minor-upgrade.md){.md-button}


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.24-19](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.24-19.html) and [Percona Backup for MongoDB 2.9.1](https://docs.percona.com/percona-backup-mongodb/release-notes/2.9.1.html).

## Release Highlights

### Packaging changes

Regular builds of Percona Distribution for MongoDB 6.0.24 are no longer supported on Ubuntu 20.04 (Focal Fossa) as this operating system has reached end of life. 

Percona Server for MongoDB Pro remains supported on Ubuntu 20.04 for Percona Customers. 

### Upstream Improvements

Improvements and bug fixes, provided by MongoDB and included in Percona Distribution for MongoDB are the following:

* [SERVER-93120](https://jira.mongodb.org/browse/SERVER-93120) - Fixed the issue with blocking Full Time Diagnostic Data Capture (FTDC) collection when checking the state of the bacupCursor by using atomic mode instead of a lock
* [SERVER-82037](https://jira.mongodb.org/browse/SERVER-82037) - Fixed the issue with exceeding the amount of memory allocated for index creation by limiting the number of file iterators a sorter can create
* [SERVER-88400](https://jira.mongodb.org/browse/SERVER-88400) - Fixed the issue with the `shardedDataDistribution` aggregation stage returning null value for timeseries when executed against bucket collections by computing metrics based on `timeseries.bucketCount` and `timeseries.avgBucketSize`
* [SERVER-92806](https://jira.mongodb.org/browse/SERVER-92806) -  Tracked nested paths through MatchExpression trees while encoding indexability for plan cache entries
* [SERVER-95976](https://jira.mongodb.org/browse/SERVER-95976) -  Introduced the "matchCollectionUUIDForUpdateLookup" parameter to enforce `updateLookup` to only return a document from the correct collection in the changestream stage
* [WT-13283](https://jira.mongodb.org/browse/WT-13283) - Fixed the bug where WiredTiger "cache aggressive mode" for better cache usage showed the "garbage values" by applying the compare-and-swap operation to the code to avoid
the value dropping to -1(which is `int_max` as `evict_aggressive_score` is
an unsigned int)

Find the full list of changes in the release notes of [MongoDB 6.0.21 Community Edition](https://www.mongodb.com/docs/v6.0/release-notes/6.0/#6.0.21---mar-17--2025) through [MongoDB 6.0.24 Community Edition](https://www.mongodb.com/docs/v6.0/release-notes/6.0/#6.0.24---jun-04--2025).

### Percona Backup for MongoDB 2.9.1 improvements:

* Fixed the issue that prevented PBM from taking physical backups in deployments using both MongoDB Community and Percona Server for MongoDB.