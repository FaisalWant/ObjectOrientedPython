# backtopython6.
# USING PIP- comman commands:
# --------------------------

# # Install/Uninstall a package
# $ pip install package_name
# $ pip uninstall package_name

# # Upgrade an existing package to the newest version
# $ pip install --upgrade package_name

# # Install from requirements file
# $ pip freeze > requirements.txt
# $ pip install -r requirements.txt

# USING PIP-- UNCOMMON COMMANDS:
# ------------------------------
# # Install to Python user-specific install directory
# $ pip install --user package_name
# # Require specific versions to be installed
# $ pip install "package_name==4.1.0"
# $ pip install "package_name >= 1.0, != 1.4.0, < 2.0"
# # Show information about a particular package
# $ pip show package_name
# # Search PyPI for matching packages
# $ pip search query

# --------------
#              |
# HTTP:        |
# --------------
# # A simple GET request
# response = requests.get('https://api.example.com/users')
# if response.ok:
# 	raw_data = response.content
# 	json_data = response.json() # If server response is in JSON format


# # GET with params]
# ------------------
# payload = {'name': 'sredmond', 'field': ['email', 'org']}
# response = requests.get('https://api.example.com/users', params=payload)
# print(response.url)
# # => https://api.example.com/users?name=sredmond&field=email&field=org

# # POST with params]
# -------------------
# payload = {'username': 'sredmond', 'password': 'pyth0n'}
# response = requests.post('https://api.example.com/login', data=payload



# NUMPY(NUMERICAL PYTHON):
# -------------------------

# N-dimensional array object
# Sophisticated functions
# Capabilities
# Linear algebra
# Fourier transform
# Random sampling


# USING NUMPY:
# -----------------
# a = np.arange(15).reshape(3, 5)
# print(a)
# # array([[ 0, 1, 2, 3, 4],
# # [ 5, 6, 7, 8, 9],
# # [10, 11, 12, 13, 14]])

# a.shape # => (3, 5)
# a.ndim # => 2
# a.dtype.name # => 'int64'
# type(a) # => numpy.ndarray
# print(a[:, 1]) # => array([ 1, 6, 11])

# a = np.array([3, 4, 5])
# a + 4 # => array([7, 8, 9])
# a * 1.5 # => array([ 4.5, 6. , 7.5])
# b = np.array([4, -1, 0])
# np.dot(a, b) # => 8 (= 3 * 4 + 4 * -1 + 5 * 0)
# a.sum() # => 12
# space = np.linspace(0, 2 * np.pi, 100)
# sinusoid = np.sin(b)

# USING PYPLOT:
# --------------------------
# import numpy as np
# import matplotlib.pyplot as plt
# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = np.pi * (15 * np.random.rand(N))**2
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.show()
