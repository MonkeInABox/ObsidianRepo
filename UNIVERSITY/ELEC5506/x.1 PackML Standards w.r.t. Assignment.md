	(ANSI/ISA TR88.02-2015)
# Assignment Background
- 2 products: red container with fluid A, blue container with fluid B
- Each step is a work-cell, robot arms between cells
- **BATCH** process consists of
	- Cell that empties red containers
	- Cell that empties blue containers
	- Cell that fills containers depending on colour of container
		- Supplied by a robot which places container on the conveyor belt of filling station
		- Separate robot collects filled containers
	- Cell that seals the containers (common lid)

## We are to control the filling cell
- Sensors: 
	- Acoustic level sensor (high when full)
	- Proximity sensor for the container at the input (high when present)
	- Solenoids that fill fluids A and B (high opens filling injector)
- Conveyor belt to location to fill and to where robot moves it
- Should consider fault situations
	- Abort
	- Stop

Reference: [PackML: The Packaging Machine Language Driving Automation](https://www.automationreadypanels.com/automation-and-systems/packml-the-packaging-machine-language-driving-automation/)
[PackML States Explained: All 17 States & Modes | Frostbyte Pro](https://frostbytesoftware.co.nz/blog/packml-states-explained)


![[Pasted image 20260328170853.png]]
## Core Components
- Modes
	- Auto, manual, maintenance
- States
	- Starting, executing, holding
- Actions
	- What they do when enabled
- Transitions

### 8 Execution States
- Stopping
- Stopped
- Starting
- Execute
- Suspending
- Suspended
- Unsuspending
```
17 States:
- STOPPED : powered and stationary after STOPPING or CLEARING
	  NOTHING IS HAPPENING - ALL LOW
- IDLE : RESETTING complete, until STARTING
	  NOTHING IS HAPPENING - ALL LOW
- STARTING : when a command is given, steps to start EXECUTION
	  INITIALISE SENSORS
	  START UP CONVEYOR
- SUSPENDING : brough to controlled SUSPENDED, status saved
	  REMAIN IN CURRENT STATE
	  TURN OFF FILLING AND CONVEYOR
- SUSPENDED : once process conditions are normal moves to UNSUS
	  REMAIN IN CURRENT STATE
	  TURN OFF FILLING AND CONVEYOR
- UNSUSPENDING : transition from SUSPENDED to EXECUTE
	  MAKE SURE SENSORS ARE CORRECT IN CURRENT STATE
- EXECUTE : performing the required action
	  WAIT FOR CONTAINER ON CONVEYOR
	  TURN ON CONVEYOR TO MOVE UNTIL AT FILLING STATION
		  NEEDS TO MOVE TO CORRECT FILLING STATION
	  TURN OFF CONVEYOR WHEN APPROPRIATE FILL SENSOR TRIGGERED
	  TURN ON APPROPRIATE SOLENOID ONCE SENSOR HIGH
	  TURN BACK ON CONVEYOR
	  TURN OFF CONVEYOR ONCE SENSOR AT END TRIGGERED
- STOPPING : bring to controlled stop, until RESETTING takes place
	  TURN OFF FILLING
	  TURN OFF CONVEYOR
	  DECELERATE
- ABORTING : rapid safe stop
	  TURN OFF FILLING 
	  TURN OFF CONVEYOR
- ABORTED : only exit after a CLEAR command
	  NOTHING ON
	  MUST RECEIVE A CLEAR OR RESET COMMAND
- HOLDING : minor STOP
	  STOP FILLING 
	  TURN OFF CONVEYOR
		  DECELERATE
- HELD : until UNHOLD
	  NOTHIING ON
- COMPLETING : from EXECUTE when the run is complete
	  FINISH ALL CURRENT CONVEYOR ITEMS
- COMPLETE : until RESET
	  NO NEW ITEMS LEFT ON CONVEYOR
- RESETTING : transition to IDLE
	  AFTER UN-STOPPED
	  RESET ALL SENSORS TO LOW
	  TURN OFF CONVEYOR
- CLEARING : when cleared faults occurred when ABORTING
```

**Normal production cycle:**

```
Stopped → [Reset] → Resetting → Idle → [Start] → Starting → Execute → Completing → Complete → [Reset] → Resetting → Idle
```

**Operator pause (Hold): INTERNAL**

```
Execute → [Hold] → Holding → Held → [Unhold] → Unholding → Execute
```

**External blockage (Suspend): EXTERNAL**

```
Execute → Suspending → Suspended → Unsuspending → Execute
```

**Fault / emergency stop: MOST SERIOUS**

```
[Any state] → [Abort] → Aborting → Aborted → [Clear] → Clearing → Stopped
```

**End of shift shutdown:**

```
Execute → [Stop] → Stopping → Stopped
```

