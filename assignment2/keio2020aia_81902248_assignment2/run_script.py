##
from digits.digits_data import * 
from digits.digits_model import * 
from digits.digits_trainer import * 
##

##
def main():

    data = Digits_Data()
    #parameters are input dimension,array of hidden layers ,can be[100,60],output categories
    model = Digits_Model(784,[100,50],10) # hint: describe the shape of your simple neural network by a list of hidden layer sizes
    trainer = Digits_Trainer(data, model)
    trainer.train(0.01,10) # hint: choose a learning rate and the number of epochs to train for
    model.save_model()
##

##
if __name__ == "__main__":
    main()
##
