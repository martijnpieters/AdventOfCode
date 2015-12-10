from __future__ import absolute_import, print_function
import numpy as np
import pyopencl as cl
import datetime

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)
prg = cl.Program(ctx, """
__kernel void look(__global const int* numbers, __global int* result) {
    unsigned int gid = get_global_id(0);
    unsigned int i = 0;
    
    while (numbers[gid] == numbers[gid + i]) i++;
    
    result[gid] = i;
}
__kernel void say(__global const int* numbers, __global const int* amount, __global int* result) {
    unsigned int gid = get_global_id(0);
    
    if (gid == 0 || (amount[gid] >= amount[gid - 1])) {
        result[gid*2] = amount[gid];
        result[gid*2 + 1] = numbers[gid];
    }
}
""").build()

# Initialize client side (CPU) array
numberList = [3,1,1,3,3,2,2,1,1,3]
numbers = np.array(numberList).astype(np.int32)
a = datetime.datetime.now()

for i in range(50):
    # Create OpenCL buffers
    mf = cl.mem_flags
    numbers_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=numbers)
    amount_buf = cl.Buffer(ctx, mf.READ_WRITE, numbers.nbytes)
    results_buf = cl.Buffer(ctx, mf.WRITE_ONLY, numbers.nbytes * 2)

    # Execute the look kernel
    prg.look(queue, numbers.shape, None, numbers_buf, amount_buf)
    
    # Execute the say kernel
    prg.say(queue, numbers.shape, None, numbers_buf, amount_buf, results_buf)

    # Read results from buffer
    results = np.empty(shape=(numbers.size * 2,)).astype(np.int32)
    cl.enqueue_read_buffer(queue, results_buf, results).wait()
    
    # Filter zeros from list
    numbers = results[results > 0]
    
print(len(numbers))
b = datetime.datetime.now()
print(b-a)