   okay so ig i'll explain whatever i did





1)csvfile.py

   pandas:this is a data analyzing library

   a function csv is defined with df as its parameter
   in the function:
         1)a new column to the df data is added named Mega Evolution with its content being Yes and No depending on if the pokemon is MegaEvolved or not.
The fact that the Name contained the term Mega in it if the pokemon was mega evolved is used to make this column....Meganium being the exception was dealt seperately.
         2)2 lists keepem and numstuff are created where the names of columns i want are put in and then get concatenated to a new data file called dfp.
         3)this function returns dfp(the processed csv file)

   the parameter df represents the read csv file.
   fp(main.py):this is the file path of the CSV dataset.
   df=pd.read_csv(fp):reads the CSV file and stores it in df
   dfp=csv(df):gives the processed table.










2)pkmnmastertraining.py

   from sklearn.model_selection import train_test_split ====to split data into training and testing parts
   from sklearn.linear_model import LogisticRegression ====for making the lr model

   train_pkmn(df) function:

         1)A list named drop is created with the column heading names which are not supposed to be used while training the data which is the index numbering and Name(of pokemon).The list is dropped from the entered parameter i.e df

         2)Two seperate dataframes x and y are created where x has all the rest of the values except the column of Mega Evolution whereas y has only Mega evolution

         3)xtr-training x, xte-testing x, ytr-training y, yte-testing y, the data is spilted with training testing spilt being 80-20.Stratify parameter is used to ensure the same ratio of mega and non mega in the splited parts as there was in the overall data to avoid errors.

         4)in a vriable named "trainer" a LR model is assigned. LR models make an algorithm which are supposed to predict binary outcomes(yes and no).max iterations is set 2000 means it updates it algorithm 2000 times. Why 2000? below it i was getting convergence warning which means the model couldnt fully learn cuz the different algos were not converging in less changes of the algo.

         5).fit(x,y) is used to train the model trainer with x as input data and y as the result.

         6)the model trainer and the testing datas are returned now.






4)modelcheck.py

   import matplotlib.pyplot as plt---plotting
   import seaborn as sns---Enhances visualizations.
   from sklearn.metrics import confusion_matrix, roc_curve, auc, precision_recall_curve


   evalmod(trainer, xte, yte)
            ytb = testing data with yes and no converted to 1s and 0s
            yhat = predicted data for xte inputs with yes and no converted to 1s and 0s
            making CONFUSION MATRIX
            ROC:if the model supports probability predictions it calculates the ROC curve and plots it









5)main.py

   imports functions from every other files
         1)df stores the given pokemon csv file in a pandas dataframe which is when sent through csv function to get dfp.
         2)trainer model and testing datas are taken by sending dfp through the train_pkmn function.
         3)then evalmod gives the required curves.
         4)then makes a new dataframe named predictions which has the names of the testing data and their predictions.
         5)this dataframe is sent to a csv file named final_predictions.csv which can be accessed now
