# Install Percona Distribution for MongoDB

We recommend to install Percona Distribution for MongoDB from Percona repositories using the package manager of your operating system. Find the list of supported Linux distributions on the [Percona Software and Platform Lifecycle](https://www.percona.com/services/policies/percona-software-platform-lifecycle#mongodb) page.

Alternatively, you can download Percona Distribution for MongoDB from Percona website and install it manually from binary tarballs.

Choose how you wish to install Percona Distribution for MongoDB:

=== "On Debian/Ubuntu"

    Run the following commands as root or by using the **sudo** command.

    1. Install **percona-release** repository management tool to subscribe to Percona repositories:    

        * Install `curl`    

           ```{.bash data-prompt="$"}
           $ sudo apt update
           $ sudo apt install curl
           ```    

        * Download the **percona-release** package    

           ```{.bash data-prompt="$"}
           $ curl -O https://repo.percona.com/apt/percona-release_latest.generic_all.deb
           ```    

        * Install the package and dependencies    

           ```{.bash data-prompt="$"}
           $ sudo apt install gnupg2 lsb-release ./percona-release_latest.generic_all.deb
           ```    

        * Refresh the local cache    

           ```{.bash data-prompt="$"}
           $ sudo apt update
           ``` 

        !!! note

            If you have already installed `percona-release`, [upgrade it to the latest version](https://docs.percona.com/percona-software-repositories/updating.html).

    2. Enable the repository    

        Percona provides [two repositories](repo-overview.md#repo-overview) for Percona Distribution for MongoDB. To enable a repo, we recommend using the `setup` command:    

        ```{.bash data-prompt="$"}
        $ sudo percona-release setup pdmdb-7.0
        ```    

    3. Install Percona Distribution for MongoDB packages    

        ```{.bash data-prompt="$"}
        $ sudo apt install percona-server-mongodb percona-backup-mongodb
        ```


=== "On RHEL/derivatives"

    Run the following commands as root or by using the **sudo** command.

    1. Install **percona-release** repository management tool to subscribe to Percona repositories:    

        ```{.bash data-prompt="$"}
        $ sudo yum install -y https://repo.percona.com/yum/percona-release-latest.noarch.rpm
        ```
         
        !!! note

            If you have already installed `percona-release`, [upgrade it to the latest version](https://docs.percona.com/percona-software-repositories/updating.html).   

    2. Enable the repository    

        Percona provides [two repositories](repo-overview.md#repo-overview) for Percona Distribution for MongoDB. To enable a repo, we recommend using the `setup` command:    

        ```{.bash data-prompt="$"}
        $ sudo percona-release setup pdmdb-7.0
        ```    

    3. Install Percona Distribution for MongoDB packages    

        ```{.bash data-prompt="$"}
        $ sudo yum install percona-server-mongodb percona-backup-mongodb
        ```
    

=== "From tarballs"

    You can find binary tarballs on the [Percona software downloads page](https://www.percona.com/downloads/percona-distribution-mongodb-7.0/LATEST/)

    1. Select *Generic Linux* from the dropdown.

    2. Download binary tarballs. Replace the &#60;version&#62; variable with the desired version:

        ```{.bash data-prompt="$"}
        $ wget https://downloads.percona.com/downloads/percona-distribution-mongodb-7.0/percona-distribution-mongodb-<version>/binary/tarball/percona-backup-mongodb-<version>-x86_64.tar.gz
        $ wget https://downloads.percona.com/downloads/percona-distribution-mongodb-7.0/percona-distribution-mongodb-<version>/binary/tarball/percona-server-mongodb-<version>-x86_64.glibc2.17.tar.gz
        ```

    3. Extract the tarballs

        ```{.bash data-prompt="$"}
        $ tar -xf percona-backup-mongodb-<version>-x86_64.tar.gz
        $ tar -xf percona-server-mongodb-<version>-x86_64.glibc2.17.tar.gz
        ```

    4. Export the location of the binaries to the PATH variable

        For example, if you’ve extracted the tarballs to your home directory, the commands would be the following:

        ```{.bash data-prompt="$"}
        $ export PATH=~/percona-backup-mongodb-<version>/:~/percona-server-mongodb-<version>/:$PATH
        ```

    5. Create the default data directory for *Percona Server for MongoDB*:

        ```{.bash data-prompt="$"}
        $ sudo mkdir -p /data/db
        ```

    6. Check that you have read and write permissions for the data directory and run `mongod`.

=== "On Kubernetes"

    Deploy and run Percona Distribution for MongoDB on Kubernetes with [Percona Operator for MongoDB](https://www.percona.com/software/percona-kubernetes-operators). See [Quickstart guides](https://docs.percona.com/percona-operator-for-mongodb/helm.html) for the installation instructions on your favorite Kubernetes flavor.

To set up monitoring of your Percona Distribution for MongoDB in PMM, see [Set up PMM to monitor MongoDB](https://docs.percona.com/percona-monitoring-and-management/setting-up/client/mongodb.html)

## Uninstall Percona Distribution for MongoDB

To uninstall Percona Distribution for MongoDB, remove the packages using the package manager of your
operation system. Optionally, disable *Percona* repository.

!!! admonition "See also"

    * [Uninstall Percona Server for MongoDB](https://docs.percona.com/percona-server-for-mongodb/7.0/install/uninstall.html)

    * [Uninstall Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/manage/uninstalling.html)




    


    
