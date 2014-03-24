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
ret
