from tkinter.constants import END
import numpy as np
import matplotlib.pyplot as plt

C1 = 1
C2 = 2 
C3 = 3
C4 = 4 
C5 = 5
C6 = 1
C7 = 2
C8 = 3
C9 = 4
C10 = 5
C11 = 1
C12 = 2
C13 = 3
C14 = 4
C15 = 5

R1 = 0
R2 = 0
R3 = 0
R4 = 0
R5 = 0

A1 = int(input('ข้อ 1 ตอบ : '))
A2 = int(input('ข้อ 2 ตอบ : '))
A3 = int(input('ข้อ 3 ตอบ : '))
A4 = int(input('ข้อ 4 ตอบ : '))
A5 = int(input('ข้อ 5 ตอบ : '))
A6 = int(input('ข้อ 6 ตอบ : '))
A7 = int(input('ข้อ 7 ตอบ : '))
A8 = int(input('ข้อ 8 ตอบ : '))
A9 = int(input('ข้อ 9 ตอบ : '))
A10 = int(input('ข้อ 10 ตอบ : '))
A11 = int(input('ข้อ 11 ตอบ : '))
A12 = int(input('ข้อ 12 ตอบ : '))
A13 = int(input('ข้อ 13 ตอบ : '))
A14 = int(input('ข้อ 14 ตอบ : '))
A15 = int(input('ข้อ 15 ตอบ : '))

if C1 == A1 :
    print('ข้อ 1 ตอบ : ถูก')
    R1 = R1 + 1
else :
    print('ข้อ 1 ตอบ : ผิด')

if C2 == A2 :
    print('ข้อ 2 ตอบ : ถูก')
    R2 = R2 + 1
else :
    print('ข้อ 2 ตอบ : ผิด')

if C3 == A3 :
    print('ข้อ 3 ตอบ : ถูก')
    R3 = R3 + 1
else :
    print('ข้อ 3 ตอบ : ผิด')

if C4 == A4 :
    print('ข้อ 4 ตอบ : ถูก')
    R4 = R4 + 1
else :
    print('ข้อ 4 ตอบ : ผิด')

if C5 == A5 :
    print('ข้อ 5 ตอบ : ถูก')
    R5 = R5 + 1
else :
    print('ข้อ 5 ตอบ : ผิด')

if C6 == A6 :
    print('ข้อ 6 ตอบ : ถูก')
    R1 = R1 + 1
else :
    print('ข้อ 6 ตอบ : ผิด')

if C7 == A7 :
    print('ข้อ 7 ตอบ : ถูก')
    R2 = R2 + 1
else :
    print('ข้อ 7 ตอบ : ผิด')

if C8 == A8 :
    print('ข้อ 8 ตอบ : ถูก')
    R3 = R3 + 1
else :
    print('ข้อ 8 ตอบ : ผิด')

if C9 == A9 :
    print('ข้อ 9 ตอบ : ถูก')
    R4 = R4 + 1
else :
    print('ข้อ 9 ตอบ : ผิด')

if C10 == A10 :
    print('ข้อ 10 ตอบ : ถูก')
    R5 = R5 + 1
else :
    print('ข้อ 10 ตอบ : ผิด')

if C11 == A11 :
    print('ข้อ 1 ตอบ : ถูก')
    R1 = R1 + 1
else :
    print('ข้อ 1 ตอบ : ผิด')

if C12 == A12 :
    print('ข้อ 2 ตอบ : ถูก')
    R2 = R2 + 1
else :
    print('ข้อ 2 ตอบ : ผิด')

if C13 == A13 :
    print('ข้อ 3 ตอบ : ถูก')
    R3 = R3 + 1
else :
    print('ข้อ 3 ตอบ : ผิด')

if C14 == A14 :
    print('ข้อ 4 ตอบ : ถูก')
    R4 = R4 + 1
else :
    print('ข้อ 4 ตอบ : ผิด')

if C15 == A15 :
    print('ข้อ 5 ตอบ : ถูก')
    R5 = R5 + 1
else :
    print('ข้อ 5 ตอบ : ผิด')

