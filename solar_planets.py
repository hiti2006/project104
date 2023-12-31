import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(img,"SUN",(20,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"MERCURY",(130,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"VENUS",(200,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"EARTH",(290,265),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"MARS",(390,255),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"JUPITER",(590,385),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"SATURN",(770,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"URANUS",(980,290),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"NEPTUNE",(1120,285),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.imshow("soLaR SysteM",img)
cv2.waitKey(5000)