# IPContainer

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

[![Build Status](https://travis-ci.com/harvestcore/IPContainer.svg?branch=master)](https://travis-ci.com/harvestcore/IPContainer)


- [Despliegue Heroku](https://ipcontainer.herokuapp.com/)
- `Inactivo` [Despliegue OpenShift]()
- `Inactivo` [Despliegue Azure](https://ipcontainer.azurewebsites.net/)



## ¿Qué es?

IPContainer es un microservicio centrado en el almacenamiento y gestión básica de direcciones IP. Permite tener almacenadas una serie de direcciones IP en un mismo lugar, agrupadas por tipo de red:

- **PAN** (Personal Area Network)
- **LAN** (Local Area Network)
- **WAN** (Wide Area Network)
- **SAN** (Storage Area Network)
- **VLAN** (Virtual Local Area Network)
- **WLAN** (Wireles Local Area Network)

Por otro lado permite almacenar direcciones IP de servidores DNS.



## ¿Por qué?

La idea surge tras necesitar un lugar donde tener una serie de direcciones IP organizadas y almacenadas en un mismo lugar, sin depender de mirar archivos de configuración o uso de otras aplicaciones.

Más info:

- [**Documentación**](#doc)
- [**Web del proyecto**](https://harvestcore.github.io/es/ipcontainer/index.html)
- [**Web del repositorio**](https://harvestcore.github.io/IPContainer)



## Herramientas y servicios

- [**Python**](https://www.python.org/): Lenguaje principal de programación.
  - [**Flask**](http://flask.pocoo.org/): Framework principal.
  - [**SQLAlchemy**](https://www.sqlalchemy.org/): Como [ORM](https://es.wikipedia.org/wiki/Mapeo_objeto-relacional).
- [**MariaDB**](https://mariadb.org/): Gestor de base de datos.
- [**Travis-CI**](https://travis-ci.org/): Para integración contínua.
- [**Heroku**](https://www.heroku.com/): Como PaaS.
- [**Microsoft Azure**](https://azure.microsoft.com/es-es/): Como PaaS.

<div id='doc' />

## Documentación:

- [**API**](docs/api.md)
- [**Autenticación con token**](docs/auth.md)
- [**Base de datos**](docs/bd.md)
- [**Instalación**](docs/install.md)
- [**Despliegue en Heroku**](docs/heroku.md)
- [**Despliegue en Microsoft Azure**](docs/azure.md)
- [**Despliegue en OpenShift**](docs/openshift.md)
- [**Archivo de configuración de TravisCI**](.travis.yml)
- `Inactivo` [**ReadTheDocs**](https://ipcontainer.readthedocs.io)


## Varios

- [**Repositorio en DockerHub**](https://hub.docker.com/r/harvestcore/ipcontainer)

## Test News

[!] Finalmente los tests con la BD en [db4free](https://www.db4free.net/) están implementados en este repositorio. Por otro lado no ha sido necesario utilizar docker para los mismos.

-----

Debido a que el microservicio necesita una base de datos estoy probando una serie de tests con Docker en estos repositorios:

- [ipcontainer-test](https://github.com/harvestcore/ipcontainer-test)
- [IPContainer2](https://github.com/harvestcore/IPContainer2)

Resumiendo: Levanto dos contenedores Docker, uno con una BD (MySQL) y el otro con Python. El segundo se conecta al primero para acceder a los datos. El repositorio *IPContainer2* contiene una versión más actualizada de este mismo repositorio. Cuando los contenedores y el sistema de test esté perfectamente comprobado y funcionando lo implementaré en este repositorio.

Por otro lado, he probado una nueva serie de tests (en IPContainer2) con una BD en [db4free](https://www.db4free.net/). Aunque la latencia no es la mejor, para probar el microservicio pienso que es más que suficiente.


## Pasos a seguir en el desarrollo de IPContainer

- [x] Descripción general.
- [x] Elección de herramientas para su desarrollo.
- [x] Integración continua. Tests.
- [x] Autenticación con token.
- [ ] Despliegue del microservicio en un PaaS.
- [ ] Despliegue en docker.
- [ ] Despliegue automático a las plataformas de producción.
