import multiprocessing 

num_cores = multiprocessing.cpu_count() # For newer CPUs will be the number of virtual cores!
proc_list = list() # This list is so you can "join" them. Important!
my_queue = multiprocessing.Queue() # Queues do q.put() and q.get() and other things. 

def your_worker_function(a_range, the_data, my_queue) # Your args will most likely differ.
  pass # This is just a sample that does nothing, your function goes here.


# Main-like here:
for a_range in chunk_ranges: 
      # The number of chunks in my code equals the number of processes (making them not shown here).
      # "chunk_ranges" is a list of lists, [[index_a, index_b], ...], indexes in a Pandas DF I am parsing. Easy to parallelize.
      # Your for loop will differ, depending on your data.
  a_proc = multiprocessing.Process(target=your_worker_function, args=(a_range, the_data, my_queue))
      # To your worker function, pass the args -- here it's the data range, a pointer to that data, and the queue object. 
      # In your code it will probably differ.
  proc_list.append(a_proc)
      # So you have a list of them and can iterate through the list for join to end them nicely. 
  a_proc.start() # Starts one! 

# Waits for them to end and ends them nicely, cleanup. 
for p in proc_list: 
  p.join()
  print '%s.exitcode = %s' % (p.name, p.exitcode)
    # You don't need this but it's nice to see them end and their exit status number in case they don't!

print 'Getting elements from the queue.'  
while not my_queue.empty(): 
  one_procs_data = my_queue.get() 
  # Then do something with that, maybe add it to a list, depends on what it is. 
