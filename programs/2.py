import pandas as pd

def main():
    dict= {"Age" : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
         "weight" : [15,19,20,23,25,26,27,28,30,34,36,38,40,42,45],}
    
    df = pd.DataFrame(dict)

    print("a) DataFrame:")
    print(df)

    print("b) first five records of the DataFrame:")
    print(df.head(5))

    print("c) last ten records of the DataFrame:")
    print(df.tail(10))

main()


