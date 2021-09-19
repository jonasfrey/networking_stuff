#!/bin/bash
repetitions=100
for i in {1..10000}
do
   echo "curl http://11235.ch/test"
   curl "http://11235.ch/test"
done