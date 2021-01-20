import pandas as pd

def main():
    nFile = 25 # total csv files
    R = 104 # total rows in a csv file
    
    for ds in range(9):
        rd = pd.concat([pd.read_csv(f"Data/Hash_D{str(ds).zfill(2)}-R{str(i).zfill(2)}.csv") for i in range(nFile)], ignore_index=True)        

        outd = pd.concat([pd.DataFrame([[rd.step.iloc[i], 
                                     
                                     rd.mod1InTm[i::R].median(), rd.mod1InTm[i::R].mean(), rd.mod1InTm[i::R].std(),
                                     rd.mod1RtTm[i::R].median(), rd.mod1RtTm[i::R].mean(), rd.mod1RtTm[i::R].std(),
                                     rd.mod1CMed[i::R].median(), rd.mod1CMed[i::R].mean(), rd.mod1CMed[i::R].std(),
                                     rd.mod1CMax[i::R].median(), rd.mod1CMax[i::R].mean(), rd.mod1CMax[i::R].std(),
                                     rd.mod1CAvg[i::R].median(), rd.mod1CAvg[i::R].mean(), rd.mod1CAvg[i::R].std(),
                                     rd.mod1CStd[i::R].median(), rd.mod1CStd[i::R].mean(), rd.mod1CStd[i::R].std(),

                                     rd.mod2InTm[i::R].median(), rd.mod2InTm[i::R].mean(), rd.mod2InTm[i::R].std(),
                                     rd.mod2RtTm[i::R].median(), rd.mod2RtTm[i::R].mean(), rd.mod2RtTm[i::R].std(),
                                     rd.mod2CMed[i::R].median(), rd.mod2CMed[i::R].mean(), rd.mod2CMed[i::R].std(),
                                     rd.mod2CMax[i::R].median(), rd.mod2CMax[i::R].mean(), rd.mod2CMax[i::R].std(),
                                     rd.mod2CAvg[i::R].median(), rd.mod2CAvg[i::R].mean(), rd.mod2CAvg[i::R].std(),
                                     rd.mod2CStd[i::R].median(), rd.mod2CStd[i::R].mean(), rd.mod2CStd[i::R].std(),

                                     rd.mod3InTm[i::R].median(), rd.mod3InTm[i::R].mean(), rd.mod3InTm[i::R].std(),
                                     rd.mod3RtTm[i::R].median(), rd.mod3RtTm[i::R].mean(), rd.mod3RtTm[i::R].std(),
                                     rd.mod3CMed[i::R].median(), rd.mod3CMed[i::R].mean(), rd.mod3CMed[i::R].std(),
                                     rd.mod3CMax[i::R].median(), rd.mod3CMax[i::R].mean(), rd.mod3CMax[i::R].std(),
                                     rd.mod3CAvg[i::R].median(), rd.mod3CAvg[i::R].mean(), rd.mod3CAvg[i::R].std(),
                                     rd.mod3CStd[i::R].median(), rd.mod3CStd[i::R].mean(), rd.mod3CStd[i::R].std(),

                                     rd.mod4InTm[i::R].median(), rd.mod4InTm[i::R].mean(), rd.mod4InTm[i::R].std(),
                                     rd.mod4RtTm[i::R].median(), rd.mod4RtTm[i::R].mean(), rd.mod4RtTm[i::R].std(),
                                     rd.mod4CMed[i::R].median(), rd.mod4CMed[i::R].mean(), rd.mod4CMed[i::R].std(),
                                     rd.mod4CMax[i::R].median(), rd.mod4CMax[i::R].mean(), rd.mod4CMax[i::R].std(),
                                     rd.mod4CAvg[i::R].median(), rd.mod4CAvg[i::R].mean(), rd.mod4CAvg[i::R].std(),
                                     rd.mod4CStd[i::R].median(), rd.mod4CStd[i::R].mean(), rd.mod4CStd[i::R].std(),

                                     rd.mod5InTm[i::R].median(), rd.mod5InTm[i::R].mean(), rd.mod5InTm[i::R].std(),
                                     rd.mod5RtTm[i::R].median(), rd.mod5RtTm[i::R].mean(), rd.mod5RtTm[i::R].std(),
                                     rd.mod5CMed[i::R].median(), rd.mod5CMed[i::R].mean(), rd.mod5CMed[i::R].std(),
                                     rd.mod5CMax[i::R].median(), rd.mod5CMax[i::R].mean(), rd.mod5CMax[i::R].std(),
                                     rd.mod5CAvg[i::R].median(), rd.mod5CAvg[i::R].mean(), rd.mod5CAvg[i::R].std(),
                                     rd.mod5CStd[i::R].median(), rd.mod5CStd[i::R].mean(), rd.mod5CStd[i::R].std(),

                                     rd.mod6InTm[i::R].median(), rd.mod6InTm[i::R].mean(), rd.mod6InTm[i::R].std(),
                                     rd.mod6RtTm[i::R].median(), rd.mod6RtTm[i::R].mean(), rd.mod6RtTm[i::R].std(),
                                     rd.mod6CMed[i::R].median(), rd.mod6CMed[i::R].mean(), rd.mod6CMed[i::R].std(),
                                     rd.mod6CMax[i::R].median(), rd.mod6CMax[i::R].mean(), rd.mod6CMax[i::R].std(),
                                     rd.mod6CAvg[i::R].median(), rd.mod6CAvg[i::R].mean(), rd.mod6CAvg[i::R].std(),
                                     rd.mod6CStd[i::R].median(), rd.mod6CStd[i::R].mean(), rd.mod6CStd[i::R].std(),

                                     rd.mul1InTm[i::R].median(), rd.mul1InTm[i::R].mean(), rd.mul1InTm[i::R].std(),
                                     rd.mul1RtTm[i::R].median(), rd.mul1RtTm[i::R].mean(), rd.mul1RtTm[i::R].std(),
                                     rd.mul1CMed[i::R].median(), rd.mul1CMed[i::R].mean(), rd.mul1CMed[i::R].std(),
                                     rd.mul1CMax[i::R].median(), rd.mul1CMax[i::R].mean(), rd.mul1CMax[i::R].std(),
                                     rd.mul1CAvg[i::R].median(), rd.mul1CAvg[i::R].mean(), rd.mul1CAvg[i::R].std(),
                                     rd.mul1CStd[i::R].median(), rd.mul1CStd[i::R].mean(), rd.mul1CStd[i::R].std(),

                                     rd.mul2InTm[i::R].median(), rd.mul2InTm[i::R].mean(), rd.mul2InTm[i::R].std(),
                                     rd.mul2RtTm[i::R].median(), rd.mul2RtTm[i::R].mean(), rd.mul2RtTm[i::R].std(),
                                     rd.mul2CMed[i::R].median(), rd.mul2CMed[i::R].mean(), rd.mul2CMed[i::R].std(),
                                     rd.mul2CMax[i::R].median(), rd.mul2CMax[i::R].mean(), rd.mul2CMax[i::R].std(),
                                     rd.mul2CAvg[i::R].median(), rd.mul2CAvg[i::R].mean(), rd.mul2CAvg[i::R].std(),
                                     rd.mul2CStd[i::R].median(), rd.mul2CStd[i::R].mean(), rd.mul2CStd[i::R].std(),

                                     rd.mul3InTm[i::R].median(), rd.mul3InTm[i::R].mean(), rd.mul3InTm[i::R].std(),
                                     rd.mul3RtTm[i::R].median(), rd.mul3RtTm[i::R].mean(), rd.mul3RtTm[i::R].std(),
                                     rd.mul3CMed[i::R].median(), rd.mul3CMed[i::R].mean(), rd.mul3CMed[i::R].std(),
                                     rd.mul3CMax[i::R].median(), rd.mul3CMax[i::R].mean(), rd.mul3CMax[i::R].std(),
                                     rd.mul3CAvg[i::R].median(), rd.mul3CAvg[i::R].mean(), rd.mul3CAvg[i::R].std(),
                                     rd.mul3CStd[i::R].median(), rd.mul3CStd[i::R].mean(), rd.mul3CStd[i::R].std(),

                                     rd.mul4InTm[i::R].median(), rd.mul4InTm[i::R].mean(), rd.mul4InTm[i::R].std(),
                                     rd.mul4RtTm[i::R].median(), rd.mul4RtTm[i::R].mean(), rd.mul4RtTm[i::R].std(),
                                     rd.mul4CMed[i::R].median(), rd.mul4CMed[i::R].mean(), rd.mul4CMed[i::R].std(),
                                     rd.mul4CMax[i::R].median(), rd.mul4CMax[i::R].mean(), rd.mul4CMax[i::R].std(),
                                     rd.mul4CAvg[i::R].median(), rd.mul4CAvg[i::R].mean(), rd.mul4CAvg[i::R].std(),
                                     rd.mul4CStd[i::R].median(), rd.mul4CStd[i::R].mean(), rd.mul4CStd[i::R].std(),

                                     rd.mul5InTm[i::R].median(), rd.mul5InTm[i::R].mean(), rd.mul5InTm[i::R].std(),
                                     rd.mul5RtTm[i::R].median(), rd.mul5RtTm[i::R].mean(), rd.mul5RtTm[i::R].std(),
                                     rd.mul5CMed[i::R].median(), rd.mul5CMed[i::R].mean(), rd.mul5CMed[i::R].std(),
                                     rd.mul5CMax[i::R].median(), rd.mul5CMax[i::R].mean(), rd.mul5CMax[i::R].std(),
                                     rd.mul5CAvg[i::R].median(), rd.mul5CAvg[i::R].mean(), rd.mul5CAvg[i::R].std(),
                                     rd.mul5CStd[i::R].median(), rd.mul5CStd[i::R].mean(), rd.mul5CStd[i::R].std(),

                                     rd.mul6InTm[i::R].median(), rd.mul6InTm[i::R].mean(), rd.mul6InTm[i::R].std(),
                                     rd.mul6RtTm[i::R].median(), rd.mul6RtTm[i::R].mean(), rd.mul6RtTm[i::R].std(),
                                     rd.mul6CMed[i::R].median(), rd.mul6CMed[i::R].mean(), rd.mul6CMed[i::R].std(),
                                     rd.mul6CMax[i::R].median(), rd.mul6CMax[i::R].mean(), rd.mul6CMax[i::R].std(),
                                     rd.mul6CAvg[i::R].median(), rd.mul6CAvg[i::R].mean(), rd.mul6CAvg[i::R].std(),
                                     rd.mul6CStd[i::R].median(), rd.mul6CStd[i::R].mean(), rd.mul6CStd[i::R].std()]],

                           columns=["step", 
                                    
                                    "mod1InTmMed", "mod1InTmAvg", "mod1InTmStd", 
                                    "mod1RtTmMed", "mod1RtTmAvg", "mod1RtTmStd", 
                                    "mod1CMedMed", "mod1CMedAvg", "mod1CMedStd", 
                                    "mod1CMaxMed", "mod1CMaxAvg", "mod1CMaxStd",
                                    "mod1CAvgMed", "mod1CAvgAvg", "mod1CAvgStd", 
                                    "mod1CStdMed", "mod1CStdAvg", "mod1CStdStd", 
                        
                                    "mod2InTmMed", "mod2InTmAvg", "mod2InTmStd", 
                                    "mod2RtTmMed", "mod2RtTmAvg", "mod2RtTmStd", 
                                    "mod2CMedMed", "mod2CMedAvg", "mod2CMedStd", 
                                    "mod2CMaxMed", "mod2CMaxAvg", "mod2CMaxStd",
                                    "mod2CAvgMed", "mod2CAvgAvg", "mod2CAvgStd", 
                                    "mod2CStdMed", "mod2CStdAvg", "mod2CStdStd", 
                        
                                    "mod3InTmMed", "mod3InTmAvg", "mod3InTmStd", 
                                    "mod3RtTmMed", "mod3RtTmAvg", "mod3RtTmStd", 
                                    "mod3CMedMed", "mod3CMedAvg", "mod3CMedStd", 
                                    "mod3CMaxMed", "mod3CMaxAvg", "mod3CMaxStd",
                                    "mod3CAvgMed", "mod3CAvgAvg", "mod3CAvgStd", 
                                    "mod3CStdMed", "mod3CStdAvg", "mod3CStdStd", 
                        
                                    "mod4InTmMed", "mod4InTmAvg", "mod4InTmStd", 
                                    "mod4RtTmMed", "mod4RtTmAvg", "mod4RtTmStd", 
                                    "mod4CMedMed", "mod4CMedAvg", "mod4CMedStd", 
                                    "mod4CMaxMed", "mod4CMaxAvg", "mod4CMaxStd",
                                    "mod4CAvgMed", "mod4CAvgAvg", "mod4CAvgStd", 
                                    "mod4CStdMed", "mod4CStdAvg", "mod4CStdStd", 
                        
                                    "mod5InTmMed", "mod5InTmAvg", "mod5InTmStd", 
                                    "mod5RtTmMed", "mod5RtTmAvg", "mod5RtTmStd", 
                                    "mod5CMedMed", "mod5CMedAvg", "mod5CMedStd", 
                                    "mod5CMaxMed", "mod5CMaxAvg", "mod5CMaxStd",
                                    "mod5CAvgMed", "mod5CAvgAvg", "mod5CAvgStd", 
                                    "mod5CStdMed", "mod5CStdAvg", "mod5CStdStd", 
                        
                                    "mod6InTmMed", "mod6InTmAvg", "mod6InTmStd", 
                                    "mod6RtTmMed", "mod6RtTmAvg", "mod6RtTmStd", 
                                    "mod6CMedMed", "mod6CMedAvg", "mod6CMedStd", 
                                    "mod6CMaxMed", "mod6CMaxAvg", "mod6CMaxStd",
                                    "mod6CAvgMed", "mod6CAvgAvg", "mod6CAvgStd", 
                                    "mod6CStdMed", "mod6CStdAvg", "mod6CStdStd", 
                        
                                    "mul1InTmMed", "mul1InTmAvg", "mul1InTmStd", 
                                    "mul1RtTmMed", "mul1RtTmAvg", "mul1RtTmStd", 
                                    "mul1CMedMed", "mul1CMedAvg", "mul1CMedStd", 
                                    "mul1CMaxMed", "mul1CMaxAvg", "mul1CMaxStd",
                                    "mul1CAvgMed", "mul1CAvgAvg", "mul1CAvgStd", 
                                    "mul1CStdMed", "mul1CStdAvg", "mul1CStdStd", 
                        
                                    "mul2InTmMed", "mul2InTmAvg", "mul2InTmStd", 
                                    "mul2RtTmMed", "mul2RtTmAvg", "mul2RtTmStd", 
                                    "mul2CMedMed", "mul2CMedAvg", "mul2CMedStd", 
                                    "mul2CMaxMed", "mul2CMaxAvg", "mul2CMaxStd",
                                    "mul2CAvgMed", "mul2CAvgAvg", "mul2CAvgStd", 
                                    "mul2CStdMed", "mul2CStdAvg", "mul2CStdStd", 
                        
                                    "mul3InTmMed", "mul3InTmAvg", "mul3InTmStd", 
                                    "mul3RtTmMed", "mul3RtTmAvg", "mul3RtTmStd", 
                                    "mul3CMedMed", "mul3CMedAvg", "mul3CMedStd", 
                                    "mul3CMaxMed", "mul3CMaxAvg", "mul3CMaxStd",
                                    "mul3CAvgMed", "mul3CAvgAvg", "mul3CAvgStd", 
                                    "mul3CStdMed", "mul3CStdAvg", "mul3CStdStd", 
                        
                                    "mul4InTmMed", "mul4InTmAvg", "mul4InTmStd", 
                                    "mul4RtTmMed", "mul4RtTmAvg", "mul4RtTmStd", 
                                    "mul4CMedMed", "mul4CMedAvg", "mul4CMedStd", 
                                    "mul4CMaxMed", "mul4CMaxAvg", "mul4CMaxStd",
                                    "mul4CAvgMed", "mul4CAvgAvg", "mul4CAvgStd", 
                                    "mul4CStdMed", "mul4CStdAvg", "mul4CStdStd", 
                        
                                    "mul5InTmMed", "mul5InTmAvg", "mul5InTmStd", 
                                    "mul5RtTmMed", "mul5RtTmAvg", "mul5RtTmStd", 
                                    "mul5CMedMed", "mul5CMedAvg", "mul5CMedStd", 
                                    "mul5CMaxMed", "mul5CMaxAvg", "mul5CMaxStd",
                                    "mul5CAvgMed", "mul5CAvgAvg", "mul5CAvgStd", 
                                    "mul5CStdMed", "mul5CStdAvg", "mul5CStdStd", 
                        
                                    "mul6InTmMed", "mul6InTmAvg", "mul6InTmStd", 
                                    "mul6RtTmMed", "mul6RtTmAvg", "mul6RtTmStd", 
                                    "mul6CMedMed", "mul6CMedAvg", "mul6CMedStd", 
                                    "mul6CMaxMed", "mul6CMaxAvg", "mul6CMaxStd",
                                    "mul6CAvgMed", "mul6CAvgAvg", "mul6CAvgStd", 
                                    "mul6CStdMed", "mul6CStdAvg", "mul6CStdStd"]
                                  ) for i in range(R)], ignore_index=True)

        outd.to_csv(f"Data/Hash_D{str(ds).zfill(2)}.csv", index=False)

if __name__ == '__main__':
    main()
