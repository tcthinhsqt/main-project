#!/bin/bash
python main.py &
P1=$!
cd ui
npm install
npm update
npm run serve &
P2=$!
wait $P1 $P2