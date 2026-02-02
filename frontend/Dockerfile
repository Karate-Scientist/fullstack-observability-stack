FROM nginx:alpine

COPY . /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/
COPY main.js /usr/share/nginx/html/

COPY test-index.html /usr/share/nginx/html/
COPY test-script.js /usr/share/nginx/html/

COPY . /app
#COPY nginx.conf /etc/nginx/nginx.conf


