start:
  mov z 1
  mov i 0

loop:
  mul z 2
  inc i
  ifn i 10
  jmp loop

  mov rv z
  ret
