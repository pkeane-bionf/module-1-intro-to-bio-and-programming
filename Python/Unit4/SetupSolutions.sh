#!/bin/bash

if [ -z "$1" ]
then
    echo "No transition argument supplied"
    exit 1
fi

# Rate of Transitions
TRANSITIONVAL=$1

mkdir submissions
cp ImpactOfMutationsSol.ipynb submissions/.

# run solution to check marking
python3 Unit4MarkingScript.py ImpactOfMutationsSol.ipynb --$TRANSITIONVAL

echo
echo
echo DID THAT SCORE 70/70? If not there is a problem!






