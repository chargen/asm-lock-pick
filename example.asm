start:
  pop rv
#  ret

  mov x 10
  sub x 20
  mov rv x
#  ret

  mov x 254
  add x 10
  mov rv x
#  ret

  mov z 1
  mov i 0

loop:
  mul z 2
  inc i
  ifn i 10
  jmp loop

  mov rv z
  ret
