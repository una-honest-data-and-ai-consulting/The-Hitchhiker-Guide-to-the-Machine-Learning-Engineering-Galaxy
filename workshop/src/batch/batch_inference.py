import argparse
import logging

def run_batch(path_to_model):
    raw_data = get_raw_data()

    model = BatchModel.load(path_to_model)
    X = model.preprocess(raw_data)
    predictions = model.predict_batch(X)

    write_to_sqldb(predictions)


if __name__ = "__main__"":
    run_batch(args.path_to_model)