#!/bin/bash
pd ./tests/network_test.pd &
sleep 8
python ./tests/network_test.py &

exit_script() {
   echo -e "\nShutting down..."
   trap - SIGINT SIGTERM # clear the trap
   kill -- -$$ # Sends SIGTERM to child/sub processes
}

trap exit_script SIGINT SIGTERM
wait
