# Percona Distribution for MongoDB 6.0.5 (2023-03-29)

| Release date:     | March 29, 2023      |
|:------------------|:----------------------|
| **Installation**: | [Installing Percona Distribution for MongoDB](installation.md)


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.5-4](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.5-4.html) and [Percona Backup for MongoDB 2.0.5](https://docs.percona.com/percona-backup-mongodb/release-notes/2.0.5.html).


## Release Highlights
  
* Added support for [authentication using AWS IAM](https://docs.percona.com/percona-server-for-mongodb/6.0/aws-iam.html) enables you to natively integrate Percona Server for MongoDB with AWS services, increase security of your infrastructure by setting up password-less authentication and offload your DBAs from managing different sets of secrets. This is a [technical preview feature](https://docs.percona.com/percona-server-for-mongodb/6.0/glossary.html#technical-preview-feature)
* Improved master key rotation for data at rest encrypted with HashiCorp Vault enables you to use the same secret key path on every server in your entire deployment thus significantly simplifying the secrets management and key rotation process.

Bug fixes and improvements introduced in MongoDB and included in Percona Distribution for MongoDB are the following:

* Fixed a hang when inserting or deleting a document with large number of index entries
* Fixed the issue with filtering time-series collections that contain the date values earlier than Unix epoch (1970)
* Fixed the issue with adding a new unencrypted node into an encrypted replica set by removing options which might not apply for this node.
* Changed the default log verbosity level for `_killOperations` to D2.
* Fixed deadlock that can occur during index creation
* Resolved the issue with the sort order on clustered collections where requested decreasing order returned returned results in increasing order
* Fixed the issue with indexes reported as valid while being inconsistent by improving the validation of those indexes
* Fixed the migration of distributed transactions by registering the migration source operation observer hook in all paths where transactions transition into the prepared state.
  
Percona Backup for MongoDB 2.0.5 introduces the fixes:

* for the physical restore process for deployments where the `mongod` `--dbpath` option has a forward slash (‘/’) as the last char
* for security vulnerability [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723) by updating the Golang library dependencies to the latest versions


