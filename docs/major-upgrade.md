# Major upgrade of Percona Distribution for MongoDB

To stay up-to-date with the latest features, performance improvements and security enhancements, consider to upgrade your Percona Distribution for MongoDB to the latest major version. 

The upgrade flow consists of the following stages:

* Upgrade of Percona Server for MongoDB in a rolling-restart way
* Upgrade of Percona Backup for MongoDB
* Post-upgrade steps

This document describes the upgrade from Percona repositories as the recommended method.

## Considerations

1. You must be running Percona Distribution 6.0 before upgrading to 7.0. Upgrades from earlier versions directly to 7.0 are not supported.
2. Before the upgrade, test your applications with the new version in a testing environment to ensure compatibility. For more information see [Compatibility Changes in MongoDB 7.0](https://www.mongodb.com/docs/v7.0/release-notes/7.0-compatibility/).


## Upgrade of Percona Server for MongoDB

This section describes the in-place upgrade where the existing data and configuration files are preserved.

<i info>:material-information: Info:</i> The steps below describe the upgrade of a single `mongod` instance. To upgrade a replica set or a sharded cluster, use the rolling restart way where you upgrade nodes individually while the other nodes remain operational.

### Before you start

1. Back up your data and configuration files in order to be on the safe side if anything goes wrong.
2. In Percona Server for MongoDB 7.0, journaling is enabled by default. Both the `storage.journal.enabled` configuration option and the corresponding `--journal`, `--no-journal` command-line options are ignored. You receive the corresponding warning during the server start after the upgrade. To get rid of this warning, change your configuration to remove the journaling options.

### Procedure

=== ":material-debian: Upgrade on Debian and Ubuntu"

    Run all commands as root or via `sudo`.
    {.power-number}

     1. Stop the `mongod` service:

          ```{.bash data-prompt="$"}
          $ sudo systemctl stop mongod
          ```

     2. Enable the repository for Percona Distribution for MongoDB 7.0:

         ```{.bash data-prompt="$"}
         $ sudo percona-release enable pdmdb-7.0
         ```

     3. Update the local cache:

         ```{.bash data-prompt="$"}
         $ sudo apt update
         ```

     4. Install Percona Server for MongoDB 7.0 packages:

         ```{.bash data-prompt="$"}
         $ sudo apt install percona-server-mongodb
         ```

     5. Start the `mongod` instance:

         ```{.bash data-prompt="$"}
         $ sudo systemctl start mongod
         ```

=== ":material-redhat: Upgrade on Red Hat Enterprise Linux and derivatives"

    Run all commands as root or via `sudo`.
    {.power-number}

     1. Stop the `mongod` service:

          ```{.bash data-prompt="$"}
          $ sudo systemctl stop mongod
          ```

     2. Enable Percona repository for Percona Distribution for MongoDB 7.0:

         ```{.bash data-prompt="$"}
         $ sudo percona-release enable pdmdb-7.0
         ``` 

     3. Install Percona Server for MongoDB 7.0 packages:

         ```{.bash data-prompt="$"}
         $ sudo yum install percona-server-mongodb
         ```

     4. Start the `mongod` instance:

         ```{.bash data-prompt="$"}
         $ sudo systemctl start mongod
         ```

After the upgrade, Percona Server for MongoDB is started with the feature set of 6.0 version. Assuming that your applications are compatible with the new version, enable 7.0 version features. Run the following command against the `admin` database:

```{.javascript data-prompt=">"}
> db.adminCommand( { setFeatureCompatibilityVersion: "7.0" } )
```

!!! admonition "See also"

    MongoDB Documentation:

    * [Upgrade a Standalone](https://docs.mongodb.com/manual/release-notes/7.0-upgrade-standalone/)
    * [Upgrade a Replica Set](https://docs.mongodb.com/manual/release-notes/7.0-upgrade-replica-set/)
    * [Upgrade a Sharded Cluster](https://docs.mongodb.com/manual/release-notes/7.0-upgrade-sharded-cluster/)

## Upgrade of Percona Backup for MongoDB

Upgrade Percona Backup for MongoDB on all nodes where it is installed.

=== ":material-debian: On Debian and Ubuntu Linux"

    Run all commands as root or via `sudo`.
    {.power-number}

    1. Stop `pbm-agent`

        ```{.bash data-prompt="$"}
        $ sudo systemctl stop pbm-agent
        ```

    2. Install new packages

        ```{.bash data-prompt="$"}
        $ sudo apt install percona-backup-mongodb
        ```  

    3. Reload the `systemd` process to update the unit file with the following command:

        ```{.bash data-prompt="$"}
        $ sudo systemctl daemon-reload
        ```

    4. Update permissions

        For a *filesystem-based backup storage*, grant read / write permissions to the backup directory to the `mongod` user.


    5. Start `pbm-agent`

        ```{.bash data-prompt="$"}
        $ sudo systemctl start pbm-agent
        ```

=== ":material-redhat: On Red Hat Enterprise Linux and derivatives"

    Run all commands as root or via `sudo`.
    {.power-number}

    1. Stop `pbm-agent`

        ```{.bash data-prompt="$"}
        $ sudo systemctl stop pbm-agent
        ```

    2. Install new packages

        ```{.bash data-prompt="$"}
        $ sudo yum install percona-backup-mongodb
        ```

    3. Reload the `systemd` process to update the unit file with the following command:

       ```{.bash data-prompt="$"}
       $ sudo systemctl daemon-reload
       ```

    4. Update permissions

        For a *filesystem-based backup storage*, grant read / write permissions to the backup directory to the `mongod` user.

    5. Start `pbm-agent`

        ```{.bash data-prompt="$"}
        $ sudo systemctl start pbm-agent
        ``` 

### Post-upgrade steps

Make a fresh backup to ensure you have the latest data in case of a failure.
