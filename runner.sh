#!/bin/bash

run_stock(){
    echo "Running Stock with the value $1"
    python3 /home/torrezmn/Documentos/Py_Prices/src/stock/stock_main.py $1
}

run_super6(){
    echo "Running Super6 with the value $1"
    python3 /home/torrezmn/Documentos/Py_Prices/src/super6/super6_main.py $1
}

gen_random() {
    local max_value=$1
    RANDOM_VALUE=$((1 + RANDOM % max_value))
    echo $RANDOM_VALUE
}

MAX_VALUE=30

# Generate a random number of runs between 1 and 20
TOTAL_RUNS=$(gen_random 20)

# Using a standard for loop compatible with sh
i=1
while [ $i -le $TOTAL_RUNS ]; do
    echo "******************************************************"
    echo -e "\n\n\n\n\n"
    RANDOM_NUM=$(gen_random $MAX_VALUE)
    echo "Run $i of $TOTAL_RUNS: Running Stock"
    run_stock $RANDOM_NUM
    
    RANDOM_NUM=$(gen_random $MAX_VALUE)
    echo "Run $i of $TOTAL_RUNS: Running Super6"
    run_super6 $RANDOM_NUM

    i=$((i + 1))
done

