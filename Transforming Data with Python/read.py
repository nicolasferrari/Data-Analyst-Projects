# The load_data function, will read the file hn_stories.csv into a Pandas Dataframe make some process and print them.  This database has 4 columns with no header row. Then I use the columns method of Pandas to generate the header for the 4 columns

def load_data():
    import pandas as pd
    hn_stories = pd.read_csv("hn_stories.csv")
    hn_stories.columns = ['submission_time','upvotes','url','headline']
    print(hn_stories)
    return hn_stories 
if __name__ == "__main__": 
    load_data()

    








