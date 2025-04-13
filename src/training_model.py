
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.model_selection import train_test_split

# Assuming X and y are already defined and preprocessed

# Create the Sequential model
model = Sequential()

# Add a series of Conv1D layers with MaxPooling for feature extraction
model.add(Conv1D(filters=64, kernel_size=3, activation='relu', kernel_regularizer=l2(0.001), input_shape=(2000, 1)))  # First Conv1D layer
model.add(MaxPooling1D(pool_size=2))  # MaxPooling after the first Conv1D layer

model.add(Conv1D(filters=128, kernel_size=3, activation='relu', kernel_regularizer=l2(0.001)))  # Second Conv1D layer
model.add(MaxPooling1D(pool_size=2))  # MaxPooling after the second Conv1D layer

model.add(Conv1D(filters=256, kernel_size=3, activation='relu', kernel_regularizer=l2(0.001)))  # Third Conv1D layer
model.add(MaxPooling1D(pool_size=2))  # MaxPooling after the third Conv1D layer

model.add(Conv1D(filters=512, kernel_size=3, activation='relu', kernel_regularizer=l2(0.001)))  # Fourth Conv1D layer
model.add(MaxPooling1D(pool_size=2))  # MaxPooling after the fourth Conv1D layer

# Flatten the output to connect to fully connected layers
model.add(Flatten())

# Add fully connected Dense layers for classification
model.add(Dense(512, activation='relu', kernel_regularizer=l2(0.001)))  # First Dense layer
model.add(Dropout(0.5))  # Dropout to prevent overfitting

model.add(Dense(256, activation='relu', kernel_regularizer=l2(0.001)))  # Second Dense layer
model.add(Dropout(0.5))  # Dropout to prevent overfitting

model.add(Dense(128, activation='relu', kernel_regularizer=l2(0.001)))  # Third Dense layer
model.add(Dense(64, activation='relu', kernel_regularizer=l2(0.001)))  # Fourth Dense layer

# Output layer with sigmoid activation for binary classification
model.add(Dense(1, activation='sigmoid'))

# Compile the model with Adam optimizer and binary crossentropy loss
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Display the model summary to inspect the architecture
model.summary()

# Split the dataset into training and validation sets (70% training, 30% validation)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)

# Configure EarlyStopping to stop training if validation loss does not improve
early_stopping = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)

# Configure ReduceLROnPlateau to reduce learning rate if validation loss plateaus
reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',  # Monitor the validation loss
    factor=0.5,          # Reduce the learning rate by a factor of 0.5
    patience=5,          # Wait for 5 epochs without improvement before reducing the learning rate
    min_lr=1e-6          # Ensure the learning rate does not drop below 1e-6
)

# Train the model with the training set and use the validation data for evaluation
history = model.fit(
    X_train, y_train, 
    epochs=80, 
    batch_size=64, 
    validation_data=(X_val, y_val),  # Pass validation data explicitly for evaluation
    callbacks=[early_stopping, reduce_lr]  # Include EarlyStopping and ReduceLROnPlateau callbacks
)
