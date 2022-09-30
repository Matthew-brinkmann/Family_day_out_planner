#!/bin/bash
docker image build -t family_day_out_server .
docker run -p 5000:5000 -d family_day_out_server
