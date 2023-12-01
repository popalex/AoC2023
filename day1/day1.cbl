       IDENTIFICATION DIVISION.
       PROGRAM-ID. DAY1.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
            SELECT INPUT-FILE ASSIGN TO INPUTF.
      
       DATA DIVISION.
       FILE SECTION.
      
       FD INPUT-FILE.
       01 INPUT-RECORD.
           05 DATA-FIELD PIC X(80).
      
       WORKING-STORAGE SECTION.
       01 WS-EOF-SWITCH PIC X VALUE 'N'.
       01 FirstNumber   PIC 9(10).
       01 LastNumber    PIC 9(10).
       01 FullNumber    PIC 9(11).
       01 SumOfNumbers  PIC 9(11).
       01 CurrentNumber PIC 9.
       01 NumberFound   PIC X VALUE 'N'.
       01 I             PIC 9(3).
      
       PROCEDURE DIVISION.
           OPEN INPUT INPUT-FILE
           MOVE ZEROES TO SumOfNumbers 

           PERFORM UNTIL WS-EOF-SWITCH = 'Y'
               READ INPUT-FILE
                   AT END
                       MOVE 'Y' TO WS-EOF-SWITCH
                   NOT AT END
                       DISPLAY 'Record: ' DATA-FIELD
                       PERFORM ProcessLine
                       COMPUTE SumOfNumbers = SumOfNumbers + FullNumber 
                       DISPLAY 'SumOfNumbers=' SumOfNumbers
               END-READ
           END-PERFORM

           DISPLAY 'RESULT=' SumOfNumbers
           CLOSE INPUT-FILE
           STOP RUN.
       
       ProcessLine.
           MOVE ZEROES TO FirstNumber LastNumber NumberFound.
           DISPLAY 'Init done...'
           MOVE 'N' TO NumberFound

           PERFORM VARYING I FROM 1 BY 1 UNTIL I > LENGTH OF DATA-FIELD
              MOVE ZEROES TO CurrentNumber
      *       DISPLAY 'I=' I ' DATA-FIELD(I:1)=' DATA-FIELD(I:1)
              IF DATA-FIELD(I:1) = SPACE 
                 EXIT PERFORM
              END-IF 
              IF DATA-FIELD(I:1) NUMERIC
                  MOVE DATA-FIELD(I:1) TO CurrentNumber
      *           DISPLAY 'Converted Number: ' CurrentNumber
                  IF NumberFound = 'N'
                       MOVE CurrentNumber TO FirstNumber
                       MOVE 'Y' TO NumberFound
                   ELSE
                       MOVE CurrentNumber TO LastNumber
                   END-IF
              END-IF
           END-PERFORM.
           
      *    DISPLAY 'After Perform=' NumberFound
           IF NumberFound = 'Y'
                 COMPUTE FullNumber = (FirstNumber * 10) + LastNumber
                 DISPLAY 'First Number: ' FirstNumber
                 DISPLAY 'Last Number: ' LastNumber
                 DISPLAY 'Full Number: ' FullNumber
           END-IF.
