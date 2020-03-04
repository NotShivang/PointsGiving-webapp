# PointsGiving-webapp

Situation: Your boss has come to you and wants you to create a website that allows all employees to thank each other using a system of points and rewards. Each employee will be given 1,000 points per month to give to their coworkers. They can determine the number of points to give and include a message if they wish to any other coworker. If they do not hand out all their points for the month, they lose what they do not use, and the points reset at midnight on the last day of the month. Employees can use points they have been given to turn them into gift cards – every 10,000 points is a $100 gift card. More details are below in the Requirements section.


Requirements:
You must have the following in your database:
•	As mentioned above, users:
o	One administrator – they can see reports but cannot give or receive points
o	Five individual users – they cannot see reports; they can only give and redeem points
•	At least one stored procedure using a transaction to handle the giving of points from one user to another
•	At least one view that simplifies how the admin gets raw report data for all users of the system. This could be used to power a report below or for some other purpose
•	At least one sequence must be used for a primary key
•	All passwords must be encrypted somehow
•	Foreign keys are required on your tables as appropriate
•	Sample data for the two previous months – you will need to create a way to insert random but valid data into your tables (part of building a system is figuring out how to test it)
•	Three reports (these should show up on the website but do not need to be fancy, the data can be raw on the page)
o	One that shows the Aggregate Usage Of Points On A Monthly Basis – both rewards given out and rewards cashed in, as well as broken down by user, ranked in order of most points received to least
o	One that shows Who Isn’t Giving Out All Of Their Points For The Current Recent Month only (including those that haven’t used any) 
o	One that shows All Redemptions, By Month By User, For The Previous Two Months
•	Include a button for the Admin to force a month end (which will reset all points to give out)
•	Each user should be able to see a complete history of both points received and points given
•	Users cannot re-gift points they receive.  There are separate balances for points to give and points received.
Other Notes:
•	It is HIGHLY suggested that you store your DDL and DML in some form of source control
•	Requirements are subject to change/clarification as the project progresses. The Piazza discussion board will be the official medium for communication about requirements.  No requirements change/clarification is official unless it has been posted on Piazza and tagged with the “project_requirements” label.
