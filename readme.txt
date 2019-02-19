FRIDAY Code Challenge
======================

1. Setup
----------

Install required libs from requirements.txt
Command to run 'python3 main.py' or 'python main.py'


2. Test Cases
--------------

Test Cases are in test_parser.py
Command to run 'pytest -v' or 'pytest'

I've written few test cases for Custom built parser only and not for third-party libraries (mentioned below)


3. Additional
---------------

I've tried to solve the problem using three methods

a) Custom parser written using regex.
   -- /libs/parser.py

b) Google geocoding Library
   -- /libs/google

   To try with this method, please comment line 26 and uncomment line 29 in main.py

c) Streetaddress library (https://github.com/pnpnpn/street-address)
   -- /libs/streetaddress

   To try with this method, please comment line 26 and uncomment lines (32, 33, 34) in main.py
