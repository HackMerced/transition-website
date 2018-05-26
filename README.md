# Transition Website

Transition website for hiring people to join the hackmerced team.
This will be rolled out during the period after the hackathon and before the summer.  It's purpose is to display
information about the positions available at hack merced, as well as a link to apply to become a part of 
the organization.

Hosted on heroku here:  hackmerced.com

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* python version >= 3.6 -> install here:  https://www.python.org/downloads/
* pip package manager -> install here:    https://pip.pypa.io/en/stable/installing/ (note: pip may be installed along with python already)

To check if they are installed, run these commands in bash:
```bash
python --version
```
Then check the version
```bash
pip --version
```

### Installing

Now that we know that python and pip are installed, we can clone the repository to get a basic setup.
Steps:
1. cd into a working directory
```bash
cd somedirectory
```
2. clone the repo
```bash
git clone https://github.com/HackMerced/transition-website.git transition-website
```
3. cd into the 'transition-website' directory
```bash
cd transition-website
```
4. create a virtual environment (in python3). This will ensure that the dependencies are isolated and won't interfere with the global packages
```bash
python3 -m venv env
```
5. activate the virtual environment to "quarantine" the project's dependencies
```bash
source env/bin/activate
```
you should see (env) pre-pended to the bash prompt. This verifies that you are in the virtual environment
6. make sure you are at the root of the 'transition-website' directory, and install the dependencies
```bash
pip install -r requirements.txt
```
7. run the app locally
```bash
python app.py
```
8. open up a browser, and enter whichever local link that flask will run on (look at terminal output)
usually its http://127.0.0.1:5000/
9. Now, we have the environment setup!  Open up a text editor and play around with the code.

## Deployment

Deployed through heroku.  Must have admin credentials to update the live website.

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used

## Contributing

If you would like to contribute to this repo, follow these steps.
1. fork the repository, so you can have a copy
2. make a new branch, with a descriptive branch name of the feature/change would like to add.
3. make desired changes on forked repo
4. when done, make a commit, push to your repo
5. submit a pull request from your local 'forked' branch to the 'master' branch of the original repo
6. wait for your pull request to either be accepted, rejected, or flagged as 'needs work'

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
