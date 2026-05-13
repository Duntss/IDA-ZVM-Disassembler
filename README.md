# IDA-ZVM-Disassembler

IDA Pro processor module and loader for the Zeus VM custom bytecode instruction set, ported from the [OALabs Binary Ninja plugin](https://github.com/OALabs/ZVM).

## Installation

Copy the two files into your IDA Pro installation:

- `zvm_ida_loader.py` → `<IDA_DIR>/loaders/`
- `zvm_ida_proc.py` → `<IDA_DIR>/procs/`

Then open any `.zvm` bytecode file — IDA will auto-detect the format and use the Zeus VM processor.

## Features

- 69 instructions fully decoded (arithmetic, bitwise, memory, control flow, RC4, shuffle)
- XOR key chain decryption handled transparently during analysis
- Cross-references for loop branch targets
- Auto-comments describing instruction semantics
- Register display with size suffixes (`.b`, `.w`)

## References

### OALabs - Zeus VM

- Original Binary Ninja plugin: https://github.com/OALabs/ZVM
- OALabs Patreon (subscription required): https://www.patreon.com/cw/oalabs
- Intro to VMs: https://research.openanalysis.net/vmzues/zeus/vm/obfuscation/tutorial/2024/01/07/into-to-vms.html
- Zeus VM Disassembler: https://research.openanalysis.net/vmzues/zeus/vm/obfuscation/tutorial/2024/01/21/vmzeus-disassembler.html

### IDA Pro Plugin Development

- [IDAPython: Generating disassembly lines and instruction decoding](https://www.youtube.com/watch?v=qRS6310gDoQ)