plt.style.use('seaborn-dark')
categories = ['Conversation','Error', 'Vocabulary', 'Readind', 'Analyze']
categories = [*categories,categories[0]]

Prt = [R1,R2,R3,R4,R5]
H = [3,3,3,3,3]

Prt = [*Prt,Prt[0]]
H = [*H,H[0]]

label_loc = np.linspace(start=0, stop=2*np.pi, num=len(Prt))

plt.figure(figsize=(6,6))
plt.subplot(polar=True)

plt.plot(label_loc, Prt)
plt.plot(label_loc, H)

plt.fill(label_loc, Prt, 'blue', alpha=0.1)
plt.legend(['Pre-test','maximum point'],loc=(0.95,0.8))

plt.title('Pre-test results',size='18')
lines, labels = plt.thetagrids(np.degrees(label_loc),labels=categories)
plt.text("กายหล่อมาก", size='18')
plt.show()

print('\n')
print ('แหล่งเรียนรู้ที่ควรไปศึกษาเพิ่มเติม')
print('\n')
print ('https://www.triam-ent.com/%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B8%84%E0%B8%B3%E0%B8%A8%E0%B8%B1%E0%B8%9E%E0%B8%97%E0%B9%8C-gat-eng/')
print('\n')
print ('https://www.wallstreetenglish.in.th/%E0%B9%80%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%99%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B8%AD%E0%B8%B1%E0%B8%87%E0%B8%81%E0%B8%A4%E0%B8%A9/%E0%B8%A3%E0%B8%A7%E0%B8%A1-%E0%B8%84%E0%B8%B3%E0%B8%A8%E0%B8%B1%E0%B8%9E%E0%B8%97%E0%B9%8C%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B8%AD%E0%B8%B1%E0%B8%87%E0%B8%81%E0%B8%A4%E0%B8%A9-gat-pat-100/')
print('\n')
print ('https://anywhere.learn.co.th/main/%E0%B9%80%E0%B8%97%E0%B8%84%E0%B8%99%E0%B8%B4%E0%B8%84-gat-%E0%B8%AD%E0%B8%B1%E0%B8%87%E0%B8%81%E0%B8%A4%E0%B8%A9/')
print('\n')
print ('https://www.englishbychris.com/portfolio-item/english-conversations/')
print('\n')

