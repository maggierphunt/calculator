# calculator
Python / SQL calculator

Shortcuts:
- Lifting from buttons and some css from past projects
- Did not set up virtualenv or anything strong in terms of cyber sec or auth
- Did not do anything fancy SQL wise - only a few rows of data
- requirements.txt is not refined
- picked bigquery for ease but not convinced it was the best solution


Possible interpretations:
1 Build front end where users select items from a pre-existing db; the landing pge dispays each item's cost And then once submitted the results page shows the total
2 Build front end where users enter custom items and amounts; these are added to the db when submitted and the total vaule of the items they havelisted is displayed on the results page
3 Build front end where users enter custom items and amounts; these are added to the db when submitted and the total vauel of all items listed in the db is displayed on the results page

At first I set on option 3 but after 3 hours realised this was not feasible when using a new library and working full stack in one evening; I therefore opted to work on option 1, with option 2 a potential 'nice to have'.