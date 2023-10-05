import numpy as np;import matplotlib.pyplot as plt;import random;import math; import time
#implement either quicksort or merge sort (depending on worst case scenario) (maybe talk about how heapsort is great)
def create_points():
    xydata=np.zeros((50,2)) # initialize array CHANGE DATA POINTS HERE
    for i in range(len(xydata)):
        xydata[i,0]=random.uniform(0, 1)*10;xydata[i,1]=random.uniform(0,1)*10 # generate random set of xy points
    return xydata
def find_ymin(xydata):
    index = 0  # Initialize the index to the first element
    for i in range(1, len(xydata)): # Start the loop from the second element
        if xydata[i, 1] <= xydata[index, 1] or (xydata[i, 1] == xydata[index, 1]and xydata[i, 0] < xydata[index, 0]): # Compare points
            index = i  # Update the index if a smaller value is found
    return index
def polar_angles(min_index, xydata):
    polar = np.zeros(len(xydata));polarind = np.zeros(len(xydata));x1, y1 = xydata[min_index]
    for i in range(len(polar)):
        x2, y2 = xydata[i,:];polarind[i] = i;polar[i] = math.atan2(y2 - y1, x2 - x1)
    return polar, polarind
def get_cross_product(p1,p2,p3):
    return ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))
def merge_sort_with_indices(arr):
    if len(arr) <= 1:
        return arr, list(range(len(arr)))  # Base case: Return the array and its original indices

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_indices = list(range(mid))
    right_indices = list(range(mid, len(arr)))

    # Recursively sort the two halves and merge them
    left_half_sorted, left_indices_sorted = merge_sort_with_indices(left_half)
    right_half_sorted, right_indices_sorted = merge_sort_with_indices(right_half)

    # Merge the sorted halves while keeping track of the original indices
    sorted_arr = []
    merged_indices = []
    i, j = 0, 0

    while i < len(left_half_sorted) and j < len(right_half_sorted):
        if left_half_sorted[i] <= right_half_sorted[j]:
            sorted_arr.append(left_half_sorted[i])
            merged_indices.append(left_indices[left_indices_sorted[i]])
            i += 1
        else:
            sorted_arr.append(right_half_sorted[j])
            merged_indices.append(right_indices[right_indices_sorted[j]])
            j += 1

    # Append any remaining elements
    sorted_arr.extend(left_half_sorted[i:])
    for k in range(i, len(left_half_sorted)):
        merged_indices.append(left_indices[left_indices_sorted[k]])
    sorted_arr.extend(right_half_sorted[j:])
    for k in range(j, len(right_half_sorted)):
        merged_indices.append(right_indices[right_indices_sorted[k]])
    merged_indices= np.array(merged_indices,dtype="int")
    return sorted_arr, merged_indices
def build_hull(xy_data,polar_ind):
    sorted_list = [xy_data[i,:] for i in polar_ind.astype(int)] # covert to integer to sort list (Time Complexity O(n)) can do a better job of this with initialized variables
    sort_arr= np.array(sorted_list,dtype="float64") # convert to np array (Time Complexity (O(n))) can do a better job of this with initialized variables
    if len(xy_data) < 3:
        print("You fucked up not enough points to build hull")
    hull = [sort_arr[0,:], sort_arr[1,:]]
    for i in range(2, len(sort_arr)):
        while len(hull) > 2 and get_cross_product(hull[-2],hull[-1],sort_arr[i]) < 0:
            hull.pop()
        hull.append(sort_arr[i])
    hull.append(hull[0])    
    hull = np.array(hull)
    return hull
def figure_plot(xydata,sort_dat):
    plt.scatter(xydata[:,0], xydata[:,1], c='k', marker='o');plt.scatter(sort_dat[0][0], sort_dat[0][1], c='r', marker='o');plt.plot(sort_dat[:,0], sort_dat[:,1], c='g')
    plt.title('Option 4,5: Find convex hull of a random set of points');plt.xlabel('X axis');plt.ylabel('Y axis');plt.grid();plt.show();plt.close()   

xy_data = create_points()
start = time.perf_counter_ns() # Start timer
min_ind = find_ymin(xy_data) # Find point with lowest y coordinate [Time Complexity: O(n)]
polar,polar_ind = polar_angles(min_ind, xy_data) # Convert points to polar form to see angle it creates with lowest y coordinate point [Time Complexity: O(n)]
sorted_array, polar_ind = merge_sort_with_indices(polar) # Sort polar angles based on angle with starting point and sort indices (Time Complexity (n(log(n)) due to mergesort)
con_hull = build_hull(xy_data,polar_ind) # There is a while loop that may pop points from the hull. Worst case, [Time Complexity O(n)]
end = time.perf_counter_ns()# End timer
print("nanoseconds elapsed: ",end-start) # Print elapsed time
figure_plot(xy_data,con_hull) # Plot points in black and convex hull in green, starting point is red
