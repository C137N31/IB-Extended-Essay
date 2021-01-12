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
        
        self.ch = "ch" if step == 0 else "lp" # Collision handling strategy
        self.mf = (sqrt(5)-1)/2 # (3^40)/(2^64) Use golden ratio as mulplicative factor
        
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

    # hash code: convert string to integer
    def hash_number(self, key):
        #hash_num = 0
        #for i in range(len(key)):
        #    hash_num += ord(key[i]) * (10**i)
        #return hash_num
        return key

    # hash function, return slot
    def hash_function(self, key):
        hash_num = self.hash_number(key)
        slot = hash_num % self.size if self.hf == "mod" else floor( self.size * modf(hash_num*self.mf)[0] )
        return slot

    # double hash function: slot = slot0 + j * hf2(key,j)
    # must > 0 for open addressing / closed hashing
    def double_hash_function(self, key, chain):
        hash_num = self.hash_number(key)

        if self.step > 0: # linear probing
            return self.step
        elif self.step == -1: # quadratic probing
            return chain
        elif self.step in [-2,-3]: # double hash modular function
            return 1 + hash_num % (self.size-2) # better if self.size and self.size-2 are twin primes
        elif self.step in [-4,-5]: # double hash mulplicative function
            return ceil((self.size-2) * modf(hash_num * self.mf)[0])
        else:
            raise Exception(f"Invalid collision handling strategy! Check the step input.")

    # insert key, return bucket slot
    def __setitem__(self, key): 
        slot = self.hash_function(key) # slot0

        if self.ch == "ch":
            self.bucket[slot].append(key)
        else:
            j = 0 # chain counting
            step0 = self.double_hash_function(key,j)

            while self.bucket[slot] is not None:
                j += 1
                if j == self.size :
                    raise Exception(f"Insertion failed after {j} probing for key={key}.")

                # slot = slot0 + j * hf2(key,j)
                # linear probing    if step  >  0: hf2(key,j) = step            => step_j = (slot0 + j*step) - (slot0 + (j-1)*step) = step
                # quadratic probing if step  = -1: hf2(key,j) = j               => step_j = (slot0 + j^2) - (slot0 + (j-1)^2) = j^2 - (j-1)^2 = 2*j-1
                # double hash       if step  < -1: hf2(key,j) = step0 + (j+1)/2 => step_j = (slot0 + j*(step0+(j+1)/2)) - (slot0 + (j-1)*(step0+(j-1+1)/2)) = step0 + j
                if self.step > 0 : # linear probing
                    slot += self.step
                elif self.step == -1 : # quadratic probing
                    slot += 2*j-1
                elif self.step in [-2,-4]: # double hash without j in hf2(key,j) = step0: it is just key-varied linear probing
                    slot += step0
                elif self.step in [-3,-5]: # double hash with j in hf2(key,j) = step0 + (j+1)/2
                    slot += step0 + j
                else:
                    raise Exception(f"Invalid collision handling strategy! Check the step input.")
                
                slot = slot % self.size
            
            self.bucket[slot] = key
            
        return slot

    # query key, return chain location
    def __getitem__(self, key): 
        slot = self.hash_function(key) # slot0

        if self.ch == "ch":
            for chain in range(len(self.bucket[slot])):
                if self.bucket[slot][chain] == key:
                    return chain
        else:
            j = 0 # chain counting
            step0 = self.double_hash_function(key,j)

            while self.bucket[slot] != key:
                j += 1
                if j == self.size :
                    raise Exception(f"Retrieval failed after {j} probing for key={key}.")

                if self.step > 0 : # linear probing
                    slot += self.step
                elif self.step == -1 : # quadratic probing
                    slot += 2*j-1
                elif self.step in [-2,-4]: # double hash without j in hf2(key,j) = step0: it is just key-varied linear probing
                    slot += step0
                elif self.step in [-3,-5]: # double hash with j in hf2(key,j) = step0 + (j+1)/2
                    slot += step0 + j
                else:
                    raise Exception(f"Invalid collision handling strategy! Check the step input.")

                slot = slot % self.size

            return j

    # return slot for each key
    def insert(self, keys):
        slot_list = []
        for key in keys:
            slot_list.append(self.__setitem__(key))
        return slot_list

    # return collision / chain length for each key
    def retrieve(self, keys):
        chain_list = []
        for key in keys:
            chain_list.append(self.__getitem__(key))
        return chain_list

