FROM osgeo/gdal:alpine-normal-latest

WORKDIR /app

RUN apk update && apk add --no-cache gcc g++ make libc-dev linux-headers python3-dev

RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY .env /app/

COPY ./server /app

RUN python /app/manage.py collectstatic --noinput

COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]
