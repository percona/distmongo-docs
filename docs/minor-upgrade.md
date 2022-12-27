# Minor upgrade of Percona Distribution for MongoDB

To receive bug fixes and feature enhancements that come with minor releases, keep your Percona Distribution for MongoDB upgraded to the latest version.

Before the upgrade, we recommend to back up your data in order to be on the safe side if anything goes wrong.

Similar to installing, Percona Distribution for MongoDB is upgraded from *Percona* repositories using the **percona-release** utility. Update **percona-release** to the latest version using [these instructions](https://www.percona.com/doc/percona-repo-config/percona-release.html#updating-percona-release-to-the-latest-version). This is required to install new version packages of Percona Distribution for MongoDB.

Run the following commands as root or by using the **sudo** command.

The upgrade procedure includes the following steps:

## Enable Percona repository

If you installed Percona Distribution for MongoDB from the Major release repository, this step is optional. This repository automatically includes new version packages and you receive a prompt for an upgrade from the package manager of your operating system.

If you installed Percona Distribution for MongoDB from the Minor release repository, you must enable the new version repository (for example, `pdmdb-6.0.2`) to upgrade. We recommend to use the `setup` subcommand:

```{.bash data-prompt="$"}
$ sudo percona-release setup pdmdb-6.0.2
```

!!! admonition "See also"

    [Install Percona Distribution for MongoDB](installation.md#install)

## Stop the service

Stop Percona Server for MongoDB:

```{.bash data-prompt="$"}
$ sudo systemctl mongod stop
```

Stop **pbm-agent**:

```{.bash data-prompt="$"}
$ sudo systmectl pbm-agent stop
```

## Install new version packages

Install Percona Server for MongoDB and Percona Backup for MongoDB using the package manager of your operating system. Please refer to the pdmdb-install section for the corresponding installation instructions.

## Restart the service

Start Percona Server for MongoDB:

```{.bash data-prompt="$"}
$ sudo systemctl mongod start
```

Start **pbm-agent**:

```{.bash data-prompt="$"}
$ sudo systmectl pbm-agent start
```