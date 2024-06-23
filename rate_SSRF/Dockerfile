# Dockerfile
FROM node:14

# Set working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install npm dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Make the run script executable
RUN chmod +x run.sh

# Install Python (if necessary) and set up server dependencies
RUN apt-get update && apt-get install -y python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose ports
EXPOSE 2000 1729

# Command to run the SSRF vulnerable application
CMD ["./run.sh"]
