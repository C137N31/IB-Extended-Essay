import matplotlib.pyplot as plt
import pandas as pd

def main():
    i1 = 9     # start row as Excel index-2
    i2 = 1001     # end row as Excel index-1
    od = pd.read_csv("/Project/Hash/Hash01.csv")

    plt.plot(od.Step[i1:i2], [od.Mo1RtTmMed[0] for i in range(i1,i2)], label = "Mo1RtTmMed-Chaining")
    plt.plot(od.Step[i1:i2], [od.Mo1RtTmMed[1] for i in range(i1,i2)], label = "Mo1RtTmMed-Quadratic")
    plt.plot(od.Step[i1:i2], od.Mo1RtTmMed[i1:i2], label = "Mo1RtTmMed")
    plt.plot(od.Step[i1:i2], od.Mo2RtTmMed[i1:i2], label = "Mo2RtTmMed")
    plt.plot(od.Step[i1:i2], od.Mo3RtTmMed[i1:i2], label = "Mo3RtTmMed")
    plt.plot(od.Step[i1:i2], od.Mo4RtTmMed[i1:i2], label = "Mo4RtTmMed")
    plt.plot(od.Step[i1:i2], od.Mo5RtTmMed[i1:i2], label = "Mo5RtTmMed")
    plt.plot(od.Step[i1:i2], od.Mo6RtTmMed[i1:i2], label = "Mo6RtTmMed")

    #plt.plot(od.Step[i1:i2], od.Mo1RtTmStd[i1:i2], label = "Mo1RtTmStd")
    #plt.plot(od.Step[i1:i2], od.Mo2RtTmStd[i1:i2], label = "Mo2RtTmStd")
    #plt.plot(od.Step[i1:i2], od.Mo3RtTmStd[i1:i2], label = "Mo3RtTmStd")
    #plt.plot(od.Step[i1:i2], od.Mo4RtTmStd[i1:i2], label = "Mo4RtTmStd")
    #plt.plot(od.Step[i1:i2], od.Mo5RtTmStd[i1:i2], label = "Mo5RtTmStd")
    #plt.plot(od.Step[i1:i2], od.Mo6RtTmStd[i1:i2], label = "Mo6RtTmStd")

    #plt.plot(od.Step[i1:i2], od.Mo1CMedAvg[i1:i2], label = "Mo1CMedAvg")
    #plt.plot(od.Step[i1:i2], od.Mo2CMedAvg[i1:i2], label = "Mo2CMedAvg")
    #plt.plot(od.Step[i1:i2], od.Mo3CMedAvg[i1:i2], label = "Mo3CMedAvg")
    #plt.plot(od.Step[i1:i2], od.Mo4CMedAvg[i1:i2], label = "Mo4CMedAvg")
    #plt.plot(od.Step[i1:i2], od.Mo5CMedAvg[i1:i2], label = "Mo5CMedAvg")
    #plt.plot(od.Step[i1:i2], od.Mo6CMedAvg[i1:i2], label = "Mo6CMedAvg")

    #plt.plot(od.Step[i1:i2], od.Mo1CMedStd[i1:i2], label = "Mo1CMedStd")
    #plt.plot(od.Step[i1:i2], od.Mo2CMedStd[i1:i2], label = "Mo2CMedStd")
    #plt.plot(od.Step[i1:i2], od.Mo3CMedStd[i1:i2], label = "Mo3CMedStd")
    #plt.plot(od.Step[i1:i2], od.Mo4CMedStd[i1:i2], label = "Mo4CMedStd")
    #plt.plot(od.Step[i1:i2], od.Mo5CMedStd[i1:i2], label = "Mo5CMedStd")
    #plt.plot(od.Step[i1:i2], od.Mo6CMedStd[i1:i2], label = "Mo6CMedStd")

    #plt.plot(od.Step[i1:i2], od.Mo1CStdAvg[i1:i2], label = "Mo1CStdAvg")
    #plt.plot(od.Step[i1:i2], od.Mo2CStdAvg[i1:i2], label = "Mo2CStdAvg")
    #plt.plot(od.Step[i1:i2], od.Mo3CStdAvg[i1:i2], label = "Mo3CStdAvg")
    #plt.plot(od.Step[i1:i2], od.Mo4CStdAvg[i1:i2], label = "Mo4CStdAvg")
    #plt.plot(od.Step[i1:i2], od.Mo5CStdAvg[i1:i2], label = "Mo5CStdAvg")
    #plt.plot(od.Step[i1:i2], od.Mo6CStdAvg[i1:i2], label = "Mo6CStdAvg")

    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()    
