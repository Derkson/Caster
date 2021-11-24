# Caster
---
## What is Caster?

Caster is meant to be an automation utility, allowing for the easy installation and configuration of semi-pre-built automated systems. This is a work in progress and one with an admittedly unclear scope. I'll probably change this README sometime to more accurately reflect what this all is.

## Standards

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