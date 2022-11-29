# calculator
Python / SQL calculator - practice with SQL Alchemy

Shortcuts / to do next:
- Logging
- Have not yet not set up virtualenv or anything strong in terms of cyber sec or auth
- Did not do anything fancy SQL wise - only a few rows of data
- Security is low - json etc
- initially built to run locally and push to a csv - now working on operatiolaising that fully in this branch. hosting pending
- requirements.txt is not refined
- picked bigquery for ease but not convinced it was the best solution
- display is symmetrical, unlike wireframe
- usually would add some comments explaining / documenting
- price format on display page does not add extra 0 if needed


Possible interpretations of calc screen updagte
1 Build front end where users select items from a pre-existing db; the landing pge dispays each item's cost And then once submitted the results page shows the total
2 Build front end where users enter custom items and amounts; these are added to the db when submitted and the total vaule of the items they havelisted is displayed on the results page
3 Build front end where users enter custom items and amounts; these are added to the db when submitted and the total vauel of all items listed in the db is displayed on the results page

At first I set on option 1 but after 3 hours realised this was not feasible when using a new library and working full stack in one evening; I therefore opted to work on option 2 (with option 3 a potential 'nice to have').

I've had some auth issues with GCP - so tested out pushing to a csvfile while I tried to debug.
