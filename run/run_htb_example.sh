#!/bin/sh

rm -rf output
mkdir output
python3 green-tracer/green_tracer.py example/computation/htbv0.py > output/v0.trace
python3 example/computation/htbv0_pyjouled.py
mv result.csv output/result_v0.csv
python3 green-tracer/green_tracer.py example/computation/htbv1.py > output/v1.trace
python3 example/computation/htbv1_pyjouled.py
mv result.csv output/result_v1.csv
