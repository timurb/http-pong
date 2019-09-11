# Http-Pong

This is a single app to play with docker exposing ports.

## Usage

```
docker build . -t http-pong
docker run --rm -d -p 5000:5000 http-pong
# fd15987d2a3a837d63b7efd49825254e8f4e2b75bc9cbd3ba86f4ff9667c01d4

curl localhost:5000
# User-Agent: curl/7.54.0
# Host: localhost:5000
# Accept: */*

docker stop fd15987d2a3a837d63b7efd49825254e8f4e2b75bc9cbd3ba86f4ff9667c01d4 # use id produced by docker-run command
```

### License and author
* License:: MIT
* Author:: Timur Batyrshin <erthad@gmail.com>
