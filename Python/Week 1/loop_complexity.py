import time
start_time = time.time()

for i in range(10):
    for j in range(10):
        print(0 , end=" " )  # end to output in the same line
    print()  # newline after the inner loop finish

print(round((time.time()-start_time),2))  #time it takes to execute the looping rounded