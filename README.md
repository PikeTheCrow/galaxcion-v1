IDE used: C9 (cloud based IDE https://c9.io)
SCM: git with Github private repo

Diary Entry June 5th 2020
Humanity has been on edge since the latest financial collapse left 99.99% of the earth's population with 0.01% of the wealth. You can feel the despair in the air. Some have moved off planet, some remain to fight, to survive, to live some kind of life which resembles the past.

Diary Entry June 29th 2020
The world has fallen into further chaos. Riots have broken out. I fear for my life. I have managed to scrap together over the years a messily sum of money and some materials, raw resources and other personal items. A friend of mine has advised me of a black market scrap yard selling “refurbished” spaceships. Who are we kidding, they are stolen, guts ripped out and reassembled for those looking for a break. I will buy one. 

Diary Entry July 6th 2020
I have decided to leave this forsaken planet behind. This will be my last entry.

With only 10 hours remaining before I flee, I was informed of how the galaxy’s trading system works (well, the basics). With such little time and no money to purchase a Currency Converter I have decided to create my own. A base model which I hope to improve over time. Something to occupy my mind as I glide endlessly through the dark void that is space.

A statement I have chosen to live my life by is:
“Why reinvent the wheel when your true innovation is the tire”.

I decided to learn and write the application in Python for its ease of use and ability to easily manipulate data. 

For now, all I need to concern myself with is the following:
The ability to calculate values based on the Roman Numerals
    -	Therefore, write / find an algorithm which understand Roman Numeral patterns
The ability to translate Roman Numerals to Earth Values for better understanding
The ability to read a text file (which I have been informed has a standard layout)
    -	Broken down as follows:
        o	Initial section is the merchant’s currency compared to Roman Numerals
        o	Followed by information containing certain ‘undefined’ values which are generally minerals (as minerals are of high value in the Galaxy)
    o	Followed by questions which requiring interpreting and answering

I have named my application Galaxicion and v1 has come along quite well. 
I have documented the processes throughout the scripts in case someone reads over the application and tries to improve on it.

Galaxicion v2 is in progress. I have started detailing feature improvements which will most likely slight refactoring of the code and therefore I will have a v1.5 as well.

In v1.5 I would like to do the following:
    -	Create a script to update my currencies database (which is currently a .py file)
    -	Create a function to track each merchant I come in contact with in the galaxy
    -	Establish better file formatting which allows for more information and easier interpretation
    -	Create a script to log my ships GPS
    -	Create a script which pushes retrieve merchant info to a centralized repo of merchants

In v2 we would implement the features of v1.5:
    -	We have a centralized / remote database system most likely (OrientDB – scalability is better than MongoDB with 220 000 transactions per sec as a norm, JSON file structure unlike BSON as well as the ability to use SQL to access info from the DB.
    -	Each merchant will be added to the DB will all their corresponding information
        o	Currency conversion
        o	Questions
        o	Mineral costs
        o	And more to be determined
    -	A file submission process (drop files) or form submitting
    -	My GPS is now logged to the DB

In v3 I will implement the centralized merchant repo for trading

Now if only there was a way to share my work with keen, open-source developers across the Galaxy and to work collaboratively with them on bettering the merchant trading system…

Next – I will work on Jounral. A platform to share work and find people who are interested in working on your posted solution. With a built in crypto-currency reward system.  
