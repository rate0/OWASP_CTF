#!/bin/bash

# Ensure that the Python HTTP server is started in the background
python3 -m http.server 1729 --bind 127.0.0.1 --directory /usr/src/app/flag &

# Install npm dependencies (if necessary, though ideally already done in Dockerfile)
npm install

# Start your Node.js application
node app.js
