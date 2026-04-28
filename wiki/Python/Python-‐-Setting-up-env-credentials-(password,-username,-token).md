
# Create a .env file in the base of your code folder# 
Do the same for a .gitignore file

The .env file operates like bash and not python, so there are no spaces in the creds below:
username=test123
password-test123

Add .env in the gitignore file. That's it.
For your code, add the following
~~~
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
~~~
~~~
Credentials
username = os.getenv("username")
password = os.getenv("password")  
~~~