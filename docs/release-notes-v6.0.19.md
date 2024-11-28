# Percona Distribution for MongoDB 6.0.19 ({{date.6_0_19}})

[Upgrade now](minor-upgrade.md){.md-button}


Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. The aim of Percona Distribution for MongoDB is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.


Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 6.0.19-16](https://docs.percona.com/percona-server-for-mongodb/6.0/release_notes/6.0.19-16.html) and [Percona Backup for MongoDB 2.7.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.7.0.html).


## Release Highlights

!!! important

    This release of Percona Distribution for MongoDB includes a fix for a security vulnerability [CVE-2024-10921](https://nvd.nist.gov/vuln/detail/CVE-2024-10921). This vulnerability allowed an authorized user to trigger server crashes or receive the contents of the buffer over-reads of the server memory by sending specially crafted requests that constructed malformed BSON in MongoDB. The issue is fixed and included in Percona Server for MongoDB 6.0.19-16 and Percona Distribution for MongoDB 6.0.19.     

    Users running any minor version of Percona Distribution for MongoDB 6.0.x before 6.0.19 should [upgrade to this version](minor-upgrade.md) as soon as possible.  

### Upstream Improvements

Improvements and bug fixes, provided by MongoDB and included in Percona Distribution for MongoDB are the following:

* Fixed the issue with improper neutralization of null bytes that may have led to buffer over-reads in MongoDB Server.
* Use a new C++ type for BSON field names to ensure validity.

### Percona Backup for MongoDB 2.7.0 improvements:

#### Single authentication point for PBM running in Amazon EKS

Now PBM running in Amazon Elastic Kubernetes Service (EKS) can access AWS services using the credentials from the IAM role associated with the service account that is assigned to the Pod where PBM is running. Since with this improvement you don't have to pass the credentials to every individual Pods, the overall security of your infrastructure increases.

Consider the following limitation if you run Percona Operator for MongoDB: a restore does not work with this feature without the modification of default serviceAccount. It will be improved in future releases of the Operator to cover this case.

