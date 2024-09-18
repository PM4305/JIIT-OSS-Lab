import numpy as np
import matplotlib.pyplot as plt
def totalsales(a,l):
    print('Total units sold across all weeks:')
    for i in range(4):
        print(l[i],': ',a[:,i].sum())
    print('\nTotal sales per week:')
    for i in range(4):
        print('Week 1: ',a[i,:].sum())
    print('\nAverage sales per product for all weeks:')
    for i in range(4):
        print(l[i],': ',a[:,i].sum()/4)
    print('\nPlots')
    k=['red','blue','green','black']
    x=np.arange(1,5)
    for i in range(4):
        y=a[:,i]
        plt.plot(x,y,color=k[i],label=l[i])
    plt.title('Plots')
    plt.xlabel('Weeks')
    plt.ylabel('Sales')
    plt.legend()
    plt.show()
    print("Worst selling: ",a.min())
    print("Best Selling: ",a.max())
    x=np.arange(1,5)
    y=[a[:,0].sum(),a[:,1].sum(),a[:,2].sum(),a[:,3].sum()]
    for i in range(4):
        plt.bar(x[i],height=y[i],width=1,label=l[i])
        plt.title('Total Sales of each category')
    plt.ylabel('Total Sales')
    plt.xlabel('Categories')
    plt.legend()
    plt.show()
l=[[120,500,230,75,45],[130,520,210,80,40],[125,530,220,70,50],[140,540,200,90,60]]
arr=np.array(l)
p=['Electronics','Groceries','Clothing','Furniture','Stationary']
totalsales(arr,p)