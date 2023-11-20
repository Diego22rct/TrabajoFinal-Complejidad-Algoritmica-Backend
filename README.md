# Trabajo Final para el curso de Complejidad Algorítmica UPC

Para este proyecto usamos grafos no dirigidos y usamos las oponderaciones para representar las relaciones entre animes y asi tener la posibilidad de recomendar animes.

## Instalación

Para instalar la aplicación, necesita tener Python 3.6 o superior instalado en su máquina. También necesita tener Poetry instalado. Si no tiene Poetry, puede instalarlo siguiendo las instrucciones en el [sitio web oficial de Poetry](https://python-poetry.org/docs/#installation).

Una vez que tenga Python y Poetry instalados, puede instalar la aplicación clonando el repositorio e instalando las dependencias:

```bash
git clone https://github.com/Diego22rct/TrabajoFinal-Complejidad-Algoritmica-Backend.git
cd TrabajoFinal-Complejidad-Algoritmica-Backend
poetry install
```

## Uso


```bash
poetry run uvicorn app.main:app --reload
```

se abrirá en:  `http://localhost:8000`.

## Testing

Para correrlos test, use el siguiente comando:

```bash
poetry run pytest
```

## Contributing

If you want to contribute to the project, please create a fork of the repository, make your changes, and create a pull request.

## License

This project is licensed under the terms of the MIT license.