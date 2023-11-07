[[VHDL]]


|   |   |
|---|---|
|Created|@August 21, 2023 3:16 PM|
|Class|Digital System Design|
|Reviewed||

```
ENTITY DUT_name_tb IS --no port decs
END ENTITY;

ARCHITECTURE arch OF DUT_name_tb IS
	COMPONENT DUT_name
		PORT (inputs IN intype; outputs OUT outtype);
	END COMPONENT;

SIGNAL test_inputs : intype;
SIGNAL test_outputs : outtype;

BEGIN
	[DUT:] DUT_name PORT MAP ( inputs => test_inputs, outputs => test_outputs );
	test_inputs <= waveform_expression;
END arch;
```

********************************After Statement:********************************

```
signal <= <initial_value>, <end_value> after <time>;
```