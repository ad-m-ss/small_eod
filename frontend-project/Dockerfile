FROM node:16.15.1-slim@sha256:16b5d00e95c0c9fc4b4c5493b3c9c648cb39d96869170585ebfedc0d84ce33ca AS env

RUN apt update && apt install -y g++ git make python3
WORKDIR /code

# PRODUCTION BUILD
FROM env AS builder
COPY ./ /code
RUN yarn && yarn build

FROM nginx:stable-alpine@sha256:ff557e536e5c697c5a28db13ab81bdf9b0c6a20161aa0a46419b9b251872c7df AS prod
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /code/dist /usr/share/nginx/html
EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]

# DEVELOPMENT BUILD
FROM env
CMD ["bash", "-c", "yarn && yarn start"]
