# justforpaws-paymentgateway

## Details

EC2: i-0e4d37cf195ea5e5d
Name: niran-payment-gateway

All secrets are stored in `niran/niran-payment-gateway-secret` AWS Secrets Manager.


## Deployment

Get into an EC2 and pull a code from Github.

This EC2 instance can access a repo via a ssh key (Deploy Key feature in Github).

Start a server.
```bash
sudo docker build --rm -t justforpaws-paymentgateway .
docker stop justforpaws-paymentgateway
docker rm justforpaws-paymentgateway
sudo docker run --name justforpaws-paymentgateway -p 80:8082 -d --env-file .env justforpaws-paymentgateway
```