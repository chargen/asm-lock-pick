mov a 1
mov b 2
add a b
push 1
push 2
push 3
pop c
mov rv a
add rv c
ifg a b
add rv 10
save 0x00 123
save 0x01 1
mov x 0x00
inc x
load y x
add rv y
ret
