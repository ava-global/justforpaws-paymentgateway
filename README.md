# justforpaws-paymentgateway

## Details

All secrets are backed up in `niran/niran-payment-gateway-secret` AWS Secrets Manager.


## Deployment

Get ready with [fly.io](https://fly.io/docs/) and login with `1buck4life@gmail.com` account (Password is the same as Gmail password).

Recomend readings
- [Custom Domain and SSL Certificate](https://fly.io/docs/app-guides/custom-domains-with-fly/#teaching-your-app-about-custom-domains)
- [Dockerfile Deployment](https://fly.io/docs/languages-and-frameworks/dockerfile/)

All credentials are store using Fly io's secrets.

```bash
flyctl deploy
```