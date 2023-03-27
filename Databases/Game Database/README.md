=== Game Database ===

A self-hosted web application for managing a database of videogames owned by the user.\
Currently mostly an exercise in ~~frustration~~ following Microsoft's Razor Pages tutorials and trying to
understand how to work with databases in this context.\
\
Uses the ASP.NET Core web framework.\
\
TODO:\
Implement a proper, full database as defined in schema.sql.\
	This would require Games to have many-many relations with tags, developers, etc.,
something the Migration system does not seem to be particularly keen on.