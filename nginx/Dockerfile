FROM nginx:1.21.6

RUN rm /var/log/nginx/*
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx
COPY conf.d/ /etc/nginx/conf.d/
