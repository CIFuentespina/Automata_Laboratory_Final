Diagram of the Mealy and Moore Machine


<img width="1024" height="1536" alt="Diagram MealyMooreMAchine" src="https://github.com/user-attachments/assets/e2c49d8c-267c-4619-8fa7-4c1dc7f2eacb" />

 Moore machine-Text
graph LR
  A_init(["A_init (start)"])
  A_A(["A_A / A"])
  A_B(["A_B / B"])
  B_B(["B_B / B"])
  C_A(["C_A / A"])
  C_C(["C_C / C"])
  D_B(["D_B / B"])
  D_C(["D_C / C"])
  E_C(["E_C / C"])

  A_init -->|0| A_A
  A_init -->|1| A_B

  A_A -->|0| A_A
  A_A -->|1| A_B

  A_B -->|0| C_A
  A_B -->|1| C_C

  B_B -->|0| C_A
  B_B -->|1| D_B

  C_A -->|0| D_C
  C_A -->|1| B_B

  C_C -->|0| D_C
  C_C -->|1| B_B

  D_B -->|0| B_B
  D_B -->|1| C_C

  D_C -->|0| B_B
  D_C -->|1| C_C

  E_C -->|0| D_C
  E_C -->|1| E_C
 Mealy machine-text
graph LR
  A -->|0 / A| A
  A -->|1 / B| A

  B -->|0 / A| C
  B -->|1 / B| D

  C -->|0 / C| D
  C -->|1 / B| B

  D -->|0 / B| B
  D -->|1 / C| C

  E -->|0 / C| D
  E -->|1 / C| E

