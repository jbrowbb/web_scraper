# Creating Environment

In Miniconda an environment was created called 'scraper'
    ```ruby
        $ conda create --name scraper python=3.10
    ```

Activate the environment in Miniconda
    ```ruby
        $ conda activate scraper
    ```

Install these packages into the environment
    ```ruby
        $ conda install numpy
        $ conda install matplotlib
        $ conda install beautifulsoup4
    ```

Export the environment
    ```ruby
        $ conda env export > requirements.yaml
    ```