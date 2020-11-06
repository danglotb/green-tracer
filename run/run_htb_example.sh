#!/bin/sh

rm -rf output
mkdir output
python green-tracer/green_tracer.py example/computation/htbv0.py > output/v0.trace
python green-tracer/green_tracer.py example/computation/htbv1.py > output/v1.trace
