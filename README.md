# Caster
This is a work in progress and one with an admittedly unclear scope. Changes will be ongoing. This project is also strangely personal and so I'm not sure how specific I can be as to the nature of what i'm trying to build here. 

Mainly view it as a exercise for me as a programmer, attempting various projects to I can hopefully piece together into something greater.
## What is Flow?

Flow is meant to be an automation utility, allowing for the design and configuration of automated flow systems such as those found in the game Factorio. 
## Flow .json Standards

Input:

The input is a command line string of the name of the json file representing the model of the system's environment (referred to as the contextual model). The json file consists of an object assumed to be the contextual model. Each of the included with the following fields:

Contextual Model:
*name (string)
*timescale (string: discrete, continuous, instant)
*isFinite (boolean)
    if True:
    *endpoint
*output (array: Flow objects)
*container (Container object)

Containers:
*dimensions (integer: 1, 2, 3, 0(abstract)))
    if not abstract:
    *size (array of integers (-1 is infinite))
*constraints 

Process:
*input (array: Flow objects)
*output (array: Flow objects)

Flow:
*tokenName (string)
*rate (number)

Amount:
*tokenName (string)
*amount (number)