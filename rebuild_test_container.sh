#!/bin/bash
if [[ $(docker images | grep "family_day_out_server") ]]
then
    echo "CLEANING OLD DOCKER ENVIRONMENT..." 
    oldDockerImageId=$(docker images | grep "family_day_out" | tr -s ' ' | cut -d ' ' -f3)
    echo "found docker image $oldDockerImageId"
    var="docker image rm $oldDockerImageId"
    if [[ $(docker ps | grep "family_day_out_server") ]]
    then
        oldDockerContainerId=$(docker ps | grep "family_day_out" | tr -s ' ' | cut -d ' ' -f1)
        echo "found docker container $oldDockerContainerId"
        echo "removing old container... please wait..."
        stopVar="docker stop $oldDockerContainerId && docker rm $oldDockerContainerId"
        eval $stopVar
    fi
    echo "removing old image... please wait..."
    eval $var
    echo "DOCKER ENVIRONMENT CLEAN!"
fi
echo "creating new image and building container"
docker image build -t family_day_out_server .
docker run -p 5000:5000 --name fdo_dev_container -d family_day_out_server
