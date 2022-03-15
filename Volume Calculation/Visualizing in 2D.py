import matplotlib.pyplot as plt
data2d = [[6.7,6.6,6.5,7.0,6.8,6.9,6.6,6.7,6.3,6.4,6.0,6.9,6.6,6.8,6.2,6.5,6.5,6.8,6.9,7.0,],    
         [6.2,6.6,6.5,6.3,6.5,6.4,6.5,6.4,6.3,6.5,6.4,6.5,6.6,6.6,6.3,6.6,6.6,6.5,6.5,6.9,],
         [6.2,6.6,6.5,6.3,6.5,6.4,6.5,6.4,6.3,6.7,6.3,6.1,6.8,6.5,6.2,6.7,6.1,6.5,6.3,6.8,],
         [6.7,6.7,6.6,6.3,6.5,6.0,6.9,6.7,6.5,6.7,6.3,6.6,6.3,6.8,6.9,6.6,6.7,6.5,6.3,6.2,],
         [6.8,6.3,6.5,6.9,6.6,6.7,6.5,6.8,6.5,6.4,6.7,6.5,6.6,6.4,6.5,6.6,6.6,6.3,6.8,6.9,],
         [7.0,6.7,6.6,6.5,6.4,6.8,6.6,6.3,6.7,6.5,6.2,6.6,6.5,6.3,6.5,6.4,6.5,6.4,6.3,6.5],
         [6.2,6.3,6.8,6.3,6.7,6.9,6.3,6.6,6.4,6.5,6.5,6.6,6.5,6.5,6.3,6.8,6.4,6.5,6.4,6.8,],
         [6.6,6.7,6.3,6.1,6.8,6.5,6.2,6.7,6.1,6.5,6.3,6.8,6.4,6.5,6.4,6.8,6.2,6.6,6.5,6.7,],
         [6.7,6.3,6.5,6.4,6.5,6.7,6.0,6.3,6.3,6.5,6.6,6.4,6.5,6.6,6.6,6.3,6.8,6.9,6.6,6.7,],
         [6.2,6.5,6.1,6.6,6.3,6.8,6.3,6.8,6.4,6.5,6.4,6.8,6.2,6.6,6.5,6.7,6.2,6.5,6.5,6.5,],
         [6.3,6.3,6.8,6.4,6.5,6.4,6.8,6.2,6.6,6.5,6.7,6.1,6.4,6.5,6.4,6.7,6.3,6.5,6.7,6.4],
         [6.4,6.4,6.7,6.5,6.6,6.4,6.5,6.6,6.6,6.3,6.8,6.9,6.6,6.7,6.5,6.3,6.2,6.3,6.5,6.6,],
         [6.5,6.4,6.5,6.2,6.7,6.7,6.3,6.8,6.5,6.6,6.3,6.8,6.9,6.6,6.7,6.5,6.3,6.2,6.3,6.1,],
         [6.8,6.6,6.6,6.4,6.8,6.9,6.6,6.3,6.9,6.5,6.4,6.4,6.7,6.5,6.6,6.6,6.9,6.5,6.7,6.5],
         [6.9,6.7,6.4,6.6,6.9,6.3,6.7,6.6,6.3,6.5,6.5,6.7,6.5,6.7,6.3,6.4,6.0,6.9,6.6,6.8,],
         [6.2,6.3,6.7,6.7,6.6,6.5,6.4,6.7,6.6,6.5,6.5,6.5,6.9,6.3,6.6,6.4,6.5,6.2,6.5,6.5,],
         [6.3,6.4,6.3,6.5,6.6,6.7,6.7,6.8,6.9,6.5,6.5,6.3,6.7,6.6,6.5,6.5,6.5,6.3,6.8,6.4,],
         [6.6,6.8,6.8,6.8,6.3,6.4,6.8,6.6,6.3,6.8,6.9,6.6,6.7,6.5,6.3,6.2,6.3,6.5,6.1,6.5,],
         [6.1,6.2,6.4,6.5,6.6,6.6,6.3,6.6,6.6,6.5,6.5,6.7,6.1,6.4,6.5,6.9,6.6,6.3,6.7,6.4],
         [6.2,6.4,6.7,6.3,6.5,6.9,6.6,6.7,6.3,6.3,6.9,6.5,6.4,6.4,6.7,6.5,6.6,6.6,6.9,7.0,],
         [6.6,6.5,6.4,6.4,6.5,6.4,6.7,6.8,6.5,6.5,6.7,6.3,6.4,6.0,6.9,6.3,6.2,6.3,6.9,6.3,],
         [6.3,6.7,6.5,6.5,6.3,6.7,6.6,6.5,6.5,6.5,6.3,6.8,6.4,6.5,6.4,6.8,6.2,6.6,6.5,6.7,],
         [6.7,6.4,6.7,6.6,6.7,6.9,6.3,6.7,6.6,6.5,6.5,6.6,6.7,6.7,6.8,6.9,6.5,6.5,6.5,6.5,],
         [6.8,6.5,6.3,6.2,6.8,6.5,6.5,6.5,6.7,6.5,6.7,6.3,6.4,6.0,6.9,6.6,6.8,6.2,6.5,6.9,],
         [6.1,6.3,6.6,6.3,6.5,6.9,6.3,6.6,6.6,6.3,6.6,6.6,6.5,6.5,6.7,6.1,6.4,6.2,6.8,6.9],
         [6.3,6.1,6.7,6.4,6.3,6.7,6.4,6.3,6.4,6.7,6.5,6.6,6.6,6.9,7.0,6.3,6.2,6.3,6.5,6.7,],
         [6.7,6.8,6.9,6.6,6.7,6.5,6.2,6.3,6.0,6.7,6.8,6.5,6.5,6.7,6.3,6.4,6.0,6.8,6.9,6.6,],
         [6.3,6.9,6.2,6.7,6.3,6.7,6.4,6.4,6.5,6.4,6.7,6.8,6.5,6.5,6.7,6.3,6.4,6.0,6.2,6.8,],
         [6.5,6.4,6.6,6.8,6.5,6.8,6.5,6.4,6.5,6.9,6.8,6.6,6.9,6.5,6.5,6.7,6.3,6.4,6.0,6.2],
         [6.3,6.5,6.7,6.5,6.8,6.5,6.7,6.6,6.3,6.5,6.4,6.5,6.6,6.6,6.3,6.6,6.6,6.5,6.5,6.7,],
         [6.6,6.2,6.4,6.8,6.5,6.4,6.2,6.2,6.5,6.5,6.6,6.9,6.5,6.5,6.7,6.3,6.4,6.0,6.9,6.6,],
         [6.5,6.8,6.6,6.6,6.4,6.7,6.5,6.8,6.8,6.5,6.7,6.5,6.6,6.4,6.5,6.6,6.6,6.3,6.5,6.5,],
         [6.7,6.5,6.9,6.5,6.8,6.5,6.7,6.3,6.5,6.5,6.5,6.4,6.6,6.8,6.5,6.8,6.5,6.4,6.2,6.5,],
         [6.3,6.6,6.5,6.4,6.5,6.9,6.8,6.6,6.9,6.5,6.5,6.7,6.3,6.4,6.0,6.9,6.6,6.8,6.2,6.5,],
         [6.8,6.3,6.4,6.5,6.7,6.5,6.8,6.3,6.4,6.5,6.5,6.5,6.8,6.6,6.6,6.4,6.8,6.9,6.6,6.4],
         [6.1,6.9,6.5,6.8,6.4,6.4,6.5,6.5,6.6,6.5,6.7,6.5,6.7,6.3,6.4,6.0,6.9,6.6,6.8,6.5,] ]     
         
plt.imshow(data2d,cmap='gray')
plt.colorbar()
plt.show()