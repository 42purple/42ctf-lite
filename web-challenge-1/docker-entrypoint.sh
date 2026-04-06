#!/bin/bash

npm run dev 2>&1 &
node server 2>&1 &

nginx -g 'daemon off;'