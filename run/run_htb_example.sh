#!/bin/sh

rm -rf output
mkdir output
python3 green-tracer/green_tracer.py --path-to-script example/computation/ --script htbv0.py --output-path output/v0.trace
#python3 example/computation/htbv0_pyjouled.py
python3 green-tracer/green_tracer.py --path-to-script example/computation/ --script htbv1.py --output-path output/v1.trace
#python3 example/computation/htbv1_pyjouled.py
mv result.csv output/result_v1.csv
gumtree textdiff example/computation/htbv0.py example/computation/htbv1.py > text.diff
mv text.diff output/text.diff
