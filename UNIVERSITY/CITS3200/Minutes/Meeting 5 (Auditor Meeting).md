**TEAM 31** 
**CITS3200 PROFESSIONAL COMPUTING**
Time: 1300 - 1400
Date: 27/08/25
Venue: Barry J Marshall
Present: Jeremy, Will, Ben, Dongkai, Steve, Suman Inamdar (AUDITOR), Noah (after 1340)
Apologies: Noah (until 1340)

## 1. Last Meeting Recap
**Backend Status:**
- Hoping to have it finished by the end of this week (Friday afternoon)
**GUI Progress:** 
- The next step is wiring the UI components to the backend logic.  
**Development Workflow & Version Control:** 
- Conflicts:
	- Fragile so backed off for now
	- Should be done this afternoon
## 2. Past Action Items
1. **Backend Team:** Finalize the last two remaining functions. 
	1. Done (bar minor tweaks) by Friday (more likely early next week)
2. **GUI:** Continue UI development and prepare for backend integration. 
	1. Pyarrow to pass from parquet to graph
3. **All Developers:** Push current commits to their respective branches to synchronize progress. 
	1. Not pushed current work: Ben
4. **Integration:** Determine the specific method/files for calling the Python backend from the GUI. 
	1. Dongkai made data flow

## 3. New Meeting Points
- Dongkai shows us the new workflow
	- Using mock data
	- Because Piers has to select directly from the maps
	- Renders HTML in window for the interactive map
	- Worried about performance
	- Click on data instead of map
	- Currently using about 400MB memory
		- Static rendering is option 
	- Window pop-ups for the graphs
- Steve might try to organise meeting with Piers, Dongkai and Jeremy
	- We need to figure out which points are actually shown on the map
- Issues usage is really good, keep it up and updating it
	- Dongkai's temporal data, ask Piers for another CSV
- Ben gives I/O update
	- Just pushed to branch
	- Added a file that cleans the CSV file, adding k-value
	- Added a validate CSV file
		- Checks if it is in the correct format (type checking, columns, etc)
	- C-file that executes all the Python
	- Add coordinate file has not been added due to not having coordinate test data
- Will gives an update
	- Grouping function is nearly done
	- Doc string along it
	- Steve wants to do a codejam with Will and Noah (maybe Friday?)
- Noah gives an update
	- Inputs are handled differently, with multiple different C files that need to be compiled
	- Help to all be in the same room when merging
	- Issues will probably arise when we push test data through
	- Slower progress due to sickness (get well!!)
- Clarifying the data flow through the program
	- Raw CSV --> Entropy --> Parquet File --> Python Middle Layer Reader --> Then Grouped To Put Into UI
### Next Meeting
2pm, Next Wednesday 03/09/2025