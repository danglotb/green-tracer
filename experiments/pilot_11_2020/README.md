# Pilot Experiments

Here, we conduct a preliminary experimentation.

In the following text, `v0` refers to the program before the changes, and `v1` refers
to the program after the changes. On diff, `v0` is on the left, while `v1` is on the right.

## First example

### Overview

We will use a slightly modified version of this [pull-request](https://github.com/TheAlgorithms/Python/pull/3817).
The used branch are avalaible [here (v0)](https://github.com/danglotb/Python/tree/commit-0-v0) and [here (v1)](https://github.com/danglotb/Python/tree/commit-0-v1).

The `webdiff` by gumtree is the following:

![diff-commit-1](pictures/screen_diff_c0.png)

IMO, the most impactful changes, is that in `v1`, the balance of the parenthesis
is checked before the process, while in `v0`, it is checked during the process.

### Traces
