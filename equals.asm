start:
  pop x
  ifn x 97
  jmp fail

  pop x
  ifn x 98
  jmp fail

  pop x
  ifn x 99
  jmp fail

  pop x
  ifn x 100
  jmp fail

  jmp success

fail:
  mov rv 0
  ret

success:
  mov rv 1
  ret
