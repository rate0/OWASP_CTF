FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
ENV PORT=2000
ENV COOKIE_KEY=SECRET
ENV FLAG=IR{B055_0F_X55}
EXPOSE 2000
CMD ["node", "index.js"]
