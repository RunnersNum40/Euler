.text
.global _start
_start:
	MOV R0, #1000	// loop until
	MOV R1, #0		// loop from
	MOV R2, #0		// sum register
	Loop:
		ADD R1, R1, #1
		CMP R0, R1
		BEQ End
		MOV R3, R1
		MOV R4, #3
		BL Modulo
		CMP R3, #0
		BEQ AddN
		MOV R3, R1
		MOV R4, #5
		BL Modulo
		CMP R3, #0
		BEQ AddN
	B Loop
	
	AddN:
		ADD R2, R2, R1
	B Loop

	Modulo: // Compute R3%R4 and store in R3
		CMP R3, R4
		BLT EndSub
		SUB R3, R3, R4
		B Modulo
	B EndSub
	
	EndSub:
		BX LR
End: B End
.end