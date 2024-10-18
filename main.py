import cv2

# Load the image
color_image = cv2.imread('astronomia-do-ceu-noturno-galactico-e-ciencia-combinaram-ia-generativa.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Resize the image to a smaller resolution (small window)
width = 400  # Desired width
height = 300  # Desired height
resized_color_image = cv2.resize(color_image, (width, height))
resized_gray_image = cv2.resize(gray_image, (width, height))


# Apply effects
blurred_image = cv2.GaussianBlur(resized_color_image, (15, 15), 0)  # Blur effect
edges_image = cv2.Canny(resized_gray_image, 100, 200)  # Edge detection
inverted_image = cv2.bitwise_not(resized_color_image)  # Color inversion

# Function to add text to the image
def add_text(image, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    return cv2.putText(image.copy(), text, (10, 25), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

# Add descriptive text to the images
original_with_text = add_text(resized_color_image, 'Original')
gray_with_text = add_text(resized_gray_image, 'Grayscale')
blurred_with_text = add_text(blurred_image, 'Blurred')
edges_with_text = add_text(edges_image, 'Edge Detection')
inverted_with_text = add_text(inverted_image, 'Color Inversion')

# Display the images with effects in small windows
cv2.imshow('Original Image', original_with_text)
cv2.imshow('Grayscale Image', gray_with_text)
cv2.imshow('Blurred Image', blurred_with_text)
cv2.imshow('Edge Detection Image', edges_with_text)
cv2.imshow('Color Inversion Image', inverted_with_text)

# Wait until a key is pressed to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
