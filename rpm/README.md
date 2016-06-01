# Create Mattermost rpm

* Download the release you want to create the rpm for:
	``wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz``

* Edit the mattermost.spec to reflect the version
* Build the rpm by running: ``make``

# Will work on

This is tested only on RHEL7

# Configuration 

The specfile is created according to the steps described in:
	http://docs.mattermost.com/install/prod-rhel-7.html

# Build requirements

Make sure rpm-build and rpmdevtools are installed:
	``yum install -y  rpm-build rpmdevtools``
