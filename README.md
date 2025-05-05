
# CreditApi

API para gestionar productos con FastAPI


## API Reference


Toda la documentación de respecto a la Api la pueden encontrar en su respectivo swagger https://creditapi.onrender.com/docs


## Autores

- [@JhogerOlmos](https://github.com/JAOLMOS07)


## Variables de entorno

Para correr este proyecto vas necesitar las siguientes variables de entorno

`DATABASE_URL`




## Run Locally

Clone the project

```bash
  git clone https://github.com/JAOLMOS07/creditapi.git
```

Go to the project directory

```bash
  cd creditapi
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Activate virtual enviroment python

```bash
  .\venv\Scripts\activate 
```


Start the server

```bash
  uvicorn main:app --reload 
```


## Running Tests

To run tests, run the following command (activate venv previously)

```bash
  pytest -s
```


## Used By

This project is used by the following companies:

- Punto de pago (prueba técnica)
