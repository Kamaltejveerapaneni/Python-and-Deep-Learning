from first import model,x_test,y_test,batch_size
c = model.load_weights("C:\\Users\kamal\PycharmProjects\DeepLearning_SourceCode6\\abc.h5")
score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
