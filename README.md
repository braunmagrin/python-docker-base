Python Docker Base Files
========================

These are the base files I use when building a Python application that will
run inside a Docker container.

## What's inside

This repository contains:
- Configiuration files:
  - .editorconfig
  - .flake8
  - .gitignore
  - pytest.ini
- Files to build a Docker image:
  - docker-compose.yml
  - Dockerfile
- Application dependencies file:
  - requirements.txt
- (Dumb) Sample code and tests:
  - src
  - tests

## How to use it

The source code goes into `src` and your tests go into `tests`.

To run the tests, simply use:

```
$ docker-compose run test
```

And to run the application locally, you can use `run` or `up`, like so:

```
$ docker-compose run local
```

(check the `docker-compose`'s help to see which is appropriate for each case)


## Contributing

Please feel free to contribute with changes and feedback