def main():
    starting_time = time.time()
    N       = 10000 # raw dataset size
    roundN  = 25    # total rounds to test
    stepN   = 100   # total steps to test
    stepS   = -5    # starting step

    # test different M for modular and mulplicative funcation
    operations = ([9999973, "mod"], [19993, "mod"], [11119, "mod"], [10429, "mod"], [10039, "mod"], [10009, "mod"],
                  [9999973, "mul"], [19993, "mul"], [11119, "mul"], [10429, "mul"], [10039, "mul"], [10009, "mul"])

    # repeat round for a group of operations and steps
    for r in range(roundN): 
        # reset round initial time
        round_initial_time = time.time()

        # create a new raw dataset for each new round
        keys = random.sample(range(1, N*N), N)

        # create a new output csv file for each new round
        file = open(f"/Project/Hash/Hash{str(r).zfill(3)}.csv","a")
        file.write("Step,Mo1InTm,Mo1RtTm,Mo1CMed,Mo1CMax,Mo1CAvg,Mo1CStd"
                     + ",Mo2InTm,Mo2RtTm,Mo2CMed,Mo2CMax,Mo2CAvg,Mo2CStd"
                     + ",Mo3InTm,Mo3RtTm,Mo3CMed,Mo3CMax,Mo3CAvg,Mo3CStd"
                     + ",Mo4InTm,Mo4RtTm,Mo4CMed,Mo4CMax,Mo4CAvg,Mo4CStd"
                     + ",Mo5InTm,Mo5RtTm,Mo5CMed,Mo5CMax,Mo5CAvg,Mo5CStd"
                     + ",Mo6InTm,Mo6RtTm,Mo6CMed,Mo6CMax,Mo6CAvg,Mo6CStd"
                     + ",Mu1InTm,Mu1RtTm,Mu1CMed,Mu1CMax,Mu1CAvg,Mu1CStd"
                     + ",Mu2InTm,Mu2RtTm,Mu2CMed,Mu2CMax,Mu2CAvg,Mu2CStd"
                     + ",Mu3InTm,Mu3RtTm,Mu3CMed,Mu3CMax,Mu3CAvg,Mu3CStd"
                     + ",Mu4InTm,Mu4RtTm,Mu4CMed,Mu4CMax,Mu4CAvg,Mu4CStd"
                     + ",Mu5InTm,Mu5RtTm,Mu5CMed,Mu5CMax,Mu5CAvg,Mu5CStd"
                     + ",Mu6InTm,Mu6RtTm,Mu6CMed,Mu6CMax,Mu6CAvg,Mu6CStd")

        # step < -1: open addressing / closed hashing: double hash
        # step = -1: open addressing / closed hashing: quadratic probing
        # step =  0: seperate chaining / open hashing
        # step >  0: open addressing / closed hashing: linear probing
        for step in range(-5,stepN):
            # start with a return and step for each new row
            file.write(f"\n{step}")

            # test different operations in one row
            for i, op in enumerate(operations):
                hash_table = HashTable(op[0],op[1],step)

                #Insertion
                initial_time   = time.time()
                slot_list      = hash_table.insert(keys)
                insertion_time = time.time() - initial_time
    
                #Retrieval
                initial_time   = time.time()
                chain_list     = hash_table.retrieve(keys)
                retrieval_time = time.time() - initial_time
    
                # collision / chain length on every bucket slot
                df = pandas.DataFrame({'slot':slot_list, 'chain':chain_list})
                cdf = df.groupby(['slot']).max()

                # one operation completed                
                file.write(f",{insertion_time:.10f},{retrieval_time:.10f},{cdf.chain.median()},{cdf.chain.max()},{cdf.chain.mean()},{cdf.chain.std()}")
                print(f"{i} operation completed with {step} step in {r} round.")

            # one row calculation completed            
            round_time  = time.time() - round_initial_time
            elapse_time = time.time() - starting_time

            print(f"{r} round {100*(step-stepS+1)/(stepN-stepS):.2f}% completed in {timedelta(seconds=round_time)}. " + 
                  f"Total rounds {100*((step-stepS+1)+r*(stepN-stepS))/((stepN-stepS)*roundN):.4f}% completed in {timedelta(seconds=elapse_time)}")
        
        # one round test completed
        file.close()

if __name__ == '__main__':
    main()
