import time #Measures execution time in seconds
import random #For randomization of strings
import string #For random strings
import pandas #Process bucket slot and chain length
from datetime import timedelta #Display elapse time
from sys import getsizeof #Measures memory usage in bytes
from math import floor, ceil, modf, sqrt #For multiplicative Hashing only

class HashTable: #Hash Table Specification
    def __init__(self, bs, hf, step):
        self.size = bs # Prime number of bucket size
        self.hf = hf # Hash function: modular or multiplicative
        self.step =  step # < -1: double hash / -1: quadratic probing / 0: chaining / > 0: linear probing
        self.max_probing = bs # max probing to quit
        
        self.ch = "ch" if step == 0 else "lp" # Collision handling strategy
        self.mf = (sqrt(5)-1)/2 # (3^40)/(2^64) Use golden ratio as multiplicative factor
        
        # [] for chaining, None for linear probing
        self.bucket = [[] for generation in range(self.size)] if self.ch == "ch" else [None for generation in range(self.size)]

    #print every key and its slot/chain
    def print_bucket(self):
        if self.ch == "ch":
            for slot in range(self.size):
                for chain in range(len(self.bucket[slot])):
                    print(slot,chain,self.bucket[slot][chain])
        else:
            for slot in range(self.size):
                if self.bucket[slot] is not None:
                    print(slot,self.bucket[slot])

    #measure memory usage in bytes
    def memory_usage(self):
        return getsizeof(self.bucket)

    # hash key: convert key string to a integer for hash function input
    def hash_key(self, key):
        #hash_key = 0
        #for i in range(len(key)):
        #    hash_key += ord(key[i]) * (10**i)
        #return hash_key
        return key

    # hash function, return slot
    def hash_function(self, key):
        hash_key = self.hash_key(key)
        slot = hash_key % self.size if self.hf == "mod" else floor( self.size * modf(hash_key*self.mf)[0] )
        return slot

    # double hash function: slot = slot0 + j * hf2(key,j)
    # must > 0 for open addressing / closed hashing
    def double_hash_function(self, key, j):
        hash_key = self.hash_key(key)

        if self.step > 0 :     # linear probing
            return self.step   
        elif self.step == -1 : # classic quadratic probing
            return j           
        elif self.step == -2 : # faster quadratic probing
            return j           
        elif self.step == -3 : # double hash modular function   ###    better if self.size and self.size-2 are twin primes
            return 1 + hash_key % (self.size-2)     
        elif self.step == -4 : # double hash multiplicative function
            return ceil((self.size-2) * modf(hash_key * self.mf)[0]) 
        elif self.step == -5 : # classic quadratic probing with a large starting step
            return j           
        elif self.step == -6 : # faster quadratic probing with a large starting step
            return j           
        elif self.step == -7 : # double hash modular function with quadratic probing
            return 1 + hash_key % (self.size-2) 
        elif self.step == -8 : # double hash multiplicative function with quadratic probing
            return ceil((self.size-2) * modf(hash_key * self.mf)[0])
        else:
            raise Exception(f"Invalid collision handling strategy! Check the step input.")

    # find next slot based on current slot and j-th probing
    # Warning: fixed-step (-4,-3,>0) always success if it is coprime to bucket size; however, j-varied-step (-8,-7,-6,-5,-2,-1) may fail after many probings in small bucket
    def next_slot(self, slot_now, j, step0): 
        if self.step > 0 :                      # linear probing
            slot_next = slot_now + self.step    # hf2(key,j) = step    => step_j = (slot0 + j*step) - (slot0 + (j-1)*step) = step
        elif self.step == -1 :                  # classic quadratic probing
            slot_next = slot_now + 2*j-1        # hf2(key,j) = j       => step_j = (slot0 + j^2) - (slot0 + (j-1)^2) = j^2 - (j-1)^2 = 2*j-1
        elif self.step == -2 :                  # faster quadratic probing
            slot_next = slot_now + j            # hf2(key,j) = (j+1)/2 => step_j = (slot0 + j*(j+1)/2) - (slot0 + (j-1)*(j-1+1)/2) = j
        elif self.step in [-3,-4] :             # double hash function
            slot_next = slot_now + step0        # double hash without j in hf2(key,j) = step0: it is just a key-varied-step linear probing
        elif self.step == -5 :                  # classic quadratic probing with a large starting step
            slot_next = slot_now + 2*j + 999    # hf2(key,j) = j + stepK
        elif self.step == -6 :                  # faster quadratic probing with a large starting step
            slot_next = slot_now + j + 1000     # hf2(key,j) = (j+1)/2 + stepK
        elif self.step in [-7,-8] :             # double hash function with quadratic probing
            slot_next = slot_now + step0 + j    # double hash with j in hf2(key,j) = step0 + (j+1)/2
        
        return slot_next % self.size

    # insert key, return bucket slot
    def __setitem__(self, key, hash_key): 
        slot = self.hash_function(hash_key)

        if self.ch == "ch":
            self.bucket[slot].append(key)
            return slot
        else:
            step0 = self.double_hash_function(key,0) # key-varied-step for double hash

            for j in range(1,self.max_probing): # chain counting
                if self.bucket[slot] is None:
                    self.bucket[slot] = key
                    return slot

                slot = self.next_slot(slot, j, step0)
            
            raise Exception(f"Insertion failed after {j} probing for (key, hash_key) = ({key}, {hash_key}).")
            

    # query key, return chain location
    def __getitem__(self, key, hash_key): 
        slot = self.hash_function(hash_key)

        if self.ch == "ch":
            for j in range(len(self.bucket[slot])):
                if self.bucket[slot][j] == key:
                    return j
        else:
            step0 = self.double_hash_function(key,0) # key-varied-step for double hash

            for j in range(1,self.max_probing): # chain counting
                if self.bucket[slot] == key:
                    return j

                slot = self.next_slot(slot, j, step0)

            raise Exception(f"Retrieval failed after {j} probing for (key, hash_key) = ({key}, {hash_key}).")

    # return slot for each key
    def insert(self, keys):
        slot_list = []
        for i in range(len(keys)):
            slot_list.append(self.__setitem__(i,keys[i]))
        return slot_list

    # return collision / chain length for each key
    def retrieve(self, keys):
        chain_list = []
        for i in range(len(keys)):
            chain_list.append(self.__getitem__(i,keys[i]))
        return chain_list

