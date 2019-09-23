
# Data Engineering and Reccommendation for med-cabinet

> ETL of data (see sources).  Data engineering provides structure/unstructure? db of strain information for returns through API and construction of structured data for recommendation engine development.
> REST API for user search query and return of recomendatiosn from engine
> Recommendation engine


**Source List** of used data:

* [Kaggle - Cannabis Strains](https://www.kaggle.com/kingburrito666/cannabis-strains)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Important Links

* [Build-Week-Med-Cabinet Repository](https://github.com/Build-Week-Med-Cabinet/DS)
* [Trello task management](trello.com)
* [Product Vision Document](https://docs.google.com/document/d/1p2ubrQoOpv5yrzj9yZ-4cZuBkqywU5BCpT5pxPXeYBM/edit?usp=sharing)

### Prerequisites

Python >= 3.6.8
Anaconda or MiniConda or Pip

### Installing

#### Django development environment

* Conda: Create a conda environment for the django application with

```python
conda env create -f django_env.yml
```

* Run server with

```python
python manage.py runserver <ip_address>:<port>
```

IP address and port are optional parameters for runserver.


#### ETL development environment


#### Predictor development environment


## Running the tests

Automated tests(if available) and tests for backend

## Deployment

Not currently deployed.  Deployment notes here.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST framework](https://www.django-rest-framework.org) - API endpoint extension for Django
* [Jupyter](https://jupyter.org/) - Test ETL's and Develop Predictive Model

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Steve Elliott** - *Initial work* - [GitHubLink](https://github.com/)
* **Vincent Brandon** - *Initial work* - [GitHubLink](https://github.com/)

*TODO*
See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the XXX License - see the [LICENSE.md](LICENSE.md) file for details


## Contributors

**Backend** Developers:
* [Louie Williford](https://github.com/dustyfingers)
* [Landry Irakoze](https://github.com/LandryIrakoze)


## Acknowledgments
