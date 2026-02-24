# Grafana / Prometheus setup with docker

Install docker compose and docker from the docker website
Create the dockerfile and the prometheus.yml files with the
info below.

### dockerfile
~~~
# Use the official Grafana image as the base
FROM grafana/grafana:latest

# Embed the admin credentials
ENV GF_SECURITY_ADMIN_USER=username1 \
    GF_SECURITY_ADMIN_PASSWORD=password


# Expose Grafana’s UI port
EXPOSE 3000
~~~


### Prometheus.yml
~~~
global:
          scrape_interval:     15s   
          evaluation_interval: 15s
      scrape_configs:
          - job_name: 'prometheus'
            scrape_interval: 15s
            static_configs:
            - targets: ['localhost:9090']
~~~

### Launch grafana
docker run -d   --name grafana   -p 3000:3000   -v grafana-data:/var/lib/grafana  grafana/grafana:latest
### Launch the prometheus container
docker run -d -p 9090:9090 prom/prometheus:latest