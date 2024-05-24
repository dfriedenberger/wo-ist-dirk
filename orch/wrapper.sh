#!/bin/bash

#Start subscriber
python subscribe.py &

#uvicorn server:app --host 0.0.0.0 --port 8884 &

# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?