Q = input('คุณไปเรียนรู้เพิ่มเติมมาแล้วจริงๆ ใช่หรือไม่ : ')
if Q == ('ใช่') :
    PC1 = 1
    PC2 = 2 
    PC3 = 3
    PC4 = 4 
    PC5 = 5
    PC6 = 1
    PC7 = 2
    PC8 = 3
    PC9 = 4
    PC10 = 5
    PC11 = 1
    PC12 = 2 
    PC13 = 3
    PC14 = 4 
    PC15 = 5

    PR1 = 0
    PR2 = 0
    PR3 = 0
    PR4 = 0
    PR5 = 0

    PA1 = int(input('ข้อ 1 ตอบ : '))
    PA2 = int(input('ข้อ 2 ตอบ : '))
    PA3 = int(input('ข้อ 3 ตอบ : '))
    PA4 = int(input('ข้อ 4 ตอบ : '))
    PA5 = int(input('ข้อ 5 ตอบ : '))
    PA6 = int(input('ข้อ 6 ตอบ : '))
    PA7 = int(input('ข้อ 7 ตอบ : '))
    PA8 = int(input('ข้อ 8 ตอบ : '))
    PA9 = int(input('ข้อ 9 ตอบ : '))
    PA10 = int(input('ข้อ 10 ตอบ : '))
    PA11 = int(input('ข้อ 11 ตอบ : '))
    PA12 = int(input('ข้อ 12 ตอบ : '))
    PA13 = int(input('ข้อ 13 ตอบ : '))
    PA14 = int(input('ข้อ 14 ตอบ : '))
    PA15 = int(input('ข้อ 15 ตอบ : '))

    if PC1 == PA1 :
        print('ข้อ 1 ตอบ : ถูก')
        PR1 = PR1 + 1
    else :
        print('ข้อ 1 ตอบ : ผิด')

    if PC2 == PA2 :
        print('ข้อ 2 ตอบ : ถูก')
        PR2 = PR2 + 1
    else :
        print('ข้อ 2 ตอบ : ผิด')

    if PC3 == PA3 :
        print('ข้อ 3 ตอบ : ถูก')
        PR3 = PR3 + 1
    else :
        print('ข้อ 3 ตอบ : ผิด')

    if PC4 == PA4 :
        print('ข้อ 4 ตอบ : ถูก')
        PR4 = PR4 + 1
    else :
        print('ข้อ 4 ตอบ : ผิด')

    if PC5 == PA5 :
        print('ข้อ 5 ตอบ : ถูก')
        PR5 = PR5 + 1
    else :
        print('ข้อ 5 ตอบ : ผิด')

    if PC6 == PA6 :
        print('ข้อ 6 ตอบ : ถูก')
        PR1 = PR1 + 1
    else :
        print('ข้อ 6 ตอบ : ผิด')

    if PC7 == PA7 :
        print('ข้อ 7 ตอบ : ถูก')
        PR2 = PR2 + 1
    else :
        print('ข้อ 7 ตอบ : ผิด')

    if PC8 == PA8 :
        print('ข้อ 8 ตอบ : ถูก')
        PR3 = PR3 + 1
    else :
        print('ข้อ 8 ตอบ : ผิด')

    if PC9 == PA9 :
        print('ข้อ 9 ตอบ : ถูก')
        PR4 = PR4 + 1
    else :
        print('ข้อ 9 ตอบ : ผิด')

    if PC10 == PA10 :
        print('ข้อ 10 ตอบ : ถูก')
        PR5 = PR5 + 1
    else :
        print('ข้อ 10 ตอบ : ผิด')

    if PC11 == PA11 :
        print('ข้อ 1 ตอบ : ถูก')
        PR1 = PR1 + 1
    else :
        print('ข้อ 1 ตอบ : ผิด')

    if PC12 == PA12 :
        print('ข้อ 2 ตอบ : ถูก')
        PR2 = PR2 + 1
    else :
        print('ข้อ 2 ตอบ : ผิด')

    if PC13 == PA13 :
        print('ข้อ 3 ตอบ : ถูก')
        PR3 = PR3 + 1
    else :
        print('ข้อ 3 ตอบ : ผิด')

    if PC14 == PA14 :
        print('ข้อ 4 ตอบ : ถูก')
        PR4 = PR4 + 1
    else :
        print('ข้อ 4 ตอบ : ผิด')

    if PC15 == PA15 :
        print('ข้อ 5 ตอบ : ถูก')
        PR5 = PR5 + 1
    else :
        print('ข้อ 5 ตอบ : ผิด')

    plt.style.use('seaborn-dark')
    categories = ['Conversation','Error', 'Vocabulary', 'Readind', 'Analyze']
    categories = [*categories,categories[0]]

    Prt = [R1,R2,R3,R4,R5]
    Pt = [PR1,PR2,PR3,PR4,PR5]
    H = [3,3,3,3,3]

    Prt = [*Prt,Prt[0]]
    Pt = [*Pt,Pt[0]]
    H = [*H,H[0]]

    label_loc = np.linspace(start=0, stop=2*np.pi, num=len(Prt))

    plt.figure(figsize=(6,6))
    plt.subplot(polar=True)

    plt.plot(label_loc, Prt)
    plt.plot(label_loc, Pt)
    plt.plot(label_loc, H)

    plt.fill(label_loc, Prt, 'blue', alpha=0.1)
    plt.fill(label_loc, Pt, 'red', alpha=0.1)
    plt.legend(['Pre-test','Post-test','maximum point'],loc=(0.95,0.8))

    plt.title('Post-test results',size='18')
    lines, labels = plt.thetagrids(np.degrees(label_loc),labels=categories)
    plt.show()
    print('เก่งมาก')
else :
    print ('ไปเรียนมาก่อนนะจ๊ะ')
