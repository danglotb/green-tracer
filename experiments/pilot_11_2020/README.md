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

Omitting the check at the begin of `v1`, the algorithm starts as follow for both versions:

#### [v0]()

```text
<string>:__main__:infix_to_postfix:22:expression=a+b*(c^d-e)^(f+g*h)-i
<string>:__main__:infix_to_postfix:30:expression=a+b*(c^d-e)^(f+g*h)-i
/home/benjamin/workspace/PythonV0/data_structures/stacks/stack.py:stack:__init__:14:self,limit=21
/home/benjamin/workspace/PythonV0/data_structures/stacks/stack.py:stack:__init__:15:self,limit=21
/home/benjamin/workspace/PythonV0/data_structures/stacks/stack.py:stack:__init__:16:self=[],limit=21
/home/benjamin/workspace/PythonV0/data_structures/stacks/stack.py:stack:__init__:16:self=[],limit=21
<string>:__main__:infix_to_postfix:31:expression=a+b*(c^d-e)^(f+g*h)-i,stack=[]
<string>:__main__:infix_to_postfix:32:expression=a+b*(c^d-e)^(f+g*h)-i,stack=[],postfix=[]
<string>:__main__:infix_to_postfix:33:expression=a+b*(c^d-e)^(f+g*h)-i,stack=[],postfix=[],char=a
```

#### [v1]()

```text
<string>:__main__:infix_to_postfix:41:expression_str=a+b*(c^d-e)^(f+g*h)-i
/home/benjamin/workspace/Python/data_structures/stacks/stack.py:stack:__init__:14:self,limit=10
/home/benjamin/workspace/Python/data_structures/stacks/stack.py:stack:__init__:15:self,limit=10
/home/benjamin/workspace/Python/data_structures/stacks/stack.py:stack:__init__:16:self=[],limit=10
/home/benjamin/workspace/Python/data_structures/stacks/stack.py:stack:__init__:16:self=[],limit=10
<string>:__main__:infix_to_postfix:42:expression_str=a+b*(c^d-e)^(f+g*h)-i,stack=[]
<string>:__main__:infix_to_postfix:43:expression_str=a+b*(c^d-e)^(f+g*h)-i,stack=[],postfix=[]
<string>:__main__:infix_to_postfix:44:expression_str=a+b*(c^d-e)^(f+g*h)-i,stack=[],postfix=[],char=a
```

Here, the main difference, is that the `stack` is constructed with the `len(expressions)`
in `v0`, while it uses the default size in `v1`. Does it impact the rest of the algorithm?

```diff
- stack = Stack(len(expression))
+ stack = Stack()
```
