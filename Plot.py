import matplotlib.pyplot as plt
import pandas as pd
from math import floor

def main():
    nFile = 9  # total csv files (different distribution dataset)
    R = 104   # total rows in a csv file
    
    i1 = 0     # start row as Excel index-2
    i2 = 5   # end row as Excel index-1

    rd = pd.concat([pd.read_csv(f"Data/Hash_D{str(i).zfill(2)}.csv") for i in range(nFile)], ignore_index=True)        
    
    #################################################
    """
    #compare -4,-3,-2,-1,0 with different distribution: X-dataset even distribution, Y-retrival average time
    i1 = 0
    i2 = 5
    for j in range(i1,i2):
        #need to change mod1-6 and mul1-6 manually
        plt.plot([i for i in range(nFile)], rd.mod1RtTmAvg[j::R], label = f"mod1RtTmAvg-{j-4}")
        plt.plot([i for i in range(nFile)], rd.mul1RtTmAvg[j::R], label = f"mul1RtTmAvg-{j-4}", linestyle = ":")
    """
    #################################################
    """
    #compare -4,-3,-2,-1,0 with different distribution: X-dataset even distribution, Y-retrival average time
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
    fig.suptitle('compare -4,-3,-2,-1,0 with different distribution')

    i1 = 0
    i2 = 5

    ax1.set_title("load factor=0.001")
    for j in range(i1,i2):
        #need to change mod1-6 and mul1-6 manually
        ax1.plot([i for i in range(nFile)], rd.mod1RtTmAvg[j::R], color = 'blue')
        ax1.plot([i for i in range(nFile)], rd.mul1RtTmAvg[j::R], linestyle = ":", color = 'blue')

    ax2.set_title("load factor=0.5")
    for j in range(i1,i2):
        #need to change mod1-6 and mul1-6 manually
        ax2.plot([i for i in range(nFile)], rd.mod2RtTmAvg[j::R], color = 'cyan')
        ax2.plot([i for i in range(nFile)], rd.mul2RtTmAvg[j::R], linestyle = ":", color = 'cyan')

    ax3.set_title("load factor=0.899")
    for j in range(i1,i2):
        #need to change mod1-6 and mul1-6 manually
        ax3.plot([i for i in range(nFile)], rd.mod3RtTmAvg[j::R], color = 'green')
        ax3.plot([i for i in range(nFile)], rd.mul3RtTmAvg[j::R], linestyle = ":", color = 'green')

    ax4.set_title("load factor=0.959")
    for j in range(i1,i2):
        #need to change mod1-6 and mul1-6 manually
        ax4.plot([i for i in range(nFile)], rd.mod4RtTmAvg[j::R], color = 'magenta')
        ax4.plot([i for i in range(nFile)], rd.mul4RtTmAvg[j::R], linestyle = ":", color = 'magenta')

    ax5.set_title("load factor=0.996")
    for j in range(i1,i2):
        #need to change mod1-6 and mul1-6 manually
        ax5.plot([i for i in range(nFile)], rd.mod5RtTmAvg[j::R], color = 'red')
        ax5.plot([i for i in range(nFile)], rd.mul5RtTmAvg[j::R], linestyle = ":", color = 'red')

    ax6.set_title("load factor=0.999")
    for j in range(i1,i2):
        #need to change mod1-6 and mul1-6 manually
        ax6.plot([i for i in range(nFile)], rd.mod6RtTmAvg[j::R], color = 'black')
        ax6.plot([i for i in range(nFile)], rd.mul6RtTmAvg[j::R], linestyle = ":", color = 'black')

    for axi in fig.get_axes():
        axi.label_outer()
    """
    #################################################
    """
    #compare -4,-3,-2,-1,0 with different bucket size and hash function combination: X-dataset even distribution, Y-retrival average time
    j = 0 # 5 # need to change j manually to get different step
    plt.plot([i for i in range(nFile)], rd.mod1RtTmAvg[j::R], label = f"mod1RtTmAvg-{j-4}", color = 'blue')
    plt.plot([i for i in range(nFile)], rd.mod2RtTmAvg[j::R], label = f"mod2RtTmAvg-{j-4}", color = 'cyan')
    plt.plot([i for i in range(nFile)], rd.mod3RtTmAvg[j::R], label = f"mod3RtTmAvg-{j-4}", color = 'green')
    plt.plot([i for i in range(nFile)], rd.mod4RtTmAvg[j::R], label = f"mod4RtTmAvg-{j-4}", color = 'magenta')
    plt.plot([i for i in range(nFile)], rd.mod5RtTmAvg[j::R], label = f"mod5RtTmAvg-{j-4}", color = 'red')
    plt.plot([i for i in range(nFile)], rd.mod6RtTmAvg[j::R], label = f"mod6RtTmAvg-{j-4}", color = 'black')
    plt.plot([i for i in range(nFile)], rd.mul1RtTmAvg[j::R], label = f"mul1RtTmAvg-{j-4}", linestyle = ":", color = 'blue')
    plt.plot([i for i in range(nFile)], rd.mul2RtTmAvg[j::R], label = f"mul2RtTmAvg-{j-4}", linestyle = ":", color = 'cyan')
    plt.plot([i for i in range(nFile)], rd.mul3RtTmAvg[j::R], label = f"mul3RtTmAvg-{j-4}", linestyle = ":", color = 'green')
    plt.plot([i for i in range(nFile)], rd.mul4RtTmAvg[j::R], label = f"mul4RtTmAvg-{j-4}", linestyle = ":", color = 'magenta')
    plt.plot([i for i in range(nFile)], rd.mul5RtTmAvg[j::R], label = f"mul5RtTmAvg-{j-4}", linestyle = ":", color = 'red')
    plt.plot([i for i in range(nFile)], rd.mul6RtTmAvg[j::R], label = f"mul6RtTmAvg-{j-4}", linestyle = ":", color = 'black')
    """
    #################################################
    """
    #compare -4,-3,-2,-1,0 with different bucket size and hash function combination: X-dataset even distribution, Y-retrival average time
    fig, ax = plt.subplots(3, 2)
    fig.suptitle('compare -4,-3,-2,-1,0 with different bucket size and hash function combination')

    # need to change j manually to get different step
    for j in range(6):
        ix = floor(j/2)
        iy = j%2

        if j == 0 :
            ax[ix,iy].set_title("double hash multiplicative function")
            ax[ix,iy].set_ylim([0.015, 0.063])
        elif j == 1 :
            ax[ix,iy].set_title("double hash modular function")
            ax[ix,iy].set_ylim([0.015, 0.063])
        elif j == 2 :
            ax[ix,iy].set_title("faster quadratic probing")
            ax[ix,iy].set_ylim([0, 0.42])
        elif j == 3 :
            ax[ix,iy].set_title("classic quadratic probing")
            ax[ix,iy].set_ylim([0, 0.42])
        elif j == 4 :
            ax[ix,iy].set_title("seperate chaining")
        elif j == 5 :
            ax[ix,iy].set_title("linear probing")
    
        ax[ix,iy].plot([i for i in range(nFile)], rd.mod1RtTmAvg[j::R], color = 'blue')
        ax[ix,iy].plot([i for i in range(nFile)], rd.mod2RtTmAvg[j::R], color = 'cyan')
        ax[ix,iy].plot([i for i in range(nFile)], rd.mod3RtTmAvg[j::R], color = 'green')
        ax[ix,iy].plot([i for i in range(nFile)], rd.mod4RtTmAvg[j::R], color = 'magenta')
        ax[ix,iy].plot([i for i in range(nFile)], rd.mod5RtTmAvg[j::R], color = 'red')
        ax[ix,iy].plot([i for i in range(nFile)], rd.mod6RtTmAvg[j::R], color = 'black')
        ax[ix,iy].plot([i for i in range(nFile)], rd.mul1RtTmAvg[j::R], linestyle = ":", color = 'blue')
        ax[ix,iy].plot([i for i in range(nFile)], rd.mul2RtTmAvg[j::R], linestyle = ":", color = 'cyan')
        ax[ix,iy].plot([i for i in range(nFile)], rd.mul3RtTmAvg[j::R], linestyle = ":", color = 'green')
        ax[ix,iy].plot([i for i in range(nFile)], rd.mul4RtTmAvg[j::R], linestyle = ":", color = 'magenta')
        ax[ix,iy].plot([i for i in range(nFile)], rd.mul5RtTmAvg[j::R], linestyle = ":", color = 'red')
        ax[ix,iy].plot([i for i in range(nFile)], rd.mul6RtTmAvg[j::R], linestyle = ":", color = 'black')
    """
    #################################################
    """
    #compare 1-99 with different distribution: X-step 1-99, Y-retrival average time
    i1 = 5
    i2 = 104
    for i in range(nFile):
        # need to change mod1-6 and mul1-6 manually
        plt.plot(rd.step[i1+i*R:i2+i*R], rd.mod1RtTmAvg[i1+i*R:i2+i*R], label = f"mod1RtTmAvg{i}")
        plt.plot(rd.step[i1+i*R:i2+i*R], rd.mul1RtTmAvg[i1+i*R:i2+i*R], label = f"mul1RtTmAvg{i}", linestyle = ":")
    """
    #################################################
    """
    #compare 1-99 with different distribution: X-step 1-99, Y-retrival average time
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
    fig.suptitle('compare 1-99 with different distribution')

    i1 = 5
    i2 = 104

    ax1.set_title("load factor=0.001")
    for i in range(nFile):
        # need to change mod1-6 and mul1-6 manually
        ax1.plot(rd.step[i1+i*R:i2+i*R], rd.mod1RtTmAvg[i1+i*R:i2+i*R], label = f"mod1RtTmAvg{i}", color = 'blue')
        ax1.plot(rd.step[i1+i*R:i2+i*R], rd.mul1RtTmAvg[i1+i*R:i2+i*R], label = f"mul1RtTmAvg{i}", linestyle = ":", color = 'blue')

    ax2.set_title("load factor=0.5")
    for i in range(nFile):
        # need to change mod1-6 and mul1-6 manually
        ax2.plot(rd.step[i1+i*R:i2+i*R], rd.mod2RtTmAvg[i1+i*R:i2+i*R], color = 'cyan')
        ax2.plot(rd.step[i1+i*R:i2+i*R], rd.mul2RtTmAvg[i1+i*R:i2+i*R], linestyle = ":", color = 'cyan')

    ax3.set_title("load factor=0.899")
    for i in range(nFile):
        # need to change mod1-6 and mul1-6 manually
        ax3.plot(rd.step[i1+i*R:i2+i*R], rd.mod3RtTmAvg[i1+i*R:i2+i*R], color = 'green')
        ax3.plot(rd.step[i1+i*R:i2+i*R], rd.mul3RtTmAvg[i1+i*R:i2+i*R], linestyle = ":", color = 'green')

    ax4.set_title("load factor=0.959")
    for i in range(nFile):
        # need to change mod1-6 and mul1-6 manually
        ax4.plot(rd.step[i1+i*R:i2+i*R], rd.mod4RtTmAvg[i1+i*R:i2+i*R], color = 'magenta')
        ax4.plot(rd.step[i1+i*R:i2+i*R], rd.mul4RtTmAvg[i1+i*R:i2+i*R], linestyle = ":", color = 'magenta')

    ax5.set_title("load factor=0.996")
    for i in range(nFile):
        # need to change mod1-6 and mul1-6 manually
        ax5.plot(rd.step[i1+i*R:i2+i*R], rd.mod5RtTmAvg[i1+i*R:i2+i*R], color = 'red')
        ax5.plot(rd.step[i1+i*R:i2+i*R], rd.mul5RtTmAvg[i1+i*R:i2+i*R], linestyle = ":", color = 'red')

    ax6.set_title("load factor=0.999")
    for i in range(nFile):
        # need to change mod1-6 and mul1-6 manually
        ax6.plot(rd.step[i1+i*R:i2+i*R], rd.mod6RtTmAvg[i1+i*R:i2+i*R], color = 'black')
        ax6.plot(rd.step[i1+i*R:i2+i*R], rd.mul6RtTmAvg[i1+i*R:i2+i*R], linestyle = ":", color = 'black')

    for axi in fig.get_axes():
        axi.label_outer()
    """
    #################################################
    """
    #compare 1-99 with different bucket size and hash function combination: X-step 1-99, Y-retrival average time
    i1 = 10
    i2 = 104
    i = 0 # nFile # need to change i manually to get different distribution
    plt.plot(rd.step[i1+i*R:i2+i*R], rd.mod1RtTmAvg[i1+i*R:i2+i*R], label = f"mod1RtTmAvg{i}", color = 'blue')
    plt.plot(rd.step[i1+i*R:i2+i*R], rd.mod2RtTmAvg[i1+i*R:i2+i*R], label = f"mod2RtTmAvg{i}", color = 'cyan')
    plt.plot(rd.step[i1+i*R:i2+i*R], rd.mod3RtTmAvg[i1+i*R:i2+i*R], label = f"mod3RtTmAvg{i}", color = 'green')
    plt.plot(rd.step[i1+i*R:i2+i*R], rd.mod4RtTmAvg[i1+i*R:i2+i*R], label = f"mod4RtTmAvg{i}", color = 'magenta')
    plt.plot(rd.step[i1+i*R:i2+i*R], rd.mod5RtTmAvg[i1+i*R:i2+i*R], label = f"mod5RtTmAvg{i}", color = 'red')
    plt.plot(rd.step[i1+i*R:i2+i*R], rd.mod6RtTmAvg[i1+i*R:i2+i*R], label = f"mod6RtTmAvg{i}", color = 'black')
    plt.plot(rd.step[i1+i*R:i2+i*R], rd.mul1RtTmAvg[i1+i*R:i2+i*R], label = f"mul1RtTmAvg{i}", linestyle = ":", color = 'blue')
    plt.plot(rd.step[i1+i*R:i2+i*R], rd.mul2RtTmAvg[i1+i*R:i2+i*R], label = f"mul2RtTmAvg{i}", linestyle = ":", color = 'cyan')
    plt.plot(rd.step[i1+i*R:i2+i*R], rd.mul3RtTmAvg[i1+i*R:i2+i*R], label = f"mul3RtTmAvg{i}", linestyle = ":", color = 'green')
    plt.plot(rd.step[i1+i*R:i2+i*R], rd.mul4RtTmAvg[i1+i*R:i2+i*R], label = f"mul4RtTmAvg{i}", linestyle = ":", color = 'magenta')
    plt.plot(rd.step[i1+i*R:i2+i*R], rd.mul5RtTmAvg[i1+i*R:i2+i*R], label = f"mul5RtTmAvg{i}", linestyle = ":", color = 'red')
    plt.plot(rd.step[i1+i*R:i2+i*R], rd.mul6RtTmAvg[i1+i*R:i2+i*R], label = f"mul6RtTmAvg{i}", linestyle = ":", color = 'black')
    """
    #################################################
    
    fig, ax = plt.subplots(3, 3)
    fig.suptitle('compare 1-99 with different bucket size and hash function combination')

    i1 = 10
    i2 = 104

    # nFile # need to change i manually to get different distribution
    for i in range(nFile):
        ix = floor(i/3)
        iy = i%3

        if i == 0 :
            ax[ix,iy].set_title("extremely uneven distribution-500")
            ax[ix,iy].set_ylim([0, 3.3])
        elif i == 1 :
            ax[ix,iy].set_title("very uneven distribution-1000")
            ax[ix,iy].set_ylim([0, 3.3])
        elif i == 2 :
            ax[ix,iy].set_title("fairly uneven distribution-2500")
            ax[ix,iy].set_ylim([0, 3.3])
        elif i == 3 :
            ax[ix,iy].set_title("little uneven distribution-5000")
            ax[ix,iy].set_ylim([0, 1.7])
        elif i == 4 :
            ax[ix,iy].set_title("uneven distribution-7500")
            ax[ix,iy].set_ylim([0, 1.7])
        elif i == 5 :
            ax[ix,iy].set_title("distribution-10000")
            ax[ix,iy].set_ylim([0, 1.7])
        elif i == 6 :
            ax[ix,iy].set_title("even distribution-20000")
            ax[ix,iy].set_ylim([0, 0.3])
        elif i == 7 :
            ax[ix,iy].set_title("very even distribution-40000")
            ax[ix,iy].set_ylim([0, 0.3])
        elif i == 8 :
            ax[ix,iy].set_title("extremely even distribution-20000000")
            ax[ix,iy].set_ylim([0, 0.3])

        ax[ix,iy].plot(rd.step[i1+i*R:i2+i*R], rd.mod1RtTmAvg[i1+i*R:i2+i*R], color = 'blue')
        ax[ix,iy].plot(rd.step[i1+i*R:i2+i*R], rd.mod2RtTmAvg[i1+i*R:i2+i*R], color = 'cyan')
        ax[ix,iy].plot(rd.step[i1+i*R:i2+i*R], rd.mod3RtTmAvg[i1+i*R:i2+i*R], color = 'green')
        ax[ix,iy].plot(rd.step[i1+i*R:i2+i*R], rd.mod4RtTmAvg[i1+i*R:i2+i*R], color = 'magenta')
        ax[ix,iy].plot(rd.step[i1+i*R:i2+i*R], rd.mod5RtTmAvg[i1+i*R:i2+i*R], color = 'red')
        ax[ix,iy].plot(rd.step[i1+i*R:i2+i*R], rd.mod6RtTmAvg[i1+i*R:i2+i*R], color = 'black')
        ax[ix,iy].plot(rd.step[i1+i*R:i2+i*R], rd.mul1RtTmAvg[i1+i*R:i2+i*R], linestyle = ":", color = 'blue')
        ax[ix,iy].plot(rd.step[i1+i*R:i2+i*R], rd.mul2RtTmAvg[i1+i*R:i2+i*R], linestyle = ":", color = 'cyan')
        ax[ix,iy].plot(rd.step[i1+i*R:i2+i*R], rd.mul3RtTmAvg[i1+i*R:i2+i*R], linestyle = ":", color = 'green')
        ax[ix,iy].plot(rd.step[i1+i*R:i2+i*R], rd.mul4RtTmAvg[i1+i*R:i2+i*R], linestyle = ":", color = 'magenta')
        ax[ix,iy].plot(rd.step[i1+i*R:i2+i*R], rd.mul5RtTmAvg[i1+i*R:i2+i*R], linestyle = ":", color = 'red')
        ax[ix,iy].plot(rd.step[i1+i*R:i2+i*R], rd.mul6RtTmAvg[i1+i*R:i2+i*R], linestyle = ":", color = 'black')
    
    for axi in fig.get_axes():
        axi.label_outer()
    
    #################################################
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
