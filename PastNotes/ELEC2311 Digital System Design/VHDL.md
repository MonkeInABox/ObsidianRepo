

|   |   |
|---|---|
|Created|@August 1, 2023 3:56 PM|
|Class|Digital System Design|
|Reviewed||

************************VHDL Basics:************************

```
LIBRARY ieee;                         --library declaration
USE ieee.std_logic_1164.all;          --use all defs from package st...64 from ieee

ENTITY logic IS                       --description of the gate named "logic"
	PORT (                
		a,b,c: IN STD_LOGIC;              --inputs of the module are a, b and c
		h: IN STD_LOGIC_VECTOR(11 DOWNTO 0); --bus with 12 wires
		f: OUT STD_LOGIC                  --output is f (no semicolon after last port)
	);
END logic;                            --end the ports of "logic"

USE WORK.a_package_name.ALL;

ARCHITECTURE archlogic OF logic IS   --the architecture, what does the entity "logic" do
	SIGNAL d: STD_LOGIC;
BEGIN
	d <= a AND b;                        --behavioural
	g1: nor2 PORT MAP (c, d, f);         --structural
END archlogic;
```

- — for comment

- /= for not equal

- not case sensitive

- .vhd files (i.e. nand_gate.vhd)

[![](Untitled%2023.png)](VHDL%2004d9497b0f0d4dfdb48bbb8277dbe04d/Untitled.png)

[![](Untitled%201%204.png)](VHDL%2004d9497b0f0d4dfdb48bbb8277dbe04d/Untitled%201.png)

[![](Untitled%202%202.png)](VHDL%2004d9497b0f0d4dfdb48bbb8277dbe04d/Untitled%202.png)

****************************************Conflict Resolution:****************************************

[![](Untitled%203%202.png)](VHDL%2004d9497b0f0d4dfdb48bbb8277dbe04d/Untitled%203.png)

******ENTITY:******

- description of the interface

- the PORT defines all the signals that will be visible to external design entities
    
    - IN data comes into this port, and can only be read in the entity
    
    - OUT data goes out through this port, can be set but not read
    
    - INOUT data is bidirectional, can be read and set
    
    - BUFFER data goes out of entity and is also fed-back internally

- types of VHDL
    
    - std_logic = models one wire
    
    - std_logic_vector = a grouping of bits to model a collection of wires, a bus
    
    - BIT a signal of 1 or 0
    
    - BIT_VECTOR a grouping of bits
    
    - INTEGER
    
    - BOOLEAN
    
    - ENUMERATED `TYPE states IS (start, slow, fast, stop);`

**************************ARCHITECTURE:**************************

- describes the content or the functionality of the module

- two types:
    
    - structural = instantiations of blocks referred to as components (placements of logic gates)
    
    - behavioural = descriptions `IF ... THEN...; x <= (a OR b) AND c;...`

- multiple architectures can be made for a particular entity
    - maybe to be optimised to a different end goal

- signal declaration
    - `signal signal_name, signal_name_2 : std_logic := '0';`

[![](Untitled%204%201.png)](VHDL%2004d9497b0f0d4dfdb48bbb8277dbe04d/Untitled%204.png)

- 2 types of statements:
    
    - sequential
    
    - concurrent

********ARCHITECTURE modelling styles:********

- STRUCTURAL MODELLING:
    
    - multiple VHDL units are connected together
    
    - hierarchy can simplify design descriptions
    
    - may connect simple gates or components
    
    - use COMPONENT & PORT MAP statements
    
    - COMPONENT for the following block:
        
        ```
        COMPONENT XY_gate
        	PORT (
        		X, Y : IN std_logic; 
        		s1, s2 : OUT std_logic
        	);
        END COMPONENT;
        
        COMPONENT QZ_gate
        	PORT (
        		Z1, Z2 : IN std_logic;
        		Q : IN std_logic_vector(7 DOWNTO 0); 
        		ST : OUT std_logic
        	);
        END COMPONENT;
        ```
        
    
    [![](Untitled%205%201.png)](VHDL%2004d9497b0f0d4dfdb48bbb8277dbe04d/Untitled%205.png)
    
    - INSTANTIATION:
        
        ```
        instance_label : component_name
        	PORT MAP (
        		component_port1 =>signal1,
        		component_port2 =>signal2,
        		…
        		component_portn =>signaln
        	);
        ```
        
        [![](Untitled%206%201.png)](VHDL%2004d9497b0f0d4dfdb48bbb8277dbe04d/Untitled%206.png)
        
    
    [![](Untitled%207%201.png)](VHDL%2004d9497b0f0d4dfdb48bbb8277dbe04d/Untitled%207.png)
    

- DATAFLOW Modelling:
    - works well for small and simple circuits

- BEHAVIOURAL Modelling:
    
    - the behaviour is in an algorithmic manner
    
    - process statement is a concurrent statement
    
    - process syntax:
    
    ```
    [Process_label] : PROCESS (sensitivity list)
    -- declarations
    BEGIN
    -- sequential statements
    END PROCESS [Process_label];
    ```
    
    - the sensitivity list is a list of signals to which the process is sensitive
        
        - process is evaluated when an event on any of the signals are listed and only them
        
        - if no sensitivity listed, then it occurs on any signal
    
    - statements are evaluated sequentially in terms of simulation and in zero simulation time
    
    - <= in a process it means schedule an assignment at the end of the process, outside of the process it means assign immediately
    
    ```
    OR3_1 : process(A,B,C) --3-input OR gate sequential 
    begin
    	F <=‘0’;
    	if A = ‘1’ then F <= ‘1’;
    		elsif B = ‘1’ then F <=‘1’;
    		elsif C = ‘1’ then F <=‘1’;
    		else F <=‘0‘;
    	end if;
    end process OR3_1;
    ```
    
    [![](Untitled%208%201.png)](VHDL%2004d9497b0f0d4dfdb48bbb8277dbe04d/Untitled%208.png)
    

********************************LOOP statements:********************************

```
E3: loop
	a := a + 1;
	exit E3 when a > 10;
end loop E3;
```

- can also be WAIT statements