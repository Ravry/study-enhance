import cv2
import numpy as np
import matplotlib.pyplot as plt



def __main__():
    IMAGE_PATHS = []
    BRIGHTNESS_VALUES = np.zeros((3, 8))

    #gather image paths
    for i in range(8):
        _index = (i + 1)
        IMAGE_PATHS.append(f"assets/img/front/kRT/{_index}.png")
        IMAGE_PATHS.append(f"assets/img/front/RT/{_index}.png")
        IMAGE_PATHS.append(f"assets/img/front/30/{_index}.png")

    #iterate over image paths and gain the mean brightness value
    for i in range(len(IMAGE_PATHS)):
        path = IMAGE_PATHS[i]

        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

        if img.shape[2] == 4:
            rgb = img[:, :, :3]
            alpha = img[:, :, 3]
        else:
            rgb = img
            alpha = np.ones(rgb.shape[:2], dtype=np.uint8) * 255

        gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

        mask = alpha > 0

        mean_brightness = gray[mask].mean()

        BRIGHTNESS_VALUES[i % 3][int(i / 3)] = mean_brightness

        print(f"> [{i % 3}][{int(i / 3)}] [{path.split('img/')[1]}] mittlere helligkeit (alpha > 0): {mean_brightness:.2f}")

        if ((i + 1) % 3 == 0):
            print("-" * 40)
    
    ROW_LABELS = ['kRT-S', 'RT-S', '30-S']

    fig = plt.figure(figsize=(3, 8))
    fig.canvas.manager.set_window_title("Blatt Helligkeit - Abbildung")
    plt.imshow(BRIGHTNESS_VALUES, cmap='gray', vmin=0, vmax=255)
    plt.colorbar(label='Helligkeit')

    for i in range(BRIGHTNESS_VALUES.shape[0]):
        for j in range(BRIGHTNESS_VALUES.shape[1]):
            plt.text(j, i, f"{BRIGHTNESS_VALUES[i, j]:.0f}",
                    ha='center', va='center', color='black', fontsize=18)

    
    plt.yticks(ticks=np.arange(BRIGHTNESS_VALUES.shape[0]), labels=ROW_LABELS)
    
    plt.title('Blatt Helligkeit')
    plt.show()

__main__()