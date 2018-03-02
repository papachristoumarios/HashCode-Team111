# HashCode Team 111

## Qualification Round Problem for HashCode 2018

HashCode 2018 Team 111 Submission for **Self-driving rides** Qualification Round Problem at NTUA ECE Hub

### Problem Statement

The problem statement can be found under `Problem.pdf`. This repository also hosts datasets.

### Overview of solution

We followed a greedy approach on the solution.

 1. We sorted the rides following a linear combination of criteria (comparator function)

 ```
 f(ride) = w * (ride distance) + (1 - w) / (starting time)
 ```
with `0 <= w <= 1`

 2. Then we sent each available (not busy) driver to which serves the nearest customer.

### Observations

 1. The metropolis dataset had many accumulated rides so we threw away 'useless' rides

### Team Members

The members of the Team 111 (NTUA ECE Hub) were (in alphabetical order):
  1. Ioannis Daras
  2. Dimitris Brallios
  3. Marios Papachristou
  4. Miltiadis Stouras
