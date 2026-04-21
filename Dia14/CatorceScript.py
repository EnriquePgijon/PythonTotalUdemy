#RECONOCIMIENTO FACIAL
#Hay que descargar visualStudio, versión comunity, y el complemento
#Desarrollo para el escritorio C++
import cmake
import dlib
import face_recognition as fr
import numpy
import cv2

#CARGAR IMÁGENES
foto_control= fr.load_image_file("nombre del archivo","ubicacion")
foto_prueba= fr.load_image_file("nombre del archivo","prueba")
#Pasar imágenes a RGB
foto_contol=cv2.cvtColor(foto_control,cv2.COLOR_BGR2RGB)
foto_prueba=cv2.cvtColor(foto_prueba,cv2.COLOR_BGR2RGB)

#Localizar cara control
lugar_cara_A=fr.face_locations(foto_control)[0]
cara_codificada_A= fr.face_encodings(foto_control)[0]
#Localizar cara control
lugar_cara_B=fr.face_locations(foto_prueba)[0]
cara_codificada_B= fr.face_encodings(foto_prueba)[0]

#Mostrar rectangulo
cv2.rectangle(foto_control,
              lugar_cara_A[3],
              lugar_cara_A[0],
              lugar_cara_A[1],
              lugar_cara_A[2],
              (0,255,0),2)

cv2.rectangle(foto_prueba,
              lugar_cara_B[3],
              lugar_cara_B[0],
              lugar_cara_B[1],
              lugar_cara_B[2],
              (0,255,0),2)
#Realizar comparación
resultado=fr.compare_faces([cara_codificada_A],cara_codificada_B)

#Medir la distancia
distancia=fr.face_distance([cara_codificada_A],cara_codificada_B)

#Mostrar resultado
cv2.putText(foto_prueba,f"{resultado} {distancia.round(2)}",
            (50,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),
            2)

#Mostrar imagenes
cv2.imshow("foto_control",foto_control)
cv2.imshow("foto_prueba",foto_prueba)
#Mantener el programa abierto
cv2.waitKey(0)

#Enseñar las caras
