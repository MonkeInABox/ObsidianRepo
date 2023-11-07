[[VHDL]]


|   |   |
|---|---|
|Created|@July 25, 2023 10:00 AM|
|Class|Digital System Design|
|Reviewed||

[![](Untitled%201.png)](Design%20&%20Signals%201af169bfe5d34b6d87b3d8f1cea6c31a/Untitled.png)

Digital signals are either 1 or 0, hence they have better noise immunity:

- the sender and receivers have to agree upon voltage levels and logical signals so that they can communicate

- forbidden regions separates two valid regions to outlaw close calls

- V(IL) must be greater than V(OL) and V(OH) must be greater than V(IH)

- NM(L) = V(IL) - V(OL) || NM(H) = V(OH) - V(IH)

- Static discipline if they can talk to each other

- In digital systems noise is cancelled at each stage

****************************************Signal Regeneration:****************************************

- The circuit must restore marginal valid inputs and provide unquestionable inputs

- The regeneration can occur many times without causes errors

- Regeneration can occur due to the voltage transfer characteristic (VTC) of the digital circuit

- VTC is a graph showing the equilibrium output voltage of the digital device when an input voltage is applied and time is allowed for the output to settle

- VTC measures static behaviour

**************Buffer:**************

- A buffer copies its input value to its output

**********Design:**********

- ABSTRACTION:
    
    - we use models to different levels of details and/or from different perspectives
    
    - provides a simplified model, only retaining information relevant to a particular purpose

- HIERARCHICAL/MODULAR DESIGN:
    
    - top-down = decompose each component into small components, to lowest level primitive components
    
    - bottom-up = build-up from primitive components, combined to form complex components
    
    - mixed strategies = mostly top-down but also with bits of bottom-up, in reality we need to know both top level

- HARDWARE DESCRIPTION LANGUAGE:
    
    - schematic entry (k-maps > optimise booleans > draw new schematic) is good for fairly small designs, but not good for large designs
    
    - schematic entry not feasible for large designs
        - time consuming, prone to mistakes, difficult design entry, not easy to modify
    
    - describe in text using Hardware Description Language (HDL)
    
    - Allows quick time to market, allows creation of device-independent designs that are portable to multiple vendors, with one language for design and simulation

**************************************************************************************VHDL (VHSIC Hardware Description Language):**************************************************************************************

- VHSIC = very high speed integrated circuit

- The ENTITY describes the periphery of the black box (Ports I/O) and ARCHITECTURE is the behaviour of the entity:

```
ENTITY logic IS PORT (
	a,b,c: IN STD_LOGIC;
	f: OUT STD_LOGIC);
END logic;

USE WORK.a_package_name.ALL;
ARCHITECTURE archlogic OF logic IS
	SIGNAL d: STD_LOGIC;
BEGIN
	d <= a AND b;                              --behavioural
	g1: nor2 PORT MAP (c, d, f);               --structural
END archlogic;
```

[![](Untitled%201%201.png)](Design%20&%20Signals%201af169bfe5d34b6d87b3d8f1cea6c31a/Untitled%201.png)

**************The Modest Switch:**************

- Controllable switch is controlled by the voltage, high voltage at input turns switch on

************************************************Transistors as Switches:************************************************

- CMOS (complementary metal oxide on semiconductor)
    
    - MOS act as voltage-controlled switches
    
    - they have three terminals: drain, gate and source
    
    [![](Untitled%202.png)](Design%20&%20Signals%201af169bfe5d34b6d87b3d8f1cea6c31a/Untitled%202.png)
    

********************************************************************Programmable Logic Devices (PLDs):********************************************************************

- PLA small PLD that includes two levels of programmable logic, AND plane and OR plane

- PAL small PLD that has a programmable AND plane and a fixed OR plane

- SPLD any simple PLD usually PLA or PAL

- CPLD a more complex PLD that includes an arrangement of multiple SPLD blocks on a chip

- FPGA a field programmable gate array is a PLD featuring a general structure that allows very high logic capacity

**********************************************Why Do We Need Testing:**********************************************

- Properly designed chip may fail in field
    
    - transient (under heating, radiation…)
    
    - intermittent (random, finite duration)
    
    - permanent failures

- Manufacturing Defects
    
    - wafer defects
    
    - contaminated atmosphere in clean room, dust…
    
    - impure processing gasses, water, chemicals…
    
    - photomask misalignmens