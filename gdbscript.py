import gdb 
res = gdb.execute("vmmap",to_string=True)
binbase = int(res[res.find('0x') : res.find('0x')+8*2+2],16)
print("binbase : "+hex(binbase))

bp_off = [0x000D8E]
for i in bp_off:
    gdb.execute("b * "+hex(binbase + i))
gdb.exeecute("c")
# gdb -q -x ./gdbscript.py at pid