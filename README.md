# Paper

The paper that utilizes this repository can be found in the 'paper.pdf' file.

## Context

In this repository, you will find each of the merge scenarios used in the study. Each directory corresponds to a specific project, and within each of these directories, you'll find a scenario with four JAR files, each representing one component of the merge scenario.

More details about each scenario can be obtained from the 'data_base.json' file, where you can see the class and method(s) modified in that scenario.

Further information on how the dataset was constructed can be found in the "3.1 Construção da amostra" section of the paper.

## How to Use

As detailed in the paper, we use this repository with the [SMAT tool](https://github.com/spgroup/SMAT). To run the tool, execute the 'script.py' file, which will generate a 'data.json' file. This file should be used to configure the tool as described in the SMAT README under the "Providing Input" section.

To create new scenarios, as described in the paper, you can use the [SytheticMergeSample project](https://github.com/thaisabr/SyntheticMergeSample).
