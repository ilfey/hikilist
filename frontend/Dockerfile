FROM node:20-alpine3.18 as builder

EXPOSE 80

WORKDIR /srv

COPY . /srv/

RUN yarn install

RUN yarn vite build

ENTRYPOINT [ "yarn" ]

CMD [ "vite", "preview", "--port", "80", "--host" ]