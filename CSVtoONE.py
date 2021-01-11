import pandas as pd

def main():
    nFile = 100 # total csv files
    R = 1001 # total rows in a csv file
    
    rd = pd.concat([pd.read_csv(f"/Project/Hash/Hash1{str(i).zfill(2)}.csv") for i in range(nFile)], ignore_index=True)        

    outd = pd.concat([pd.DataFrame([[rd.Step.iloc[i], 
                                     
                                     rd.Mo1InTm[i::R].median(), rd.Mo1InTm[i::R].mean(), rd.Mo1InTm[i::R].std(),
                                     rd.Mo1RtTm[i::R].median(), rd.Mo1RtTm[i::R].mean(), rd.Mo1RtTm[i::R].std(),
                                     rd.Mo1CMed[i::R].median(), rd.Mo1CMed[i::R].mean(), rd.Mo1CMed[i::R].std(),
                                     rd.Mo1CAvg[i::R].median(), rd.Mo1CAvg[i::R].mean(), rd.Mo1CAvg[i::R].std(),
                                     rd.Mo1CStd[i::R].median(), rd.Mo1CStd[i::R].mean(), rd.Mo1CStd[i::R].std(),

                                     rd.Mo2InTm[i::R].median(), rd.Mo2InTm[i::R].mean(), rd.Mo2InTm[i::R].std(),
                                     rd.Mo2RtTm[i::R].median(), rd.Mo2RtTm[i::R].mean(), rd.Mo2RtTm[i::R].std(),
                                     rd.Mo2CMed[i::R].median(), rd.Mo2CMed[i::R].mean(), rd.Mo2CMed[i::R].std(),
                                     rd.Mo2CAvg[i::R].median(), rd.Mo2CAvg[i::R].mean(), rd.Mo2CAvg[i::R].std(),
                                     rd.Mo2CStd[i::R].median(), rd.Mo2CStd[i::R].mean(), rd.Mo2CStd[i::R].std(),

                                     rd.Mo3InTm[i::R].median(), rd.Mo3InTm[i::R].mean(), rd.Mo3InTm[i::R].std(),
                                     rd.Mo3RtTm[i::R].median(), rd.Mo3RtTm[i::R].mean(), rd.Mo3RtTm[i::R].std(),
                                     rd.Mo3CMed[i::R].median(), rd.Mo3CMed[i::R].mean(), rd.Mo3CMed[i::R].std(),
                                     rd.Mo3CAvg[i::R].median(), rd.Mo3CAvg[i::R].mean(), rd.Mo3CAvg[i::R].std(),
                                     rd.Mo3CStd[i::R].median(), rd.Mo3CStd[i::R].mean(), rd.Mo3CStd[i::R].std(),

                                     rd.Mo4InTm[i::R].median(), rd.Mo4InTm[i::R].mean(), rd.Mo4InTm[i::R].std(),
                                     rd.Mo4RtTm[i::R].median(), rd.Mo4RtTm[i::R].mean(), rd.Mo4RtTm[i::R].std(),
                                     rd.Mo4CMed[i::R].median(), rd.Mo4CMed[i::R].mean(), rd.Mo4CMed[i::R].std(),
                                     rd.Mo4CAvg[i::R].median(), rd.Mo4CAvg[i::R].mean(), rd.Mo4CAvg[i::R].std(),
                                     rd.Mo4CStd[i::R].median(), rd.Mo4CStd[i::R].mean(), rd.Mo4CStd[i::R].std(),

                                     rd.Mo5InTm[i::R].median(), rd.Mo5InTm[i::R].mean(), rd.Mo5InTm[i::R].std(),
                                     rd.Mo5RtTm[i::R].median(), rd.Mo5RtTm[i::R].mean(), rd.Mo5RtTm[i::R].std(),
                                     rd.Mo5CMed[i::R].median(), rd.Mo5CMed[i::R].mean(), rd.Mo5CMed[i::R].std(),
                                     rd.Mo5CAvg[i::R].median(), rd.Mo5CAvg[i::R].mean(), rd.Mo5CAvg[i::R].std(),
                                     rd.Mo5CStd[i::R].median(), rd.Mo5CStd[i::R].mean(), rd.Mo5CStd[i::R].std(),

                                     rd.Mo6InTm[i::R].median(), rd.Mo6InTm[i::R].mean(), rd.Mo6InTm[i::R].std(),
                                     rd.Mo6RtTm[i::R].median(), rd.Mo6RtTm[i::R].mean(), rd.Mo6RtTm[i::R].std(),
                                     rd.Mo6CMed[i::R].median(), rd.Mo6CMed[i::R].mean(), rd.Mo6CMed[i::R].std(),
                                     rd.Mo6CAvg[i::R].median(), rd.Mo6CAvg[i::R].mean(), rd.Mo6CAvg[i::R].std(),
                                     rd.Mo6CStd[i::R].median(), rd.Mo6CStd[i::R].mean(), rd.Mo6CStd[i::R].std(),

                                     rd.Mu1InTm[i::R].median(), rd.Mu1InTm[i::R].mean(), rd.Mu1InTm[i::R].std(),
                                     rd.Mu1RtTm[i::R].median(), rd.Mu1RtTm[i::R].mean(), rd.Mu1RtTm[i::R].std(),
                                     rd.Mu1CMed[i::R].median(), rd.Mu1CMed[i::R].mean(), rd.Mu1CMed[i::R].std(),
                                     rd.Mu1CAvg[i::R].median(), rd.Mu1CAvg[i::R].mean(), rd.Mu1CAvg[i::R].std(),
                                     rd.Mu1CStd[i::R].median(), rd.Mu1CStd[i::R].mean(), rd.Mu1CStd[i::R].std(),

                                     rd.Mu2InTm[i::R].median(), rd.Mu2InTm[i::R].mean(), rd.Mu2InTm[i::R].std(),
                                     rd.Mu2RtTm[i::R].median(), rd.Mu2RtTm[i::R].mean(), rd.Mu2RtTm[i::R].std(),
                                     rd.Mu2CMed[i::R].median(), rd.Mu2CMed[i::R].mean(), rd.Mu2CMed[i::R].std(),
                                     rd.Mu2CAvg[i::R].median(), rd.Mu2CAvg[i::R].mean(), rd.Mu2CAvg[i::R].std(),
                                     rd.Mu2CStd[i::R].median(), rd.Mu2CStd[i::R].mean(), rd.Mu2CStd[i::R].std(),

                                     rd.Mu3InTm[i::R].median(), rd.Mu3InTm[i::R].mean(), rd.Mu3InTm[i::R].std(),
                                     rd.Mu3RtTm[i::R].median(), rd.Mu3RtTm[i::R].mean(), rd.Mu3RtTm[i::R].std(),
                                     rd.Mu3CMed[i::R].median(), rd.Mu3CMed[i::R].mean(), rd.Mu3CMed[i::R].std(),
                                     rd.Mu3CAvg[i::R].median(), rd.Mu3CAvg[i::R].mean(), rd.Mu3CAvg[i::R].std(),
                                     rd.Mu3CStd[i::R].median(), rd.Mu3CStd[i::R].mean(), rd.Mu3CStd[i::R].std(),

                                     rd.Mu4InTm[i::R].median(), rd.Mu4InTm[i::R].mean(), rd.Mu4InTm[i::R].std(),
                                     rd.Mu4RtTm[i::R].median(), rd.Mu4RtTm[i::R].mean(), rd.Mu4RtTm[i::R].std(),
                                     rd.Mu4CMed[i::R].median(), rd.Mu4CMed[i::R].mean(), rd.Mu4CMed[i::R].std(),
                                     rd.Mu4CAvg[i::R].median(), rd.Mu4CAvg[i::R].mean(), rd.Mu4CAvg[i::R].std(),
                                     rd.Mu4CStd[i::R].median(), rd.Mu4CStd[i::R].mean(), rd.Mu4CStd[i::R].std(),

                                     rd.Mu5InTm[i::R].median(), rd.Mu5InTm[i::R].mean(), rd.Mu5InTm[i::R].std(),
                                     rd.Mu5RtTm[i::R].median(), rd.Mu5RtTm[i::R].mean(), rd.Mu5RtTm[i::R].std(),
                                     rd.Mu5CMed[i::R].median(), rd.Mu5CMed[i::R].mean(), rd.Mu5CMed[i::R].std(),
                                     rd.Mu5CAvg[i::R].median(), rd.Mu5CAvg[i::R].mean(), rd.Mu5CAvg[i::R].std(),
                                     rd.Mu5CStd[i::R].median(), rd.Mu5CStd[i::R].mean(), rd.Mu5CStd[i::R].std(),

                                     rd.Mu6InTm[i::R].median(), rd.Mu6InTm[i::R].mean(), rd.Mu6InTm[i::R].std(),
                                     rd.Mu6RtTm[i::R].median(), rd.Mu6RtTm[i::R].mean(), rd.Mu6RtTm[i::R].std(),
                                     rd.Mu6CMed[i::R].median(), rd.Mu6CMed[i::R].mean(), rd.Mu6CMed[i::R].std(),
                                     rd.Mu6CAvg[i::R].median(), rd.Mu6CAvg[i::R].mean(), rd.Mu6CAvg[i::R].std(),
                                     rd.Mu6CStd[i::R].median(), rd.Mu6CStd[i::R].mean(), rd.Mu6CStd[i::R].std()]],

                           columns=["Step", 
                                    
                                    "Mo1InTmMed", "Mo1InTmAvg", "Mo1InTmStd", 
                                    "Mo1RtTmMed", "Mo1RtTmAvg", "Mo1RtTmStd", 
                                    "Mo1CMedMed", "Mo1CMedAvg", "Mo1CMedStd", 
                                    "Mo1CAvgMed", "Mo1CAvgAvg", "Mo1CAvgStd", 
                                    "Mo1CStdMed", "Mo1CStdAvg", "Mo1CStdStd", 
                        
                                    "Mo2InTmMed", "Mo2InTmAvg", "Mo2InTmStd", 
                                    "Mo2RtTmMed", "Mo2RtTmAvg", "Mo2RtTmStd", 
                                    "Mo2CMedMed", "Mo2CMedAvg", "Mo2CMedStd", 
                                    "Mo2CAvgMed", "Mo2CAvgAvg", "Mo2CAvgStd", 
                                    "Mo2CStdMed", "Mo2CStdAvg", "Mo2CStdStd", 
                        
                                    "Mo3InTmMed", "Mo3InTmAvg", "Mo3InTmStd", 
                                    "Mo3RtTmMed", "Mo3RtTmAvg", "Mo3RtTmStd", 
                                    "Mo3CMedMed", "Mo3CMedAvg", "Mo3CMedStd", 
                                    "Mo3CAvgMed", "Mo3CAvgAvg", "Mo3CAvgStd", 
                                    "Mo3CStdMed", "Mo3CStdAvg", "Mo3CStdStd", 
                        
                                    "Mo4InTmMed", "Mo4InTmAvg", "Mo4InTmStd", 
                                    "Mo4RtTmMed", "Mo4RtTmAvg", "Mo4RtTmStd", 
                                    "Mo4CMedMed", "Mo4CMedAvg", "Mo4CMedStd", 
                                    "Mo4CAvgMed", "Mo4CAvgAvg", "Mo4CAvgStd", 
                                    "Mo4CStdMed", "Mo4CStdAvg", "Mo4CStdStd", 
                        
                                    "Mo5InTmMed", "Mo5InTmAvg", "Mo5InTmStd", 
                                    "Mo5RtTmMed", "Mo5RtTmAvg", "Mo5RtTmStd", 
                                    "Mo5CMedMed", "Mo5CMedAvg", "Mo5CMedStd", 
                                    "Mo5CAvgMed", "Mo5CAvgAvg", "Mo5CAvgStd", 
                                    "Mo5CStdMed", "Mo5CStdAvg", "Mo5CStdStd", 
                        
                                    "Mo6InTmMed", "Mo6InTmAvg", "Mo6InTmStd", 
                                    "Mo6RtTmMed", "Mo6RtTmAvg", "Mo6RtTmStd", 
                                    "Mo6CMedMed", "Mo6CMedAvg", "Mo6CMedStd", 
                                    "Mo6CAvgMed", "Mo6CAvgAvg", "Mo6CAvgStd", 
                                    "Mo6CStdMed", "Mo6CStdAvg", "Mo6CStdStd", 
                        
                                    "Mu1InTmMed", "Mu1InTmAvg", "Mu1InTmStd", 
                                    "Mu1RtTmMed", "Mu1RtTmAvg", "Mu1RtTmStd", 
                                    "Mu1CMedMed", "Mu1CMedAvg", "Mu1CMedStd", 
                                    "Mu1CAvgMed", "Mu1CAvgAvg", "Mu1CAvgStd", 
                                    "Mu1CStdMed", "Mu1CStdAvg", "Mu1CStdStd", 
                        
                                    "Mu2InTmMed", "Mu2InTmAvg", "Mu2InTmStd", 
                                    "Mu2RtTmMed", "Mu2RtTmAvg", "Mu2RtTmStd", 
                                    "Mu2CMedMed", "Mu2CMedAvg", "Mu2CMedStd", 
                                    "Mu2CAvgMed", "Mu2CAvgAvg", "Mu2CAvgStd", 
                                    "Mu2CStdMed", "Mu2CStdAvg", "Mu2CStdStd", 
                        
                                    "Mu3InTmMed", "Mu3InTmAvg", "Mu3InTmStd", 
                                    "Mu3RtTmMed", "Mu3RtTmAvg", "Mu3RtTmStd", 
                                    "Mu3CMedMed", "Mu3CMedAvg", "Mu3CMedStd", 
                                    "Mu3CAvgMed", "Mu3CAvgAvg", "Mu3CAvgStd", 
                                    "Mu3CStdMed", "Mu3CStdAvg", "Mu3CStdStd", 
                        
                                    "Mu4InTmMed", "Mu4InTmAvg", "Mu4InTmStd", 
                                    "Mu4RtTmMed", "Mu4RtTmAvg", "Mu4RtTmStd", 
                                    "Mu4CMedMed", "Mu4CMedAvg", "Mu4CMedStd", 
                                    "Mu4CAvgMed", "Mu4CAvgAvg", "Mu4CAvgStd", 
                                    "Mu4CStdMed", "Mu4CStdAvg", "Mu4CStdStd", 
                        
                                    "Mu5InTmMed", "Mu5InTmAvg", "Mu5InTmStd", 
                                    "Mu5RtTmMed", "Mu5RtTmAvg", "Mu5RtTmStd", 
                                    "Mu5CMedMed", "Mu5CMedAvg", "Mu5CMedStd", 
                                    "Mu5CAvgMed", "Mu5CAvgAvg", "Mu5CAvgStd", 
                                    "Mu5CStdMed", "Mu5CStdAvg", "Mu5CStdStd", 
                        
                                    "Mu6InTmMed", "Mu6InTmAvg", "Mu6InTmStd", 
                                    "Mu6RtTmMed", "Mu6RtTmAvg", "Mu6RtTmStd", 
                                    "Mu6CMedMed", "Mu6CMedAvg", "Mu6CMedStd", 
                                    "Mu6CAvgMed", "Mu6CAvgAvg", "Mu6CAvgStd", 
                                    "Mu6CStdMed", "Mu6CStdAvg", "Mu6CStdStd"]
                                  ) for i in range(R)], ignore_index=True)

    outd.to_csv("/Project/Hash/Hash01.csv", index=False)

if __name__ == '__main__':
    main()
