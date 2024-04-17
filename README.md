This repository contains Python code implementing two popular dithering algorithms, Floyd-Steinberg and Atkinson, using the **Numba** library for performance optimization. These algorithms are commonly used for reducing the color palette of images while preserving visual quality.

## Dithering Algorithms

### 1. Floyd-Steinberg Dithering

- Developed by Robert W. Floyd and Louis Steinberg in 1976.
- Distributes quantization errors to neighboring pixels in a specific pattern.
- Produces sharp images with noticeable noise.

### 2. Atkinson Dithering

- Developed by Bill Atkinson in 1982.
- Similar to Floyd-Steinberg but distributes errors differently.
- Produces smoother images with less visible noise.

## Dependencies

- Python 3.x
- NumPy
- Numba
- PIL (Python Imaging Library)

## Usage

1. Ensure you have Python installed on your system.
2. Install the required dependencies using pip:
```bash
pip install numpy numba pillow
```
3. Clone this repository to your local machine.
4. Place the image file (e.g., test.JPG) you want to process in the same directory as the Python script.
5. Run the script `dithering.py`: 
```bash
python dithering.py
```
6. The processed images (`floyd_steinberg.jpg` and `atkinson.jpg`) will be saved in the same directory as the input image.

## Customization

- You can adjust parameters or experiment with different images to observe varying results.
- Feel free to modify the code to suit your specific requirements or integrate it into your projects.

## License

This project is licensed under the MIT License.

