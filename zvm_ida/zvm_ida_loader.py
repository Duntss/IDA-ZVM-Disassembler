import idaapi as ida

LOADER_NAME = 'Zeus VM bytecode'

NUM_OPCODES = 69

perm_RX = ida.SEGPERM_READ | ida.SEGPERM_EXEC
perm_RW = ida.SEGPERM_READ | ida.SEGPERM_WRITE


def accept_file(f, n):
    data = f.read(1)
    if len(data) < 1:
        return 0
    opcode = data[0] & 0x7F
    if opcode < NUM_OPCODES:
        return {'format': LOADER_NAME, 'processor': 'zvmproc', 'options': 1 | ida.ACCEPT_FIRST}
    return 0


def load_file(li: ida.loader_input_t, neflags, fmt):

    ida.set_processor_type("zvmproc",
                           ida.SETPROC_LOADER_NON_FATAL | ida.SETPROC_LOADER)
    ida.set_compiler_id(ida.COMP_GNU)

    image_base = 0
    ida.set_imagebase(image_base)

    def create_segment(name, sclass, start, end, perms):
        s = ida.segment_t()
        s.start_ea = start
        s.end_ea = end
        s.bitness = 1  # 32-bit
        s.align = ida.saRelByte
        s.perm = perms
        s.set_loader_segm(True)
        ida.add_segm_ex(s, name, sclass, 0)

    li.file2base(0, 0, li.size(), True)
    create_segment(".text", "CODE", 0, li.size(), perm_RX)

    ida.add_entry(0, image_base, "start", 1)

    return 1