def main():
    starting_time = time.time()
    N             = 10000 # raw dataset size
    roundN        = 25    # repeat round for average statistics
    hk_range      = [500, 1000, 2500, 5000, 7500, 10000, 20000, 40000, 20000000] # create hash_key from extremely uneven to even distribution
    datasetN      = len(hk_range)     # total datasets to test
    stepN         = 100   # total steps to test
    stepS         = -4    # starting step
    hf_list       = ["mod", "mul"] # hash function list
    bs_list       = [9999973, 19993, 11119, 10429, 10039, 10009] # bucket size list

    # repeat rounds for average statistics
    for r in range(roundN):
        # reset round initial time
        round_initial_time = time.time()
        
        # test on different distribution datasets
        for ds in range(datasetN): 
            # reset dataset initial time
            dataset_initial_time = time.time()

            # create a new raw dataset for each new round
            keys = [random.randint(1, hk_range[ds]) for i in range(N)]

            # create a new output csv file for each new round
            file = open(f"Hash_D{str(ds).zfill(2)}-R{str(r).zfill(2)}.csv","a")
            
            # first row of output csv file
            file_header = "step,"
            for hf in hf_list:
                for bs in range(len(bs_list)):
                    col = hf + str(bs+1)
                    file_header += col+"InTm,"+col+"RtTm,"+col+"CMed,"+col+"CMax,"+col+"CAvg,"+col+"CStd,"
                    
            # remove the last comma
            file.write(file_header[:-1])

            # step = -8: open addressing / closed hashing: double hash multiplicative function with quadratic probing
            # step = -7: open addressing / closed hashing: double hash modular function with quadratic probing
            # step = -6: open addressing / closed hashing: faster quadratic probing with a large starting step
            # step = -5: open addressing / closed hashing: classic quadratic probing with a large starting step
            # step = -4: open addressing / closed hashing: double hash multiplicative function
            # step = -3: open addressing / closed hashing: double hash modular function
            # step = -2: open addressing / closed hashing: faster quadratic probing
            # step = -1: open addressing / closed hashing: classic quadratic probing
            # step =  0: seperate chaining / open hashing
            # step >  0: open addressing / closed hashing: linear probing
            for step in range(stepS, stepN):
                # start with a return and step for each new row
                file.write(f"\n{step}")

                # test different operations in one row
                for hf in hf_list: # hash function
                    for bs in bs_list: # change bucket size (prime number) to have different load factor
                        hash_table = HashTable(bs, hf, step)

                        # Insertion
                        initial_time   = time.time()
                        slot_list      = hash_table.insert(keys)
                        insertion_time = time.time() - initial_time

                        # Retrieval
                        initial_time   = time.time()
                        chain_list     = hash_table.retrieve(keys)
                        retrieval_time = time.time() - initial_time

                        # collision / chain length on every bucket slot
                        df = pandas.DataFrame({'slot':slot_list, 'chain':chain_list})
                        cdf = df.groupby(['slot']).max()

                        # one operation completed                
                        file.write(f",{insertion_time:.10f},{retrieval_time:.10f},{cdf.chain.median()},{cdf.chain.max()},{cdf.chain.mean()},{cdf.chain.std()}")

                # one step row calculation completed            
                dataset_percent = 100*(step-stepS+1)/(stepN-stepS)
                round_percent   = 100*((step-stepS+1)+ds*(stepN-stepS))/((stepN-stepS)*datasetN)
                total_percent   = 100*((step-stepS+1)+ds*(stepN-stepS)+r*(stepN-stepS)*datasetN)/((stepN-stepS)*datasetN*roundN)
                dataset_time    = round( time.time() - dataset_initial_time )
                round_time      = round( time.time() - round_initial_time )
                total_time      = round( time.time() - starting_time )

                print(f"{step:4d} step in dataset({ds+1:2d}/{datasetN}) {dataset_percent:6.2f}% completed in {timedelta(seconds=dataset_time)}. " + 
                      f"Round({r+1:2d}/{roundN}) {round_percent:6.2f}% completed in {timedelta(seconds=round_time)}. " + 
                      f"Total {total_percent:8.4f}% completed in {timedelta(seconds=total_time)}")

            # one dataset file output completed            
            file.close()

            #round_percent = 100*(ds+1)/datasetN
            #total_percent = 100*(ds+1+r*datasetN)/(datasetN*roundN)
            #round_time    = round( time.time() - round_initial_time )
            #total_time    = round( time.time() - starting_time )

            #print(f"{ds+1:2d}/{datasetN} dataset file output in round({r+1:2d}/{roundN}) {round_percent:6.2f}% completed in {timedelta(seconds=round_time)}. " + 
            #      f"Total {total_percent:8.4f}% completed in {timedelta(seconds=total_time)}")

if __name__ == '__main__':
    main()
