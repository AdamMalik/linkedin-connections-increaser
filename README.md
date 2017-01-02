# linkedin-connections-increaser
This is a script written in python using selenium
 It is just a few lines of script. Through this I increased my number of LinkedIn connections from one hundred something to 525 (today’s count).

This is a python script. For this you need to install selenium.

Those who did a little bit of Web development may familiar with selecting element using Id, or class name or tag name. As I was unable to find the connect buttons with any of these predefined selection procedure, I chose XPath.

To find the xpath of a element in Chrome, just inspect the element and right click upon it, there you will find a option to copy the xpath. When I analysed the connect buttons xapths for sending each request, I understood It is dynamic and so I need to change the xpath too on each loop. (See line no 45)

I kept my script running for an Hour or so and I sent 450 connections request on LinkedIn.
