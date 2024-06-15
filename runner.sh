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
  return $((1 + $RANDOM % 100))
}


for i in {0..8}; do  # Use curly braces for inclusive range
    gen_random
    run_stock $?
    gen_random
    run_super6 $?
done

