import os

# delete volumes folder
os.system("sudo rm -rf /var/lib/docker/volumes")

# remake volumes folder
os.system("sudo mkdir /var/lib/docker/volumes")

# start app and db
os.system("sudo docker compose up -d")

# seed database
os.system("sudo docker exec -it app node seeds/seed.js")