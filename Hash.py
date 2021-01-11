import time #Measures execution time in seconds
import random #For randomization of strings
import string #For random strings
import pandas #Process bucket index and chain length
#import sympy #For random step used in linear probing
from datetime import timedelta #Display elapse time
from sys import getsizeof #Measures memory usage in bytes
from math import floor, modf, sqrt #For multiplicative Hashing only

class HashTable: #Hash Table Specification
    def __init__(self, M, hf, step):
        self.size = M # Prime number of bucket size
        self.hf = hf # Hash function: modular or multiplicative
        self.step =  step # quadratic probing if step == 0, else linear probing
        
        self.ch = "ch" if step < 0 else "lp" # Collision handling strategy
        self.mf = (sqrt(5)-1)/2 # (3^40)/(2^64) Use golden ratio as mulplicative factor
        
        #[] for chaining, None for linear probing
        if self.ch == "lp": # linear probing
            self.bucket = [None for generation in range(self.size)] 
        elif self.ch == "ch": # chaining
            self.bucket = [[] for generation in range(self.size)]

    #print every key and its index/chain
    def print_bucket(self):
        if self.ch == "ch":
            for i in range(self.size):
                for j in range(len(self.bucket[i])):
                    print(i,j,self.bucket[i][j])
        elif self.ch == "lp":
            for i in range(self.size):
                if self.bucket[i] is not None:
                    print(i,self.bucket[i])

    #measure memory usage in bytes
    def memory_usage(self):
        return getsizeof(self.bucket)

    # hash function, return index
    def hash_function(self, key):
        hash_code = 0
        for character in key:
            hash_code += ord(character)
        if self.hf == "mod":
            return hash_code % self.size
        elif self.hf == "mul":
            return floor(self.size * modf(hash_code * self.mf)[0])

    # insert key, return bucket index
    def __setitem__(self, key): 
        index = self.hash_function(key)
        if self.ch == "ch":
            self.bucket[index].append(key)
        elif self.ch == "lp":
            j = 0
            while self.bucket[index] is not None:
                j += 1
                # quadratic probing if step = 0, step = (index0 + j^2) - (index0 + (j-1)^2) = j^2 - (j-1)^2 = 2*j-1
                # linear probing if step > 0
                index = index+2*j-1 if self.step == 0 else index+self.step
                index = index % self.size
            self.bucket[index] = key
            
        return index

    # query key, return chain location
    def __getitem__(self, key): 
        index = self.hash_function(key)
        if self.ch == "ch":
            for j in range(len(self.bucket[index])):
                if self.bucket[index][j] == key:
                    return j
        elif self.ch == "lp":
            j = 0
            while self.bucket[index] != key:
                j += 1
                # quadratic probing if step = 0, step = (index0 + j^2) - (index0 + (j-1)^2) = j^2 - (j-1)^2 = 2*j-1
                # linear probing if step > 0
                index = index+2*j-1 if self.step == 0 else index+self.step
                index = index % self.size
            return j
            
        raise Exception("Key does not exist in Hash Table")

    # return index for each key
    def insert(self, keys):
        index_list = []
        for key in keys:
            index_list.append(self.__setitem__(key))
        return index_list

    # return collision length for each key
    def retrieve(self, keys):
        collison_list = []
        for key in keys:
            collison_list.append(self.__getitem__(key))
        return collison_list

def main():
    N = 10000 # raw dataset size
    roundN = 100 # total rounds to test
    stepN = 1000 # total steps to test
    letters = string.ascii_letters + string.digits

    # test different M for modular and mulplicative funcation
    operations = ([9999991,"mod"], [19997,  "mod"], [11113,  "mod"], [10193,  "mod"], [10037,  "mod"], [10007,  "mod"],
                  [9999991,"mul"], [19997,  "mul"], [11113,  "mul"], [10193,  "mul"], [10037,  "mul"], [10007,  "mul"])

    # repeat round for a group of operations and steps
    for r in range(roundN): 
        # reset round initial time
        round_initial_time = time.time()

        # create a new raw dataset for each new round
        keys = []
        for i in range(N):
            keys.append("".join([random.choice(letters) for i in range(random.randint(1,16))]))  # random 16-bit password as key

        # create a new output csv file for each new round
        file = open(f"/Project/Hash/Hash{str(r).zfill(3)}.csv","a")
        file.write("Step,Mo1InTm,Mo1RtTm,Mo1CMed,Mo1CAvg,Mo1CStd"
                     + ",Mo2InTm,Mo2RtTm,Mo2CMed,Mo2CAvg,Mo2CStd"
                     + ",Mo3InTm,Mo3RtTm,Mo3CMed,Mo3CAvg,Mo3CStd"
                     + ",Mo4InTm,Mo4RtTm,Mo4CMed,Mo4CAvg,Mo4CStd"
                     + ",Mo5InTm,Mo5RtTm,Mo5CMed,Mo5CAvg,Mo5CStd"
                     + ",Mo6InTm,Mo6RtTm,Mo6CMed,Mo6CAvg,Mo6CStd"
                     + ",Mu1InTm,Mu1RtTm,Mu1CMed,Mu1CAvg,Mu1CStd"
                     + ",Mu2InTm,Mu2RtTm,Mu2CMed,Mu2CAvg,Mu2CStd"
                     + ",Mu3InTm,Mu3RtTm,Mu3CMed,Mu3CAvg,Mu3CStd"
                     + ",Mu4InTm,Mu4RtTm,Mu4CMed,Mu4CAvg,Mu4CStd"
                     + ",Mu5InTm,Mu5RtTm,Mu5CMed,Mu5CAvg,Mu5CStd"
                     + ",Mu6InTm,Mu6RtTm,Mu6CMed,Mu6CAvg,Mu6CStd")

        # step < 0: chaining; 
        # step = 0: quadratic probing; 
        # step > 0: linear probing
        for step in range(-1,stepN):
            # start with a return and step for each new row
            file.write(f"\n{step}")

            # test different operations in one row
            for i, op in enumerate(operations):
                hash_table = HashTable(op[0],op[1],step)

                #Insertion
                initial_time = time.time()
                index_list = hash_table.insert(keys)
                insertion_time = time.time() - initial_time
    
                #Retrieval
                initial_time = time.time()
                collision_list = hash_table.retrieve(keys)
                retrieval_time = time.time() - initial_time
    
                #Collision on every bucket index
                df = pandas.DataFrame({'index':index_list, 'col':collision_list})
                cdf = df.groupby(['index']).max()

                # one operation completed                
                file.write(f",{insertion_time:.10f},{retrieval_time:.10f},{cdf.col.median()},{cdf.col.mean()},{cdf.col.std()}")
                print(f"Done {i} operation with {step} step in {r} round.")

            # one row calculation completed            
            elapse_time = time.time() - round_initial_time
            print(f"Time {timedelta(seconds=elapse_time)} passed. {100*(step+2)/(stepN+1):.4f}% completed in {r} round.")
        
        # one round test completed
        file.close()

if __name__ == '__main__':
    main()
