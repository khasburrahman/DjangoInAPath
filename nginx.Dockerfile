FROM nginx:1.15.10-alpine

COPY /nginxconf/nginx.conf /etc/nginx/conf.d/default.conf