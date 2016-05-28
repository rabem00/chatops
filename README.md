# chatops
ChatOps setup using mattermost, ansible, hu-bot

# Will work on
This will only work on RHEL 7, postgresql 9.2 (default on RHEL 7)

# Run playbook
To run the play book first add a hosts file with the ip-addresses of the hosts
that the playbook needs to run on. Then use the following command to play:
  ansible-playbook play.yml -i hosts

# Test db connection
Attempt to connect with the new created user to verify everything looks good,
for example:

  # psql --host=127.0.0.1 --dbname=mattermost --username=mmuser --password
  
  mattermost=> \q
