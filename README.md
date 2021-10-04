# Natas
Help scripts and writeup for natas challenges hosted by OverTheWire

All scripts have been written in Python 3.6.

## Disclaimer
The primary goal of this repository is showing how to use Python in CTF
challenges. That's why the passwords are not written in the credentials file:
at least try the scripts!

There is a plethora of specialized libraries and frameworks for penetration
testing, but for didactic purposes, we will use only the Python's standard
library.

## Usage
The file natas.json contains the credentials for each level. Scripts
automatically read the correct credentials. As you progress you can write here
the found flags.
Each script can be run on its own, without any dependency.

## natas0

Here you will learn how to make a basic HTTP request with basic authentication
and how to fetch the results.

## natas1

Apparently natas0 was meant to be done using a GUI web browser, because this
challenge is exactly the same, but the right-click has been deactivated.

## natas2

Here you will learn how to list directories and inspect its content.

## natas3

One of the comments in the code hints you to look for a robots.txt file.
Using what you learned, you will be able to figure out how to navigate the site
to extract the password from a file.

## natas4

The site checks from which page the request came by means of the `Referer`
header. Use this to your advantage.

## natas5

In this challenge you will have to manipulate a cookie to continue.

## natas6

Use what you learned to inspect the included PHP files.

## natas7

Use the hints in the code to perform a **Local File Inclusion**.

## natas8

Look for the encoded secret and the function to generate it. You will get
familiar with base64 and hexadecimal conversions.

## natas9

Here you will face a pretty obvious case of command injection.

## natas10

Similar to the previous challenge, but you will have to dodge a lousy input
validation.

## natas11

This case is a classical case of predictable encryption: you can use the default
value of the cookie to find the pattern in the encryption algorithm.

## natas12

In this challenge the uploaded file is not being validated at all. Use it to
your advantage.

## natas13

Now the fyletype is checked, but this is not enough to stop you, or is it?

## natas14

SQL Injection 101

## natas15

Another SQL injection where you will have to use conditionals to guess the
password letter by letter.

## natas16

Knowing that the value of one of the fields can be executed is key.

## natas17

Blind SQL injection. Here the only hint it the processing time of the request.

## natas18

A poorly designed session ID assignation, that can be brute-forced.

## natas19

Another version of the prior challenge.

## natas20

Yet another version of the same challenge.

## natas21

Another weak session ID generator, but this time the vulnerability is not in the
main page, making this a sort of side-channel exploitation.

## natas22

The page in this challenge keeps redirecting us somewhere else to distract us
from its flaws.

## natas23

In this challenge you will see how to exploit weak typing in PHP.

## natas24

Here the backend seems to be implemented in C, and inspecting the manpages of
certain string-handling functions will give you the hints you need.

## natas25

This one is fun. You will have to bypass several basic input validations to 
build up to a LFI.

## natas26

Object deserialization can be used to inject code in PHP too.

## natas27

Use a truncation issue in SQL to bypass some control conditions.

## natas28

Remember the predictable session IDs? Weak encryption algorithms are exactly as
bad.

## natas29

In this challenge you will have your first contact with vulnerable Perl calls.

## natas30

There is a way to bypass the quote() function in perl.

## natas31

This is a complex challenge. You will have to search for the CCC presentations
titled "The Perl Jam" where it is explained why Perl is not a suitable language
for the web.

## natas32

There is a perl script that can execute whatever you give as an argument.

## natas33

There is a way to exploit the PHP function md5_file().