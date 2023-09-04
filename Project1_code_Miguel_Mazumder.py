import time
import numpy as np
import matplotlib.pyplot as plt
j = 5
n_size = int(2e6)
step_size = int(4e5)
sum = 0
n_times = np.zeros([1,1])
start = time.perf_counter_ns()
for n in range(1,n_size,step_size):
    while (j < n/2):
        k = 5
        while (k < n):
            a_j= np.random.rand(1, 1)*100
            b_k= np.random.rand(1, 1)*100
            sum += int(a_j)*int(b_k)
            k = k*np.sqrt(2)
        j = np.sqrt(3)*j
    end = time.perf_counter_ns()
    n_times = np.append(n_times,end-start)
    #print(n_times)
n_steps = np.linspace(1.01, n_size, int(n_size/step_size)+1)
#one=np.ones((len(n_steps), 1))
#flat_one = one.flatten()
#plt.plot(n_steps,flat_one,linewidth=3)
plt.plot(n_steps,np.log(n_steps),'g--',linewidth=3)
plt.plot(n_steps,n_steps*np.log(n_steps),'r--',linewidth=3)
plt.plot(n_steps,n_times,'k',linewidth=3)
plt.xlabel('Number of steps (n)')
plt.ylabel('Time Complexity of n (nano seconds)')
plt.legend(['O(log(n))','O(n(log(n)))','O(f(n))'])
plt.show()