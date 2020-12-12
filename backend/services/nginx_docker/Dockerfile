FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY services/nginx_docker/nginx.conf /etc/nginx/conf.d
RUN mv /etc/nginx/conf.d/nginx.conf /etc/nginx/conf.d/default.conf