class BatchModel(Model):

    def __init__(self, model):
        self.model = model

    def load(self):
        pass

    def predict_batch(self, batch_input_features):
        '''
        Predicts a batch.

        Parameters:
        batch_input_features: A batch of features required by the model to
        generate predictions. For example: numpy arrays of a particular
        dimension.

        Returns:
        predictions: Predictions of the model. For example: a numpy array
        '''
        pass

    def metadata(self):
        pass

    def scheme_input_data(self):
        pass

    def scheme_output_data(self):
        pass

    def preprocess_data(self, data):
        pass