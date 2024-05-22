docker-compose up -d

docker-compose down

docker build -t py_auto_test .

docker run --network="host" py_auto_test