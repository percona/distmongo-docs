# Percona Distribution for MongoDB 7.0.15 ({{date.7_0_15}})

[Upgrade now](installation.md){.md-button}

Percona Distribution for MongoDB is a freely available MongoDB database alternative, giving you a single solution that combines enterprise components from the open source community, designed and tested to work together. Its aim is to enable you to run and operate your
MongoDB efficiently with the data being consistently backed up.

Percona Distribution for MongoDB includes the following components:

* *Percona Server for MongoDB* is a fully compatible source-available, drop-in replacement
for MongoDB.

* *Percona Backup for MongoDB* is a distributed, low-impact solution for achieving
consistent backups of MongoDB sharded clusters and replica sets.

This release of Percona Distribution for MongoDB is based on the production release of [Percona Server for MongoDB 7.0.15-9](https://docs.percona.com/percona-server-for-mongodb/7.0/release_notes/7.0.15-9.html) and [Percona Backup for MongoDB 2.7.0](https://docs.percona.com/percona-backup-mongodb/release-notes/2.7.0.html).

## Release Highlights

!!! important

    This release of Percona Distribution for MongoDB includes a fix for a security vulnerability [CVE-2024-10921](https://nvd.nist.gov/vuln/detail/CVE-2024-10921). This vulnerability allowed an authorized user to trigger server crashes or receive the contents of the buffer over-reads of the server memory by sending specially crafted requests that constructed malformed BSON in MongoDB. The issue is fixed and included in Percona Server for MongoDB 7.0.15-9 and Percona Distribution for MongoDB 7.0.15.    

    Users running any minor version of Percona Distribution for MongoDB 7.0.x before 7.0.15 should [upgrade to this latest version](minor-upgrade.md) as soon as possible. 


### Percona Server for MongoDB improvements

### Prevent master encryption key loss on the Vault server

Before Percona Server for MongoDB puts a new master encryption key to the Vault server as the versioned secret, it now checks if the secret's version reached the defined maximum (10 by default). This prevents the loss of the old secret and the master encryption key it stores on the Vault server. 

Make sure Percona Server for MongoDB has read permissions for the secret's metadata and the secrets engine configuration. To learn more, refer to the [documentation](https://docs.percona.com/percona-server-for-mongodb/7.0/vault.html#master-key-loss-prevention). 

#### Upstream Improvements

* Fixed the issue with improper neutralization of null bytes that may have led to buffer over-reads in MongoDB Server.
* Use a new C++ type for BSON field names to ensure validity.

### Percona Backup for MongoDB 2.7.0 improvements:

#### Single authentication point for PBM running in Amazon EKS

Now PBM running in Amazon Elastic Kubernetes Service (EKS) can access AWS services using the credentials from the IAM role associated with the service account that is assigned to the Pod where PBM is running. Since with this improvement you don't have to pass the credentials to every individual Pods, the overall security of your infrastructure increases.

Consider the following limitation if you run Percona Operator for MongoDB: a restore does not work with this feature without the modification of default serviceAccount. It will be improved in future releases of the Operator to cover this case.
