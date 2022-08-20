docker image rm zanfranceschi/desafio-20220820-scroll_infinito
docker build -t zanfranceschi/desafio-20220820-scroll_infinito .
# docker run --rm -p 8000:80 zanfranceschi/desafio-20220820-scroll_infinito
docker push zanfranceschi/desafio-20220820-scroll_infinito
# uvicorn main:app --reload
# curl -v -X OPTIONS -H "Origin: xpto.com" -H "Access-Control-Request-Method: GET" http://127.0.0.1:8000