import cv2
import albumentations as A
import numpy as np
import os

# Função para ler as bounding boxes a partir de um arquivo de texto
def read_bounding_boxes(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        boxes = []
        for line in lines:
            values = line.strip().split(' ')
            class_id = int(values[0])
            x_center, y_center, width, height = map(float, values[1:])
            boxes.append({'class_id': class_id, 'bbox': [x_center, y_center, width, height,class_id]})
    return boxes

# Função para aplicar data augmentation nas imagens e bounding boxes
def augment_data(image_path, bounding_boxes, augmentation):
    image = cv2.imread(image_path)
    augmented = augmentation(image=image, bboxes=[box['bbox'] for box in bounding_boxes],
                             category_id=[box['class_id'] for box in bounding_boxes])
    augmented_image = augmented['image']
    augmented_boxes = np.array(augmented['bboxes'])

    return augmented_image, augmented_boxes

# Exemplo de utilização
image_path = 'cvat_data/images/carcinoma_1.jpg'
annotations_path = 'cvat_data/labels/carcinoma_1.txt'

# Pasta contendo as imagens
input_folder = 'cvat_data/img'
# Pasta para salvar as imagens aumentadas
output_folder = './imagens_aumentadas2'
output_folder2 = './imagens_aumentadas2_txt'
# Criar a pasta de saída se ela não existir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if not os.path.exists(output_folder2):
    os.makedirs(output_folder2)

# Lista de arquivos na pasta de entrada
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Iterar sobre cada imagem na pasta
for image_file in image_files:
    # Caminho completo da imagem de entrada
    input_image_path = os.path.join(input_folder, image_file)
    print(input_image_path)

     # Caminho completo para o arquivo de anotações correspondente
    annotations_file = os.path.splitext(image_file)[0] + '.txt'
    annotations_path = os.path.join(input_folder, annotations_file)
    annotations_path = f'cvat_data/lab/{annotations_file}'
    print(annotations_path)

    # Leitura das bounding boxes
    bounding_boxes = read_bounding_boxes(annotations_path)

    # Definição das transformações de aumento
    transform = A.Compose([
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(p=0.2),
        # Adicione outras transformações conforme necessário
    ], bbox_params=A.BboxParams(format='yolo', label_fields=['category_id']))

    # Aplicação das transformações
    augmented_image, augmented_boxes = augment_data(input_image_path, bounding_boxes, transform)
    # Salvar a imagem aumentada
    output_image_path = os.path.join(output_folder, f'augmented_{image_file}')
    cv2.imwrite(output_image_path, augmented_image)

    # Salvar as bounding boxes aumentadas em um formato YOLO
    output_boxes_path = os.path.join(output_folder2, f'augmented_{annotations_file}')
    with open(output_boxes_path, 'w') as file:
        for box in augmented_boxes:
            class_id = int(box[-1])
            x_center, y_center, width, height = map(float, box[0:-1])
            file.write(f"{class_id} {x_center} {y_center} {width} {height}\n")
# Salvar a imagem aumentada
#output_path = './imagem_aumentada.jpg'
#cv2.imwrite(output_path, augmented_image)
# Visualização da imagem original e aumentada
# cv2.imshow('Original Image', cv2.imread(image_path))
# cv2.imshow('Augmented Image', augmented_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
