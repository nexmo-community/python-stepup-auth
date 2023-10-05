# Python Stepup Authentication Using the Vonage Verify API

## ❗❗❗ **This repo is now deprecated. You can find up-to-date sample code for this and other tasks in the [Vonage Python Code Snippets repo](https://github.com/Vonage/vonage-python-code-snippets). Check the [Vonage Developer Blog](https://developer.vonage.com/en/blog) for more blog posts and tutorials. For more sample Vonage projects, check the [Vonage Community GitHub repo](https://github.com/Vonage-Community).**

Please refer to the [tutorial](/verify/tutorials/step-up-authentication/introduction/python) for instructions on how to configure and run this application.

This repo contains the example code for our tutorial on using the Vonage Verify API to authenticate a user by their mobile phone number. It is written in Python 3 using the Flask framework.

## Installing your own version
Follow these steps to get your own version of this up and running:

```
git clone https://github.com/nexmo-community/python-stepup-auth.git
cd node-stepup-auth
```

## Configuring the application
Once installed, copy the `.env-example` file to `.env` in the application's root directory. Enter your API key and secret from the Developer Dashboard and also a name for your application which will appear on the home page and also in the `from` field of any SMS sent via the Verify API.

```
VONAGE_API_KEY=YOUR VONAGE API KEY
VONAGE_API_SECRET=YOUR VONAGE API SECRET
VONAGE_BRAND_NAME=UP TO 11 ALPHANUMERIC CHARACTERS
```

## Running the application
You should then be able to run the app with `python server.py`. Open http://localhost:5000 in your browser to begin.
