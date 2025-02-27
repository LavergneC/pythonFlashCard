# Product Name
> This application is a Flash card tool based on small python exercises.

[![Downloads Stats][npm-downloads]][npm-url] <- TODO ADD RUFF


Idealy you would use it every day and try to solve some python problems. Thoses problems are usally based on important core python features. 

The 'flash card' part is managed using a score system, you are promted with exercise with a low score, the score is updated wenether you solved the problem or not.

![](header.png) # TODO une image / un gif

## Installation

OS X & Linux:

```sh
TODO setup.py
```

## Usage 
From project root directory, execute :
```sh
`python -m main.generate_exercise`  TODO better
```

A exercise.py file has been created/updated. Open it and try to solve the problem the best way possible.

Open another terminal and type 
```sh
pytest exercise.py
```
to check if the problem is solved.

Then, check the solution.py file to see if you found the best way of solving the problem.

Finally, go back to the first terminal to register your result.


## Development setup

```sh
venv venvPythonFlashCards
source /path/to/venv/venvPythonFlashCards/bin/activate
pip install -r requirements.txt
pytest
```

## Release History

* 0.0.1
    * Work in progress


## Contributing

1. Fork it (<https://github.com/LavergneC/pythonFlashCard/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's --> TODO
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics 