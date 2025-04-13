import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import numpy as np

# Set the style for the plots using seaborn
sns.set_theme(style="whitegrid")

# Evaluate the model on the validation set
loss, accuracy = model.evaluate(X_val, y_val, batch_size=32)  # Evaluate using batch_size of 32

# Print the loss and accuracy metrics on the validation set
print(f"Validation loss: {loss}")
print(f"Validation accuracy: {accuracy}")

# Define custom colors for training and validation curves
train_color = "green"  # Green color for training curve
val_color = "purple"   # Purple color for validation curve

# Create a figure with a specific size
plt.figure(figsize=(12, 5))

# Plot accuracy
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training', color=train_color, linewidth=2)  # Plot training accuracy
plt.plot(history.history['val_accuracy'], label='Validation', color=val_color, linestyle='--', linewidth=2)  # Plot validation accuracy
plt.title('Accuracy during training', fontsize=14)  # Title of the accuracy plot
plt.xlabel('Epochs', fontsize=12)  # X-axis label (Epochs)
plt.ylabel('Accuracy', fontsize=12)  # Y-axis label (Accuracy)
plt.legend(fontsize=10)  # Display legend with font size 10
plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Add grid for better visualization

# Plot loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training', color=train_color, linewidth=2)  # Plot training loss
plt.plot(history.history['val_loss'], label='Validation', color=val_color, linestyle='--', linewidth=2)  # Plot validation loss
plt.title('Loss during training', fontsize=14)  # Title of the loss plot
plt.xlabel('Epochs', fontsize=12)  # X-axis label (Epochs)
plt.ylabel('Loss', fontsize=12)  # Y-axis label (Loss)
plt.legend(fontsize=10)  # Display legend with font size 10
plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Add grid for better visualization

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()

# Make predictions with the trained model
y_pred = model.predict(X)  # Get the predicted probabilities for each class

# Convert the predicted probabilities to labels (0 or 1) based on a threshold of 0.5
y_pred_labels = (y_pred > 0.5).astype(int)  # Convert probabilities to binary labels (0 or 1)

# Generate the confusion matrix to compare true labels with predicted labels
cm = confusion_matrix(y, y_pred_labels)  # Compute confusion matrix

# Visualize the confusion matrix with a heatmap for better interpretation
plt.figure(figsize=(8, 6))  # Set the figure size
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['AGN', 'Starburst'], yticklabels=['AGN', 'Starburst'])  # Plot confusion matrix
plt.title('Confusion Matrix')  # Title of the confusion matrix plot
plt.xlabel('Prediction')  # X-axis label (Predicted class)
plt.ylabel('Actual')  # Y-axis label (True class)
plt.show()  # Display the plot

# Save the trained model to a file for later use
model.save('modelo_david_galaxies.keras')  # Save the model in Keras' .keras format
