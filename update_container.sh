#!/bin/bash
echo "Trying to update container"
if [[ $(docker ps | grep "family_day_out") ]]
then
    echo "copying files"
    DockerContainerId=$(docker ps | grep "family_day_out" | tr -s ' ' | cut -d ' ' -f1)
    commandToExec="docker cp . $DockerContainerId:/app"
    eval $commandToExec
    echo "restarting Container"
    dockerRestartContainer="docker restart $DockerContainerId"
    eval $dockerRestartContainer
else
    echo "No active docker container found to update"
fi