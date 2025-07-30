**TEAM 31** 
**CITS3200 PROFESSIONAL COMPUTING**
Time: 1410 - 1510
Date: 30/07/25
Venue: E-Zone
Present: Jeremy, Will, Ben, Dongkai, Steve and Noah 
# Client Discussion 1
### Background
- Sediments in coastal zone and on sediment shelf
	- Montebello Islands
	- How radioactivity has moved around the seafloor
	- Looking at sediment grain size
	- Risks to people visiting the area/fishing/eating
	- Where do the sediments accumulate
- Frequency and log of size graphs used to analyse
	- Multimodal means more than one source, or more than one process
### Issues of Old Entropy Program
- Spits the sizes into a number of groupings, displays number of groupings that best explain/display the data
- To try to work out how many groups separates the grain size groupings
- Automated plotting needs to be done, has to be done manually at the moment
- Too big excel file to manage
	- Bands drawn to show different modal sizes
- You copy and paste data from Excel into old EntropyMax (by Lachlan Stewart, CSIRO)
	- Select input file (.csv)
	- Tell it what type of output file (lots of little for each group, or composite) and define a file name or choose existed file to overwrite
	- Does 2 to 20 groups
	- Looks at whole grain size distribution of samples, splits into 2 groups, 3, etc.
		- Maximise the difference between the grain sizes
	- Run time error YAY
	- Performance is not too big of a deal
	- The green line is the proportion of data explained (Rs value), red is the groups (Calinski-Harabasz statistic)
		- First flattish area is where they would start looking
		- These graphs are not necessary
		- Only shows best group size, spits out file for grain size
			- Says what the best group size is 
		- Spits out excel file with the groupings
- Each group has a geographic position
	- Has to look at map and put number in manually at the moment
	- Needs to automate putting group numbers to map positions (from google earth)
	- Great to be able to plot modal ranges on the seabed
		- Currently from separate program, manually finding the sample name and typing in the modal size
- Lots of mistake, using manual input, and also doesn't allow others to use it
	- Needs to be user friendly
### Key Updates Required
- Improve graphical output of groupings and and individual particle size distribution curves
	- This is the priority
- Export results in KMZ files for viewing in Google Earth and other forms (integration with spatial data, so results can be chosen based on their true location and viewed easily on screen)
- Show progression of grain size through any hypothesized transport pathway (select locations and show the plots)
- Increase accessibility and operability
	- Concept could be applied to other similar profile inputs and outputs
	- Scalings and etc on the output graphs
- Nicer GUI program
- Hopefully something publishable at the end of the day
### Communications
- Data will be sent and the entropy outputs as an example
- Code will be sent
- Piers and Ingrid are available for meetings almost any time
	- Open for suggestions for how it looks, etc.
- Would like as much back and forth as possible
# Tasks
#### Next Deliverables
**Sprint 1**: Due 5pm Wednesday 13th August to client & MS teams directory
- A scope of work (the Epic), a general statement of what the project is to achieve
	- Requirements Document
- Skills and Resources Audit
- Risk Register
- Project Acceptance Tests
- A set of stories
### Reports
- N/A
### Discussions/Clarifications
- Potential for website to expand its use
	- Also to allow for extra processing power
- Step by step for the data processing
- Python libraries easy to change how to the file is processed
### To Do
- Requirements Document
- Skills and Resources Audit
>Everyone: Due Friday
- Risk Register
- A formal test manual
- A set of stories
- Set up GitHub
>Jeremy: Due Friday
### Next Meeting
2pm, Next Wednesday 06/08/2025