# computer-science-challenge
Challenge 01: Computer Science

Our company has always been known for throwing epic parties for their employees, and the next one will not be the exception. For the next event we have prepared a game to make everyone have a good time and win prizes while also dancing and having fun. In this occasion, the dance floor will look like a square matrix and HR has designed a very interesting game called Longest Dance Line. Knowing the age of the person is very important for this game, so HR has designed a series of banners with this information for every guest, which must be held at all times. As shown in Figure 1.

![1](https://github.com/gabrielcosson/computer-science-challenge/assets/71792818/97c84a3c-2f0b-4503-ba62-bd0dbc5f28f5)
Figure 1. A person holding the banner.

Figure 2 shows an image of what the dance floor will look like from a camera above. A member of the staff will make sure that everyone is following the rules and will check who the winners will be in the end.

![2](https://github.com/gabrielcosson/computer-science-challenge/assets/71792818/929a9214-15fd-4498-8a19-36d95fa08ad9)
Figure 2. Dance Floor seen from the above.

The winners of the game will be those who manage to create the longest dance line, considering the following rules:
  a)	There can only be one person for each position available on the dance floor matrix.
  b)	The age of the starting person does not matter.
  c)	The next person should be located only to the right or down.
  d)	The next person in the line must be one year younger or one year older.

For example, if we analyze the dance floor shown in Figure 2, we can see that the longest dance line is that with the path 25-24-25-26-27-28-27-26 (with a length of 8 people). However, even though there may be different routes with the same longest dance line, the staff team is only interested in knowing one that maximizes the number of people. For example, the path 23-24-25-26-27-28-27-26 will also be valid, as shown in Figure 3. 

![3](https://github.com/gabrielcosson/computer-science-challenge/assets/71792818/a5502695-845a-4775-890f-1d331761ea2d)
Figure 3. Different valid routes.

The staff team knows that it is complicated to keep track of so many people at a party and that it may get a wrong answer if the number of contestants increases. Since it can be too difficult to process the information manually, they have given the task to a developer to create a program that can perform validation quickly and accurately.


