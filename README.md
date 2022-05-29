# Kaybot
This is a whatsapp chatbot using Openai's GPT-3, python, twilio and flask


## Usage
> Installation:
## Packages needed
* Flask
* Openai
* python-dotenv
* pyngrok

# create a virtual environment
> Mac Os

```$ mkdir kaybot
$ cd kaybot
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install openai twilio flask python-dotenv pyngrok
```
> Windows

```$ md kaybot
$ cd kaybot
$ python -m venv venv
$ venv\Scripts\activate
(venv) $ pip install openai twilio flask python-dotenv pyngrok
```
**This line of code are the packages/modules we are going to need to make our chatbot a success. This uses the `pip` command which is the python package manager.**
```
(venv) $ pip install openai twilio flask python-dotenv pyngrok
```
 > Accounts needed for a successfull application

  * An [OPENAI](https://openai.com/) Account, this helps you to get the OPENAI_API KEY to be able to use the GTP-3 model. You can request access for the beta here [OPENAI Beta](https://beta.openai.com/).

  * A [Twilio](http://www.twilio.com/) Account to use their Whatsapp Sandbox 

  * An [ngrok](https://ngrok.com/) Account use their api to help configure a localhost address that can be use via `Https`. The `<URL>` generated from the command line using `ngrok http 500` will be used on **Twilio** to access your application locally.