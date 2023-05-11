import os
import pandas as pd
import numpy as np
# import networkx as nx
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from graph import GNNNodeClassifier

def run_experiment(model, x_train, y_train):
    # Compile the model.
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate),
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=[keras.metrics.SparseCategoricalAccuracy(name="acc")],
    )
    # Create an early stopping callback.
    early_stopping = keras.callbacks.EarlyStopping(
        monitor="val_acc", patience=50, restore_best_weights=True
    )
    # Fit the model.
    history = model.fit(
        x=x_train,
        y=y_train,
        epochs=num_epochs,
        batch_size=batch_size,
        validation_split=0.15,
        callbacks=[early_stopping],
    )

    return history

def get_graph_info():
    # # Create an edges array (sparse adjacency matrix) of shape [2, num_edges].
    # edges = citations[["source", "target"]].to_numpy().T
    # # Create an edge weights array of ones.
    # edge_weights = tf.ones(shape=edges.shape[1])
    # # Create a node features array of shape [num_nodes, num_features].
    # node_features = tf.cast(
    #     papers.sort_values("paper_id")[feature_names].to_numpy(), dtype=tf.dtypes.float32
    # )
    # # Create graph info tuple with node_features, edges, and edge_weights.
    # graph_info = (node_features, edges, edge_weights)
    #
    # print("Edges shape:", edges.shape)
    # print("Nodes shape:", node_features.shape)
    return ("node_features", "edges", "edge_weights")

def getStatus(statusDesc) -> int:
    return statusDesc == "Accepted" if 1 else 0

if __name__ == "__main__":
    hidden_units = [32, 32]
    learning_rate = 0.01
    dropout_rate = 0.5
    num_epochs = 300
    batch_size = 256

    problem_id = "p03949"
    problem_data = pd.read_csv("./data/Project_CodeNet/metadata/p03949.csv")
    language_extension = ("C++", "cpp")

    data = {"submission_id": [], "code": []}

    for row in range(len(problem_data)):
        submission_id = problem_data.iloc[[row]]["submission_id"].values
        path = f'./data/Project_CodeNet/data/{problem_id}/{language_extension[0]}/{submission_id[0]}.{language_extension[1]}'
        if os.path.exists(path):
            with open(path, encoding="utf8") as f:
                code = f.readlines()
                # print(submission_id, code)
                data["submission_id"].append(submission_id[0])
                data["code"].append(code[0])
    # print(data)
    code_df = pd.DataFrame(data)
    code_df=code_df.set_index('submission_id')
    problem_data=problem_data.set_index('submission_id')
    problem_data=problem_data.join(code_df, on='submission_id')



                # feature_names = {"code"}
    # x_train =

    # model = GNNNodeClassifier(get_graph_info(), 2, hidden_units)
    # run_experiment(model, x_train, y_train)
    # feature_names = set(papers.columns) - {"paper_id", "subject"}
    # num_features = len(feature_names)
    # num_classes = len(class_idx)
    #
    # # Create train and test features as a numpy array.
    # x_train = train_data["problem_id"].to_numpy()
    # x_test = test_data["problem_id"].to_numpy()
    # # Create train and test targets as a numpy array.
    # y_train = train_data["status"]
    # y_test = test_data["status"]

    pass