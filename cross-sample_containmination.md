## Objective: Design a dry lab testing plan to figure out the best solution for contamination check for WES sample.

### Sample preparation:
<ul> Contaimination level based on amount of reads mixed:
<li> Level 0(control): no mixing
<li> Level 1: Mixing 1% reads from sample A to sample B
<li> Level 2: Mixing 2% reads from sample A to sample B
<li> Level 3: Mixing 5% reads from sample A to sample B
And so on...
<ul> Containmination level based on number of samples mixed:
Level 0(control): Mixing 5% reads from sample A to sample E
Level 1: Mixing 5% reads from sample A, 5% reads from sample B to sample E
Level 2: Mixing 5% reads from sample A, 5% reads from sample B, 5% reads from sample C to sample E
Level 3: Mixing 5% reads from sample A, 5% reads from sample B, 5% reads from sample C, 5% reads from sample D to sample e
And so on...

### Testing pipeline
Running three different pipeline from three different sources tools for testing the cross-sample containmination level.

### Analysis
Calculate the specificity and sensitivity for each of the results came from each tools.